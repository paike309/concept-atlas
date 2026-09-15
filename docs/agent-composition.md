# Agent 组成总览 · Agent Composition

这份文档回答一个问题：**一个 Agent 由哪几部分组成，每一部分起什么作用。**

它是 [`maps/agent.md`](../maps/agent.md) 那张依赖图的**文字版**——图回答"谁依赖谁"，本文把那些边讲成因果。

> **定位**：结构地图，不是事实依据。内容整理自 [`concepts/agent/`](../concepts/agent/) 下的卡片，目前信源等级均为 `link-checked`（来源链接已核验可达性与标题，正文表述与来源原文尚未逐条比对）。见 [`verification-log.md`](verification-log.md)。

---

## 一句话总述

**Agent 的复杂度不在模型，在循环周边的四件事。**

这是这个领域最反直觉的一点：选模型只是其中一步，真正决定能不能上线的是——**下一步谁决定**（控制流）、**模型的手是什么**（工具）、**它记不记得住**（状态）、**出问题你怎么知道**（质量与安全）。四件事里任何一件没做，系统就上不了线。

这四件事就是 [`concepts/agent/`](../concepts/agent/) 属性表里「领域」字段的四种取值。

---

## 四组总览

| 组 | 它在回答什么 | 不做的后果 | 卡片数 |
|---|---|---|---|
| **控制流** | 下一步做什么，由模型运行时决定还是人预先写死 | 用 Agent 去做 Workflow 能做的事，又贵又不可测；多个 Agent 时失败会成网络 | 7 |
| **工具** | 模型的手能碰到什么、怎么碰到 | 描述没写清楚的能力模型不会用，也不会自己发现 | 6 |
| **状态与记忆** | 它没有内部状态变量，"我做到哪了"从哪来 | 上下文一被截断或污染就"失忆"、重复动作、目标漂移；多方写入则"记乱了" | 5 |
| **质量与安全** | 出问题你怎么知道，以及怎么限制它的破坏半径 | 没有轨迹就无法调试；防御建在概率层等于没有安全；凭据失控则越权 | 6 |

层级分布（截至 2026-09-16）：**基础 7 / 进阶 13 / 前沿 4**。

---

## 逐组：每张卡起什么作用

### 1 控制流 —— 下一步是谁决定的（5）

判断标准只有一条：**下一步做什么，由模型在运行时产生，还是由人预先写死。**

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [Agent 循环](../concepts/agent/agent-loop.md) | 由模型自身决定下一步动作、执行后再回到模型的闭环——观察、决策、行动、再观察。**所有 Agent 结构的基元** | 基础 | [上下文窗口](../concepts/ai/context-window.md) |
| [终止条件与预算](../concepts/agent/termination-and-budget.md) | 让循环在有限步数、时间与成本内停止的**外部强制**机制。相对"完成任务后请停止"这类提示词请求，它是硬约束 | 基础 | Agent 循环 |
| [ReAct 与规划范式](../concepts/agent/react-and-planning.md) | 让模型交替产出"推理"与"动作"、并用观察结果修正下一步。Thought → Action → Observation → 下一轮 Thought | 进阶 | Agent 循环 |
| [计划-执行 Plan-and-Execute](../concepts/agent/plan-and-execute.md) | 先产出完整计划再逐步执行，计划失效时重规划。规划 → 执行 → 修正三阶段 | 进阶 | ReAct 与规划范式 |
| [单 Agent 与多 Agent 的取舍](../concepts/agent/single-vs-multi-agent.md) | 用单个循环做完，还是拆成多个 Agent 各负责一部分并协作——这是一个**取舍**，不是升级路径 | 进阶 | Agent 循环 |

> **能用 Workflow 解决的不要用 Agent。** 路径可以事先枚举时，Workflow 更便宜、更快、可测试。Agent 的价值只存在于"路径事先无法枚举"的场景。

### 2 工具 —— 模型的手（5）

工具这一层的质量，对成功率的影响**不低于模型选择**。

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [工具定义](../concepts/agent/tool-definition.md) | 向模型描述一个可调用能力的三要素——名字、用途描述、参数模式（通常是 JSON Schema）。**描述没写清楚的能力模型不会用** | 基础 | Agent 循环 |
| [函数调用 Function Calling](../concepts/agent/function-calling.md) | 模型输出结构化调用请求而不是自然语言，由外部运行时解析、执行，并把结果回灌上下文 | 基础 | 工具定义 |
| [MCP 模型上下文协议](../concepts/agent/mcp.md) | 把「AI 应用」与「工具、数据源」之间的对接**标准化**的开放协议，让工具不必为每个应用重写一遍 | 基础 | 工具定义 |
| [代码执行沙箱](../concepts/agent/code-execution-sandbox.md) | 让模型生成并执行代码的环境，以及为控制风险而设的隔离约束（进程内 → 子进程 → 容器 → 虚拟机） | 进阶 | 工具定义 |
| [权限与最小授权](../concepts/agent/least-privilege.md) | 让 Agent 及每个工具只持有完成当前任务所需的**最小权限**，必要时显式授权 | 进阶 | 提示注入防御 |

