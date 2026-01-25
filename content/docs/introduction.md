---
title: "Introduction"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---
# Introduction

## What is EmELand?

The Emerging Enterprise Landscape is an abstract model to structure the data needed to manage a complex integrated enterprise IT landscape.

It defined abstract data objects, their relationships and semantics for manipulation of the created model. This model can then be queried for information about the IT landscape to support efficient management of the landscape itself as well as the digitized business processes that rely on this landscape.

### Why do we need another abstract data model?

An Enterprise Architectures are intended to align and coordinate the information technology (IT) landscape of a business with its business processes, in order to most efficiently support said processes and facilitate communication of vital information between different parts of the enterprise.

But depending on the type of your organization, the processes of your business are not supported by all of the IT you are managing. In an organization that provides IT products, some of the systems in you landscape may be part of the product, some parts may support commercial organization. Only the latter should be considered part of your Enterprise Landscape, while the former are either part of your production management system or customer service data, depending on the type of product. The former only generates deliverables and measurement data, but are not part of your core business process, but rather an input to it.

The differentiation may be appear overly pedantic, but not taking separate view points will result in miscommunication and mode confusion between the business management and product management departments of your organization.

## What is the archetype of your business?

 

- **Hyperscaler**: your central product is IT infrastructure and the processes with operating and maintaining that infrastructure. If you have higher value services e.g. databases or stream processing, they can only be as good as the infrastructure services that you are providing. Should the infrastructure fail, your costs of downtime are only compounded by the downtime costs of your higher layer services.

- **IT Products**: even if you offer your product in the form of a cloud service, it is the features of the database, log aggregator, security scanner, API gateway/catalog, AI API, etc., not the infrastructure it runs on.

- **Non-IT Products**: anything else, even if highly IT bound like banks or insurance company, your business process uses the IT only as a means to an end, not as the core capability of your organization.

## Why you may not need the EmELand

If you already have a working Enterprise Architecture and are satisfied with the insights it provides, then you have already implicitly solved the problem EmELand addresses. There is no benefit gained from changing a working system.

But learning about EmELand may help you talk about your implicit IT management data pipeline. And help you make the gathering of the information more transparent and explicit. It should also help when communicating with colleagues, as well as vendors of IT management products. Maybe even potential customers of the IT management product that you offer to others (that have hopefully read this book).

## Structure of this Book

This book consist of three separate parts:

### Part 1: the Abstract Model

 Gathering information for IT management at enterprise level is never green field project. By the time your organization has somebody thinking about connecting sources of data with points need for consuming this data, you will already have some tooling, some processes and somebody will have locally solved a number of problems. A wide range of people will need to be participating in integrating that information into a single landscape. They need to have a common language in order to be able to communicate in the first place  they needs.

 EmELand proposes a singular model for IT management data, how to structure it, and separates concerns into 9 distinct phases, to allow people to take on the complexity of the effort in discrete steps.

 The design goal of this part is to be able to cover any existing, real world, IT system structure and any information gathering use-case. 

### Part 2: the Example Mapping

The abstract model of part 1 is exactly that: abstract. It does not identify tools, formats, nor semantics on how to manage the model. It is only granular enough to help talking about the information needed to enable efficient communication and an aid to structure the problem space.

The example mapping defines 

* A logical entity model, defining resource relationships.
* Data fields of these entity
* Provides an API, in the form of an OpenAPI 3.0 spec, on how to query the model, should there exist an implementation to hold the information.

The **example** mapping ist **not** a **reference** mapping. It is just one possible way to map the abstract model. It is neither inherently better or more canonical than other mappings. Any integration with a different mapping would require some form of adapter as intended by the hexagonal architecture[^1]. This is intentional and hopefully help the development of integrations between different products and projects to form a EmELand eco-system.

[^1]: [Wikipedia: Hexagonal Architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software))

The design goal of the mapping is to minimize the complexity of the structure (less resource types, less relationship types), but still allow any use-case that can be described in the abstract model of part 1.

### Part 3: the Example Implementation

Testing a concept or a protocol / API should always be done through an actual implementation of the concept. The example implementation is such an implementation of the example mapping from part 2.

The design goal of this implementation is the ability to construct highly complex landscapes form basic building blocks. It does not provide a polished user interface, but is intended to support a maximum in automation for the organisation that deploys it.

## Naming Conventions

|Term | Description |
|---|---|
| Resource | Entities of the EmELand model, which represent elements and structure of the enterprise landscape. |
| Resource Type | The element of the model that represents resources of that type. |

### Type and Object Duality

A number of resource types are structured in a type and object duality (similar to class and object in object oriented programming languages).

The resource types of the type are named with the base name (e.g. `System`, `API`, etc.), the resource type for corresponding object of that type has the name of the base type with the suffix "Instance" attached (i.e. `SystemInstance`, `ApiInstance`, etc.)

Beyond the model, two exceptions to the above rule are introduced by the example mapping: `Node` / `NodeType` and `Finding` / `FindingType`. These resources are not defined by the organization using the model, but rather by the authors of the implementation.

## Principles

* Automation is non-negotiable

## Out of scope

 TODO
