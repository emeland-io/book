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

The resources for identity and access management cover three areas, which are tightly coupled:

- **The identity of entities** that operate within the landscape. These can be separated into three groups: a) natural entities, b) machine entities, and c) legal entities. While the two former are represented by the `Identity` resource type, `OrgUnit` represents the former.
- **Permissions** granted to perform certain actions and **roles** that group multiple of these permissions with objects which they apply. In order to track the origin of multiple permissions granted in multiple systems (e.g. the same `ClusterRole` RBAC definition in multiple Kubernetes clusters), EmELand separates the organizational definition of roles and permissions from the useable realization in the working IT landscape. The former are defined through the `RoleSpec` and `PermissionSpec` resources respectively. The latter through the `Role` and ´Permission` resource types. `RoleSpec` and `PermissionSpec` form a requirement, Role and Permission realize them within a context. Example: in Kubernetes RBAC a role must be defined in each cluster separately. The permissions are defined in the contents of the `Role` and `ClusterRole` Kubernetes resources.

  EmELand components and sensors that work with systems, that have implicit or hard coded permissions, should defined both the `Spec` as well as the actual realized resource.

- **Bindings** are used to links identities and groups with roles.

**Note:** Typically bindings consist of three fields: subject (the entity or collections of entities to which the permission is granted), verb (the operation or permission which is allowed), and the object (the resource, data or system for which the permission is granted to the subject). Currently the EmELand abstract model does not cover how the object of a binding is specified. This must be defined by the either the mapping or be implmentation specific. This may change in the future.

![An entity relationship diagram of the entities in phase-2: OrgUnit, Identity, Group, Binding, RoleSpec, PermissionSpec, Role, Permission](../images/p2-iam.svg)


## Points for later extension / discussion

The Binding lacks the documentation why it exists, in contrast to the duality of almost all others entities. While there is only one Identity, it is backed by the real world principal that it represents within the system. A similar argument can be made for the OrgUnit.

The Group and Binding need very careful tracking of who requested them. But so far, no obvious entity for modelling the duality of request and fulfillment for Group and Binding has presented itself.
