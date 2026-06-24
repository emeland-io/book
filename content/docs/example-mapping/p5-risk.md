---
title: "Phase 5: Risk"
weight: 80
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Phase 5: Risk

![a detailed entity relationship diagram of the risk entities](../images/p5-risk.svg)


Any finding MUST have one or more finding types it belongs to. A finding may potentially only be processed, if the finding type is known to the filter. 

If the finding type of a finding is unknown or not set, it will create a finding with the finding type of "unknown finding type" (see below), referencing the original finding. This will not only lead to an additional finding being created, but also has a high chance that no subsequent filter can find and process the original finding (The additional finding is mainly intended for EmELand administrators and developers, based on the assumption, that a missing or invalid finding type represents a bug or a type in configuration). 

## Well known Finding types

| **FindingTypeId** | **Name** | **Description** |
|:-------:|-------|-----|
| `9ddf677b-ff1e-49a2-b19e-6e420f149702` | Unknown Finding Type | The UUID given as the finding type in a `Finding` Resource is not known or not a valid v4 UUID.