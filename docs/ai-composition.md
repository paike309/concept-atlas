# AI 组成总览 · AI Composition

这份文档回答一个问题：**AI 由哪几部分组成，每一部分起什么作用。**

它是 [`maps/ai.md`](../maps/ai.md) 那张依赖图的**文字版**——图回答"谁依赖谁"，本文把那些边讲成因果：每层为什么存在、它替上一层还了什么债、又欠下什么新债。

> **定位**：这是一张**结构地图**，不是事实依据。全部内容整理自 [`concepts/ai/`](../concepts/ai/) 的 34 张卡片，而这些卡片目前的信源等级是 `link-checked`——含义是"来源链接的编号与标题已逐条机器核验（35 个 arXiv 编号零错配），但**正文表述与来源原文尚未逐条比对，数量级数字也未实测**"。见 [`verification-log.md`](verification-log.md) 与 [`round2-verification-checklist.md`](round2-verification-checklist.md)。

---

## 先看一个必须说清的前提

**本库的「AI」= 以 LLM 为中心的 AI 技术栈，不等于「机器学习」。**

库里没有反向传播、损失函数、梯度下降这类通用 ML 基础，也没有分类/回归/聚类、决策树、传统 NLP。这不是遗漏，而是这个库的选材：它讲的是"从一段文本到一句可用的回答"这条链路。

所以下面这份组成表，准确说是**一条 LLM 推理链路的解剖图**。

---

## 一句话总述

AI 不是一个"技术集合"，而是一条**有因果顺序的流水线**：

> 文本要变成模型能算的东西 → 才能被架构处理 → 架构得先被训练出能力 → 能力得跑得起来（成本） → 才能接到外部世界 → 最后得判断行不行

关键不在"有哪些"，而在**每一层都在替上一层还债，同时欠下新债**。这六层就是 [`concepts/ai/`](../concepts/ai/) 属性表里「领域」字段的六种取值。

---

## 六层总览

| 层 | 为什么存在（替上一层还什么债） | 欠下的新债 | 卡片数 |
|---|---|---|---|
| **L0 输入层** | 文本要变成离散符号才能进网络 | 离散化之后就只是 ID，模型看不见"字" | 3 |
| **L1 模型架构** | 序列要能并行计算（循环结构做不到） | 注意力是 $O(n^2)$；位置信息必须另行注入 | 6 |
| **L2 训练** | 架构有了，但能力是空的 | 吃海量数据与算力；行为还得对齐 | 9 |
| **L3 推理** | 权重有了，但要跑得起来 | 显存、延迟、成本变成硬约束 | 6 |
| **L4 工程** | 模型能力要变成产品能力 | 引入检索、提示、选型一整条链路 | 5 |
| **L5 评估与安全** | 上面所有工作怎么算有效？ | 基准会饱和、会被污染，评估本身成为难题 | 5 |

层级分布：**基础 15 / 进阶 15 / 前沿 4**。

---

## 逐层：每张卡起什么作用

### L0 输入层 —— 文本怎么变成数字（3）

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [分词 Tokenization](../concepts/ai/tokenization.md) | 把文本切成词表里已有的最小单位（token）并映射成整数 ID。**模型能看见的只有这些 ID**，切法决定了后面一切的长度与成本 | 基础 | 无（**整条链路的起点**） |
| [词嵌入 Embedding](../concepts/ai/embedding.md) | 把离散 ID 映射为连续向量的可学习参数表，让共现上相似的词在向量空间里靠近。**纯查表，没有计算** | 基础 | 分词 |
| [位置编码 Positional Encoding](../concepts/ai/positional-encoding.md) | 把位置信息注入模型。**因为注意力运算本身对位置完全不敏感**，不注入就没有"谁在前谁在后" | 进阶 | 注意力机制 |

