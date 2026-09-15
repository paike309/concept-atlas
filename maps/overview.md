# 总图 · Overview

三个领域不是并列关系，而是层层叠加：

> **AI 是底座**（能力从哪来）→ **Agent 是控制流**（怎么让它自己推进）→ **软件工程是工程约束**（怎么让它可靠地跑起来）。

---

## 全库总图

```mermaid
flowchart TD
    subgraph G_ai["AI / 模型"]
    n_alignment["对齐"]
    n_attention_mechanism["注意力机制"]
    n_benchmarks["基准与基准污染"]
    n_chain_of_thought_and_reasoning["思维链与推理模型"]
    n_context_window["上下文窗口"]
    n_cross_modal_alignment["跨模态对齐"]
    n_diffusion_models["扩散模型与图像生成"]
    n_dpo["直接偏好优化"]
    n_embedding["词嵌入"]
    n_evaluation["评估方法论"]
    n_feed_forward_network["前馈网络"]
    n_hallucination["幻觉"]
    n_inference_cost["推理成本与显存估算"]
    n_inference_engines["推理引擎与服务化"]
    n_instruction_tuning["指令微调与对话格式"]
    n_jailbreak["越狱与红队测试"]
    n_knowledge_distillation["知识蒸馏"]
    n_kv_cache["键值缓存"]
    n_lora["LoRA 与参数高效微调"]
    n_model_selection["模型选型与成本权衡"]
    n_moe["专家混合"]
    n_multi_head_attention["多头注意力"]
    n_positional_encoding["位置编码"]
    n_pretraining["预训练与自监督目标"]
    n_prompt_engineering["提示工程"]
    n_quantization["量化"]
    n_rag["RAG 检索增强生成"]
    n_reranking["重排序"]
    n_residual_and_normalization["残差连接与层归一化"]
    n_rlhf["基于人类反馈的强化学习"]
    n_sampling["采样策略"]
    n_scaling_laws["缩放定律"]
    n_sft["监督微调"]
    n_speech_and_audio_models["语音与音频模型"]
    n_test_time_compute["测试时计算扩展"]
    n_tokenization["分词"]
    n_training_paradigms["训练范式总览"]
    n_transformer["Transformer 架构"]
    n_vector_search["向量检索"]
    n_vision_encoder["视觉编码器"]
    end
    subgraph G_agent["Agent / 控制流"]
    n_agent_cost_accounting["Agent 成本核算"]
    n_agent_credentials["Agent 凭据与密钥管理"]
    n_agent_evaluation["Agent 评测"]
    n_agent_loop["Agent 循环"]
    n_code_execution_sandbox["代码执行沙箱"]
    n_context_budget["上下文预算管理"]
    n_context_compression["上下文压缩与摘要"]
    n_failure_modes["失败模式分类"]
    n_function_calling["函数调用"]
    n_gui_and_browser_tools["GUI 与浏览器操作工具"]
    n_human_in_the_loop["人在回路"]
    n_least_privilege["权限与最小授权"]
    n_long_term_memory["长期记忆"]
    n_mcp["模型上下文协议"]
    n_multi_agent_coordination["多 Agent 通信与协调"]
    n_plan_and_execute["计划-执行"]
    n_prompt_injection_defense["提示注入防御"]
    n_react_and_planning["ReAct 与规划范式"]
    n_shared_state_and_conflict["共享状态与冲突解决"]
    n_single_vs_multi_agent["单 Agent 与多 Agent 的取舍"]
    n_structured_state["结构化状态与外部存储"]
    n_termination_and_budget["终止条件与预算"]
    n_tool_definition["工具定义"]
    n_trajectory_observability["轨迹可观测性与回放"]
    end
    subgraph G_software["软件工程"]
    n_adr["架构决策记录"]
    n_alerting_and_on_call["告警与值班"]
    n_api_design_and_rate_limiting["API 风格取舍与限流"]
    n_authentication_and_authorization["认证与授权"]
    n_backpressure["背压与容量"]
    n_caching_strategies["缓存策略"]
    n_capacity_planning["容量规划与成本核算"]
    n_changelog["变更日志"]
    n_circuit_breaker["熔断与降级"]
    n_code_review["代码审查"]
    n_composition_over_inheritance["组合优于继承"]
    n_concurrency_and_locking["并发与锁"]
    n_configuration_management["配置管理"]
    n_connection_pooling["连接池与容量"]
    n_contract_design["契约与接口设计"]
    n_contract_testing["契约测试"]
    n_dependency_injection["依赖注入"]
    n_dependency_inversion["依赖倒置原则"]
    n_dependency_supply_chain["依赖供应链"]
    n_deployment_strategies["部署与发布策略"]
    n_domain_model["领域模型"]
    n_encryption_and_key_management["加密与密钥管理"]
    n_idempotency["幂等性"]
    n_incident_response["事故响应与复盘"]
    n_index_and_query_plan["索引与查询计划"]
    n_infrastructure_as_code["基础设施即代码"]
    n_input_validation["输入校验"]
    n_layered_architecture["分层架构与模块边界"]
    n_memory_model_and_races["竞态与内存模型"]
    n_normalization["范式化与反范式化"]
    n_observability["可观测性"]
    n_ports_and_adapters["端口与适配器"]
    n_profiling["性能剖析"]
    n_property_based_testing["属性测试"]
    n_replication_and_consistency["复制与一致性模型"]
    n_reproducible_build["可复现构建"]
    n_schema_migration["schema 迁移与版本化"]
    n_semantic_versioning["语义化版本"]
    n_sharding_and_partitioning["分片与分区"]
    n_single_responsibility["单一职责与职责划分"]
    n_slo_and_error_budget["SLO 与错误预算"]
    n_technical_debt_refactoring["技术债与重构"]
    n_test_pyramid["测试金字塔"]
    n_timeout_retry_backoff["超时、重试与退避"]
    n_transaction_isolation["隔离级别与并发异常"]
    n_transactions_acid["事务与 ACID"]
    n_unit_testing["单元测试与可测性"]
    n_version_control_branching["版本控制与分支策略"]
    end
    n_evaluation --> n_agent_evaluation
    n_context_window --> n_agent_loop
    n_context_window --> n_context_budget
```

