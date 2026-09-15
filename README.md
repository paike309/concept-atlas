# 概念图谱 · Concept Atlas

用中文和英文整理 **AI、Agent、软件工程** 的概念。重点不在"定义齐全"，而在**理清谁依赖谁**。

A bilingual knowledge base for AI, agent, and software engineering concepts — organized by **dependency**, not by alphabet.

---

## 为什么不做成术语词典

词典按字母或分类排列：查得到单个词，看不出词与词的关系。结果是每个词都"看过"，但不知道从哪学起、学到哪算懂，也无法判断自己现在的盲区在哪。

这个库只有一条硬要求：**每张卡必须写明「读它之前需要先懂什么」**。于是所有卡片自动连成一张有向图，学习顺序由这张图给出，而不是靠目录顺序猜。

配套的是「边界」一节：写清最容易混淆的邻近概念差在哪。普通词典里这两条都不存在。

---

## 三层结构

| 层 | 位置 | 回答什么问题 |
|---|---|---|
| 地图 | [`maps/`](maps/) | 我该按什么顺序读？现在卡在哪一步？ |
| 卡片 | [`concepts/`](concepts/) | 这个概念是什么？ |
| 清单 | [`roadmap.md`](roadmap.md) | 这个领域还缺哪些概念？下一步写什么？ |

地图不是目录。地图写的是**依赖关系和诊断方法**——哪张卡是另一张的前置，卡住了说明上一环哪里没懂。

---

## 一张卡片长什么样

每张卡固定八节。其中五节是常规内容，三节是防"看着懂了"用的：

| 节 | 作用 |
|---|---|
| 一句话定义 | 中英各一句。英文那句用来对齐术语 |
| **我的理解** | 用自己的话。**这一节不能由 AI 代劳** |
| 核心机制 | 内部怎么运作。给数量级，不给"很大""很快" |
| **边界：它不是什么** | 最易混的邻近概念差在哪 |
| 常见误解 | 写成「误解 → 实际情况」 |
| 应用场景 | 什么时候该用、什么时候不该用，给判断依据 |
| **自测** | 问"为什么""怎么判断"，不问名词解释 |
| 来源对应 | 逐条说明每个来源支撑了上面哪一段 |

加粗的三节是这个库和普通笔记的分界线。跳过它们，卡片退化成摘抄。

完整规格见 [`docs/schema.md`](docs/schema.md)；新建卡片直接复制 [`docs/template.md`](docs/template.md)。

---

## 双语约定

**不建 `zh/` 和 `en/` 两套平行文档。** 平行目录一旦某侧修订就会分叉，之后无法判断哪边是最新的。

实际做法：

- 卡片标题写成 `中文名 · English Term`
- 属性表里单列「英文」和「别名」两行
- 「一句话定义」中英各一句
- 正文以中文为主，**关键术语首次出现时保留英文原文**（注意力机制 Attention、控制反转 IoC），之后再出现统一用中文
- 文件名和路径一律用英文短名，中文只出现在标题和正文里——路径要进 URL，中英混排会在编码上反复出问题

英文入口：[`README.en.md`](README.en.md)。

---

## 图谱怎么画

用 **Mermaid**，写在 markdown 的代码块里：

````
```mermaid
flowchart LR
    A["注意力机制"] --> B["Transformer"] --> C["上下文窗口"]
```
````

GitHub 原生渲染，不需要工具、不需要构建、不需要部署。全库总图见 [`maps/overview.md`](maps/overview.md)。

Mermaid 图里的节点**不加链接**（GitHub 对图内链接支持不稳定），链接放在图下方的表格里。

---

## 索引

### 地图

| 地图 | 内容 |
|---|---|
| [总图](maps/overview.md) | 三个领域的关系、阅读顺序、卡住时的诊断 |
| [AI 地图](maps/ai.md) | 从算子到系统的五层结构 |
| [Agent 地图](maps/agent.md) | 控制流、工具、状态、质量四条线 |
| [软件工程地图](maps/software.md) | 设计、正确性、变更、运行四条线 |

### 文档

| 文档 | 内容 |
|---|---|
| [`docs/schema.md`](docs/schema.md) | 卡片规格：字段、命名、信源等级、正文八节 |
| [`docs/template.md`](docs/template.md) | 新建卡片时复制这个 |
| [`docs/glossary.md`](docs/glossary.md) | 中英术语对照 + 译名约定 |
| [`docs/verification-log.md`](docs/verification-log.md) | 每次核查做了什么、查出什么、**没做什么** |
| [`docs/round2-verification-checklist.md`](docs/round2-verification-checklist.md) | 第 2 轮核查的方法与纪律 |
| [`docs/ai-composition.md`](docs/ai-composition.md) | **AI 由哪些部分组成、每部分起什么作用** |
| [`docs/agent-composition.md`](docs/agent-composition.md) | **Agent 由哪些部分组成、每部分起什么作用** |
| [`docs/software-composition.md`](docs/software-composition.md) | **软件从头到尾需要什么**；数据库与运维的落点与缺口 |

### 卡片

