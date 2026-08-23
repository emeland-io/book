---
title: "Phase 6: Observability"
weight: 70
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Phase 6: Observability



* The `Metric` does not represent the timeseries, but rather an abstract measurement, that the administrator or developer of the overall IT system is interested in. This is analog to the Service Level Indicator (SLI) described in the [Google SRE Book (Chapter on Service Level Objectives)](https://sre.google/sre-book/service-level-objectives/)
* Resources may have multiple `Threshholds` and `Values`, referenced by annotations.
* A `Threshhold` is likely to be referenced by multiple resources. And while technically possible, this is unlikely for resource to `Value` references. Example: each `ApiInstance` in a scale-out system has its own value, but all share the same `Threshholds` for their four golden signals.