实线 = 前置依赖，箭头方向即阅读方向。总图只画跨领域的衔接边——各领域内部的依赖顺序，在对应的领域地图里看。

节点不加链接（GitHub 对图内链接支持不稳定），链接在下面的表里。

---

## 四步主线

最短的一条能读通的路：

| 顺序 | 卡片 | 这一层要建立的核心认识 |
|---|---|---|
| 1 | [注意力机制](../concepts/ai/attention-mechanism.md) | 一个算子：按相关度做加权聚合。纯数学，可脱离语言理解 |
| 2 | [Transformer 架构](../concepts/ai/transformer.md) | 把算子组装成架构。重点是"为什么并行化、代价是什么" |
| 3 | [上下文窗口](../concepts/ai/context-window.md) | 架构带来的硬约束。核心认识：**模型无状态，所谓记忆是重放** |
| 4 | [Agent 循环](../concepts/agent/agent-loop.md) | 约束之上长出控制流。多数 Agent 工程问题是第 3 步的预算问题 |

第 3 步是这个库的分水岭。**没建立"模型无状态"这一条，后面所有关于 Agent、RAG、长上下文的理解都会长在错的地基上。**

---

## 卡住时的诊断

概念本身没有内在顺序，但理解有先后。顺序错了会出现"每个字都认识、连起来不懂"的状态。

| 卡在这张 | 典型症状 | 说明上一环的哪个认识没建立 |
|---|---|---|
| [注意力机制](../concepts/ai/attention-mechanism.md) | 说不清缩放因子为什么是 $\sqrt{d_k}$ | —（这是起点） |
| [Transformer](../concepts/ai/transformer.md) | 说不清位置编码为什么必需 | 没抓住"注意力是位置无关的"——它不知道谁在前谁在后 |
| [上下文窗口](../concepts/ai/context-window.md) | 以为"窗口大 = 记得住" | 没抓住"每次前向是独立计算、算完就丢" |
| [Agent 循环](../concepts/agent/agent-loop.md) | 说不清 Agent 和 Workflow 的界线 | 没建立"状态载体即上下文"的认识 |

规律：**卡在第 $n$ 步，问题通常在 $n-1$ 步。** 往回退，不要硬读。

---

## 领域地图

| 地图 | 内容 |
|---|---|
| [AI 地图](ai.md) | 从算子到系统的五层结构 |
| [Agent 地图](agent.md) | 控制流、工具、状态、质量四条线 |
| [软件工程地图](software.md) | 设计、正确性、变更、运行四条线 |

---

## 当前进度

| | 数量 |
|---|---|
| 已写卡片 | 112 |
| 清单待写 | 0（第四批 38 项已全部处理：35 项成卡 + 3 项明确排除） |
| 前置链断点（P0） | 12 个，已补齐 |
| 主干概念（P1） | 26 个，已补齐 |
| 补充与延伸（P2） | 34 个，已补齐 |
| 信源等级 | 111 张 `link-checked`，1 张 `unverified` |

概念已铺齐，来源链接也已逐条机器核验（35 个 arXiv 编号零错配）。但**正文表述与来源原文尚未逐条比对**，数量级数字也未实测——所以现在的正确用法仍是当作索引与提问清单，不是当作事实依据。核查记录见 [`docs/verification-log.md`](../docs/verification-log.md)；第 2 轮逐卡核查清单见 [`docs/round2-verification-checklist.md`](../docs/round2-verification-checklist.md)。

本页的 Mermaid 图由 [`scripts/build_maps.py`](../scripts/build_maps.py) 从各卡「前置」字段自动生成，**不要手改图**——加卡或改前置后跑一次脚本即可同步，CI 也会比对一致性。

每一项的明细和优先级见 [概念清单](../roadmap.md)。**清单里未勾选的部分，就是这个库当前承认的缺口**——把它显式写出来，比靠记忆维护 TODO 可靠。