| 领域 | 已写 | 待写 | 地图 |
|---|---|---|---|
| AI | 34 | 0 | [AI 地图](maps/ai.md) |
| Agent | 19 | 0 | [Agent 地图](maps/agent.md) |
| 软件工程 | 24 | 0 | [软件工程地图](maps/software.md) |

**完整卡片索引在 [`roadmap.md`](roadmap.md)** —— 那份清单同时是任务列表和索引，`[x]` 是可点的链接，`[ ]` 表示还没写。

索引不在这里列第二份：同一个信息存两处，改一处必然漏另一处。这一点和双语策略是同一个理由。

---

## 怎么加一张卡

1. 复制 [`docs/template.md`](docs/template.md) 到 `concepts/<领域>/<english-slug>.md`
2. 填属性表。**「前置」栏必须填**，确实没有前置就写"无"
3. 正文里「我的理解」必须用自己的话写，否则这张卡最多只能标到 `machine-confirmed`
4. 回到 [`roadmap.md`](roadmap.md)，把对应条目的 `[ ]` 改成 `[x]`
5. 如果有别的卡引用过这个概念，回去把引用处的「待写」改成链接

---

## 变更怎么进 main

**main 已开启分支保护**：不允许直接推送、不允许强推、不允许删除，且必须走 Pull Request。`validate` 检查不通过就合不进去。

```
从 main 开分支 → 改内容 → 推送分支 → 开 PR → 等 validate 通过 → 合并 → 删分支
```

分支命名：

| 前缀 | 用途 |
|---|---|
| `improve/` | 内容完善（补卡、改错、核查） |
| `docs/` | 只改说明性文件 |
| `chore/` | 工具与配置（校验脚本、工作流） |

**为什么要多走这一步**：这个库的资产是内容，而内容最容易出的错是**结构性的**——漏一个属性字段、章节标题打错一个字、链接指到不存在的卡。这些错误肉眼很难察觉，但脚本能。

代价是改一张卡也要走一次 PR。这个代价是故意付的：**它换来的是"main 上任何一版都是结构完整的"。**

校验检查什么、不检查什么，见 [`scripts/validate.py`](scripts/validate.py) 的文件头说明。**它不检查内容对不对**——通过了不等于卡片可信，只等于卡片合规。

---

## 状态与信源等级

**卡片状态**：`stub` 只有框架内容未写 · `stable` 自洽可依赖 · `stale` 可能已过期待复核

**信源等级**（属性表内）：

| 等级 | 含义 |
|---|---|
| `unverified` | 内容未经任何核查 |
| `link-checked` | 来源链接已机器核验：可达，且指向的资源就是卡片声称的那一篇。**不保证该资源支撑正文表述** |
| `machine-confirmed` | 已逐条确认每个来源确实支撑它标注的那一段 |
| `human-reviewed` | 正文逐句读过，「我的理解」是自己的话 |

四个等级是递进的。**跳级是这一栏最常见的失效方式**——把"链接能打开"当成"内容有据"，再把"内容有据"当成"我懂了"。

「最近核对」日期超过一年未更新的卡片，按 `stale` 处理。

信源等级不是形式要求。三个月后回看，它是唯一能区分"我真懂"和"我存过"的标记。

**当前状态：77 张卡片中，76 张是 `link-checked`，1 张是 `unverified`。**

`link-checked` 的含义要看清：**来源链接的编号与标题已逐条核对（35 个 arXiv 编号零错配），但正文表述与来源原文尚未逐条比对，数量级数字也未实测。** 也就是说，现在能保证的是"引用没引错东西"，不能保证"引用的东西支持这句话"。

**本次核查查出并修正了 10 个问题**，其中一条是标注造假——最初 5 张卡被标成 `human-reviewed`，而那一步从未做过。完整记录（含"没做什么"）见 [`docs/verification-log.md`](docs/verification-log.md)。

所以现在的正确用法仍然是**索引与提问清单**（知道有哪些概念、它们怎么依赖、每张卡该问什么），不是事实依据。升级路径见 [`roadmap.md`](roadmap.md) 的「下一步」。

---

## 许可与第 2 轮核查

- 知识性内容（concepts/、maps/、docs/ 下的说明性文本）采用 **CC BY-SA 4.0**，见 [LICENSE](LICENSE)；代码与构建脚本（scripts/）采用 **MIT**，见 [LICENSE-CODE](LICENSE-CODE)。
- 第 1 轮只做了来源链接的机器核验（`link-checked`）。第 2 轮核查清单与纪律见 [docs/round2-verification-checklist.md](docs/round2-verification-checklist.md)；逐卡结论沉淀在 [docs/verification-log.md](docs/verification-log.md)。

## 结构取自哪里

- [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)——bundle / concept 的定义方式，以及 provenance 与 trust 字段的思路
- [iwe](https://github.com/iwe-org/iwe)——区分「包含关系」与「交叉引用」，同一文档可挂多个父节点
- [ai-llm-glossary](https://github.com/JingHao-Leon/ai-llm-glossary)——中英名称 + 一句话定义 + 简明解释的三段式
- [ai-concept-learner](https://github.com/178-com/ai-skill-mawenwen-)——固定节结构生成学习资料、人工核查后沉淀的流程
