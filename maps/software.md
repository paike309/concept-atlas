# 软件工程地图 · Software Engineering Map

软件工程的概念多数不是"知识"，而是**权衡的记法**。每一条原则背后都有一个具体的失败模式，理解那条失败模式比记住原则名字有用。

这一块只收**跨项目通用**的概念。具体框架、语言特性、部署工具不收——那些属于文档，不属于概念。

> 这张图只画依赖关系。**结构切面**——系统由哪几块组成、每块起什么作用、动一处会牵连哪几处——见 [`docs/system-anatomy.md`](../docs/system-anatomy.md)；按"一条软件从设计到退役"重排的文字版本，以及**数据库与运维在本库的落点和缺口**，见 [`docs/software-composition.md`](../docs/software-composition.md)。

---

## 五条线

```mermaid
flowchart TD
    subgraph G_software["软件工程"]
    n_adr["架构决策记录"]
    n_backpressure["背压与容量"]
    n_changelog["变更日志"]
    n_circuit_breaker["熔断与降级"]
    n_code_review["代码审查"]
    n_composition_over_inheritance["组合优于继承"]
    n_connection_pooling["连接池与容量"]
    n_contract_design["契约与接口设计"]
    n_contract_testing["契约测试"]
    n_dependency_injection["依赖注入"]
    n_dependency_inversion["依赖倒置原则"]
    n_domain_model["领域模型"]
    n_idempotency["幂等性"]
    n_index_and_query_plan["索引与查询计划"]
    n_layered_architecture["分层架构与模块边界"]
    n_normalization["范式化与反范式化"]
    n_observability["可观测性"]
    n_ports_and_adapters["端口与适配器"]
    n_property_based_testing["属性测试"]
    n_replication_and_consistency["复制与一致性模型"]
    n_reproducible_build["可复现构建"]
    n_schema_migration["schema 迁移与版本化"]
    n_semantic_versioning["语义化版本"]
    n_sharding_and_partitioning["分片与分区"]
    n_single_responsibility["单一职责与职责划分"]
    n_technical_debt_refactoring["技术债与重构"]
    n_test_pyramid["测试金字塔"]
    n_timeout_retry_backoff["超时、重试与退避"]
    n_transaction_isolation["隔离级别与并发异常"]
    n_transactions_acid["事务与 ACID"]
    n_unit_testing["单元测试与可测性"]
    n_version_control_branching["版本控制与分支策略"]
    end
    n_changelog --> n_adr
    n_timeout_retry_backoff --> n_backpressure
    n_semantic_versioning --> n_changelog
    n_timeout_retry_backoff --> n_circuit_breaker
    n_version_control_branching --> n_code_review
    n_dependency_inversion --> n_composition_over_inheritance
    n_transactions_acid --> n_connection_pooling
    n_backpressure --> n_connection_pooling
    n_contract_testing --> n_contract_design
    n_test_pyramid --> n_contract_testing
    n_dependency_injection --> n_dependency_inversion
    n_layered_architecture --> n_domain_model
    n_timeout_retry_backoff --> n_idempotency
    n_single_responsibility --> n_layered_architecture
    n_dependency_inversion --> n_ports_and_adapters
    n_layered_architecture --> n_ports_and_adapters
    n_unit_testing --> n_property_based_testing
    n_transaction_isolation --> n_replication_and_consistency
    n_version_control_branching --> n_reproducible_build
    n_version_control_branching --> n_schema_migration
    n_version_control_branching --> n_semantic_versioning
    n_replication_and_consistency --> n_sharding_and_partitioning
    n_code_review --> n_technical_debt_refactoring
    n_transactions_acid --> n_transaction_isolation
    n_test_pyramid --> n_unit_testing
```

---

## 1 设计原则 —— 让变化点待在边界上

设计原则的共同形式是：**把会变的东西推到外面去。**

[依赖注入](../concepts/software/dependency-injection.md) 是这条思路最清晰的例子——它把"用哪个实现"的决定权从被使用者手里搬到调用方。单一职责、依赖倒置、组合优于继承都是同一件事在不同切面上的表述。

判断一条原则该不该在这个项目里用，问一句：**这里有没有第二种实现，或者预计会不会有？** 两个都是否，抽象就只是增加了一层间接。