> **一条必须记住的边界**：模型输出 → 实际执行之间是**不可信边界**，所有校验都要放在这条线上。这同时是提示注入防御和权限控制的基础。

### 3 状态与记忆 —— 它其实没有状态（4）

关键认识：**Agent 没有内部状态变量，它的"我做到哪了"完全依赖把历史重放进上下文**（根在[上下文窗口](../concepts/ai/context-window.md)）。所以**长任务跑崩的主因是上下文预算管理，不是模型能力。**

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [上下文预算管理](../concepts/agent/context-budget.md) | 在固定窗口内为系统提示、对话历史、工具返回、任务数据**分配额度并持续回收** | 基础 | Agent 循环 · 上下文窗口 |
| [上下文压缩与摘要](../concepts/agent/context-compression.md) | 减少上下文占用的具体手段——确定性裁剪、摘要、替换为引用。**是有损的，压缩后必须跑回归集** | 进阶 | 上下文预算管理 |
| [结构化状态与外部存储](../concepts/agent/structured-state.md) | 把任务状态从上下文里抽出来，存成外部结构化数据（待办列表、状态机、数据库记录） | 进阶 | 上下文预算管理 |
| [长期记忆](../concepts/agent/long-term-memory.md) | 跨会话保留并检索信息，使 Agent 不必依赖上下文重放 | 前沿 | 上下文预算管理 |

> 这一组有明确的递进关系：**压缩**是在窗口内腾挪 → **结构化状态**把关键状态移出窗口 → **长期记忆**跨会话保留。三者的边界是"这份信息要活多久"。

### 4 质量与安全 —— 没有轨迹就无法调试（5）

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [轨迹可观测性与回放](../concepts/agent/trajectory-observability.md) | 记录每一步的输入、决策、动作与返回，使整条路径可检查、可回演、可归因。**另外三张卡的前置** | 基础 | Agent 循环 |
| [失败模式分类](../concepts/agent/failure-modes.md) | 反复出现的几类可预期失败形态，以及各自的识别信号与成因 | 进阶 | 轨迹可观测性与回放 |
| [提示注入防御](../concepts/agent/prompt-injection-defense.md) | 防止外部输入（网页、文档、工具返回值、用户内容）被模型当作指令执行 | 进阶 | 函数调用 |
| [人在回路 HITL](../concepts/agent/human-in-the-loop.md) | 在执行过程中插入人工确认、修正或接管 | 进阶 | 权限与最小授权 |
| [Agent 评测](../concepts/agent/agent-evaluation.md) | 对 Agent 系统（而不只是单次模型输出）的效果进行评测 | 进阶 | 轨迹可观测性与回放 · [评估方法论](../concepts/ai/evaluation.md) |

> **防御的强度排序是这一块的核心**：
> `权限最小化（确定性）> 执行前校验 > 人工确认 > 结构分隔（概率性）> 提示层告诫（最弱）`
> 前三层是机制，漏了就是漏了；后两层是概率，攻击者只需找到一个绕过表述。**把安全建立在后两层等于没有安全。**

---

## 走一遍完整链路

一次 Agent 任务从头到尾，这些概念分别在哪儿上场：

