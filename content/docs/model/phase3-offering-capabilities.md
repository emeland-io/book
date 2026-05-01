---
title: "Phase 3: Offering Capabilities"
weight: 40
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---
# Phase 3: Offering Capabilities

![An entity relationship diagram of the entities in phase-3: Capability, CapabilityVersion, Variant, Dependency, ValidValue, Order, OrderItem, BoundValue, Parameter](/docs/model/images/p3-capabilities.svg)

Offering the capabilities provided by your IT system makes them available for consumption. When a Capability is ordered for use by a customer, it is then tracked as an Order.

Capabilities describe individual elements that can be ordered by customers. The customer may be external, i.e.  paying customer that purchase your service. Or they may be internal to your organization, e.g. a different department than the one offering the service. Capabilities can and should also hide the complexity of the **HOW** from customer, by offering a pre-defined set of capabilities.

When Capabilities are offered to external customers, they are an deliverable artefact of classical product management: Something you want to sell. But they also help structure the follow-up question: *what is needed to provide that product to the customer?* And then internally the question: *what do we need to provide these elements?*

*Example: You offer dedicated mail servers as a service (in contrast to integrated services like GMail). One such service instance needs the actual mail server. But dependent on the maximum number of concurrent users it will also need a number of support services and components. In addition it always requires various elements like storage budgets and network capabilities, e.g. DNS entries, IP-address spaces, and bandwidth allocations. All of these elements are represented as Capability. Anything from sets of instances of the actual server software, running parallel for scaling and high availability, down to individual database records representing firewall rules or DNS name records.*

A collection of Capabilities is needed to provide the end product. To define this, Capabilities have dependencies. These form a directed acyclic graph of Capabilities that need to be available and functioning for the end production to be available for use by the customer.

Capabilities also have Parameters that serve three purposes:

1. Allow the customization of the Capability, either by the customer, or by other Capabilities that request the given one through a dependency
2. Describe relevant aspects of the Capability, e.g. does it meet regulatory standards
3. Is it capable of meeting some metric. In the above mail server example this may be the supported maximum of concurrent users.

The Parameters define these aspects and metrics and define a set of valid values. Each Capability then offers these values of the Parameters, potentially as restricted subset. 

Ordering Capabilities may or may not involve a financial transaction, but that is a business process, which is beyond the scope of EmELand.

## Intent

The Capabilities represent what the system **could** provide, if ordered to. The complexity of the provided elements may be anything from single lines in a configuration file (e.g. a firewall rule) to highly complex, geo-replicated IT systems (e.g. a dedicated instance of a mail service for multiple thousands of users, spanned over multiple cloud regions and cloud providers.)

The defining characteristic for a capability is the fact that it will provide a function of value to the entity which orders it, and that it can be provided on request.

The function of value does not have to be provided in isolation, as a more or less long chain of other Capabilities may need to be ordered, before the function can be provided. The dependencies define not only these other Capabilities, but also which values to which Parameters are mapped from one Capability to the next along the directed acyclic graph spanned among the dependencies.

### Capability

A single functionality that provides value to an entity that orders it.

It is versioned and the versions each have a lifecycle.

### Parameter

Scalar parameter values are not the exact value of the system, but rather define an upper bound. E.g. if you order a virtual machine (VM) with 8 GB of RAM, than this does not signify that exactly 8 GBs are used, but rather that this is an acceptable design limit. Following the same pattern, you would not order a distributed system that will support exactly 10001 users, but rather select the smallest value, which is bigger than your requirement.
Usually this value represents architectural limits. In order to overcome them a much more complex or expensive system architecture would be needed.

This is the reason why usually a few scalar values are given as selectable values for Parameters.

Naming is hard! Therefore there may be more than one Parameter with the same DisplayName. But it is important to understand, that only if two parameters on two Capabilities are identified by the same ParameterId they are the same. In this case they must mean **exactly** the same for both Capabilities

### Variants

Variants allow the definition of different dependencies, based on the values requested through the Order. (e.g. a mail server for 10 Users may have a radically different architecture the one for 100k users.)

## Reification

Only when a capability is ordered, will it become real and provide value to the ordering entity.

### Order

Tracks the Capabilities ordered by an OrgUnit.

### Order Item

In order to determine which Order Items are needed to fulfill the order. To achieve this, a software would walk the graph of the Capabilities and identify a valid combination of Variants, resulting dependencies and selected Parameter values.

The Order Item keeps track of the Capabilities selected, as well as the parameters and specific values bound for the order.


## Mapping to Running Systems

The Order Items can be referenced by System Instances when actually creating running systems.

The actual implementation must also keep track of the Contexts in which the order item is fulfilled. This will set a number of parameters like the physical (or logical) location, the capacity or regulatory domains.

Selection of the context can be dependent on a number factors, but the Org Unit that issued the Order is usually among them.