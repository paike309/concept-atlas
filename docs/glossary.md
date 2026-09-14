# 中英术语对照 · Glossary

本库范围内出现的术语，按领域列出。

「卡片」栏有三种状态：

- `[已写](路径)`——该术语**有专门卡片**
- `[见 X](路径)`——该术语**没有专门卡片**，但内容在指向的那张卡里覆盖了（例如「思维链」在提示工程卡里、「困惑度」在缩放定律卡里）
- 空白——尚未覆盖

这个区分是有用的：查一个术语时，`已写` 说明你能读到完整的一张卡，`见 X` 说明你只能读到卡里的某几段。

用途有两个：读英文材料时反查中文；写卡片时统一译名——同一个词在不同卡里必须写成同一个中文，否则检索会漏。

---

## AI / 模型

| 中文 | English | 缩写 | 卡片 |
|---|---|---|---|
| 人工智能 | Artificial Intelligence | AI | |
| 机器学习 | Machine Learning | ML | |
| 深度学习 | Deep Learning | DL | |
| 神经网络 | Neural Network | NN | |
| 大语言模型 | Large Language Model | LLM | |
| 分词 | Tokenization | | [已写](../concepts/ai/tokenization.md) |
| 词元 | Token | | |
| 词嵌入 | Embedding | | [已写](../concepts/ai/embedding.md) |
| 位置编码 | Positional Encoding | | [已写](../concepts/ai/positional-encoding.md) |
| 注意力机制 | Attention Mechanism | | [已写](../concepts/ai/attention-mechanism.md) |
| 自注意力 | Self-Attention | | [已写](../concepts/ai/attention-mechanism.md) |
| 多头注意力 | Multi-Head Attention | MHA | [已写](../concepts/ai/multi-head-attention.md) |
| 前馈网络 | Feed-Forward Network | FFN | [已写](../concepts/ai/feed-forward-network.md) |
| 残差连接 | Residual Connection | | [已写](../concepts/ai/residual-and-normalization.md) |
| 层归一化 | Layer Normalization | LayerNorm | [已写](../concepts/ai/residual-and-normalization.md) |
| 变换器 | Transformer | | [已写](../concepts/ai/transformer.md) |
| 编码器 / 解码器 | Encoder / Decoder | | [已写](../concepts/ai/transformer.md) |
| 专家混合 | Mixture of Experts | MoE | [已写](../concepts/ai/moe.md) |
| 预训练 | Pre-training | | [已写](../concepts/ai/pretraining.md) |
| 监督微调 | Supervised Fine-Tuning | SFT | [已写](../concepts/ai/sft.md) |
| 指令微调 | Instruction Tuning | | [已写](../concepts/ai/instruction-tuning.md) |
| 基于人类反馈的强化学习 | Reinforcement Learning from Human Feedback | RLHF | [已写](../concepts/ai/rlhf.md) |
| 直接偏好优化 | Direct Preference Optimization | DPO | [已写](../concepts/ai/dpo.md) |
| 低秩自适应 | Low-Rank Adaptation | LoRA | [已写](../concepts/ai/lora.md) |
| 参数高效微调 | Parameter-Efficient Fine-Tuning | PEFT | [已写](../concepts/ai/lora.md) |
| 知识蒸馏 | Knowledge Distillation | | [已写](../concepts/ai/knowledge-distillation.md) |
| 缩放定律 | Scaling Law | | [已写](../concepts/ai/scaling-laws.md) |
| 推理 | Inference | | |
| 上下文窗口 | Context Window | | [已写](../concepts/ai/context-window.md) |
| 键值缓存 | KV Cache | | [已写](../concepts/ai/kv-cache.md) |
| 温度 | Temperature | | [已写](../concepts/ai/sampling.md) |
| 核采样 | Top-p / Nucleus Sampling | | [已写](../concepts/ai/sampling.md) |
| 量化 | Quantization | | [已写](../concepts/ai/quantization.md) |
| 推理引擎 | Inference Engine | | [已写](../concepts/ai/inference-engines.md) |
| 检索增强生成 | Retrieval-Augmented Generation | RAG | [已写](../concepts/ai/rag.md) |
| 向量检索 | Vector Search | | [已写](../concepts/ai/vector-search.md) |
| 重排序 | Reranking | | [已写](../concepts/ai/reranking.md) |
| 模型选型 | Model Selection | | [已写](../concepts/ai/model-selection.md) |
| 提示工程 | Prompt Engineering | | [已写](../concepts/ai/prompt-engineering.md) |
| 思维链 | Chain-of-Thought | CoT | [见提示工程](../concepts/ai/prompt-engineering.md) |
| 幻觉 | Hallucination | | [已写](../concepts/ai/hallucination.md) |
| 对齐 | Alignment | | [已写](../concepts/ai/alignment.md) |
| 越狱 | Jailbreak | | [已写](../concepts/ai/jailbreak.md) |
| 提示注入 | Prompt Injection | | [见 Agent 侧](../concepts/agent/prompt-injection-defense.md) |
| 护栏 | Guardrail | | |
| 评估方法论 | Evaluation Methodology | | [已写](../concepts/ai/evaluation.md) |
| 基准 | Benchmark | | [已写](../concepts/ai/benchmarks.md) |
| 困惑度 | Perplexity | PPL | [见缩放定律](../concepts/ai/scaling-laws.md) |
| 基准污染 | Benchmark Contamination | | [已写](../concepts/ai/benchmarks.md) |

