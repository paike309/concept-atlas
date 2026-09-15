# 软件工程组成总览 · Software Engineering Composition

这份文档回答一个问题：**做一套软件，从头到尾需要哪些概念，每一部分起什么作用。**

它是 [`maps/software.md`](../maps/software.md) 那张依赖图的**文字版**。与另外两份组成总览不同的是，这一份额外回答了"**数据库、运维这些日常绕不开的东西，在库里落在哪**"——答案里包含**真实的缺口**，见下方专节。

> **定位**：结构地图，不是事实依据。内容整理自 [`concepts/software/`](../concepts/software/) 下的卡片，目前信源等级均为 `link-checked`（来源链接已核验可达性与标题，正文表述与来源原文尚未逐条比对）。**2026-09-16 更新：本文原先指出的数据库、运维等缺口已全部补卡，相关缺口节已改为"已覆盖"。**

---

## 一句话总述

**软件工程的概念多数不是"知识"，而是权衡的记法。**

每一条原则背后都有一个具体的失败模式，**理解那条失败模式比记住原则名字有用**。这也是为什么本库讲"单一职责"时会讲到"改一处要动全身"，讲"熔断"时会讲到"重试会放大故障"。

还有一条收录原则必须知道：**只收跨项目通用的概念**。判断标准是——**换一个语言或框架之后，这个概念还成立吗？** 成立就收，不成立就不收。所以库里没有 Spring、没有 React、没有 Kubernetes。

---

## 从头到尾：一条软件的生命周期需要什么

按时间顺序排（库里原始分组见"库里的分组"列）：

| 阶段 | 这一步要回答的问题 | 库里的分组 | 概念 |
|---|---|---|---|
| **1 设计：让变化点待在边界上** | 这里会不会有第二种实现？抽象值不值？ | 设计原则 | [依赖注入](../concepts/software/dependency-injection.md) · [单一职责](../concepts/software/single-responsibility.md) · [依赖倒置](../concepts/software/dependency-inversion.md) · [组合优于继承](../concepts/software/composition-over-inheritance.md) |
| **2 结构与边界：改一处不该动全身** | 改动的影响半径有多大？ | 结构与边界 | [分层架构](../concepts/software/layered-architecture.md) · [端口与适配器](../concepts/software/ports-and-adapters.md) · [领域模型](../concepts/software/domain-model.md) · [契约与接口设计](../concepts/software/contract-design.md) |
| **3 正确性：测试写在哪一层** | 凭什么说它对？ | 正确性 | [测试金字塔](../concepts/software/test-pyramid.md) · [单元测试与可测性](../concepts/software/unit-testing.md) · [契约测试](../concepts/software/contract-testing.md) · [属性测试](../concepts/software/property-based-testing.md) |
| **4 变更与发布：一年后还看得懂吗** | 改动怎么安全进主线、怎么让人看懂 | 变更管理 | [版本控制与分支策略](../concepts/software/version-control-branching.md) · [代码审查](../concepts/software/code-review.md) · [语义化版本](../concepts/software/semantic-versioning.md) · [变更日志](../concepts/software/changelog.md) · [架构决策记录 ADR](../concepts/software/adr.md) · [可复现构建](../concepts/software/reproducible-build.md) |
| **5 运行：上线之后才是开始** | 跑起来之后出问题怎么办？ | 运行 | [可观测性](../concepts/software/observability.md) · [超时、重试与退避](../concepts/software/timeout-retry-backoff.md) · [熔断与降级](../concepts/software/circuit-breaker.md) · [背压与容量](../concepts/software/backpressure.md) · [幂等性](../concepts/software/idempotency.md) |
| **6 长期维护：还改得动吗** | 当初的取舍现在还剩多少价值？ | 变更管理 | [技术债与重构](../concepts/software/technical-debt-refactoring.md) |

> 表中「库里的分组」列指的是**原有五条线**。第四批补的四组（数据与一致性、安全、运维与发布、并发性能与协议）不在这条时间轴上——它们是横跨各阶段的能力，见下方「九组总览」。

### 一个容易误读的地方

**「前置」链是按"读得懂的前置"排的，不是按时间排的。** 典型例子是 [ADR](../concepts/software/adr.md)：它在依赖图上位于很靠后（前置是[变更日志](../concepts/software/changelog.md)），但它**实际发生得最早**——第一个重要决定就该记。同理，[可复现构建](../concepts/software/reproducible-build.md)在库里的分组是「正确性」（因为它回答"这个产物可信吗"），但它实际属于发布环节，前置是[版本控制与分支策略](../concepts/software/version-control-branching.md)。

