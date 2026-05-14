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

![An entity relationship diagram of the entities in phase-3: Capability, CapabilityVersion, Variant, Dependency, ValidValue, Order, OrderItem, BoundValue, Parameter](../images/p3-capabilities.svg)

Offering the capabilities provided by your IT system makes them available for consumption. When a Capability is ordered for use by a customer, it is then tracked as an Order.

Capabilities describe individual elements that can be ordered by customers. The customer may be external, i.e.  paying customer that purchase your service. Or they may be internal to your organization, e.g. a different department than the one offering the service. Capabilities can and should also hide the complexity of the **HOW** from customer, by offering a pre-defined set of capabilities.

When Capabilities are offered to external customers, they are an deliverable artifact of classical product management: Something you want to sell. But they also help structure the follow-up question: *what is needed to provide that product to the customer?* And then internally the question: *what do we need to provide these elements?*

*Example: You offer dedicated mail servers as a service (in contrast to integrated services like GMail). One such service instance needs the actual mail server. But dependent on the maximum number of concurrent users it will also need a number of support services and components. In addition it always requires various elements like storage budgets and network capabilities, e.g. DNS entries, IP-address spaces, and bandwidth allocations. All of these elements are represented as Capabilities. Anything from sets of instances of the actual server software, running parallel for scaling and high availability, down to individual database records representing firewall rules or DNS name records.*

A collection of Capabilities is needed to provide the end product. To define this, Capabilities have dependencies. These form a directed acyclic graph of Capabilities that need to be available and functioning for the end production to be available for use by the customer.

Capabilities also have Parameters that serve three purposes:

1. Allow the customization of the Capability, either by the customer, or by other Capabilities that request the given one through a dependency
2. Describe relevant aspects of the Capability, e.g. does it meet regulatory standards
3. Is it capable of meeting some metric. In the above mail server example this may be the supported maximum of concurrent users.

The Parameters define these aspects and metrics and define a set of valid values. Each Capability then offers these values of the Parameters, potentially as restricted subset. 

Ordering Capabilities may or may not involve a financial transaction, but that is a business process, which is beyond the scope of EmELand. EmELand only tracks what a valid order consist of, and if there are components of the landscape that only exist becaus of an order. This makes it possible to establish a reason for being for each element of the overall IT landscape. And every thing that has no documented reason for being should be a candidate for either deletion or at least scrutiny by the operations team. Or the CISO, Controlling or Internal Revision, depending on the style of your organization.

## Intent

The Capabilities represent what the system **could** provide, if ordered to. The complexity of the provided elements may be anything from single lines in a configuration file (e.g. a firewall rule) to highly complex, geo-replicated IT systems (e.g. a dedicated instance of a mail service for multiple thousands of users, spanned over multiple cloud regions and cloud providers.)

The defining characteristic for a capability is the fact that it will provide a function of value to the entity which orders it, and that it can be provided on request.

The function of value does not have to be provided in isolation, as a more or less long chain of other Capabilities may need to be ordered, before the function can be provided. The dependencies define not only these other Capabilities, but also which values to which Parameters are mapped from one Capability to the next along the directed acyclic graph spanned among the dependencies.

### Capability

A single functionality that provides value to any entity that orders it.

It is versioned and the versions each have a lifecycle. The lifecycle defines the timeframe through which the Capability will be available to order and through which it will be provided to the entities who ordered it.

### Variants

Dependencies between Capabilities are not linked directly, but rather through Variants, in order enable the modelling of dependencies differing when providing different values of parameters.

*Example: A mail server for 10 concurrent users will need a radically different architecture and thus have differing dependencies to databases, storage and any further ancillary functions, when compared with a provider scale mail server for 10 million users.*

### Parameter

Grouping of Values. Each Parameter defines a set of ValidValues that are possible values for that parameter. 

Naming is hard! Therefore there may be more than one Parameter with the same DisplayName. But it is important to understand, that only if two parameters on two Capabilities are identified by the same ParameterId they are the same. In this case they must mean **exactly** the same for both Capabilities

The Capabilities and Variants define subsets of valid values for a given Parameter when they define what they provide and require respectively. A dependency of a Variant to a Capability can only be valid, if the Capability offers a superset of the values that the Variant requires for each of the Parameters separately.

### ValidValues

Specific values that are valid for a parameter. In order to limit the complexity of tracking the values, these are not modeled as types of potentially unbound scalar values, but rather sets of 

Scalar parameter values are usually not the exact value of the system, but rather define an upper bound. E.g. if you order a virtual machine (VM) with 8 GB of RAM, than this does not signify that exactly 8 GBs are used, but rather that this is an acceptable design limit. Following the same pattern, you would not order a distributed system that will support exactly 10001 users, but rather select the smallest value, which is bigger than your requirement.
Often this value represents architectural limits. In order to overcome them a much more complex or expensive system architecture would be needed.

This is the reason why usually a few scalar values are given as selectable values for Parameters.

## Reification

Only when a capability is ordered, will it become real and provide value to the ordering entity.

### Order

Tracks the Capabilities ordered by an OrgUnit. The existence of an entity of this type represents that all organizational and commercial processes have been completed and the the landscape should provide this value to the OrgUnit that ordered it.

### Order Item

In order to determine which Order Items are needed to fulfill the order. To achieve this, a software would walk the graph of the Capabilities and identify a valid combination of Variants, resulting dependencies and selected Parameter values.

The OrderItem defines the list Capabilities selected, as well as specific values bound for the order for each of the parameters offered by the selected Capabilities.

## Mapping to Running Systems

The Order Items can be referenced by [System Instances](phase1-system-structure/#system-and-systeminstance) when fulfilling the order does actually creates a running systems. System Instances that hold multiple orders or tenants to which orders belong, should not be marked as belonging to that order, but rather an original order to provide that multi-tenant system.

The actual implementation must also keep track of the (Contexts)[phase0-context] in which the order item is fulfilled. This will set a number of parameters like the physical (or logical) location, the capacity or regulatory domains.

Selection of the context can be dependent on a number factors, but the Org Unit that issued the Order is usually among them.