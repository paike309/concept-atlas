# 概念清单 · Roadmap

这个库**承认自己缺什么**。勾选框由 GitHub 原生渲染，进度一眼可见。

优先级标记：

| 标记 | 含义 |
|---|---|
| **P0** | 前置链断点。不补上，后面的卡读不下去 |
| P1 | 主干概念。构成领域骨架 |
| P2 | 补充与延伸 |

---

## AI（已写 34 · 待写 9）

### L0 输入层

- [x] [分词 Tokenization](concepts/ai/tokenization.md)
- [x] [词嵌入 Embedding](concepts/ai/embedding.md)
- [x] [位置编码 Positional Encoding](concepts/ai/positional-encoding.md)

### L1 架构层

- [x] [注意力机制](concepts/ai/attention-mechanism.md)
- [x] [Transformer 架构](concepts/ai/transformer.md)
- [x] [前馈网络 FFN](concepts/ai/feed-forward-network.md)
- [x] [残差连接与层归一化](concepts/ai/residual-and-normalization.md)
- [x] [多头注意力](concepts/ai/multi-head-attention.md)
- [x] [专家混合 MoE](concepts/ai/moe.md)

### L2 训练层

- [x] [训练范式总览](concepts/ai/training-paradigms.md)
- [x] [预训练与自监督目标](concepts/ai/pretraining.md)
- [x] [监督微调 SFT](concepts/ai/sft.md)
- [x] [指令微调与对话格式](concepts/ai/instruction-tuning.md)
- [x] [LoRA 与参数高效微调](concepts/ai/lora.md)
- [x] [RLHF](concepts/ai/rlhf.md)
- [x] [DPO](concepts/ai/dpo.md)
- [x] [知识蒸馏](concepts/ai/knowledge-distillation.md)
- [x] [缩放定律](concepts/ai/scaling-laws.md)

### L3 推理层

- [x] [上下文窗口](concepts/ai/context-window.md)
- [x] [推理成本与显存估算](concepts/ai/inference-cost.md)
- [x] [KV Cache](concepts/ai/kv-cache.md)
- [x] [采样策略（温度 / Top-p）](concepts/ai/sampling.md)
- [x] [量化 Quantization](concepts/ai/quantization.md)
- [x] [推理引擎与服务化](concepts/ai/inference-engines.md)

### L4 工程层

- [x] [提示工程 Prompt Engineering](concepts/ai/prompt-engineering.md)
- [x] [RAG 检索增强生成](concepts/ai/rag.md)
- [x] [向量检索](concepts/ai/vector-search.md)
- [x] [重排序 Reranking](concepts/ai/reranking.md)
- [x] [模型选型与成本权衡](concepts/ai/model-selection.md)

### L5 评估与安全

- [x] [评估方法论](concepts/ai/evaluation.md)
- [x] [幻觉 Hallucination](concepts/ai/hallucination.md)
- [x] [对齐 Alignment](concepts/ai/alignment.md)
- [x] [越狱与红队测试](concepts/ai/jailbreak.md)（提示注入见 Agent 侧的[提示注入防御](concepts/agent/prompt-injection-defense.md)）
- [x] [基准与基准污染](concepts/ai/benchmarks.md)

---

## Agent（已写 19 · 待写 5）

### 控制流

- [x] [Agent 循环](concepts/agent/agent-loop.md)
- [x] [终止条件与预算控制](concepts/agent/termination-and-budget.md)
- [x] [ReAct 与规划范式](concepts/agent/react-and-planning.md)
- [x] [Plan-and-Execute](concepts/agent/plan-and-execute.md)
- [x] [单 Agent vs 多 Agent 的取舍](concepts/agent/single-vs-multi-agent.md)

### 工具

- [x] [工具定义与 JSON Schema](concepts/agent/tool-definition.md)
- [x] [MCP 模型上下文协议](concepts/agent/mcp.md)
- [x] [函数调用 Function Calling](concepts/agent/function-calling.md)
- [x] [代码执行沙箱](concepts/agent/code-execution-sandbox.md)
- [x] [权限与最小授权](concepts/agent/least-privilege.md)

### 状态与记忆

- [x] [上下文预算管理](concepts/agent/context-budget.md)
- [x] [上下文压缩与摘要](concepts/agent/context-compression.md)
- [x] [长期记忆](concepts/agent/long-term-memory.md)
- [x] [结构化状态与外部存储](concepts/agent/structured-state.md)

### 质量与安全

- [x] [轨迹可观测性与回放](concepts/agent/trajectory-observability.md)
- [x] [失败模式分类](concepts/agent/failure-modes.md)
- [x] [提示注入防御](concepts/agent/prompt-injection-defense.md)
- [x] [人在回路确认点 HITL](concepts/agent/human-in-the-loop.md)
- [x] [Agent 评测](concepts/agent/agent-evaluation.md)