### L1 模型架构 —— 算子怎么拼成模型（6）

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [注意力机制 Attention](../concepts/ai/attention-mechanism.md) | 核心算子：每个位置按"相关性"对其他位置做加权求和，权重由自己的 query 与其他位置的 key 相似度算出。$n$ 个 token 是 $n\times n$ 矩阵，**$O(n^2)$ 的根源** | 基础 | 无（可脱离语言单独理解） |
| [Transformer 架构](../concepts/ai/transformer.md) | 用「注意力 + 前馈层 + 残差 + 层归一化」堆叠，**抛弃循环结构**，因此能在序列维度上并行训练——大模型可行的前提 | 基础 | 注意力机制 |
| [多头注意力](../concepts/ai/multi-head-attention.md) | 把特征维度切 $h$ 份并行算，各自独立学一种关注模式再拼接。单头只能学一种加权方案 | 进阶 | 注意力机制 |
| [前馈网络 FFN](../concepts/ai/feed-forward-network.md) | 按位置独立作用的两层全连接（中间维度通常 ×4）。**模型参数量的大头在这里（约 2/3）**，不跨位置交互 | 基础 | Transformer 架构 |
| [残差连接与层归一化](../concepts/ai/residual-and-normalization.md) | 残差 $y=x+F(x)$ 加层归一化。**让深层网络能训起来**的两项基础设计 | 进阶 | Transformer 架构 |
| [专家混合 MoE](../concepts/ai/moe.md) | 把前馈层换成多个"专家"加一个路由器，每个 token 只激活其中少数几个。**扩大参数量但不等比增加计算量** | 前沿 | 前馈网络 |

### L2 训练 —— 能力从哪来（9）

这一层是 AI 的能力来源，也是算力消耗的绝大部分。

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [训练范式总览](../concepts/ai/training-paradigms.md) | 把随机初始化的网络变成可用助手的三个阶段：预训练 → 监督微调 → 偏好对齐。**这一层的索引** | 基础 | Transformer 架构 |
| [预训练 Pre-training](../concepts/ai/pretraining.md) | 在海量无标注文本上自监督训练，学到语言的统计结构与隐含世界知识。**消耗全流程 95% 以上算力** | 基础 | Transformer 架构 |
| [监督微调 SFT](../concepts/ai/sft.md) | 用「指令 → 理想回答」成对数据继续训练。**让模型从"续写文本"转为"回答问题"**——激活能力并给定形式，不注入新事实 | 基础 | 预训练 |
| [指令微调与对话格式](../concepts/ai/instruction-tuning.md) | 用覆盖大量不同任务类型的指令数据训练。让模型对**没见过的指令**也能正确响应，并固化对话角色与轮次结构 | 进阶 | 监督微调 |
| [LoRA 与参数高效微调](../concepts/ai/lora.md) | 冻结原权重，只训注入的低秩增量 $W+BA$。**用极小代价做微调**（B 初始化为零，保证起点与原模型等价） | 进阶 | 监督微调 |
| [RLHF](../concepts/ai/rlhf.md) | 用人类对成对回答的偏好训练奖励模型，再用强化学习（PPO）最大化奖励。**调整输出偏好，不增加知识** | 进阶 | 监督微调 |
| [DPO](../concepts/ai/dpo.md) | 省掉显式奖励模型与强化学习循环，直接把偏好数据写成训练目标 | 进阶 | RLHF |
| [知识蒸馏](../concepts/ai/knowledge-distillation.md) | 用大模型（教师）的输出训练小模型（学生），学到比硬标签更丰富的"暗知识" | 前沿 | 监督微调 |
| [缩放定律 Scaling Laws](../concepts/ai/scaling-laws.md) | 损失随参数量、数据量、训练算力呈可预测的幂律下降。**把"要不要加算力"从直觉变成可计算的问题** | 前沿 | 预训练 |

### L3 推理 —— 跑起来要多少钱（6）

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [上下文窗口 Context Window](../concepts/ai/context-window.md) | 一次前向计算能读取的 token 上限（输入与输出共享额度）。**"模型无状态"的直接体现——每次前向独立计算，所谓记忆是重放**。全库的分水岭 | 基础 | 注意力机制 · Transformer 架构 |
| [推理成本与显存估算](../concepts/ai/inference-cost.md) | 显存、算力与金钱的量级估算。**主要价值是在动手之前排除不可行的方案** | 基础 | 上下文窗口 |
| [KV Cache](../concepts/ai/kv-cache.md) | 缓存每层每头的 K 与 V，避免每生成一个 token 都重算整个前缀。**只缓存 K/V，不含 Q** | 进阶 | 注意力机制 · 推理成本与显存估算 |
| [采样策略 Sampling](../concepts/ai/sampling.md) | 从模型输出的概率分布中选下一个 token 的规则（温度 / Top-p）。**模型给出分布，采样决定取哪一个** | 基础 | 上下文窗口 |
| [量化 Quantization](../concepts/ai/quantization.md) | 把权重（有时还有激活与 KV Cache）从高精度浮点压到低比特表示。**减少显存占用并提升推理速度** | 进阶 | 推理成本与显存估算 |
| [推理引擎与服务化](../concepts/ai/inference-engines.md) | 把模型高效跑起来并对外提供服务的软件层。**在延迟、吞吐与显存之间做调度** | 前沿 | 推理成本与显存估算 · KV Cache |

