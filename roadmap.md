# 概念清单 · Roadmap

这个库**承认自己缺什么**。勾选框由 GitHub 原生渲染，进度一眼可见。

优先级标记：

| 标记 | 含义 |
|---|---|
| **P0** | 前置链断点。不补上，后面的卡读不下去 |
| P1 | 主干概念。构成领域骨架 |
| P2 | 补充与延伸 |

---

## AI（待写 15）

### L0 输入层

- [x] [分词 Tokenization](concepts/ai/tokenization.md)
- [x] [词嵌入 Embedding](concepts/ai/embedding.md)
- [ ] P2 位置编码 Positional Encoding

### L1 架构层

- [x] [注意力机制](concepts/ai/attention-mechanism.md)
- [x] [Transformer 架构](concepts/ai/transformer.md)
- [x] [前馈网络 FFN](concepts/ai/feed-forward-network.md)
- [ ] P2 残差连接与层归一化
- [ ] P2 多头注意力（也可并入注意力卡）
- [ ] P2 专家混合 MoE

### L2 训练层

- [x] [训练范式总览](concepts/ai/training-paradigms.md)
- [x] [预训练与自监督目标](concepts/ai/pretraining.md)
- [x] [监督微调 SFT](concepts/ai/sft.md)
- [x] [指令微调与对话格式](concepts/ai/instruction-tuning.md)
- [x] [LoRA 与参数高效微调](concepts/ai/lora.md)
- [ ] P2 RLHF
- [ ] P2 DPO
- [ ] P2 知识蒸馏
- [ ] P2 缩放定律

### L3 推理层

- [x] [上下文窗口](concepts/ai/context-window.md)
- [x] [推理成本与显存估算](concepts/ai/inference-cost.md)
- [x] [KV Cache](concepts/ai/kv-cache.md)
- [x] [采样策略（温度 / Top-p）](concepts/ai/sampling.md)
- [ ] P2 量化 Quantization
- [ ] P2 推理引擎与服务化

### L4 工程层

- [x] [提示工程 Prompt Engineering](concepts/ai/prompt-engineering.md)
- [x] [RAG 检索增强生成](concepts/ai/rag.md)
- [x] [向量检索](concepts/ai/vector-search.md)
- [ ] P2 重排序 Reranking
- [ ] P2 模型选型与成本权衡

### L5 评估与安全

- [x] [评估方法论](concepts/ai/evaluation.md)
- [x] [幻觉 Hallucination](concepts/ai/hallucination.md)
- [ ] P2 对齐 Alignment
- [ ] P2 提示注入与越狱
- [ ] P2 基准与基准污染

---

## Agent（待写 8）

### 控制流

- [x] [Agent 循环](concepts/agent/agent-loop.md)
- [x] [终止条件与预算控制](concepts/agent/termination-and-budget.md)
- [x] [ReAct 与规划范式](concepts/agent/react-and-planning.md)
- [ ] P2 Plan-and-Execute
- [ ] P2 单 Agent vs 多 Agent 的取舍

### 工具

- [x] [工具定义与 JSON Schema](concepts/agent/tool-definition.md)
- [x] [MCP 模型上下文协议](concepts/agent/mcp.md)
- [x] [函数调用 Function Calling](concepts/agent/function-calling.md)
- [ ] P2 代码执行沙箱
- [ ] P2 权限与最小授权

### 状态与记忆

- [x] [上下文预算管理](concepts/agent/context-budget.md)
- [x] [上下文压缩与摘要](concepts/agent/context-compression.md)
- [ ] P2 长期记忆
- [ ] P2 结构化状态与外部存储

### 质量与安全

- [x] [轨迹可观测性与回放](concepts/agent/trajectory-observability.md)
- [x] [失败模式分类](concepts/agent/failure-modes.md)
- [x] [提示注入防御](concepts/agent/prompt-injection-defense.md)
- [ ] P2 人在回路确认点 HITL
- [ ] P2 Agent 评测

---

## 软件工程（待写 11）

### 设计原则

- [x] [依赖注入](concepts/software/dependency-injection.md)
- [x] [单一职责与职责划分](concepts/software/single-responsibility.md)
- [x] [依赖倒置原则](concepts/software/dependency-inversion.md)
- [ ] P2 组合优于继承
- [ ] P2 幂等性

### 结构与边界

- [x] [分层架构与模块边界](concepts/software/layered-architecture.md)
- [x] [端口与适配器](concepts/software/ports-and-adapters.md)
- [ ] P2 领域模型
- [ ] P2 契约与接口设计

### 正确性

- [x] [测试金字塔](concepts/software/test-pyramid.md)
- [x] [单元测试与可测性](concepts/software/unit-testing.md)
- [x] [契约测试](concepts/software/contract-testing.md)
- [ ] P2 属性测试
- [ ] P2 可复现构建

### 变更管理

- [x] [版本控制与分支策略](concepts/software/version-control-branching.md)
- [x] [代码审查](concepts/software/code-review.md)
- [x] [语义化版本](concepts/software/semantic-versioning.md)
- [ ] P2 变更日志 CHANGELOG
- [ ] P2 架构决策记录 ADR
- [ ] P2 技术债与重构

### 运行

- [x] [可观测性（日志 / 指标 / 追踪）](concepts/software/observability.md)
- [x] [超时、重试与退避](concepts/software/timeout-retry-backoff.md)
- [ ] P2 熔断与降级
- [ ] P2 背压与容量

---

## 当前状态

| 批次 | 内容 | 状态 |
|---|---|---|
| 第一批 | 12 个 P0 前置链断点 | 已完成 |
| 第二批 | 26 个 P1 主干概念 | 已完成 |
| 第三批 | 34 个 P2 补充与延伸 | 待写 |

**P0 与 P1 全部补齐后，从「分词」到「Agent 可上线」已存在一条完整可读的链路**；软件工程侧也已覆盖设计、结构与边界、正确性、变更、运行五条线。剩下的是加厚，不是开路。

---

## 建议的写作顺序

按"补上断点、打通一条完整链路"排序，而不是按领域补齐：

| 顺序 | 概念 | 为什么排这里 |
|---|---|---|
| 1 | 分词 Tokenization | 已被引用，补上即消除唯一断链 |
| 2 | 训练范式总览 | 全库最大空白。补上后幻觉、对齐、微调这批卡才有依据 |
| 3 | 提示工程 | 与模型交互的入口，成本最低 |
| 4 | RAG 检索增强生成 | 承接上下文窗口的限制，也是 Agent 的必备能力 |
| 5 | 推理成本与显存估算 | 让前述方案的可行性可以被判断，而不是靠试 |
| 6 | 终止条件与预算控制 | Agent 上线前提 |
| 7 | 工具定义与 JSON Schema | 工具质量直接决定 Agent 成功率 |
| 8 | MCP 模型上下文协议 | 工具生态的标准接入方式 |
| 9 | 上下文预算管理 | 把前两项串成长任务所需的闭环 |
| 10 | 轨迹可观测性与回放 | 没有它，Agent 无法调试 |
| 11 | 测试金字塔 | 转入软件工程侧的第一块 |
| 12 | 版本控制与分支策略 | 承接变更管理整条线 |

**12 个 P0 全部完成时，从"分词"到"Agent 可上线"会有一条完整可读的链路。** 剩下的 P1、P2 是加厚，不是开路。

---

## 更新方式

写出一张卡之后：

1. 把这里的 `[ ]` 改成 `[x]`
2. 更新对应领域的 `待写 N` 计数
3. 更新 [`maps/overview.md`](maps/overview.md) 底部的进度表
