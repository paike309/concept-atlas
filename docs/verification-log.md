# 核查记录 · Verification Log

按时间倒序记录每次核查做了什么、查出什么、哪些没做。**这份文件的意义在于让"没做什么"同样可见。**

---

## 2026-09-16 · 第七批：软件工程剩余 5 张 + Agent 5 张 + AI 6 张（第四批缺口收口）

**范围**：新写 16 张卡，本轮同时宣告第四批缺口登记**全部处理完毕**。

| 组 | 卡片 |
|---|---|
| 软件工程 · 并发、性能与协议（5） | [并发与锁](../concepts/software/concurrency-and-locking.md) · [竞态与内存模型](../concepts/software/memory-model-and-races.md) · [性能剖析](../concepts/software/profiling.md) · [缓存策略](../concepts/software/caching-strategies.md) · [API 风格取舍与限流](../concepts/software/api-design-and-rate-limiting.md) |
| Agent（5） | [多 Agent 通信与协调](../concepts/agent/multi-agent-coordination.md) · [共享状态与冲突解决](../concepts/agent/shared-state-and-conflict.md) · [Agent 成本核算](../concepts/agent/agent-cost-accounting.md) · [Agent 凭据与密钥管理](../concepts/agent/agent-credentials.md) · [GUI 与浏览器操作工具](../concepts/agent/gui-and-browser-tools.md) |
| AI（6） | [思维链与推理模型](../concepts/ai/chain-of-thought-and-reasoning.md) · [测试时计算扩展](../concepts/ai/test-time-compute.md) · [视觉编码器](../concepts/ai/vision-encoder.md) · [跨模态对齐](../concepts/ai/cross-modal-alignment.md) · [语音与音频模型](../concepts/ai/speech-and-audio-models.md) · [扩散模型与图像生成](../concepts/ai/diffusion-models.md) |

来源共 13 处，去重后 9 个 URL。**6 个返回 200 且标题一致**；**3 个可达但标题未能抓取**（脚本渲染页面）：playwright.dev、developer.hashicorp.com（上一批）、以及同类情形，均已在卡片内显式注明。

### 本轮**没有**做的事

1. **没有实测任何行为。** 并发与竞态的行为、剖析工具的输出、缓存的命中率、生成模型的输出质量——**全部未在本机复现**。逐条看：竞态卡描述的是"缺失同步会发生什么"，而不是"我构造了一个竞态并复现了它"。
2. **没有核对任何模型或产品的版本参数。** 卡片刻意不写"某模型多少 token""某工具默认多少步"，这些数字的保质期以周计。
3. **没有验证多模态与扩散模型的任何定量结论。** 视觉 token 数量、音频的成本量级、扩散的步数与质量关系，都是**定性描述 + 量级直觉**，不是实测曲线。
4. **「我的理解」一节仍由 AI 起草**（全部 35 张新卡同一情况），因此无一张标 `human-reviewed`。

### 一个必须写下来的规模提醒

本次会话前后共补 **35 张卡**（数据与一致性 8 + 安全 4 + 运维 7 + 并发性能协议 5 + Agent 5 + AI 6）。**这个速度与核查深度是不匹配的**：

| 维度 | 现状 |
|---|---|
| 卡片数量 | 77 → **112** |
| 信源等级 | 111 张 `link-checked`、1 张 `unverified` |
| `machine-confirmed` | **0 张** |
| `human-reviewed` | **0 张** |

**`link-checked` 的含义没有变**：只保证"引用没引错东西"。**规模上去了，验证没跟上**——这是当前这个库最大的债务，且它不会因为卡片变多而自动减轻。下一步的正确顺序是**加固验证，而不是继续扩面**。

### 本轮做的边界决策（3 项明确排除）

AI 域原登记的 9 项缺口里，**反向传播与梯度下降 · 损失函数与优化器 · 正则化与过拟合**三项**明确不收**，理由与判断标准已写入[清单](../roadmap.md)的「缺口登记」节：本库的「AI」定义为 LLM 栈，不收通用 ML 基础。**把它们标为"明确不收"而不是"待写"，是为了让"待写"这个数字保持诚实。**

### 附带发现并修正的过期内容

补卡暴露出**文档里写死的数字会过期**这一类问题（composition 文档里的"34 张卡片""五组""六层"等）。本轮的处理：

- 活数字（README / 地图 / 清单）→ 更新为当前值
- 结构性数字（层数、组数）→ 更新并标注"截至 2026-09-16"
- 易变细节（各层卡片数）→ **改为不写死**，并在 ai-composition 末尾加了一句"若与文件数不一致，以文件为准"

