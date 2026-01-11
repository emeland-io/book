---
# cSpell:enable

title: "Common Elements of Model Objects"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Common Elements of Model Objects

All Elements of the abstract models are Reference Objects as defined by the DDD book[^ddd], unless noted otherwise. Therefore each element will have a) an UUID as unique identifier and b) a display name, to help humans identify the element. These to attributes are not shown in the diagrams in this chapter, as they are primarily a technical details. 

See the [Chapter on the example reference](/docs/example-mapping/) for an example on how to map the abstract EmeLand model to a useable data model.

The following sections in this chapter will not reiterate the common elements, but rather focus on the specific aims of each of the phases.

## Minimal Viable Structure

The structure of the EmELand data model is designed to support all needs of end-to-end IT management. Aspects of this are reflected in the individual phases, described in the following sub-sections of this chapter. But the aim is not to support the copying of data from every pre-existing data structure in all existing IT management software solution into EmELand. 

But rather the underlying design question is this: Can I design two transformation function `inputFunc()` and `outputFunc()`, such that any existing IT Management data can be transformed to fit into the EmELand model structure, as well any data in EmELand be transformed into potentially existing IT management solutions

EmELand defines just as much structure as is necessary to model the use-case identified by the authors to date. This means that data and processes, already present in an organization, may need to be transformed when exporting into other tools. But the data gathered in the model can fullfil any requirements for information set by external tools or processes 

## Rules

The "correctness" of the model is defined by a number of rules, each specific to the Phases that they are assigned to, as well one of four layers:

1. **Fundamental Invariants**: these define the structure of the EmELand data model. Fixing them may be a prerequisite for later analysis to work correctly. E.g. the same UUID being used for multiple resources.
1. **Technological Requirements**: In order for Kubernetes resources to be associated within the EmELand model, they have to carry certain Annotations. 
1. **Regulation, Legal Compliance**: Observed rules that are set by entities external to the organization. Examples include network designs rules by PCI DSS, or methods of calculating risk for the Sarbanes-Oxley act.
1. **Organizational Rules, Business Rules**: Any additional rule that is set by the organization.

If IT resources should not follow the rules, the model does not break or become unwieldy as a whole. Rather,
deviations from these rules are tracked as Findings. A notification of a newly detected finding is sent to the owner of the resource or any other person, role or organizational unit, that is able to act to remedy the deviation.

Some of the rules for the first bullet point is given in the following sections on specific phases. More are given in the [Chapter on the example reference](/docs/example-mapping/). Additional one are set by any orgnization using EmELand for IT management.



[^ddd]: "Domain Driven Design: Tackling Complexity in the Heart of Software", Eric Evans, 2004, Addison-Wesley, ISBN-13: 978-0-321-12521-7