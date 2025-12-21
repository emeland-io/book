---
title: "Phase 3: Offering Capabilities"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---
# Phase 3: Offering Capabilities

![An entity relationship diagram of the entities in phase-3: Feature, FeatureVersion, Variant, Dependency, ValidValue, Order, OrderItem, BoundValue, Parameter](images/p3-features.svg)

Offering the capabilities provided by your IT system as Features makes them available for consumption. When a Feature is ordered for use by a customer, it is then tracked as an Order.

Features describe individual elements that can be ordered by customers. The customer may be external, i.e.  paying customer that purchase your service. Or they may be internal to your organisation, e.g. a different department than the one offering the service. Features can and should also hide the complexity of the How from customer by offering a pre-defined set of capabilities.

When Features are offered to external customers, they are an deliverable artefact of classical product management: What do you want to sell. But they also help structure the follow-up question: *what is needed to provide that product to the customer?* And then internally the question: *what do we need to provide these elements?*

*Example: You offer dedicated mail servers as a service (in contrast to integrated services like GMail). One such service instance needs the actual mail server. But dependent on the maximum number of concurrent users it will also need a number of support services and components. In addition it always requires various elements like storage budgets and network capabilities, e.g. DNS entries, IP-address spaces, and bandwidth allocations. All of these elements are represented as Features. Anything from sets of instances of the actual server software, running parallel for scaling and high availability, down to individual database records representing firewall rules or DNS name records.*

A collection of Features is needed to provide the end product. To define this, Features have dependencies. These form a directed acyclic graph of Features that need to be available and functioning for the end production to be available for use by the customer.

Features also have Parameters that serve three purposes:

1. Allow the customization of the Feature, either by the customer, or by other Features that request the given one through a dependency
2. Describe relevant aspects of the Feature, e.g. does it meet regulatory standards
3. Is it capable of meeting some metric. In the above mail server example this may be the supported maximum of concurrent users.

The Parameters define these aspects and metrics and define a set of valid values. Each Feature then offers these values of the Parameters, potentially as restricted subset. 

Ordering Features may or may not involve a financial transaction, but that is a business process, which is beyond the scope of EmELand.

## Feature

### Parameters

Scalar parameter values are not the exact value of the system, but rather define an upper bound. E.g. if you order a virtual machine (VM) with 8 GB of RAM, than this does not signify that exactly 8 GBs are used, but rather that this is an acceptable design limit. Following the same pattern, you would not order a distributed system that will support exactly 10001 users, but rather select the smallest value, which is bigger than your requirement.
Usually this value represents architectural limits. In order to overcome them a much more complex or expensive system architecture would be needed.

This is the reason why usually a few scalar values are given as selectable values for Parameters.

Naming is hard! Therefore there may be more than one Parameter with the same DisplayName. But it is important to understand, that only if two parameters on two Capabilities are identified by the same ParameterId they are the same. In this case they must mean **exactly** the same for both Capabilities

### Variants

## Intent

## Mapping to Running Systems
