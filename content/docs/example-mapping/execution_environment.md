---
title: "Execution Environment"
weight: 20
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
---

# Execution Environment

While the example mapping does not defined how the software to run EmELand is implemented, it does make an assumption about the generation structure of the deployment: any implementation of the example mapping would be a set of cooperating pieces of software that communicate via the web API defined by the OpenAPI spec found at [https://github.com/emeland-io/openapi](https://github.com/emeland-io/openapi)

![an entity relationship diagram of the two elements of the EmELand execution environment: Node, NodeType](../images/execution_environment.svg)
