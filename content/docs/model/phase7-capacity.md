---
title: "Phase 7: Capacity"
weight: 80
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Phase 7: Capacity

## Object Model

{{< image src="images/p7-capacity.svg" alt="image of the entities of the Capacity Data Model elements" title="Capacity Data Model" loading="lazy" >}}


### Resource Types

This object defines everything that may be limited and available amount needing be tracked. Examples include anything CPU cores, RAM, drive space, network bandwidth, but also licenses, cooling budget, amortised personal capacity.

### Capacity

The capacity is sorted into three categories: **requested** by a tenant, **provided** by the context, currently **consumed** by the workloads currently running in the context.

## Out of Scope

The capacity model only covers a snapshot of the current requests, capacity and consumption. Any aggregation of use of resources over time is discussed in [Phase 4: Billing](phase4-billing.md)

## Ideas

* remaining runway for expansion: What is the limiting factor for further growth and how long will it take current grow of other metrics to be limited by this bottleneck.
  *E.g How long will it take for our current colocation site to be full, if buy new hardware at the same rate as the last quarter / the last year?*