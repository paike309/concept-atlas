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
| 事务 | Transaction | | [已写](../concepts/software/transactions-acid.md) |
| ACID | ACID | | [已写](../concepts/software/transactions-acid.md) |
| 原子性 / 隔离性 / 持久性 | Atomicity / Isolation / Durability | | [已写](../concepts/software/transactions-acid.md) |
| 事务边界 | Transaction Boundary | | [已写](../concepts/software/transactions-acid.md) |
| 隔离级别 | Isolation Level | | [已写](../concepts/software/transaction-isolation.md) |
| 脏读 | Dirty Read | | [已写](../concepts/software/transaction-isolation.md) |
| 不可重复读 | Non-repeatable Read | | [已写](../concepts/software/transaction-isolation.md) |
| 幻读 | Phantom Read | | [已写](../concepts/software/transaction-isolation.md) |
| 写偏斜 | Write Skew | | [已写](../concepts/software/transaction-isolation.md) |
| 快照隔离 | Snapshot Isolation | SI | [已写](../concepts/software/transaction-isolation.md) |
| 可串行化 | Serializable | | [已写](../concepts/software/transaction-isolation.md) |
| 索引 | Index | | [已写](../concepts/software/index-and-query-plan.md) |
| 查询计划 | Query Plan | | [已写](../concepts/software/index-and-query-plan.md) |
| 最左前缀 | Leftmost Prefix | | [已写](../concepts/software/index-and-query-plan.md) |
| 范式化 | Normalization | | [已写](../concepts/software/normalization.md) |
| 反范式化 | Denormalization | | [已写](../concepts/software/normalization.md) |
| 更新异常 | Update Anomaly | | [已写](../concepts/software/normalization.md) |
| 复制 | Replication | | [已写](../concepts/software/replication-and-consistency.md) |
| 一致性模型 | Consistency Model | | [已写](../concepts/software/replication-and-consistency.md) |
| 线性一致 | Linearizability | | [已写](../concepts/software/replication-and-consistency.md) |
| 最终一致 | Eventual Consistency | | [已写](../concepts/software/replication-and-consistency.md) |
| 复制滞后 | Replication Lag | | [已写](../concepts/software/replication-and-consistency.md) |
| 分片 | Sharding | | [已写](../concepts/software/sharding-and-partitioning.md) |
| 表分区 | Table Partitioning | | [已写](../concepts/software/sharding-and-partitioning.md) |
| 再平衡 | Rebalancing | | [已写](../concepts/software/sharding-and-partitioning.md) |
| schema 迁移 | Schema Migration | | [已写](../concepts/software/schema-migration.md) |
| 双写与回填 | Dual Write & Backfill | | [已写](../concepts/software/schema-migration.md) |
| 连接池 | Connection Pool | | [已写](../concepts/software/connection-pooling.md) |
| 连接耗尽 | Connection Exhaustion | | [已写](../concepts/software/connection-pooling.md) |
| 认证 | Authentication | | [已写](../concepts/software/authentication-and-authorization.md) |
| 授权 | Authorization | | [已写](../concepts/software/authentication-and-authorization.md) |
| 多因素认证 | Multi-Factor Authentication | MFA | [已写](../concepts/software/authentication-and-authorization.md) |
| 会话固定 | Session Fixation | | [已写](../concepts/software/authentication-and-authorization.md) |
| 访问控制 | Access Control | | [已写](../concepts/software/authentication-and-authorization.md) |
| 认证加密 | Authenticated Encryption with Associated Data | AEAD | [已写](../concepts/software/encryption-and-key-management.md) |
| 密钥轮换 | Key Rotation | | [已写](../concepts/software/encryption-and-key-management.md) |
| 信封加密 | Envelope Encryption | | [已写](../concepts/software/encryption-and-key-management.md) |
| 信任边界 | Trust Boundary | | [已写](../concepts/software/input-validation.md) |
| 参数化查询 | Parameterized Query | | [已写](../concepts/software/input-validation.md) |
| 输出编码 | Output Encoding | | [已写](../concepts/software/input-validation.md) |
| 供应链安全 | Supply Chain Security | | [已写](../concepts/software/dependency-supply-chain.md) |
| 软件物料清单 | Software Bill of Materials | SBOM | [已写](../concepts/software/dependency-supply-chain.md) |
| 部署 | Deployment | | [已写](../concepts/software/deployment-strategies.md) |
| 发布 | Release | | [已写](../concepts/software/deployment-strategies.md) |
| 蓝绿部署 | Blue-Green Deployment | | [已写](../concepts/software/deployment-strategies.md) |
| 金丝雀发布 | Canary Release | | [已写](../concepts/software/deployment-strategies.md) |
| 功能开关 | Feature Flag | | [已写](../concepts/software/deployment-strategies.md) |
| 服务等级指标 | Service Level Indicator | SLI | [已写](../concepts/software/slo-and-error-budget.md) |
| 服务等级目标 | Service Level Objective | SLO | [已写](../concepts/software/slo-and-error-budget.md) |
| 服务等级协议 | Service Level Agreement | SLA | [已写](../concepts/software/slo-and-error-budget.md) |
| 错误预算 | Error Budget | | [已写](../concepts/software/slo-and-error-budget.md) |
| 燃烧率 | Burn Rate | | [已写](../concepts/software/slo-and-error-budget.md) |
| 分页告警 | Paging | | [已写](../concepts/software/alerting-and-on-call.md) |
| 告警疲劳 | Alert Fatigue | | [已写](../concepts/software/alerting-and-on-call.md) |
| 配置漂移 | Configuration Drift | | [已写](../concepts/software/configuration-management.md) |
| 基础设施即代码 | Infrastructure as Code | IaC | [已写](../concepts/software/infrastructure-as-code.md) |
| 声明式 | Declarative | | [已写](../concepts/software/infrastructure-as-code.md) |
| 事故指挥 | Incident Commander | IC | [已写](../concepts/software/incident-response.md) |
| 无责复盘 | Blameless Postmortem | | [已写](../concepts/software/incident-response.md) |
| 容量规划 | Capacity Planning | | [已写](../concepts/software/capacity-planning.md) |
| 并发控制 | Concurrency Control | | [已写](../concepts/software/concurrency-and-locking.md) |
| 死锁 | Deadlock | | [已写](../concepts/software/concurrency-and-locking.md) |
| 乐观锁 / 悲观锁 | Optimistic / Pessimistic Locking | | [已写](../concepts/software/concurrency-and-locking.md) |
| 数据竞争 | Data Race | | [已写](../concepts/software/memory-model-and-races.md) |
| 内存模型 | Memory Model | | [已写](../concepts/software/memory-model-and-races.md) |
| happens-before | Happens-Before | | [已写](../concepts/software/memory-model-and-races.md) |
| 火焰图 | Flame Graph | | [已写](../concepts/software/profiling.md) |
| 采样剖析 | Sampling Profiler | | [已写](../concepts/software/profiling.md) |
| 缓存穿透 / 击穿 / 雪崩 | Cache Penetration / Breakdown / Stampede | | [已写](../concepts/software/caching-strategies.md) |
| 旁路缓存 | Cache-Aside | | [已写](../concepts/software/caching-strategies.md) |
| 限流 | Rate Limiting | | [已写](../concepts/software/api-design-and-rate-limiting.md) |
| 令牌桶 | Token Bucket | | [已写](../concepts/software/api-design-and-rate-limiting.md) |
| 配额 | Quota | | [已写](../concepts/software/api-design-and-rate-limiting.md) |
| 视觉编码器 | Vision Encoder | | [已写](../concepts/ai/vision-encoder.md) |
| 图像块 | Patch | | [已写](../concepts/ai/vision-encoder.md) |
| 跨模态对齐 | Cross-Modal Alignment | | [已写](../concepts/ai/cross-modal-alignment.md) |
| 对比学习 | Contrastive Learning | | [已写](../concepts/ai/cross-modal-alignment.md) |
| 零样本分类 | Zero-Shot Classification | | [已写](../concepts/ai/cross-modal-alignment.md) |
| 语音识别 | Automatic Speech Recognition | ASR | [已写](../concepts/ai/speech-and-audio-models.md) |
| 频谱图 | Spectrogram | | [已写](../concepts/ai/speech-and-audio-models.md) |
| 扩散模型 | Diffusion Model | | [已写](../concepts/ai/diffusion-models.md) |
| 潜空间扩散 | Latent Diffusion | | [已写](../concepts/ai/diffusion-models.md) |
| 思维链 | Chain-of-Thought | CoT | [已写](../concepts/ai/chain-of-thought-and-reasoning.md) |
| 推理模型 | Reasoning Model | | [已写](../concepts/ai/chain-of-thought-and-reasoning.md) |
| 测试时计算 | Test-Time Compute | | [已写](../concepts/ai/test-time-compute.md) |
| 自洽性 | Self-Consistency | | [已写](../concepts/ai/test-time-compute.md) |
| 多 Agent 协调 | Multi-Agent Coordination | | [已写](../concepts/agent/multi-agent-coordination.md) |
| 共享状态 | Shared State | | [已写](../concepts/agent/shared-state-and-conflict.md) |
| 单位任务成本 | Cost per Task | | [已写](../concepts/agent/agent-cost-accounting.md) |
| 短期凭据 | Short-Lived Credential | | [已写](../concepts/agent/agent-credentials.md) |
| 浏览器自动化 | Browser Automation | | [已写](../concepts/agent/gui-and-browser-tools.md) |

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
| Transaction | 事务 | 交易（"交易"另指业务动作，不是数据库术语） |
| Isolation | 隔离 | 孤立 |
| Index | 索引 | 下标（编程语境另用"下标"） |
| Normalization | 范式化 | 规范化（本库统一用"范式化"，避免与其他含义混） |
| Serializable | 可串行化 | 序列化（"序列化"另指 serialize，是完全不同的事） |
| Replication | 复制 | 副本（"副本"指节点，是名词，不是这层机制） |
| Sharding | 分片 | 分库分表（口语说法，本库统一用"分片"） |
| Partitioning | 分区 | 分片（两者不在同一层：分区是单库内，分片是跨节点） |