---

## Agent

| 中文 | English | 缩写 | 卡片 |
|---|---|---|---|
| 智能体 | Agent | | [见 Agent 循环](../concepts/agent/agent-loop.md) |
| Agent 循环 | Agent Loop | | [已写](../concepts/agent/agent-loop.md) |
| ReAct | ReAct | | [已写](../concepts/agent/react-and-planning.md) |
| 工具定义 | Tool Definition | | [已写](../concepts/agent/tool-definition.md) |
| 工具调用 | Tool Use | | [已写](../concepts/agent/tool-definition.md) |
| 函数调用 | Function Calling | | [已写](../concepts/agent/function-calling.md) |
| 模型上下文协议 | Model Context Protocol | MCP | [已写](../concepts/agent/mcp.md) |
| 沙箱 | Sandbox | | [已写](../concepts/agent/code-execution-sandbox.md) |
| 长期记忆 | Long-term Memory | | [已写](../concepts/agent/long-term-memory.md) |
| 上下文预算管理 | Context Budget Management | | [已写](../concepts/agent/context-budget.md) |
| 上下文压缩 | Context Compression | | [已写](../concepts/agent/context-compression.md) |
| 结构化状态 | Structured State | | [已写](../concepts/agent/structured-state.md) |
| 轨迹 | Trajectory | | [已写](../concepts/agent/trajectory-observability.md) |
| 循环检测 | Loop Detection | | [见失败模式](../concepts/agent/failure-modes.md) |
| 失败模式 | Failure Modes | | [已写](../concepts/agent/failure-modes.md) |
| 人在回路 | Human-in-the-Loop | HITL | [已写](../concepts/agent/human-in-the-loop.md) |
| 多智能体 | Multi-Agent | | [已写](../concepts/agent/single-vs-multi-agent.md) |
| 最小授权 | Least Privilege | | [已写](../concepts/agent/least-privilege.md) |
| 编排 | Orchestration | | |
| 工作流 | Workflow | | [见 Agent 循环](../concepts/agent/agent-loop.md) |
| 终止条件 | Termination Condition | | [已写](../concepts/agent/termination-and-budget.md) |
| 计划-执行 | Plan-and-Execute | | [已写](../concepts/agent/plan-and-execute.md) |
| Agent 评测 | Agent Evaluation | | [已写](../concepts/agent/agent-evaluation.md) |

---

## 软件工程