所以：**依赖图给的是阅读顺序，不是施工顺序。**

---

## 九组总览（库里的分组）

| 组 | 它在回答什么 | 卡片数 |
|---|---|---|
| **设计原则** | 让变化点待在边界上 | 4 |
| **结构与边界** | 改一处不该动全身 | 5 |
| **正确性** | 测试写在哪一层 | 5 |
| **变更管理** | 一年后还看得懂吗 | 6 |
| **运行** | 上线之后才是开始 | 4 |
| **数据与一致性** | 什么必须一次成功、什么可以晚一点一致 | 8 |
| **安全** | 谁可以做什么、数据被拿到会怎样 | 4 |
| **运维与发布** | 改完怎么发、出事怎么办 | 7 |
| **并发、性能与协议** | 同时发生时怎么不乱、慢了去哪里找 | 5 |

后四组是第四批缺口登记之后补的（此前本库没有任何数据库、安全、运维卡片）。**它们与前面五条线的性质不同**：前五条线是"一条软件的生命周期"，后四组是**横跨每个阶段的能力**——所以它们不在开头那张生命周期表的时间轴上。

层级分布（截至 2026-09-16）：**基础 20 / 进阶 23 / 前沿 5**。

> 本文按"一条软件从头到尾"排。同一个对象的**结构切面**——它由哪几块组成、每块起什么作用、动一处会牵连哪几处——见 [`system-anatomy.md`](system-anatomy.md)。

---

## 逐组：每张卡起什么作用

### 1 设计原则 —— 让变化点待在边界上（4）

共同形式是：**把会变的东西推到外面去。**

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [依赖注入](../concepts/software/dependency-injection.md) | 协作者由外部传入而不是内部构造——**把"用谁"的决定权从被使用者交给调用方**。与 DI 容器的区别：DI 是模式，容器是工具 | 基础 | 无 |
| [单一职责与职责划分](../concepts/software/single-responsibility.md) | 一个模块应该有且只有一个引起它变化的原因。内聚与耦合是同一件事的两面 | 基础 | 无 |
| [依赖倒置原则](../concepts/software/dependency-inversion.md) | 高层与低层都依赖抽象。原方向 A→B 倒置为 A→I←B，**改动不再沿依赖方向传播** | 基础 | 依赖注入 |
| [组合优于继承](../concepts/software/composition-over-inheritance.md) | 优先用组合构建行为，因为组合可在**运行时替换**，继承在编译期定死 | 基础 | 依赖倒置原则 |

> 判断一条原则该不该用，问一句：**这里有没有第二种实现，或者预计会不会有？** 两个都是否，抽象就只是增加了一层间接。

### 2 结构与边界 —— 改一处不该动全身（5）

这一组回答"**改动的影响半径有多大**"。

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [分层架构与模块边界](../concepts/software/layered-architecture.md) | 按抽象层次切分（表现层/应用层/领域层/基础设施层）并规定层间依赖方向 | 基础 | 单一职责 |
| [端口与适配器](../concepts/software/ports-and-adapters.md) | 应用核心放中心，外部通过"端口"（核心定义的接口）与"适配器"（具体实现）接入 | 进阶 | 依赖倒置原则 · 分层架构 |
| [领域模型](../concepts/software/domain-model.md) | 用对象与关系表达业务概念与规则，**让业务规则集中在领域对象里** | 前沿 | 分层架构 |
| [契约与接口设计](../concepts/software/contract-design.md) | 接口设计时明确输入输出约定——必填与可选、取值范围、错误语义、**幂等性**、兼容性承诺 | 进阶 | 契约测试 |
| [幂等性](../concepts/software/idempotency.md) | 一个操作重复执行多次与执行一次效果相同。**是重试的前提**——没有它，重试就是在制造重复副作用 | 进阶 | 超时、重试与退避 |

> **分层与端口与适配器的关键差别**：分层把业务放在**最上面**，端口与适配器把业务放在**最里面**。这个视角差异决定了业务逻辑能否脱离入口与外部组件独立测试。

