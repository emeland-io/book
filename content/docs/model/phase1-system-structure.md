---
title: "Phase 1: System Structure"
weight: 20
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

## Phase 1: System Structure

Phase 1 defines the basic structure of the overall enterprise landscape: software components that communicate over defined interfaces.

Components and APIs belong to Systems, defining the fundamental building blocks a the system landscape. Systems in turn are structured hierarchical into Systems and Sub-Systems.

![An entity relationship diagram of the entities in Phase 1: System, API, Component, SystemInstance, ApiInstance, ComponentInstance](../images/p1-structure.svg)

A `System` and its contents is the foundational building block of an enterprise IT landscape. The same abstract `System` may be running any number of times and in multiple different contexts. Each separate instance is described by the `SystemInstance` resource

A `Component` resource represents any form of executable logic, regardless of the format (e.g. interpreted script, binary executable, container, etc.). It communicates with other components via interfaces represented via `API` resources. The APIs exposed by a component belong to the same system as the component. APIs consumed by an component may either be in the same system or a separate one.

An `API` represents a potential communication channel. Multiple technical elements may be part of the same API (i.e. a Kubernetes Service, Kubernetes Ingress resource, a load-balancer, a firewall rule.) The details depend on the mapping and implementation. A potential example is sketched below:

![a 3-step example on how an API resource in the EmELand model can hide a lot of complexity: abstract model, detailed model, specific instances when model is deployed in the real world](../images/api-example.svg)


## Rules

1. Every `ComponentInstance` SHOULD have a context defined.
1. A `System` MUST be versioned. If a given `System` has multiple current versions, a `SystemInstance` MUST indicate which version of the system it belongs to. An `SystemInstance` MAY belong to multiple version of the same System, if this is supported by the mapping and the implementation.
1. An `API` SHOULD be versioned.
1. An `Component` SHOULD be versioned

## Background

Use the C4 architecture model: a system having (software) components and interacting via APIs with the outside world.

### System Context
### Containers

### Why not the rest?

The C4 model has two further layers: Components and Code.

You may choose to use these other layers of the C4 model. But they are not as relevant for the enterprise landscape. You may also have a different method of designing and modelling software architecture.

Much more relevant is the fact that you may not have this information, if you are using proprietary software. A software vendor may even try to keep you from discovering the C4 containers, e.g. in hardware appliances. But in order to ensure control over the communication intersection (TODO: ref, definition) of your overall landscape, you must force vendors to give you this information.

## Using the information

### Generate the Communication Intersection

The information described in the resources of phase 1 allows the easy generation of a set of APIs, and thus communication relationships, which connect the components in two sets of contexts. This is the basis for a number of thread modelling and compliance applications.

## Ares of further Research

### Parent Relation for `SystemInstance`

Currently only the abstract `System` is part of a hierarchy, due to the *parent* relation. The SystemInstance does not, and relies on the structure of the parent.

Should use-cases be found, which require a *parent* field in the `SystemInstance` resource it may be added.

Following the design goal of minimal required structure it is currently left out on purpose.