| 中文 | English | 缩写 | 卡片 |
|---|---|---|---|
| 依赖注入 | Dependency Injection | DI | [已写](../concepts/software/dependency-injection.md) |
| 控制反转 | Inversion of Control | IoC | [已写](../concepts/software/dependency-injection.md) |
| 服务定位器 | Service Locator | | [已写](../concepts/software/dependency-injection.md) |
| 单一职责原则 | Single Responsibility Principle | SRP | [已写](../concepts/software/single-responsibility.md) |
| 依赖倒置原则 | Dependency Inversion Principle | DIP | [已写](../concepts/software/dependency-inversion.md) |
| 开闭原则 | Open-Closed Principle | OCP | |
| 接口隔离原则 | Interface Segregation Principle | ISP | |
| 组合优于继承 | Composition over Inheritance | | [已写](../concepts/software/composition-over-inheritance.md) |
| 端口与适配器 | Ports and Adapters | | [已写](../concepts/software/ports-and-adapters.md) |
| 分层架构 | Layered Architecture | | [已写](../concepts/software/layered-architecture.md) |
| 领域模型 | Domain Model | | [已写](../concepts/software/domain-model.md) |
| 契约 | Contract | | [已写](../concepts/software/contract-design.md) |
| 幂等性 | Idempotency | | [已写](../concepts/software/idempotency.md) |
| 测试金字塔 | Test Pyramid | | [已写](../concepts/software/test-pyramid.md) |
| 单元测试 | Unit Test | | [已写](../concepts/software/unit-testing.md) |
| 契约测试 | Contract Test | | [已写](../concepts/software/contract-testing.md) |
| 属性测试 | Property-Based Testing | PBT | [已写](../concepts/software/property-based-testing.md) |
| 可复现构建 | Reproducible Build | | [已写](../concepts/software/reproducible-build.md) |
| 版本控制与分支策略 | Version Control & Branching | | [已写](../concepts/software/version-control-branching.md) |
| 代码审查 | Code Review | | [已写](../concepts/software/code-review.md) |
| 语义化版本 | Semantic Versioning | SemVer | [已写](../concepts/software/semantic-versioning.md) |
| 变更日志 | Changelog | | [已写](../concepts/software/changelog.md) |
| 架构决策记录 | Architecture Decision Record | ADR | [已写](../concepts/software/adr.md) |
| 技术债 | Technical Debt | | [已写](../concepts/software/technical-debt-refactoring.md) |
| 重构 | Refactoring | | [已写](../concepts/software/technical-debt-refactoring.md) |
| 可观测性 | Observability | | [已写](../concepts/software/observability.md) |
| 日志 / 指标 / 追踪 | Logging / Metrics / Tracing | | [已写](../concepts/software/observability.md) |
| 退避重试 | Backoff Retry | | [已写](../concepts/software/timeout-retry-backoff.md) |
| 熔断 | Circuit Breaker | | [已写](../concepts/software/circuit-breaker.md) |
| 背压 | Backpressure | | [已写](../concepts/software/backpressure.md) |
| 文档即代码 | Docs as Code | | |

---

## 译名约定

几条容易写乱的，统一如下：

| 英文 | 本库统一用 | 不要写成 |
|---|---|---|
| Token / Tokenization | 词元 / 分词 | 令牌 / 标记化 |
| Inference | 推理 | 推断（指模型运行时一律用"推理"） |
| Agent | 智能体（首次出现写 Agent） | 代理 |
| Prompt | 提示词 | 提示语 / 指令词 |
| Context | 上下文 | 语境 |
| Guardrail | 护栏 | 防护栏 |
| Trajectory | 轨迹 | 执行路径 |
| Retrieval | 检索 | 召回（召回另指 recall 指标） |
| Fine-tuning | 微调 | 精调 |
| Alignment | 对齐 | 校准（校准对应 calibration） |
| Backpressure | 背压 | 反压（两者都有人用，本库统一为"背压"） |
| Fallback / Degradation | 降级 | 兜底（"兜底"含义过宽，不用作术语） |