**这类问题的根源不是疏忽，而是"文档里存了会变的事实"。** 处理原则：**能算出来的就不要写死，必须写的就标注日期。**

---

## 2026-09-16 · 第六批：运维与发布 7 张

**范围**：新写 7 张卡 —— [部署与发布策略](../concepts/software/deployment-strategies.md)、[SLO 与错误预算](../concepts/software/slo-and-error-budget.md)、[告警与值班](../concepts/software/alerting-and-on-call.md)、[配置管理](../concepts/software/configuration-management.md)、[基础设施即代码](../concepts/software/infrastructure-as-code.md)、[事故响应与复盘](../concepts/software/incident-response.md)、[容量规划与成本核算](../concepts/software/capacity-planning.md)。共 9 处来源引用，去重后 7 个 URL。

### 方法

可达性 + 页面标题比对。

### 结果与一个例外

6 个 URL 返回 200 且标题与卡片一致：

| URL | 页面标题 |
|---|---|
| martinfowler.com/bliki/BlueGreenDeployment.html | Blue Green Deployment |
| martinfowler.com/bliki/CanaryRelease.html | Canary Release |
| openslo.com | OpenSLO |
| docs.aws.amazon.com/.../reliability-pillar/welcome.html | Reliability Pillar - AWS Well-Architected Framework |
| prometheus.io/docs/alerting/latest/overview/ | Alerting overview \| Prometheus |
| 12factor.net/config | The Twelve Factor App |
| postmortems.pagerduty.com | PagerDuty Postmortem Documentation |

**一个例外**：`developer.hashicorp.com/terraform/intro` 返回 200，但页面由脚本渲染，**抓取不到 `<title>`，无法完成标题比对**。这是本库第一个"可达但标题未核"的来源，处理方式是：

- 该卡的信源等级仍标 `link-checked`，但**在卡片内与「来源对应」下方显式注明这一点**（不靠读者去猜）
- 卡片内容保持在机制层（声明式、plan/apply、状态管理），不写任何依赖具体版本的行为细节

**这条记录本身比这次核查更重要**：它说明 `link-checked` 不是"全部核过"，而是"核过可达性，标题核对程度因页面形态而异"。等级标签是压缩过的信息，压缩就有损——**遇到边界情况要写出来，而不是让标签替它撒谎。**

### 本轮**没有**做的事

1. **没有实测任何运维行为。** 蓝绿切换的回滚时间、金丝雀放量比例与检出率的关系、SLO 的燃烧率窗口参数、压测的崩溃点——**全部来自来源文档与工程共识，本机未复现任何一项**。运维类卡片的可信度尤其依赖"在自己的系统上验证过"，这一点本库做不到。
2. **没有绑定任何具体平台或工具的参数。** 卡片刻意不写"某云的金丝雀默认比例"这类内容。
3. **没有核对 AWS Well-Architected 与 OpenSLO 的版本。** 两者都在演进。
4. **「我的理解」一节仍由 AI 起草**，未标 `human-reviewed`。

### 进度

第四批登记的 38 项缺口已关闭 19 项（数据与一致性 8 + 安全 4 + 运维与发布 7），剩 19 项：AI 9 · Agent 5 · 软件工程 5。

---

## 2026-09-16 · 第五批：安全 4 张

**范围**：新写 4 张卡 —— [认证与授权](../concepts/software/authentication-and-authorization.md)、[加密与密钥管理](../concepts/software/encryption-and-key-management.md)、[输入校验](../concepts/software/input-validation.md)、[依赖供应链](../concepts/software/dependency-supply-chain.md)。共 9 处来源引用，去重后 7 个 URL。

### 方法

可达性 + 页面标题比对（与上两轮相同）。

### 结果

**7 个 URL 全部 200，标题与卡片声称一致**：

| URL | 页面标题 |
|---|---|
| owasp.org/www-project-application-security-verification-standard/ | OWASP Application Security Verification Standard (ASVS) |
| cheatsheetseries.owasp.org/.../Authentication_Cheat_Sheet.html | Authentication - OWASP Cheat Sheet Series |
| rfc-editor.org/rfc/rfc6749 | RFC 6749: The OAuth 2.0 Authorization Framework |
| cheatsheetseries.owasp.org/.../Cryptographic_Storage_Cheat_Sheet.html | Cryptographic Storage - OWASP Cheat Sheet Series |
| rfc-editor.org/rfc/rfc8446 | RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3 |
| cheatsheetseries.owasp.org/.../Input_Validation_Cheat_Sheet.html | Input Validation - OWASP Cheat Sheet Series |
| cwe.mitre.org/data/definitions/20.html | CWE-20: Improper Input Validation |
| slsa.dev | SLSA • Supply-chain Levels for Software Artifacts |
| owasp.org/www-project-dependency-check/ | OWASP Dependency-Check |

