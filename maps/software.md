# 软件工程地图 · Software Engineering Map

软件工程的概念多数不是"知识"，而是**权衡的记法**。每一条原则背后都有一个具体的失败模式，理解那条失败模式比记住原则名字有用。

这一块只收**跨项目通用**的概念。具体框架、语言特性、部署工具不收——那些属于文档，不属于概念。

---

## 五条线

```mermaid
flowchart TD
    subgraph D["1 设计原则"]
        D1["依赖注入"]
        D2["单一职责"]
        D3["依赖倒置"]
        D4["组合优于继承"]
    end

    subgraph S["2 结构与边界"]
        S1["分层架构"]
        S2["端口与适配器"]
        S3["契约与接口设计"]
        S4["领域模型"]
        S5["幂等性"]
    end

    subgraph C["3 正确性"]
        C1["测试金字塔"]
        C2["单元测试"]
        C3["契约测试"]
        C4["属性测试"]
        C5["可复现构建"]
    end

    subgraph M["4 变更管理"]
        M1["版本控制与分支策略"]
        M2["代码审查"]
        M3["语义化版本"]
        M4["变更日志"]
        M5["ADR 决策记录"]
        M6["技术债与重构"]
    end

    subgraph O["5 运行"]
        O1["可观测性"]
        O2["超时 / 重试 / 退避"]
        O3["熔断与降级"]
        O4["背压与容量"]
    end

    D --> S --> C
    S --> M
    C --> O
    M --> O
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
