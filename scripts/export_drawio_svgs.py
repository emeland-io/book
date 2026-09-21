#!/usr/bin/env python3
"""Export selected draw.io diagram tabs to individual SVG files.

Reads a JSON manifest mapping diagram tab names to output SVG filenames next
to the given .drawio source file. Each tab is extracted into a temporary
single-page .drawio file and exported independently via the
rlespinasse/drawio-export Docker image, so a broken/empty tab that isn't in
the manifest (e.g. an empty placeholder page) cannot abort exports of the
tabs that are. A tab listed in the manifest that fails to export is logged
and the script continues with the rest, but exits non-zero overall.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


def load_manifest(path: Path) -> dict[str, str]:
    with path.open() as f:
        return json.load(f)


def extract_page(drawio_path: Path, tab_name: str, dest: Path) -> bool:
    root = ET.parse(drawio_path).getroot()  # <mxfile>
    diagram = next((d for d in root.findall("diagram") if d.get("name") == tab_name), None)
    if diagram is None:
        print(f"::error::tab '{tab_name}' not found in {drawio_path}")
        return False

    new_root = ET.Element("mxfile", root.attrib)
    new_root.append(diagram)
    ET.ElementTree(new_root).write(dest, encoding="utf-8", xml_declaration=True)
    return True


def export_svg(temp_drawio: Path, out_dir: Path) -> Path | None:
    cmd = [
        "docker", "run", "--rm", "--shm-size=1g",
        "-v", f"{temp_drawio.parent}:/data",
        "-v", f"{out_dir}:/out",
        "rlespinasse/drawio-export",
        "-f", "svg", "-o", "/out", "-e", f"/data/{temp_drawio.name}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return None

    produced = list(out_dir.glob("*.svg"))
    if len(produced) != 1:
        print(f"::error::expected exactly one exported svg in {out_dir}, found {len(produced)}")
        return None
    return produced[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drawio_file", type=Path)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    images_dir = args.drawio_file.parent
    failures: list[str] = []

    for tab_name, filename in manifest.items():
        print(f"exporting '{tab_name}' -> {filename}")
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            temp_drawio = tmp_path / "page.drawio"
            out_dir = tmp_path / "out"
            out_dir.mkdir()

            if not extract_page(args.drawio_file, tab_name, temp_drawio):
                failures.append(tab_name)
                continue

            produced = export_svg(temp_drawio, out_dir)
            if produced is None:
                print(f"::warning::failed to export '{tab_name}'")
                failures.append(tab_name)
                continue

            shutil.copyfile(produced, images_dir / filename)

    if failures:
        print(f"::error::failed to export: {', '.join(failures)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
