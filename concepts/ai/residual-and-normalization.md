# 残差连接与层归一化 · Residual & Normalization

| 属性 | 值 |
|---|---|
| 英文 | Residual Connection & Layer Normalization |
| 别名 | 残差 · 层归一化 · LayerNorm · RMSNorm |
| 领域 | AI / 模型架构 |
| 层级 | 进阶 |
| 前置 | [Transformer 架构](transformer.md) |
| 相关 | [前馈网络](feed-forward-network.md) |
| 状态 | `stable` |
| 信源等级 | `link-checked` 来源链接已于 2026-09-14 机器核验（可达性 + 编号与标题一致），正文表述未核查 |
| 最近核对 | 2026-09-14 |

**参考来源**

1. Deep Residual Learning for Image Recognition — <https://arxiv.org/abs/1512.03385>（论文）
2. Layer Normalization — <https://arxiv.org/abs/1607.06450>（论文）
3. On Layer Normalization in the Transformer Architecture — <https://arxiv.org/abs/2002.04745>（论文）

---

## 一句话定义

**中文**：残差连接（把子层的输入直接加到输出上）与层归一化（规范化特征维度上的激活分布）——让深层网络能训练起来的两项基础设计。

**English**: Residual connections (adding a sublayer's input to its output) and layer normalization — the two building blocks that make deep networks trainable.

## 我的理解

它们常被并称，但解决的是**两个不同的问题**：

- **残差连接解决"深度"**。没有它，梯度穿过几十层后会衰减到无法有效更新底层参数。它提供了一条恒等映射的捷径，让梯度可以直接回传，同时保留原始信息。
- **层归一化解决"分布漂移"**。每层的输出分布随训练不断变化，后续层要不断重新适应。归一化把激活拉回稳定范围，使训练可以用更大的学习率。

## 核心机制

- **残差**：$y = x + F(x)$。要求 $F$ 与 $x$ 维度一致，否则需要投影
- **LayerNorm vs BatchNorm**：BatchNorm 在**批**维度归一化，依赖批统计；LayerNorm 在**特征**维度归一化，与批大小无关。序列任务中批内长度不一，BatchNorm 不稳定，所以序列模型默认用 LayerNorm
- **Pre-LN vs Post-LN**：归一化放在子层**之前**（Pre）还是**之后**（Post）。**Pre-LN 训练更稳**，是当前主流；Post-LN 需要学习率预热，深层时不稳定
- **RMSNorm**：去掉均值中心化，只做缩放。更省计算，被多数现代大模型采用
- **改造注意点**：改隐藏维度会影响所有残差路径，必须同步

## 边界：它不是什么

- **与"梯度裁剪"的区别**：裁剪限制梯度的**幅度**；残差改变梯度的**传播路径**。两者解决的不是同一类问题。
- **与"初始化策略"的区别**：初始化影响训练的**起点**，残差影响**深层的传播能力**。

## 常见误解

1. **残差只是为了防梯度消失** → 它还帮助优化、保留信息、使深层网络更容易学习恒等映射。
2. **归一化只是为了数值稳定** → 它也扩大可用的学习率范围，直接影响能否训起来。
3. **Pre-LN 和 Post-LN 差别不大** → 在深层模型上，Post-LN 的不稳定性是实质性的。
4. **RMSNorm 只是简化版 LayerNorm** → 它去掉了中心化这一步，这是有意的设计取舍，不是省事的省略。

## 应用场景

- **该关注**：训练不稳定时的排查（先看归一化位置与学习率）、模型结构改造（改隐藏维度要同步残差）、跨框架推理时的归一化实现差异
- **判断依据**：如果能训起来但收敛慢，先看归一化；如果梯度异常，先看残差路径

## 自测

1. 残差连接和层归一化各自解决什么问题？用一句话分别说清。
2. 为什么序列模型用 LayerNorm 而不是 BatchNorm？
3. Pre-LN 为什么比 Post-LN 更稳？这个差别在什么规模的模型上才显著？

## 来源对应

- **《Deep Residual Learning》**——支撑残差连接的动机与恒等映射的作用
- **《Layer Normalization》**——支撑 LayerNorm 的定义与相对 BatchNorm 的性质
- **《On Layer Normalization in the Transformer Architecture》**——支撑 Pre-LN / Post-LN 的稳定性差异
