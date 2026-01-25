---
title: "Phase 5: Managing Risk"
weight: 60
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Phase 5: Managing Risk

## Where is all of that software coming from?

## Other Formats

### System Package Data Exchange (SPDX)

SPDX is a Software Bill of Material (SBOM) format, originally focussed on tracking licenses, but with [version 3.0](https://spdx.github.io/spdx-spec/v3.0.1/) having grown to cover basically all aspects of the software supply chain.

EmELand is focussed on gathering information on the currently running enterprise IT Landscape. Thus it primarily supports answering the following questions:

- **Providors / Vendors**: Who delivered the software? And do we have an unbroken chain of custody, so that we can ensure that the code we are executing is the same as the code that got delivered? Or rather the code that was published?

- **Products / Packages**: Software artifacts are seldomly delivery individually by themselves. Technically they are usually part of a package, consisting of the executable code, documents, default configuration, etc. Also they are legally part of a product, which is linked to a license. To which product version does an artifact belong? Do we have a valid license for executing that artifact?

- **Vulnerabilities / Updates**: Are there any known vulnerabilities for the artifact? How about the product version? Any Updates available, that possibly fix these vulnerabilities

Therefore, some of the details of licensing contracts and origins of vulnerabilities are out of scope. Instead EmELand only tracks the used software artifacts, and how they came to be present for execution. In addition, EmELand keeps information where copies of a given artefact are available, in order to support data logistics (the right artifact, at the right location, at the right time).