---

## 软件工程（已写 32 · 待写 16）

### 设计原则

- [x] [依赖注入](concepts/software/dependency-injection.md)
- [x] [单一职责与职责划分](concepts/software/single-responsibility.md)
- [x] [依赖倒置原则](concepts/software/dependency-inversion.md)
- [x] [组合优于继承](concepts/software/composition-over-inheritance.md)
- [x] [幂等性](concepts/software/idempotency.md)

### 结构与边界

- [x] [分层架构与模块边界](concepts/software/layered-architecture.md)
- [x] [端口与适配器](concepts/software/ports-and-adapters.md)
- [x] [领域模型](concepts/software/domain-model.md)
- [x] [契约与接口设计](concepts/software/contract-design.md)

### 正确性

- [x] [测试金字塔](concepts/software/test-pyramid.md)
- [x] [单元测试与可测性](concepts/software/unit-testing.md)
- [x] [契约测试](concepts/software/contract-testing.md)
- [x] [属性测试](concepts/software/property-based-testing.md)
- [x] [可复现构建](concepts/software/reproducible-build.md)

### 变更管理

- [x] [版本控制与分支策略](concepts/software/version-control-branching.md)
- [x] [代码审查](concepts/software/code-review.md)
- [x] [语义化版本](concepts/software/semantic-versioning.md)
- [x] [变更日志 CHANGELOG](concepts/software/changelog.md)
- [x] [架构决策记录 ADR](concepts/software/adr.md)
- [x] [技术债与重构](concepts/software/technical-debt-refactoring.md)

### 运行

- [x] [可观测性（日志 / 指标 / 追踪）](concepts/software/observability.md)
- [x] [超时、重试与退避](concepts/software/timeout-retry-backoff.md)
- [x] [熔断与降级](concepts/software/circuit-breaker.md)
- [x] [背压与容量](concepts/software/backpressure.md)

### 数据与一致性

- [x] [事务与 ACID](concepts/software/transactions-acid.md)
- [x] [隔离级别与并发异常](concepts/software/transaction-isolation.md)
- [x] [索引与查询计划](concepts/software/index-and-query-plan.md)
- [x] [范式化与反范式化](concepts/software/normalization.md)
- [x] [复制与一致性模型](concepts/software/replication-and-consistency.md)
- [x] [分片与分区](concepts/software/sharding-and-partitioning.md)
- [x] [schema 迁移与版本化](concepts/software/schema-migration.md)
- [x] [连接池与容量](concepts/software/connection-pooling.md)

> 这一组是第四批登记后**新开的一条线**（此前本库没有任何数据库卡片）。原分组只有五个是"当时就有的"，新增分组不改变旧编号。

---

## 当前状态

| 批次 | 内容 | 状态 |
|---|---|---|
| 第一批 | 12 个 P0 前置链断点 | 已完成 |
| 第二批 | 26 个 P1 主干概念 | 已完成 |
| 第三批 | 34 个 P2 补充与延伸 | 已完成 |
| 第四批 | 组成视角下的缺口登记（38 项） | 进行中（已写 8） |

**前三批完成的是原清单上的条目；第四批是把组成视角铺开后暴露的缺口正式登记进来。**

这个库的主张是"承认自己缺什么"。组成视角一铺开，三类空区就露出来了：**数据与一致性、安全与运维、跨模态与推理时计算**。把它们留在正文里说"这是缺口"、却在清单上写"待写 0"，等于让清单失真——**勾选框和正文必须说同一件事。**

信源等级方面：**77 张卡片中 76 张为 `link-checked`、1 张为 `unverified`**（该卡的来源被出版社反爬阻断，无法机器核验）。`link-checked` 只保证"引用没引错东西"，不保证"引用的东西支持这句话"。

**P0 与 P1 全部补齐后，从「分词」到「Agent 可上线」已存在一条完整可读的链路**；软件工程侧也已覆盖设计、结构与边界、正确性、变更、运行五条线。P2 补齐了细化与延伸。

---

## 缺口登记（第四批）

以下条目**不是新想法，而是已有文档里已经指出、此前没有落到清单上的缺口**：

- 领域缺口：[AI 组成总览](docs/ai-composition.md) · [Agent 组成总览](docs/agent-composition.md) · [软件工程组成总览](docs/software-composition.md)
- 组成视角下的缺口（系统由哪几块构成、哪几块是空的）：[系统组成总览](docs/system-anatomy.md)

勾选方式与前面一致：写出一张卡，就把 `[ ]` 改成 `[x]` 并补上链接。

### AI（9）

- [ ] 反向传播与梯度下降
- [ ] 损失函数与优化器
- [ ] 正则化与过拟合
- [ ] 思维链与推理模型
- [ ] 测试时计算扩展
- [ ] 视觉编码器
- [ ] 跨模态对齐
- [ ] 语音与音频模型
- [ ] 扩散模型与图像生成

