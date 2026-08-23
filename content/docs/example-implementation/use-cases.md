---
title: "Use Cases"
weight: 30
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Use Cases

To the uninitiated, EmELand often appears to be a confusing set of resource definitions and relationships. But how to generate actual benefits is not obvious.

The following use cases are intended not only to provide examples how the use the data held within the model, but also to document the useful workflows that already have been implemented.

## System Structure Documentation.

The desired structure of a large IT system complex is written manually as `System`, `Component`, and `API` resources, in order to describe the intended system.

Any running components and open interfaces are mapped to `ComponentInstance` and `ApiInstance` respectively, holding markers (e.g. annotations) of which Component or API they are an instance of. SystemInstances are either derived implicitly (e.g. through Helm chart releases) or explicitly through manually written resources.

Any missing association between these resources is marked as a `Finding` and reported to the developers of the IT system via the Web UI.

## Certificate Status from TLS Endpoints

If you manage your TLS certificates with a management solution like cert-manager, it is easy to track the remaining validity by reading the tracking Kubernetes resources. They hold status information on every managed certificate and even provide ready-made integrations with prometheus and grafana to make overdue certificates very obvious. Under normal circumstances, the managed software will renew certificates in a timely manner, so that they never run out of validity period.

But in a real environment, especially at the infrastructure level, there are very often certificates that cannot be tracked automatically. Reasons include legacy software or even hardware appliances, external services that do not provide the required interfaces as well as integrations that just have not happened yet.

In order to ensure that these certificates are tracked as well, EmELand uses its tracking of API endpoints to gather data on certificates. These are then analyzed for their validity period.

![a diagram of components involved in the data flow for extracting and evaluating certificate validity with EmELand and OpenTelemetry](images/uc_cert-validatio.svg)

## Tracking Error Budget of Services.

(Work in Progress)
