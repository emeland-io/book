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

![a diagramm of the basic entities of the emeland model in the area of observability](../images/p6_observability.svg)

Phase 6 models how the EmELand landscape observes the operational behavior of the resources it tracks, without itself becoming a metrics store or an alerting system. Four entities form the core of the model: `Metric` and `MetricInstance` describe what is being measured, while `Threshold` and `MetricValue` describe what EmELand currently knows about that measurement from external systems. The greyed-out `Resource` in the diagram is not a distinct entity of this phase — it stands for any other resource type within the EmELand model (for example an `ApiInstance` or `ComponentInstance`) that can reference `Threshold`s and `MetricValue`s.

## `Metric`

A `Metric` does not represent a timeseries, but rather an abstract measurement that the administrator or developer of the overall IT system is interested in. This is analogous to a Service Level Indicator (SLI) as described in the [Google SRE Book (Chapter on Service Level Objectives)](https://sre.google/sre-book/service-level-objectives/).

A `Metric` is deliberately defined at a higher level of abstraction than a `MetricInstance`. For example, a `Metric` might represent the overall utilization of a system, as it happens to be CPU-bound, while the corresponding `MetricInstance` is the CPU utilization of one specific system, as recorded in one specific monitoring system. A single `Metric` may have any number of `MetricInstance`s.

## `MetricInstance`

A `MetricInstance` is the concrete, bound occurrence of a `Metric` — the same relationship as between a `System` and a `SystemInstance` in Phase 1. Where the `Metric` names what is of interest in the abstract, the `MetricInstance` identifies where that measurement is actually observed, and by which monitoring system.

Each `MetricInstance` belongs to exactly one `Metric`, and is the point of reference for both `Threshold`s and `MetricValue`s.

## `Threshold`

A `Threshold` is not a static value to compare a `MetricValue` against. Instead, it represents a — potentially complex — trigger definition that is defined and evaluated in an authoritative external system, such as Prometheus or OpenTelemetry. EmELand does not evaluate thresholds itself; it observes the state of the trigger as reported by that external system.

Each `Threshold` belongs to one `MetricInstance`, but is likely to be referenced by multiple `Resource`s through annotations. For example, each `ApiInstance` in a scale-out system may reference the same `Threshold`s for their four golden signals, even though each instance has its own separate `MetricValue`s.

## `MetricValue`

A `MetricValue` represents an observed value for a `MetricInstance` — a snapshot or example reading, not a full timeseries. EmELand is not intended to replace a metrics store; it records just enough information about the current or representative value to support the landscape model.

Each `MetricValue` belongs to one `MetricInstance`. Unlike `Threshold`s, `MetricValue`s are unlikely to be shared across multiple `Resource`s: while technically possible via annotations, a `MetricValue` is typically specific to the one `Resource` it was recorded for.