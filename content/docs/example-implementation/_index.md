---
title: "Example Implementation"
weight: 4
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Example Implementation

## Types of Building Blocks

- **Sensor**: gathers information from other software components, databases or file based data. Data and its changes are passed on via events to the building blocks that subscribe to the Sensors.
- **Filter**: registers with one or more other building blocks to receive events on resources seen by those blocks. The filter will then filter, aggregate or annotate the resources in its model. The filter in turn is subscribed to by further building blocks.
- **Injector**: send information to external systems and other software components to be used in business processes of the enterprise.

## Future Developments

### Lifecycle Filter

The filter will track the building blocks that reported on the existence of resources. If a building block is removed from the list of event source that the filter has subscribed to, all resources are marked as deleted. This allows the management of the life cycles of resources, that do not have a running building block any more. 

The filter can also track the freshness of the information for resources and create findings, when the freshness is not sufficient.

#### Well Known Annotation

- `eximpl.emeland.io/last-seen`: a timestamp of the last update or freshness information gathered for the resource (TODO: find ISO number for timestamp format)

### Policy Filter
A filter, that uses policies defined in Rego, the definition language of the Open Policy Agent (OPA), to detect deviations from policy and report it as findings.