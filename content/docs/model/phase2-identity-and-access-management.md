---
title: "Phase 2: Identity and Access Management (IAM)"
weight: 30
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Phase 2: Identity and Access Management (IAM)

![An entity relationship diagram of the entities in phase-2: OrgUnit, Identity, Group, Binding, RoleSpec, PermissionSpec, Role, Permission](images/p2-iam.svg)

## Points for later extension / diskussion

The Binding lacks the documentation why it exists, in contrast to the duality of almost all others entities. While there is only one Identity, it is backed by the real world principal that it represents within the system. A similar argument can be made for the OrgUnit.

The Group and Binding need very careful tracking of who requested them. But so far, no obvious entity for modelling the duality of request and fulfillment for Group and Binding has presented itself.
