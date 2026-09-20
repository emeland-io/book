---
title: "Phase 6: Observability"
weight: 90
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Phase 6: Observability

![a detailed entity relationship diagram of the observability entities](../images/p6-observability.svg)

See [Phase 6: Observability](/docs/model/phase6-observability/) in the model chapter for the purpose and semantics of these entities. This page describes the concrete fields, types, and well-known annotations used to map them to real data.

## `Metric`

| **Field** | **Type** | **Description** |
|:---------:|:--------:|:-----------------|
| `MetricId` (PK) | UUID | Unique identifier of the `Metric`. |
| `Name` | string | Human-readable name of the metric. |
| `Description` | string | Free-text description of what the metric represents. |
| `Annotations` | map[string]string | Free-form key/value metadata. |

## `MetricInstance`

| **Field** | **Type** | **Description** |
|:---------:|:--------:|:-----------------|
| `MetricInstanceId` (PK) | UUID | Unique identifier of the `MetricInstance`. |
| `Name` | string | Human-readable name of the instance. |
| `Description` | string | Free-text description of this specific binding of the metric. |
| `MetricRef` | UUID | Reference to the `Metric` this instance is bound to. |
| `Annotations` | map[string]string | Free-form key/value metadata. |

## `Threshold`

| **Field** | **Type** | **Description** |
|:---------:|:--------:|:-----------------|
| `ThresholdId` (PK) | UUID | Unique identifier of the `Threshold`. |
| `Summary` | string | Short label for the trigger definition. |
| `Description` | string | Free-text description of the trigger condition. |
| `MetricInstanceRef` | UUID | Reference to the `MetricInstance` this threshold is defined against. |
| `State` | enum | Current state of the trigger, as last observed from the authoritative external system. See below. |
| `Annotations` | map[string]string | Free-form key/value metadata. |

### `State` values

> **Draft — needs review.** These definitions follow common alerting-system semantics (e.g. Prometheus Alertmanager) and have not yet been confirmed against EmELand's specific requirements.

| **Value** | **Meaning** |
|:---------:|:------------|
| `inactive` | The trigger definition exists but is not currently being evaluated by the external system (for example, evaluation is paused or not yet started). |
| `active` | The trigger is being evaluated and its condition is not currently met. |
| `triggered` | The trigger's condition is currently met; it is firing. |
| `acknowledged` | The trigger is firing, but a human or operator has acknowledged it (comparable to a silenced alert — not yet resolved). |
| `unknown` | EmELand could not determine the current state from the external system (for example, due to a connectivity or staleness issue). |

### Well known Annotations

| **Key** | **Value** | **Description** |
|:-------:|:---------:|:-----------------|
| | | |

## `MetricValue`

| **Field** | **Type** | **Description** |
|:---------:|:--------:|:-----------------|
| `ValueId` (PK) | UUID | Unique identifier of the `MetricValue`. |
| `DisplayName` | string | Human-readable name of the value. |
| `Description` | string | Free-text description of what this recorded value represents. |
| `MetricInstanceRef` | UUID | Reference to the `MetricInstance` this value was recorded for. |
| `Value` | string | The recorded value. |
| `Annotations` | map[string]string | Free-form key/value metadata. |

### Well known Annotations

| **Key** | **Value** | **Description** |
|:-------:|:---------:|:-----------------|
| | | |