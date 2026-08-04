---
title: "Phase 1: Structure"
weight: 40
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Phase 1: System Structure

![a detailed entity relationship diagram of the system structure entities](../images/p1-structure.svg)

## System

Systems and Subsystems are the building blocks from which the overall landscape is constructed. But as EmELand is designed to reduce the amount of manual data entry where possible, there are a number of variants when defining these resources.

The most simple way to define them, is to manually type out the YAML documents or to created as resources in a Kubernetes cluster, to be read by the Kubernetes sensor.

`System` resources can also be read by parsing software packages (e.g. Helm Charts, OCM packages, RPMs or Debian packages). For these dedicated sensors need to be written, that contain the domain specific knowledge about their respective formats.

Subsystems are identified by setting their `parent` field to a reference to another `System` resource. This allows the modelling of tightly coupled complexes that require one another to function.

Systems are not intended to be place into a single unified relationship tree. There is no "root" `System`. The overall enterprise landscape is created by systems interconnected through APIs and partitioned through contexts.

An abstract System represents a system, of which only the API is known. It is identified by the annotation `emeland.io/p1-system-abstract` (see below for details). This is usually the case when the API is provided by an entity or organization that is external to the landscape covered by EmELand. Alternatively it may identify a legacy system, which has not be documented within EmELand yet.

### Well known Annotations

| **Key** | **Values** | **Description** |
|:-------:|:----------:|:---------------:|
| `emeland.io/p1-system-template-source` | string | An identifying string, e.g. an URL or similar, of the package, that defined a system structure |
| `emeland.io/p1-system-template-artifact-id` | UUID | An ID referencing the `Artifact` resource of the package |
| `emeland.io/p1-system-abstract`     | `true`, `false`    | If set to true, the system is abstract. If set to false, or the annotation is absent, the resource represents a normal system. |

### Rules

- An abstract `System` must not have any `Component` resources linked to it. Only APIs are permitted.
- Either all components and APIs of a system must be deployed at the same time, or none at all.

## Component

The Component, the same as the API, have their own version. This allows Components and APIs to be reused in multiple Systems. If the Components and the API would share the version of the system, then all Systems sharing either at least one Component or API would have to have the same versions, to enable proper lifecycle coverage of the Components or APIs when they change.

## API

The API represents any form of communication channel between `Component` resources.

## SystemInstance

## ComponentInstance

## ApiInstance

An `ApiInstance` represents a deployed API endpoint. Well-known `emeland.io/endpoint.*` annotation keys declare where that instance is reachable on the network so external tooling (for example the certprobe service) can perform synthetic HTTP/TLS checks.

These annotations apply only to `ApiInstance` resources. `SystemInstance` carries deployment metadata only; `API` is a type/spec definition, not a deployed endpoint.

Annotation values are stored as `map[string]string` in the model and `{ key, value }` objects on the query API. Values MUST be flat UTF-8 strings — nested YAML maps under `spec.annotations` are stringified by the file sensor and MUST NOT be used.

### Well known Annotations

| **Key** | **Required** | **Values** | **Description** |
|:-------:|:------------:|:----------:|:---------------:|
| `emeland.io/endpoint.protocol` | yes | `http`, `https` | URL scheme |
| `emeland.io/endpoint.host` | yes | string | Hostname or IP. An `ApiInstance` without this key is not a probe target. |
| `emeland.io/endpoint.port` | no | string | TCP port (for example `443`). MUST be quoted in YAML when numeric. |
| `emeland.io/endpoint.path` | no | string | HTTP path (for example `/api/v1/health`). MUST start with `/`; a leading slash is added if missing. |

#### Defaults

When optional keys are omitted:

| **Key** | **Default** |
|:-------:|:-----------:|
| `emeland.io/endpoint.port` | `443` if protocol is `https`; `80` if `http` |
| `emeland.io/endpoint.path` | `/` |

#### URL construction

The probe URL is built as:

```
{protocol}://{host}:{port}{path}
```

List and detail API responses include a reference URI pointing at the resource in the EmELand catalog (for example `https://emeland.local/v1/landscape/api-instances/{uuid}`). That URI is not the live service endpoint and MUST NOT be used as a probe target.

#### Certificate metadata

Do not declare certificate expiry or issuer in `ApiInstance` annotations for v1. The certprobe service discovers certificate state live via TLS and exposes metrics (for example `certprobe_cert_remaining_seconds`).

#### Example

```yaml
version: emeland.io/v1
kind: ApiInstance
spec:
  apiInstanceId: "88888888-0000-4000-8000-000000000001"
  displayName: "Payments API (prod EU)"
  api: "aaaaaaaa-0000-4000-8000-000000000001"
  systemInstance: "77777777-0000-4000-8000-000000000102"
  annotations:
    env: prod
    emeland.io/endpoint.protocol: https
    emeland.io/endpoint.host: payments.prod.eu.example.com
    emeland.io/endpoint.port: "443"
    emeland.io/endpoint.path: /api/v1/health
```

#### Out of scope

The following MUST NOT be used as endpoint annotation keys in v1:

- `cert.notAfter`, `cert.expires`, `cert.issuer`, or similar certificate inventory keys
- Nested YAML structures under `annotations` (use flat keys or a single JSON string value)
- Probe URLs on resource types other than `ApiInstance`

## Use Cases

This is a list of use cases, to sketch specific setups and how they are potentially modelled in EmELand. They were used to validate the model, but are placed here to help understanding how the model works.

### Deploy from a helm chart.

* A helm chart is parsed to extract the `System`, `API`, and `Component` information. This information can either be placed into a central system repository or put as Kubernetes Resources into a separate Helm Chart, so that it can be referenced by any future `SystemInstance` resources.
* Any optional components are grouped into one or more sub-systems, to ensure the rule, that either all elements of a system must be deployed or none at all.
* the template is deployed. `SystemInstance`, `ApiInstance` and `ComponentInstance` resources are created by the [modelsrv-k8s-sensor](https://github.com/emeland-io/modelsrv-k8s-sensor). The Kubernetes resources are checked for annotations that point from the Kubernetes Resources to the corresponding EmELand resources (e.g. a `Deployment` or `StatefulSet` representing a `ComponentInstances` in EmELand should carry an annotation to point to the correct `Component` definition as well as the relevant `SystemInstance`. See the documentation of the `modelsrv-k8s-sensor` for pre-defined `FindingTypes` and well known K8s annotations.)