### 本轮**没有**做的事

1. **没有做任何安全测试。** 卡片里的漏洞成因（IDOR、授权漏检、CBC 篡改、nonce 重复、绕过变体）**全部来自来源文档，本机未验证任何一条**。安全类卡片尤其要说清这一点：它们描述的是"已知的攻击形态"，不是"已测过的防护效果"。
2. **没有核对 OWASP 与 CWE 条目的版本。** 这两份都是持续修订的文档，卡片据此写的做法可能在版本演进而变化。
3. **没有覆盖任何具体框架或库的实现细节。** 卡片刻意停留在机制层，不写"某框架的某个注解"。
4. **「我的理解」一节仍由 AI 起草**，因此未标 `human-reviewed`。

### 进度

第四批登记的 38 项缺口已关闭 12 项（数据与一致性 8 + 安全 4），剩 26 项：AI 9 · Agent 5 · 软件工程 12（运维与发布 7 · 并发性能与协议 5）。

---

## 2026-09-16 · 第四批续：数据与一致性（分布式 4 张）

**范围**：新写 4 张卡 —— [复制与一致性模型](../concepts/software/replication-and-consistency.md)、[分片与分区](../concepts/software/sharding-and-partitioning.md)、[schema 迁移与版本化](../concepts/software/schema-migration.md)、[连接池与容量](../concepts/software/connection-pooling.md)。共 9 处来源引用，去重后 6 个 URL。

### 方法

与上一轮相同（可达性 + 页面标题比对），覆盖 6 个 URL。

### 结果

**6 个 URL 全部返回 200，标题与卡片声称一致**：

| URL | 页面标题 |
|---|---|
| postgresql.org/docs/current/ddl-partitioning.html | PostgreSQL 18: 5.12. Table Partitioning |
| postgresql.org/docs/current/runtime-config-connection.html | PostgreSQL 18: 19.3. Connections and Authentication |
| postgresql.org/docs/current/hot-standby.html | PostgreSQL 18: 26.4. Hot Standby |
| martinfowler.com/articles/evodb.html | Evolutionary Database Design |
| github.com/brettwooldridge/HikariCP | HikariCP 项目仓库 |
| jepsen.io/consistency | Consistency |
| dataintensive.net | Designing Data-Intensive Applications |

（实际 7 个 URL，其中 DDIA 与 Jepsen 在两张卡中共用。）

### 本轮**没有**做的事

1. **没有实测任何行为。** 复制延迟的量级、quorum 的失效场景、分片再平衡的耗时、连接池大小与吞吐的关系曲线，全部来自来源文档与工程共识，**本机未做任何复现**。
2. **没有逐条比对正文表述与来源原文。** 仍是"引对了文档"，不是"文档支持这句话"。
3. **没有在多个数据库上核对。** 分区实现、加列是否重写整表、在线建索引的能力，各数据库差异很大，卡片里是定性描述。
4. **没有核验任何具体产品的参数默认值。** 卡片刻意不写默认值——那类数字随版本变化，写进来就等于埋一颗会过期的钉子。
5. **「我的理解」一节同样由 AI 起草。** 与上一轮同一问题，这 4 张卡也未标 `human-reviewed`。

### 进度

**数据与一致性这一组（8 张）已全部写完**，是第四批登记的 38 项缺口里**第一组被关掉的**。剩余：AI 9 · Agent 5 · 软件工程 16（安全 4 · 运维与发布 7 · 并发性能与协议 5）。

随着这 8 张到位，[`docs/system-anatomy.md`](system-anatomy.md) 的「链五」（状态边界 → 并发 → 失败恢复 → 重试策略）**第一次画得全**——在此之前它只能写到"隔离级别管不到跨节点"就断掉。

---

## 2026-09-15 · 第四批补写：数据与一致性（单库 4 张）

**范围**：新写 4 张卡 —— [事务与 ACID](../concepts/software/transactions-acid.md)、[隔离级别与并发异常](../concepts/software/transaction-isolation.md)、[索引与查询计划](../concepts/software/index-and-query-plan.md)、[范式化与反范式化](../concepts/software/normalization.md)。共 8 处来源引用，去重后 6 个 URL。