1. **目标进入**：系统提示、任务描述、[工具定义](../concepts/agent/tool-definition.md) 一起放进上下文——工具的**描述质量**从这一刻就开始决定成功率；
2. **循环启动**：[Agent 循环](../concepts/agent/agent-loop.md) 让模型自己决定下一步；
3. **要动手了**：[函数调用](../concepts/agent/function-calling.md) 产出结构化请求；运行时解析后执行。工具要么是代码（走[代码执行沙箱](../concepts/agent/code-execution-sandbox.md)），要么是外部系统（用 [MCP](../concepts/agent/mcp.md) 标准化对接）；
4. **结果回灌 → 上下文变长**：[上下文预算管理](../concepts/agent/context-budget.md) 决定额度怎么分；装不下就[压缩](../concepts/agent/context-compression.md)，或把状态移出去存成[结构化状态](../concepts/agent/structured-state.md)；跨会话的信息交给[长期记忆](../concepts/agent/long-term-memory.md)；
5. **任务变复杂**：用 [ReAct](../concepts/agent/react-and-planning.md) 让推理与动作交替；再复杂就用[计划-执行](../concepts/agent/plan-and-execute.md)；是否拆[多个 Agent](../concepts/agent/single-vs-multi-agent.md) 是一次取舍，不是默认升级；
6. **必须能停**：[终止条件与预算](../concepts/agent/termination-and-budget.md) 提供步数、时间、成本上的硬约束。**没有它，循环本身就是故障源**；
7. **全程留痕**：[轨迹可观测性](../concepts/agent/trajectory-observability.md) 记录每一步——没有它，下面两件事都做不了：从轨迹里认出[失败模式](../concepts/agent/failure-modes.md)、对整条轨迹做 [Agent 评测](../concepts/agent/agent-evaluation.md)；
8. **限制破坏半径**：[权限最小化](../concepts/agent/least-privilege.md) 约束每个工具能做什么；外部内容可能夹带指令，靠[提示注入防御](../concepts/agent/prompt-injection-defense.md) 挡；高风险动作插入[人在回路](../concepts/agent/human-in-the-loop.md) 确认。

---

## 三处最容易断的关节

1. **[Agent 循环](../concepts/agent/agent-loop.md) 的前置是 AI 的[上下文窗口](../concepts/ai/context-window.md)。** 一句话：**Agent 的所有限制都源自 AI 地图的 L3 推理层。** 绕开那一层直接学 Agent 框架，会停在"知道怎么调 API"的水平。
2. **[终止条件](../concepts/agent/termination-and-budget.md) 必须是硬约束。** "完成任务后请停止"是一条建议，不是约束——模型眼里"任务已完成"和"再调一次工具"没有本质区别，两者都只是"下一个 token"。
3. **[轨迹可观测性](../concepts/agent/trajectory-observability.md)。** 它是[失败模式](../concepts/agent/failure-modes.md)与 [Agent 评测](../concepts/agent/agent-evaluation.md) 共同的前置。**没有轨迹，Agent 无法调试**——这条不是可选项。

---

## 从哪读起

按「前置」拓扑排，一条不跳级的顺序：

| 顺序 | 卡片 | 为什么排这里 |
|---|---|---|
| 1 | [上下文窗口](../concepts/ai/context-window.md)（AI 域） | 唯一的外部前置，必须先有 |
| 2 | [Agent 循环](../concepts/agent/agent-loop.md) | 其余卡片的共同上游 |
| 3 | [工具定义](../concepts/agent/tool-definition.md) | Agent 的手，从描述开始 |
| 4 | [终止条件与预算](../concepts/agent/termination-and-budget.md) | 让循环一定会停 |
| 5 | [函数调用](../concepts/agent/function-calling.md) | 结构化调用是怎么落地的 |
| 6 | [上下文预算管理](../concepts/agent/context-budget.md) | 长任务的真正瓶颈 |
| 7 | [轨迹可观测性与回放](../concepts/agent/trajectory-observability.md) | 没有它后面两张卡都无法用 |

---

## 本库未覆盖的部分

**2026-09-16 更新：本节原先列的四条缺口已全部补齐。**

| 原缺口 | 现在在哪 |
|---|---|
| 多 Agent 的通信与协调 | [多 Agent 通信与协调](../concepts/agent/multi-agent-coordination.md) · [共享状态与冲突解决](../concepts/agent/shared-state-and-conflict.md) |
| Agent 的成本模型 | [Agent 成本核算](../concepts/agent/agent-cost-accounting.md) |
| 凭据与密钥管理 | [Agent 凭据与密钥管理](../concepts/agent/agent-credentials.md) |
| GUI / 浏览器操作类工具 | [GUI 与浏览器操作工具](../concepts/agent/gui-and-browser-tools.md) |

当前仍缺的是更远的两块，且**本库不打算在 Agent 域重复**：

- **Agent 的部署形态**：多实例下的会话亲和、跨区域调度、灰度发布。这些属于通用后端工程，软件工程域已有对应卡片（[部署与发布策略](../concepts/software/deployment-strategies.md) 等），在 Agent 域再写一遍会造成两份口径。
- **具体框架与平台**：与"不收 MySQL / Kubernetes"同一条标准——框架属于文档，不属于概念。

---

**相关**：[Agent 地图](../maps/agent.md)（依赖图）· [AI 组成总览](ai-composition.md) · [软件工程组成总览](software-composition.md) · [总图](../maps/overview.md)
