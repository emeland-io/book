---
title: "Phase 0: Context"
weight: 10
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Phase 0: Context

Contexts are the generic glue to structure all other elements within a large enterprise or even super-enterprise landscape.

![An entity relationship diagram of the entity in phase-0: Context](/docs/model/images/p0-contexts.svg)

Contexts form a hierarchy through a parent-child relationship. Ideally an organization as a whole is described as a tree of contexts. There are very few, ideally only one root context that encompasses the complete organization.

Contexts also play a vital role in ensuring proper life cycle management: As long as the deletion of a context can be detected, the deletion of all resources within that context can be processes correctly. See also the [example implementation](/docs/example-implementation/) for further information.

## Rules

1. A resource may only exist in exactly one context. If a resource needs to be associated with two contexts, two separate resources must be added to the model, and use-case specific information about the digital twins should be added to the resources.