### L4 工程 —— 怎么把它用起来（5）

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [提示工程 Prompt Engineering](../concepts/ai/prompt-engineering.md) | 组织输入文本来引导输出。**改变的是这一次调用的上下文，不是模型权重**——补齐缺失信息、明确输出契约、给出判断依据 | 基础 | 上下文窗口 |
| [向量检索 Vector Search](../concepts/ai/vector-search.md) | 查询与文档都表示为向量，按距离找最近邻。**把"外部的知识"变成可检索的**（分块 → 编码 → 建索引 → 最近邻搜索） | 进阶 | 词嵌入 |
| [重排序 Reranking](../concepts/ai/reranking.md) | 在召回结果之上用更精确也更贵的模型重新排序，取前几条。**两阶段：粗召回 → 精排** | 进阶 | 向量检索 |
| [RAG 检索增强生成](../concepts/ai/rag.md) | 先从外部知识库检索相关片段、放进上下文，再让模型基于它们生成。**给模型外部事实**；瓶颈通常在检索，不在生成 | 基础 | 上下文窗口 |
| [模型选型与成本权衡](../concepts/ai/model-selection.md) | 在任务、成本与约束下选择模型与配置的决策方法。**把"用哪个模型"从感觉变成流程**：定义任务 → 建小评测集 → 横向比较 → 按成本与延迟筛选 → 最后看可控性 | 基础 | 评估方法论 · 推理成本与显存估算 |

### L5 评估与安全 —— 怎么知道行不行（5）

| 概念 | 起什么作用 | 层级 | 前置 |
|---|---|---|---|
| [评估方法论 Evaluation](../concepts/ai/evaluation.md) | 判断一个模型或一套提示在**你自己的任务**上到底行不行的方法体系。**没有它，前面所有理解都无法被检验** | 进阶 | 提示工程 |
| [基准与基准污染](../concepts/ai/benchmarks.md) | 标准化评测集合用于横向比较；同时提醒它自带两类系统性偏差——**饱和**与**污染** | 进阶 | 评估方法论 |
| [幻觉 Hallucination](../concepts/ai/hallucination.md) | 流畅、自信、但事实错误或无依据的输出。**划出"能不能当依据"的边界** | 基础 | 预训练 |
| [对齐 Alignment](../concepts/ai/alignment.md) | 让模型的目标与行为符合人类意图与价值 | 进阶 | RLHF · DPO |
| [越狱与红队测试](../concepts/ai/jailbreak.md) | 通过构造特殊输入绕过安全策略。**检验对齐是否真的成立** | 进阶 | 对齐 |

---

## 走一遍完整链路

把 34 个概念串成一次真实调用，比逐条背概念有效得多：

1. 你的输入被 **[分词](../concepts/ai/tokenization.md)** 切成 token、变成整数 ID；
2. **[词嵌入](../concepts/ai/embedding.md)** 把 ID 查表成向量，**[位置编码](../concepts/ai/positional-encoding.md)** 把顺序注入；
3. 向量进入 **[Transformer](../concepts/ai/transformer.md)** 块：**[注意力](../concepts/ai/attention-mechanism.md)** / **[多头注意力](../concepts/ai/multi-head-attention.md)** 按相关性混合信息，**[前馈网络](../concepts/ai/feed-forward-network.md)** 逐位置变换，**[残差与层归一化](../concepts/ai/residual-and-normalization.md)** 保证深层训得动；
4. 这些权重的能力来自 **[预训练](../concepts/ai/pretraining.md) → [监督微调](../concepts/ai/sft.md) →（[RLHF](../concepts/ai/rlhf.md) / [DPO](../concepts/ai/dpo.md) 对齐）**，而 **[LoRA](../concepts/ai/lora.md)** / **[知识蒸馏](../concepts/ai/knowledge-distillation.md)** 是在此之上的低成本改造；
5. 生成每个 token 时，**[采样策略](../concepts/ai/sampling.md)** 决定取哪一个；**[KV Cache](../concepts/ai/kv-cache.md)** 让第 N 个 token 不必重算前 N−1 个前缀；**[量化](../concepts/ai/quantization.md)** 让权重塞得进显存；**[推理引擎](../concepts/ai/inference-engines.md)** 负责把这几件事调度起来；
6. 窗口装不下时，**[上下文窗口](../concepts/ai/context-window.md)** 是硬上限——于是有了 **[向量检索](../concepts/ai/vector-search.md) / [重排序](../concepts/ai/reranking.md) / [RAG](../concepts/ai/rag.md)** 把外部知识搬进来，以及 **[提示工程](../concepts/ai/prompt-engineering.md)** 把输入组织好；
7. 最后 **[评估方法论](../concepts/ai/evaluation.md) / [基准](../concepts/ai/benchmarks.md)** 判断行不行，**[幻觉](../concepts/ai/hallucination.md) / [对齐](../concepts/ai/alignment.md) / [越狱](../concepts/ai/jailbreak.md)** 划出可用与不可用的边界。