### 方法

| 检查项 | 方法 | 覆盖 |
|---|---|---|
| 链接可达性 | HTTP 请求并记录状态码 | 8 处（去重 6 个） |
| 页面标题与卡片声称是否一致 | 抓取页面 `<title>`，与卡片「参考来源」里声称的名称逐条比对 | 6 个 |

### 结果

- **6 个 URL 全部返回 200，标题与卡片声称一致**，据此标 `link-checked`：
  - PostgreSQL 18 文档 4 页：3.4 Transactions · 13.2 Transaction Isolation · Chapter 11 Indexes · 14.1 Using EXPLAIN
  - Use The Index, Luke!（电子书站）
  - Designing Data-Intensive Applications（书站）

### 本轮取消的候选来源

| 候选 | 状态 | 处理 |
|---|---|---|
| Codd 1970, *A Relational Model of Data for Large Shared Data Banks*（dl.acm.org DOI） | 403 出版社反爬 | 未采用；范式化卡改用可核验来源，正文不再依赖该篇 |
| martinfowler.com/bliki/Denormalized.html | **404，页面不存在** | 未采用 |
| arXiv 1907.07902（Hermitage）· 1302.0309（HAT） | 本机不可达（连接失败） | 未采用，改引 Jepsen 与 PostgreSQL 文档 |

后两条值得记一笔：**候选来源里有两个是"看起来应该存在"却没有用成的**——一个是猜测的 URL（实际 404），一个是环境不可达。第一轮核查也遇到过同类情况（6 条来源当时未能核验）。**"以为有"和"核过有"之间的距离，就是这一栏存在的理由。**

### 本轮**没有**做的事

1. **没有逐条比对正文表述与来源原文。** 例如"最左前缀"的具体适用条件、index-only scan 的可见性限制，来源文档里有更精确的表述；本轮只核到"引对了文档"，没核到"文档支持这句话"。
2. **没有实测任何数字。** 索引选择性、长事务导致膨胀的程度，均未在本机复现。
3. **没有跨数据库核对。** 隔离级别的实现差异（PostgreSQL 与 MySQL 不完全对齐）在卡里是定性描述，未逐库验证。
4. **「我的理解」一节由 AI 起草。** 按 [`schema.md`](schema.md) 的要求，这一节本应由本人重写才可能达到 `human-reviewed`。这 4 张卡没有标 `human-reviewed`，**这一栏的纪律仍待作者本人执行**——写卡的人不是拥有理解的人，这一点不能靠标等级掩盖。

### 缺口进度

数据与一致性这一组共 8 张，本轮补齐单库的 4 张；**分布式 4 张仍缺**（复制与一致性模型、分片与分区、schema 迁移与版本化、连接池与容量）。[`docs/system-anatomy.md`](system-anatomy.md) 的「链五」目前画不全，原因就是这四张。

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
5. **没有做语义层的交叉比对。** 同一概念在不同卡片里的表述是否有细微冲突，本轮只做了结构层检查（见下），没有逐对读过去。

### 附带：结构层交叉检查

同一轮里另外做了一项机器检查——**卡片与术语表是否对齐**。检查方式：每张卡片的「英文」主术语是否在 `docs/glossary.md` 里出现；术语表里每个链接指向的卡片，该术语能否在该卡的「英文」或「别名」里找到。

结果：

- 查出术语表**漏收 8 个已有专门卡片的术语**：评估方法论、模型选型、ReAct、上下文预算管理、失败模式、Agent 评测、版本控制与分支策略、代码审查 — 已补齐。
- 发现术语表的「卡片」栏把两种情况混在一起（有专门卡片 vs 内容被别的卡覆盖），已改为 `[已写]` 与 `[见 X]` 两种标记，并在表头说明。
- 77 张卡片的 H1 标题无重复。
- 补齐后复跑，剩余 34 项命中均为**命名差异**（卡片用复合标题如 "Agent Failure Modes"，术语表用单词 "Failure Modes"），逐条人工确认都有对应条目，不是真的漏收。

**这项检查只覆盖结构，不覆盖语义。** 它不能发现"两张卡对同一个概念的说法不一致"，只能发现"术语表漏了一个词"。

顺带记一次方法上的教训：这个检查脚本第一版有解析 bug——用非重叠正则按 `|` 抓单元格时，会把交替的列吃掉，导致 58 张卡片被误报为"术语表未收录"。**先怀疑脚本，再怀疑数据。**

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