### 3 正确性 —— 测试写在哪一层（5）

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [测试金字塔](../concepts/software/test-pyramid.md) | 按粒度分层组织自动化测试——底层多、中层适量、顶层少。**它决定其它测试怎么安排** | 基础 | 无 |
| [单元测试与可测性](../concepts/software/unit-testing.md) | 隔离外部依赖验证单个逻辑单元；同时定义为支撑它所需的设计性质 | 基础 | 测试金字塔 |
| [契约测试](../concepts/software/contract-testing.md) | 验证两个组件对它们之间**接口的理解是否一致**，通常由使用方驱动 | 进阶 | 测试金字塔 |
| [属性测试](../concepts/software/property-based-testing.md) | 声明应满足的通用性质，由工具生成大量随机输入寻找反例 | 前沿 | 单元测试与可测性 |
| [可复现构建](../concepts/software/reproducible-build.md) | 相同源码与配置，在任意时间、任意机器产出**完全相同**的产物 | 前沿 | 版本控制与分支策略 |

> 一条通用诊断信号：**如果一个模块改实现就要改大量测试，说明测试绑定了实现细节。**

### 4 变更管理 —— 一年后还看得懂吗（6）

这一组的价值随时间显现，所以最容易被跳过。

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [版本控制与分支策略](../concepts/software/version-control-branching.md) | 用历史记录变更、用分支隔离并行工作、用合并策略把变更汇入主线 | 基础 | 无 |
| [代码审查](../concepts/software/code-review.md) | 合并前由他人检查，目标是发现缺陷、传播知识、统一约定 | 基础 | 版本控制与分支策略 |
| [语义化版本](../concepts/software/semantic-versioning.md) | 用「主版本.次版本.修订号」表达**兼容性契约** | 基础 | 版本控制与分支策略 |
| [变更日志](../concepts/software/changelog.md) | 按版本记录**面向使用者**（而非开发者）的变更说明 | 基础 | 语义化版本 |
| [架构决策记录 ADR](../concepts/software/adr.md) | 把一次重要技术决策的背景、选项、结论与后果记成简洁文档 | 基础 | 变更日志 |
| [技术债与重构](../concepts/software/technical-debt-refactoring.md) | 技术债是为短期收益接受的长期成本；重构是**不改变外部行为**的前提下改善结构。**重写不是重构** | 基础 | 代码审查 |

> 两个特殊之处：**[ADR](../concepts/software/adr.md) 是收益最高、成本最低的一条**（几行字替代未来一次完整的重新论证）；**[变更日志](../concepts/software/changelog.md) 里"弃用"是最有价值的一类**（它给出迁移窗口）。

### 5 运行 —— 上线之后才是开始（4）

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [可观测性](../concepts/software/observability.md) | 通过日志、指标、追踪三类信号，使系统内部状态可被外部推断。**关联标识（request ID）是它们能串起来的前提** | 基础 | 无 |
| [超时、重试与退避](../concepts/software/timeout-retry-backoff.md) | 处理外部调用失败的三件套——超时（放弃等待）、重试（重新尝试）、退避（拉长间隔） | 基础 | 无 |
| [熔断与降级](../concepts/software/circuit-breaker.md) | 连续失败达阈值时暂时直接拒绝（快速失败），探测恢复后重新放行。**把等待变成快速失败** | 进阶 | 超时、重试与退避 |
| [背压与容量](../concepts/software/backpressure.md) | 下游处理不过来时主动向上游传递压力，避免系统内部无限积压 | 进阶 | 超时、重试与退避 |

> 一条贯穿这一组的判断：**重试、熔断、背压三者是配套的。** 单独用任一个都会出问题——重试会放大故障，熔断需要降级才有意义，背压需要每层都配合。

---

## 数据库在哪里

**这一块已经从"零卡片"补齐到 8 张。**

按本文开头那条标准（"换一个语言或框架之后，这个概念还成立吗？"），**事务、隔离级别、索引、范式化、一致性模型、分片**都应当收录——它们不依赖具体数据库产品。按原则**不应该**收录的是 MySQL / PostgreSQL / Redis 这类具体产品。

现状（全部已写）：

| 分组 | 条目 |
|---|---|
| **单库（4）** | [事务与 ACID](../concepts/software/transactions-acid.md) · [隔离级别与并发异常](../concepts/software/transaction-isolation.md) · [索引与查询计划](../concepts/software/index-and-query-plan.md) · [范式化与反范式化](../concepts/software/normalization.md) |
| **分布式（4）** | [复制与一致性模型](../concepts/software/replication-and-consistency.md) · [分片与分区](../concepts/software/sharding-and-partitioning.md) · [schema 迁移与版本化](../concepts/software/schema-migration.md) · [连接池与容量](../concepts/software/connection-pooling.md) |

