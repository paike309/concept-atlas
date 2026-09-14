# 核查记录 · Verification Log

按时间倒序记录每次核查做了什么、查出什么、哪些没做。**这份文件的意义在于让"没做什么"同样可见。**

---

## 2026-09-14 · 第一轮：来源链接机器核验

**范围**：全部 77 张卡片，121 处来源引用。去重后 69 个 URL——其中 35 个是 arXiv 条目页，34 个是其他站点。

### 方法

| 检查项 | 方法 | 覆盖 |
|---|---|---|
| arXiv 编号 ↔ 论文标题 | 逐个检索 arXiv 条目页，比对返回标题与卡片声称的论文 | 35 个 |
| 其他链接可达性 | 直接 HTTP 请求，记录状态码 | 34 个（其中 2 个为代码仓库，另用 GitHub API 单独确认存在） |

### 结果

- **arXiv 编号：全部正确，零错误。** 35 个编号与标题逐条比对，无一错配（明细见下）。
- **其他链接（34 个）**：25 个返回 200；3 个返回 403（反爬拦截，非链接失效）；5 个本机网络不可达（环境限制，非链接失效）；1 个是模板中的示例占位符，不计。
- **两个代码仓库**：`google/sentencepiece`、`vllm-project/vllm` 经 GitHub API 确认存在。

### 本轮查出并修正的 10 个问题

| # | 卡片 | 问题 | 处理 |
|---|---|---|---|
| 1 | 最初 5 张卡片 | 被标为 `human-reviewed` / `machine-confirmed`，但**从未做过该级别的核查** | 全部改回 `link-checked` |
| 2 | ai/sampling | Hugging Face 文档链接用了已过期的路径（`/main/en/`） | 改为现行规范路径 |
| 3 | ai/tokenization | 引用的 OpenAI tokenizer 页面**未能确认存在**（检索只返回第三方镜像） | 替换为官方分词库 tiktoken |
| 4 | ai/embedding | 把"语义算术"写成嵌入的**普遍性质**——它只对静态嵌入成立 | 加限定：现代上下文化嵌入下不适用 |
| 5 | ai/tokenization | BPE 说成"从单个字符开始"——GPT-2 之后是**字节级 BPE** | 改为"从字节或字符开始"，补字节级的动机与代价 |
| 6 | ai/tokenization | "同一段内容，中文 token 数是英文的 1.5~2 倍"表述有歧义 | 改为"表达同一含义时" |
| 7 | ai/positional-encoding | 把正弦编码说成"可解析外推" | 改为"形式上可计算任意位置，实际外推仍然有限" |
| 8 | ai/lora | "数据量在百万级以下"是**没有来源的具体数字** | 去掉数字，改为"数据量不大时"并注明无通用阈值 |
| 9 | ai/kv-cache | **缺 MQA / GQA**——长上下文成本最关键的优化，属内容缺口 | 补充说明 |
| 10 | ai/attention-mechanism | "注意力不是解释"这一论断缺来源 | 补 Attention is not Explanation（arXiv 1902.10186） |

第 1 条是最严重的一条：它不是知识错误，是**标注造假**——把一个未做的核查步骤写成已完成。这类错误比内容出错更值得记录，因为它破坏的是这一栏本身的可信度。

### 未能机器核验的来源

| URL | 原因 | 所在卡片 |
|---|---|---|
| oreilly.com/library/view/design-patterns-elements/0201633612/ | 403，出版社反爬 | software/composition-over-inheritance |
| dl.acm.org/doi/10.1145/361598.361623 | 403；但检索确认该 DOI 确为 Parnas 1972 那篇 | software/single-responsibility |
| sre.google/sre-book/table-of-contents/ | 本机不可达；检索确认页面存在 | software/observability |
| json-schema.org | 本机不可达；检索确认站点存在 | agent/tool-definition · agent/function-calling |
| huggingface.co/docs/... | 本机不可达；检索确认页面存在 | ai/sampling |
| github.com/google/sentencepiece · github.com/vllm-project/vllm | 本机不可达；经 GitHub API 确认仓库存在 | ai/tokenization · ai/inference-cost · ai/inference-engines · ai/kv-cache |

### 本轮**没有**做的事

