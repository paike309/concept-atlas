# 中英术语对照 · Glossary

本库范围内出现的术语，按领域列出。**「卡片」栏给了链接的表示已经写了卡片**，其余见 [`roadmap.md`](../roadmap.md)。

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
| 分词 | Tokenization | | 待写 |
| 词元 | Token | | |
| 词嵌入 | Embedding | | |
| 位置编码 | Positional Encoding | | |
| 注意力机制 | Attention Mechanism | | [已写](../concepts/ai/attention-mechanism.md) |
| 自注意力 | Self-Attention | | [已写](../concepts/ai/attention-mechanism.md) |
| 多头注意力 | Multi-Head Attention | MHA | [已写](../concepts/ai/attention-mechanism.md) |
| 前馈网络 | Feed-Forward Network | FFN | [已写](../concepts/ai/transformer.md) |
| 残差连接 | Residual Connection | | [已写](../concepts/ai/transformer.md) |
| 层归一化 | Layer Normalization | LayerNorm | [已写](../concepts/ai/transformer.md) |
| 变换器 | Transformer | | [已写](../concepts/ai/transformer.md) |
| 编码器 / 解码器 | Encoder / Decoder | | [已写](../concepts/ai/transformer.md) |
| 专家混合 | Mixture of Experts | MoE | |
| 预训练 | Pre-training | | |
| 监督微调 | Supervised Fine-Tuning | SFT | |
| 指令微调 | Instruction Tuning | | |
| 基于人类反馈的强化学习 | Reinforcement Learning from Human Feedback | RLHF | |
| 直接偏好优化 | Direct Preference Optimization | DPO | |
| 低秩自适应 | Low-Rank Adaptation | LoRA | |
| 参数高效微调 | Parameter-Efficient Fine-Tuning | PEFT | |
| 知识蒸馏 | Knowledge Distillation | | |
| 缩放定律 | Scaling Law | | |
| 推理 | Inference | | |
| 上下文窗口 | Context Window | | [已写](../concepts/ai/context-window.md) |
| 键值缓存 | KV Cache | | |
| 温度 | Temperature | | |
| 量化 | Quantization | | |
| 检索增强生成 | Retrieval-Augmented Generation | RAG | |
| 向量检索 | Vector Search | | |
| 重排序 | Reranking | | |
| 提示工程 | Prompt Engineering | | |
| 思维链 | Chain-of-Thought | CoT | |
| 幻觉 | Hallucination | | |
| 对齐 | Alignment | | |
| 越狱 | Jailbreak | | |
| 提示注入 | Prompt Injection | | |
| 护栏 | Guardrail | | |
| 基准 | Benchmark | | |
| 困惑度 | Perplexity | PPL | |
| 基准污染 | Benchmark Contamination | | |

---

## Agent

| 中文 | English | 缩写 | 卡片 |
|---|---|---|---|
| 智能体 | Agent | | |
| Agent 循环 | Agent Loop | | [已写](../concepts/agent/agent-loop.md) |
| 工具调用 | Tool Use | | |
| 函数调用 | Function Calling | | |
| 模型上下文协议 | Model Context Protocol | MCP | |
| 沙箱 | Sandbox | | |
| 长期记忆 | Long-term Memory | | |
| 上下文压缩 | Context Compression | | |
| 轨迹 | Trajectory | | |
| 循环检测 | Loop Detection | | |
| 人在回路 | Human-in-the-Loop | HITL | |
| 多智能体 | Multi-Agent | | |
| 编排 | Orchestration | | |
| 工作流 | Workflow | | [已写](../concepts/agent/agent-loop.md) |
| 终止条件 | Termination Condition | | [已写](../concepts/agent/agent-loop.md) |

---

## 软件工程

| 中文 | English | 缩写 | 卡片 |
|---|---|---|---|
| 依赖注入 | Dependency Injection | DI | [已写](../concepts/software/dependency-injection.md) |
| 控制反转 | Inversion of Control | IoC | [已写](../concepts/software/dependency-injection.md) |
| 服务定位器 | Service Locator | | [已写](../concepts/software/dependency-injection.md) |
| 单一职责原则 | Single Responsibility Principle | SRP | |
| 开闭原则 | Open-Closed Principle | OCP | |
| 依赖倒置原则 | Dependency Inversion Principle | DIP | |
| 接口隔离原则 | Interface Segregation Principle | ISP | |
| 端口与适配器 | Ports and Adapters | | |
| 分层架构 | Layered Architecture | | |
| 契约 | Contract | | |
| 幂等性 | Idempotency | | |
| 单元测试 | Unit Test | | |
| 契约测试 | Contract Test | | |
| 属性测试 | Property-Based Testing | PBT | |
| 测试金字塔 | Test Pyramid | | |
| 可复现构建 | Reproducible Build | | |
| 语义化版本 | Semantic Versioning | SemVer | |
| 变更日志 | Changelog | | |
| 架构决策记录 | Architecture Decision Record | ADR | |
| 技术债 | Technical Debt | | |
| 重构 | Refactoring | | |
| 可观测性 | Observability | | |
| 日志 / 指标 / 追踪 | Logging / Metrics / Tracing | | |
| 退避重试 | Backoff Retry | | |
| 熔断 | Circuit Breaker | | |
| 背压 | Backpressure | | |
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