---

## 三处最容易断的关节

理解 AI 组成时，这三处不打通，后面会整片长歪：

1. **[分词](../concepts/ai/tokenization.md)** —— 链路起点，决定了长度、成本，以及"模型看不见字"这个事实。不建立它，"中文为什么比英文费 token""模型为什么数不清字母"都无从解释。
2. **[上下文窗口](../concepts/ai/context-window.md)** —— "每次前向独立计算、算完就丢"。**没建立"模型无状态"这一条，后面所有关于 RAG、长上下文、Agent 的理解都会长在错的地基上。**
3. **[评估方法论](../concepts/ai/evaluation.md)** —— 它决定你能不能用数据推翻自己的判断。这不是收尾工作。

---

## 从哪读起

按「前置」的依赖关系拓扑排，一条不跳级的顺序（前 10 张就能立起骨架）：

| 顺序 | 卡片 | 为什么排这里 |
|---|---|---|
| 1 | [分词](../concepts/ai/tokenization.md) | 唯一无前置的起点 |
| 2 | [注意力机制](../concepts/ai/attention-mechanism.md) | 另一个无前置的起点；纯数学，可脱离语言理解 |
| 3 | [词嵌入](../concepts/ai/embedding.md) | 分词之上 |
| 4 | [Transformer 架构](../concepts/ai/transformer.md) | 注意力之上 |
| 5 | [位置编码](../concepts/ai/positional-encoding.md) | 注意力之上，补它缺的位置信息 |
| 6 | [上下文窗口](../concepts/ai/context-window.md) | 架构带来的硬约束 |
| 7 | [预训练](../concepts/ai/pretraining.md) | 能力从哪来 |
| 8 | [训练范式总览](../concepts/ai/training-paradigms.md) | 这一层的索引 |
| 9 | [监督微调](../concepts/ai/sft.md) | 从"续写"到"问答" |
| 10 | [采样策略](../concepts/ai/sampling.md) | 输出为什么有时确定、有时发散 |

其余 24 张都是在这根骨架上加厚或延伸。

---

## 本库未覆盖的部分

诚实列出边界，比含糊带过有用。以下三类是**这条链路上绕不开、但本库目前没有卡片**的：

- **多模态**：视觉编码器、跨模态对齐、语音。库里的 34 张卡全部围绕纯文本。
- **推理时计算**：思维链、推理模型、测试时扩展。目前只有 `prompt-engineering` 与 `evaluation` 沾到边。
- **生成式视觉与序列生成之外**：扩散模型、图像/音频生成。
- **通用机器学习基础**：反向传播、损失函数、优化器、正则化。库的定位是 LLM 栈，不含这一层。

另有一类不是"缺"而是**有意不收**：具体框架、推理服务产品、模型厂商对比。收录原则见 [`maps/software.md`](../maps/software.md) 末尾那句判断标准——"换一个语言或框架之后，这个概念还成立吗？"

`roadmap.md` 目前把三个领域都记为「待写 0」。若要把上面几条纳入，需要先在 [清单](../roadmap.md) 里记为待写，否则会与"待写 0"矛盾。

---

**相关**：[AI 地图](../maps/ai.md)（依赖图）· [总图](../maps/overview.md)（三个领域的关系）· [Agent 组成总览](agent-composition.md) · [软件工程组成总览](software-composition.md)