| 概念 | 卡片 |
|---|---|
| 依赖注入 / 控制反转 | [依赖注入](../concepts/software/dependency-injection.md) |
| 单一职责与职责划分 | [单一职责](../concepts/software/single-responsibility.md) |
| 依赖倒置原则 | [依赖倒置](../concepts/software/dependency-inversion.md) |
| 组合优于继承 | [组合优于继承](../concepts/software/composition-over-inheritance.md) |

---

## 2 结构与边界 —— 改一处不该动全身

这一条线回答的是"**改动的影响半径有多大**"。边界画得对，局部修改不会外溢；画错了，任何小改动都要理解整个系统。

| 概念 | 卡片 |
|---|---|
| 分层架构与模块边界 | [分层架构](../concepts/software/layered-architecture.md) |
| 端口与适配器 | [端口与适配器](../concepts/software/ports-and-adapters.md) |
| 契约与接口设计 | [契约与接口设计](../concepts/software/contract-design.md) |
| 领域模型 | [领域模型](../concepts/software/domain-model.md) |
| 幂等性 | [幂等性](../concepts/software/idempotency.md) |

**分层与端口与适配器的关键差别**：分层把业务放在**最上面**，端口与适配器把业务放在**最里面**。这个视角差异决定了业务逻辑能否脱离入口与外部组件独立测试。

---

## 3 正确性 —— 测试写在哪一层

| 概念 | 卡片 |
|---|---|
| 测试金字塔 | [测试金字塔](../concepts/software/test-pyramid.md) |
| 单元测试与可测性 | [单元测试](../concepts/software/unit-testing.md) |
| 契约测试 | [契约测试](../concepts/software/contract-testing.md) |
| 属性测试 | [属性测试](../concepts/software/property-based-testing.md) |
| 可复现构建 | [可复现构建](../concepts/software/reproducible-build.md) |

[测试金字塔](../concepts/software/test-pyramid.md)是这一条的入口，因为它决定**其它测试怎么安排**：哪个层次多写、哪个层次少写、为什么不能全压在端到端。跳过它直接学"怎么写单元测试"，会得到一堆比例失衡、跑得慢、还不敢改的测试。

一条通用的诊断信号：**如果一个模块改实现就要改大量测试，说明测试绑定了实现细节。**

---

## 4 变更管理 —— 一年后还看得懂吗

| 概念 | 卡片 |
|---|---|
| 版本控制与分支策略 | [版本控制与分支策略](../concepts/software/version-control-branching.md) |
| 代码审查 | [代码审查](../concepts/software/code-review.md) |
| 语义化版本 | [语义化版本](../concepts/software/semantic-versioning.md) |
| 变更日志 CHANGELOG | [变更日志](../concepts/software/changelog.md) |
| 架构决策记录 ADR | [架构决策记录](../concepts/software/adr.md) |
| 技术债与重构 | [技术债与重构](../concepts/software/technical-debt-refactoring.md) |

这一条线的价值随时间显现，所以最容易被跳过。其中两个特殊之处：

- **[ADR](../concepts/software/adr.md) 是收益最高、成本最低的一条**：几行字，替代的是未来一次完整的重新论证
- **[变更日志](../concepts/software/changelog.md) 里"弃用"是最有价值的一类**：它给出迁移窗口。跳过弃用直接破坏是变更管理里代价最高的做法

---

## 5 运行 —— 上线之后才是开始

| 概念 | 卡片 |
|---|---|
| 可观测性（日志 / 指标 / 追踪） | [可观测性](../concepts/software/observability.md) |
| 超时、重试与退避 | [超时、重试与退避](../concepts/software/timeout-retry-backoff.md) |
| 熔断与降级 | [熔断与降级](../concepts/software/circuit-breaker.md) |
| 背压与容量 | [背压与容量](../concepts/software/backpressure.md) |

**这一条线与 [Agent 地图](agent.md) 直接重叠。** 轨迹日志、循环超时、工具调用的幂等与重试，本质是普通后端工程搬到 Agent 上。不熟悉这一条线，Agent 就只能停在 demo 阶段。

一条贯穿这一块的判断：**重试、熔断、背压三者是配套的**。单独用任一个都会出问题——重试会放大故障，熔断需要降级才有意义，背压需要每层都配合。

---

## 一个提醒

这张地图刻意不收框架和工具。判断标准：**换一个语言或框架之后，这个概念还成立吗？** 成立就收，不成立就不收。

所以这里没有 Spring、没有 React、没有 Kubernetes。它们是好工具，但它们是文档的内容，不是概念的内容——而文档随时会变，概念不会。
