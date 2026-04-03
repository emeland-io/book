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

`System` resources can also be ready by parsing software packages (e.g. Helm Charts, OCM packages, RPMs or Debian packages). For these dedicated sensors need to be written, that contain the domain specific knowledge about their respective formats.

Subsystems are identified by setting their `parent` field to a reference to another `System` resource. This allows the modelling of tightly coupled complexes that require one another to function.

Systems are not intended to be place into a single unified relationship tree. There is no "root" `System`. The overall enterprise landscape is created by systems interconnected through APIs and partitioned through contexts.

An abstract System represents a system, of which only the API is known. It is identified by the annotation `emeland.io/p1-system-abstract` (see below for details). This is usually is the case when the API is provided by an entity or organization that is external to the landscape covered by EmELand. Alternatively it may identify a legacy system, which has not be documented within EmELand yet.

### Well known  Annotations

| **Key** | **Values** | **Description** |
|:-------:|:----------:|:---------------:|
| `emeland.io/p1-system-template-source` | string | An identifying string, e.g. an URL or similar, of the package, that defined a system structure
| `emeland.io/p1-system-template-artifact-id | UUID | An ID referencing the `Artifact` resource of the package
| `emeland.io/p1-system-abstract`     | `true`, `false`    | If set to true, the system is abstract. If set to false, or the annotation is absent, the resource represents a normal system. |

### Rules

- An abstract ´System` must not have any `Component` resources linked to it. Only APIs are permitted.
- Either all components and APIs of a system must be deployed at the same time, or none at all.

## Component

The Component, the same as the API, have their own version. This allows Components and APIs to be reused in multiple Systems. If the Components and the API would share the version of the system, than all Systems sharing either at least one Component or API would have to have the same versions, to enable proper lifecycle coverage of the Components or APIs when they change.

## API

The API represents any form of communication channel between `Component` resources.

## SystemInstance

## ComponentInstance

## ApiInstance

## Use Cases

This is a list of use cased, used to describe specific setups and how they are modelled in EmELand. They where used to validate the model, but are placed here to help understanding how the model works.

### Deploy from a helm chart.

* A helm chart is parsed to extract the `System`, `API`, and `Component` information. All resources are marked as templates
* Any optional components are grouped into one or more sub-systems, to ensure the the rule, that either all elements of a system must be deployed or none at all.
* the template is deployed. `SystemInstance`, `ApiInstance` and `ComponentInstance` resources are created. They each point to the 