为什么必须成对补齐：**隔离级别保证的是"一个数据库内部"的并发语义；数据一旦分布在多个节点上，"一致性"换了一套定义**，前者不再覆盖后者。只补单库那一半，会得到一个"看起来讲了一致性、实际只讲了单机"的错觉。

另外两处与数据打交道、可对照读的卡片：[幂等性](../concepts/software/idempotency.md)（重复执行的语义——"写两次等于写一次"，重试能成立的前提）与 Agent 域的[结构化状态与外部存储](../concepts/agent/structured-state.md)（状态怎么落到外部结构化记录里）。

缺口条目已登记在[清单](../roadmap.md)的「缺口登记（第四批）」。

---

## 运维在哪里

运维在本库里被**拆在两处，且都只是部分覆盖**：

| 拆在哪 | 覆盖内容 | 缺什么 |
|---|---|---|
| 「运行」组 | [可观测性](../concepts/software/observability.md) · [超时重试退避](../concepts/software/timeout-retry-backoff.md) · [熔断降级](../concepts/software/circuit-breaker.md) · [背压容量](../concepts/software/backpressure.md) —— 即**可靠性与容量**这一半 | 容量规划、值班与告警、事故响应 |
| 「变更管理」组 + [可复现构建](../concepts/software/reproducible-build.md) | [版本控制与分支策略](../concepts/software/version-control-branching.md) · [语义化版本](../concepts/software/semantic-versioning.md) · [变更日志](../concepts/software/changelog.md) · 构建产物一致性 —— 即**发布与变更**这一半 | 发布策略本身 |

**缺口条目（可作为 roadmap 候补）**：部署与发布策略（灰度 / 金丝雀 / 蓝绿 / 回滚）· SLO 与错误预算 · 告警阈值与值班轮换 · 配置与密钥管理 · 基础设施即代码 · 事故响应与复盘 · 容量规划与成本核算。

---

## 本库未覆盖的其他部分

除上面两节，还有几类跨项目通用、但库里没有的概念：

- **安全**：认证、授权、加密、输入校验、依赖供应链。库里的[权限与最小授权](../concepts/agent/least-privilege.md)属 Agent 域，软件工程域没有对应卡片。
- **并发与一致性**：锁、竞态、内存模型、Actor 模型。
- **性能工程**：profiling、缓存策略、批处理、延迟预算。
- **网络与 API 风格**：REST / gRPC 的取舍、幂等键、限流。[契约与接口设计](../concepts/software/contract-design.md)只触及"约定"层面。
- **构建与依赖管理**：锁定版本、依赖图、供应链可信。[可复现构建](../concepts/software/reproducible-build.md)触及一部分。

上面三节的缺口**已登记进[清单](../roadmap.md)的「缺口登记（第四批）」**，软件工程域因此记为「待写 24」。登记之前那一栏写的是「待写 0」——那与本节的缺口是矛盾的。**清单与正文说同一件事，这个矛盾才算真正关掉。**

---

## 从哪读起

按「前置」拓扑排，一条不跳级的顺序（前 8 张能覆盖主干）：

| 顺序 | 卡片 | 为什么排这里 |
|---|---|---|
| 1 | [依赖注入](../concepts/software/dependency-injection.md) | 无前置；设计原则的原型 |
| 2 | [单一职责](../concepts/software/single-responsibility.md) | 无前置 |
| 3 | [测试金字塔](../concepts/software/test-pyramid.md) | 无前置；决定其它测试怎么安排 |
| 4 | [版本控制与分支策略](../concepts/software/version-control-branching.md) | 无前置；变更管理整条线的上游 |
| 5 | [可观测性](../concepts/software/observability.md) | 无前置 |
| 6 | [超时、重试与退避](../concepts/software/timeout-retry-backoff.md) | 无前置；熔断、背压、幂等性的共同上游 |
| 7 | [依赖倒置](../concepts/software/dependency-inversion.md) | 依赖注入之上 |
| 8 | [分层架构](../concepts/software/layered-architecture.md) | 单一职责之上 |

---

**相关**：[软件工程地图](../maps/software.md)（依赖图）· [AI 组成总览](ai-composition.md) · [Agent 组成总览](agent-composition.md) · [总图](../maps/overview.md)
