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

The most simple way to define them, is to manually type out the YAML documents or to created the in a Kubernetes cluster, to be read by the Kubernetes sensor.

### System Template

But more additional sensors for Helm Charts or OCM packages can analyze existing packages and extract System definitions.

But the structural information read from packages can be applied in different forms at multiple points in the system landscape. But since system can have only one parent, a separate mechanism is need to create independent, but identical copies of the structure defined by the package.

This can be realized with two separated System definition: the template resource and a rendered resource.

The template `System` is marked by the following well known annotations:

| **Key** | **Values** | **Description** |
|:-------:|:----------:|:---------------:|
| `emeland.io/p1-system-template`     | `true`, `false`    | the resource is a system template when the value is true. If set to false or the annotation is not set, the resource is standard system resource |
| `emeland.io/p1-system-template-source` | string | An identifying string, e.g. an URL or similar, of the package, that defined a system structure
| `emeland.io/p1-system-template-artifact-id | UUID | An ID referencing the `Artifact` resource of the package

The resulting "rendered" `System` is marked by the following well known annotations:

| **Key** | **Values** | **Description** |
|:-------:|:----------:|:---------------:|
| `emeland.io/p1-system-rendered-from`     | UUID    | Id of the template `System` that this `System` is rendered from.

The elements of the system (`API`, `Component`) must not be re-specified in the rendered `System`. A visualization should render the elements to provider better understanding to human observer.

### Abstract System

An abstract System represents an external system, of which only the API is known. It is identified by the following well known annotations:

| **Key** | **Values** | **Description** |
|:-------:|:----------:|:---------------:|
| `emeland.io/p1-system-abstract`     | `true`, `false`    | the resource is a system template when the value is true. If set to false or the annotation is not set, the resource is standard system |

An abstract ´System` must not have any `Component` resources linked to it.

## Component

The Component, the same as the API, have their own version. This allows Components and APIs to be reused in multiple Systems. If the Components and the API would share the version of the system, than all Systems sharing either at least one Component or API would have to have the same versions, to enable proper lifecycle coverage of the Components or APIs when they change.

## API

## SystemInstance

## ComponentInstance

## ApiInstance