**为什么它们算缺口**：本库的「AI」定义为 LLM 栈（见 [AI 组成总览](docs/ai-composition.md) 开头），所以通用 ML 基础被有意排除在选材之外——但**推理时计算**（思维链、推理模型、测试时扩展）与**多模态**是这条链路上绕不开的，不收就成了结构性空洞。通用 ML 基础是否收录，取决于是否要把本库的边界从"LLM 栈"扩到"机器学习"，这一条需要先定方向再动笔。

### Agent（5）

- [ ] 多 Agent 通信与协调
- [ ] 共享状态与冲突解决
- [ ] Agent 成本核算
- [ ] 凭据与密钥管理
- [ ] GUI 与浏览器操作工具

**为什么它们算缺口**：[单 Agent vs 多 Agent](concepts/agent/single-vs-multi-agent.md) 回答的是"要不要拆"，但拆开之后的**消息协议、共享状态、冲突解决、失败传播**没有卡片；成本与凭据同理，都只被现有卡片"沾到边"。

### 软件工程（剩 16）

> 「数据与一致性」这一组（8 张）已全部写完，见主清单的同名分组——这是第四批登记后**第一组被关掉的缺口**。

**安全（4）**：

- [ ] 认证与授权
- [ ] 加密与密钥管理
- [ ] 输入校验
- [ ] 依赖供应链

**运维与发布（7）**：

- [ ] 部署与发布策略（灰度 / 金丝雀 / 蓝绿 / 回滚）
- [ ] SLO 与错误预算
- [ ] 告警与值班
- [ ] 配置管理
- [ ] 基础设施即代码
- [ ] 事故响应与复盘
- [ ] 容量规划与成本核算

**并发、性能与协议（5）**：

- [ ] 并发与锁
- [ ] 竞态与内存模型
- [ ] 性能剖析 Profiling
- [ ] 缓存策略
- [ ] API 风格取舍与限流

**判断标准没有变**：上面这些都是"换一个语言或框架之后仍然成立"的概念，按本库自己的收录原则**应当收录**；不该收录的仍是 MySQL / Kubernetes / Spring 这类具体产品。

---

## 下一步：核查与升级

清单清空只是「概念已铺齐」，**不等于内容已经可信**。

**已完成的第一步（2026-09-14）**：来源链接的机器核验。35 个 arXiv 编号与标题逐条比对（零错配），33 个非 arXiv 链接检查可达性。全部卡片据此标为 `link-checked`。**这一步查出 10 个问题，其中 1 个是标注造假。** 记录见 [`docs/verification-log.md`](docs/verification-log.md)。

**剩下的三步**（见 [`docs/schema.md`](docs/schema.md) 的等级定义）：

| 动作 | 结果 |
|---|---|
| 逐条比对正文表述与来源原文，确认每个来源确实支撑它标注的那一段 | `link-checked` → `machine-confirmed` |
| 把数量级数字换成实测值，或删掉数字改为定性描述 | — |
| 逐句读正文，把「我的理解」改写成自己的话 | → `human-reviewed` |

建议顺序（按出错代价排序，不按编号）：

1. **事实密集的卡片**：幻觉、基准与污染、缩放定律、量化、KV Cache、推理成本——数值与结论最多，错一条影响一片
2. **自标「待补充」的卡片**：这些卡已经承认某段缺来源，优先补上或删掉
3. **数字类断言**："1 token ≈ 4 字符"、权重显存表、KV 显存公式——用实测替换，或改成定性描述
4. **有时效性的结论**：多头注意力可剪枝、注意力不可解释、Chinchilla 的比例——都可能已被后续研究修正
5. **方法论卡片**：不依赖具体数值，出错概率最低，放最后

两条纪律：

- 卡片被改动后，等级要**退回 `link-checked`**——改动意味着上一次核查不再覆盖当前内容
- 每次核查都在 `docs/verification-log.md` 记一笔，**包括没做的部分**

---

## 建议的写作顺序（第一批的历史记录）

> 这一节是第一批开工前写的，**只对"清单上有哪些条目"成立**，对第四批登记的缺口不适用——缺口怎么排优先级见「缺口登记」那一节。保留在此是为了留下当时的判断依据。

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

---

## 许可

- 知识性内容（concepts/、maps/、docs/ 下的说明性文本）采用 **CC BY-SA 4.0**，见 [LICENSE](LICENSE)。
- 代码与构建脚本（scripts/）采用 **MIT**，见 [LICENSE-CODE](LICENSE-CODE)。
- 第 2 轮核查清单见 [docs/round2-verification-checklist.md](docs/round2-verification-checklist.md)。