`link-checked` 的含义必须说清楚：**它只保证"链接指向的资源确实存在，且就是卡片声称的那一篇"，不保证"该资源支撑正文的具体表述"。**

具体没做：

1. **没有逐条比对正文表述与来源原文。** 例如卡片写"Pre-LN 训练更稳"，我没有读完 On Layer Normalization 那篇并核对它的实验条件。
2. **没有核查任何数量级数字。** "1 token ≈ 4 字符"、"7B FP16 约 14 GB"、KV Cache 显存公式——都来自工程经验，本轮未做实测。
3. **没有核查标记为"自己的判断"的段落。** 每张卡都有若干段落属于综合判断，这是本库风险最高的部分。
4. **没有验证任何论文结论是否已被后续研究修正。** 2019 年的结论到 2026 年可能已有反例（多头注意力可剪枝那条尤其值得重查）。
5. **没有做术语一致性之外的语义检查。** 同一概念在不同卡里的表述可能有细微冲突，本轮未做交叉比对。

### arXiv 编号核对明细（35 个，全部通过）

| 编号 | 标题 |
|---|---|
| 1301.3781 | Efficient Estimation of Word Representations in Vector Space |
| 1503.02531 | Distilling the Knowledge in a Neural Network |
| 1508.07909 | Neural Machine Translation of Rare Words with Subword Units |
| 1512.03385 | Deep Residual Learning for Image Recognition |
| 1603.09320 | Efficient and Robust Approximate Nearest Neighbor Search Using HNSW Graphs |
| 1607.06450 | Layer Normalization |
| 1701.06538 | Outrageously Large Neural Networks: The Sparsely-Gated MoE Layer |
| 1706.03762 | Attention Is All You Need |
| 1810.04805 | BERT: Pre-training of Deep Bidirectional Transformers |
| 1902.10186 | Attention is not Explanation |
| 1905.10650 | Are Sixteen Heads Really Better than One? |
| 1908.10084 | Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks |
| 2001.08361 | Scaling Laws for Neural Language Models |
| 2002.04745 | On Layer Normalization in the Transformer Architecture |
| 2005.11401 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks |
| 2005.14165 | Language Models are Few-Shot Learners |
| 2012.14913 | Transformer Feed-Forward Layers Are Key-Value Memories |
| 2101.03961 | Switch Transformers |
| 2104.09864 | RoFormer: Enhanced Transformer with Rotary Position Embedding |
| 2106.09685 | LoRA: Low-Rank Adaptation of Large Language Models |
| 2109.01652 | Finetuned Language Models Are Zero-Shot Learners |
| 2201.11903 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models |
| 2202.03629 | Survey of Hallucination in Natural Language Generation |
| 2203.02155 | Training language models to follow instructions with human feedback |
| 2203.15556 | Training Compute-Optimal Large Language Models |
| 2204.05862 | Training a Helpful and Harmless Assistant with RLHF |
| 2210.03629 | ReAct: Synergizing Reasoning and Acting in Language Models |
| 2210.17323 | GPTQ: Accurate Post-Training Quantization |
| 2211.09110 | Holistic Evaluation of Language Models |
| 2303.11366 | Reflexion: Language Agents with Verbal Reinforcement Learning |
| 2305.04091 | Plan-and-Solve Prompting |
| 2305.14314 | QLoRA: Efficient Finetuning of Quantized LLMs |
| 2305.18290 | Direct Preference Optimization |
| 2307.03172 | Lost in the Middle: How Language Models Use Long Contexts |
| 2309.06180 | Efficient Memory Management for LLM Serving with PagedAttention |

---

## 下一轮的优先顺序

按**出错代价**排序，不按编号：

1. **事实密集的卡片**：幻觉、基准与污染、缩放定律、量化、KV Cache、推理成本。这些卡里数值与结论最多，错一条影响一片。
2. **自标「待补充」的卡片**：这些卡已经承认某段缺来源。先补上或删掉。
3. **数字类断言**：把"1 token ≈ 4 字符""权重显存表""KV Cache 公式"这类拿实测数据替换掉，或者删掉数字改成定性描述。
4. **可被后续研究推翻的结论**：多头注意力可剪枝、注意力不可解释、Chinchilla 的最优比例——这些都有时效性。
5. **方法论卡片**：不依赖具体数值，出错概率最低，放最后。
