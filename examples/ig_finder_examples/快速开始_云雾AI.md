# IG-Finder 快速开始指南（云雾AI版）

## 🚀 一键运行

本指南专为使用**Tavily搜索引擎**和**云雾AI代理**的用户设计。API密钥已预配置，开箱即用！

### 方法1：最简单的方式

```bash
cd /home/user/webapp
python examples/ig_finder_examples/quick_start_yunwu.py
```

这将使用默认主题 "automatic literature review generation" 运行完整分析。

### 方法2：指定自定义主题

```bash
python examples/ig_finder_examples/quick_start_yunwu.py \
    --topic "多智能体强化学习"
```

### 方法3：完全自定义参数

```bash
python examples/ig_finder_examples/quick_start_yunwu.py \
    --topic "神经架构搜索" \
    --output-dir ./my_output \
    --model gpt-4o \
    --top-k-reviews 15 \
    --top-k-research 40
```

## 📋 已配置的API信息

本脚本已预配置以下信息：

- **搜索引擎**: Tavily（更快、更准确）
- **LLM服务**: 云雾AI代理 (https://yunwu.ai/v1)
- **API密钥**: 已内置配置

无需额外设置环境变量！

## 🎯 预期输出

运行完成后，您将在输出目录看到：

```
ig_finder_output/
├── cognitive_baseline.json          # 认知基线（从综述中提取）
├── phase2_results.json              # 创新识别结果
├── innovation_gap_report.json       # 完整报告（JSON格式）
└── innovation_gap_report.md         # 完整报告（Markdown格式）
```

## 💡 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--topic` | `"automatic literature review generation"` | 研究主题 |
| `--output-dir` | `./ig_finder_output` | 输出目录 |
| `--model` | `gpt-4o` | 使用的模型 |
| `--top-k-reviews` | 10 | 检索综述论文数量 |
| `--top-k-research` | 30 | 检索研究论文数量 |

## 🔍 示例主题

### AI/机器学习
```bash
python examples/ig_finder_examples/quick_start_yunwu.py --topic "大语言模型推理"
python examples/ig_finder_examples/quick_start_yunwu.py --topic "扩散模型图像生成"
python examples/ig_finder_examples/quick_start_yunwu.py --topic "少样本学习"
```

### 交叉学科
```bash
python examples/ig_finder_examples/quick_start_yunwu.py --topic "AI药物发现"
python examples/ig_finder_examples/quick_start_yunwu.py --topic "计算神经科学"
```

### 研究方法
```bash
python examples/ig_finder_examples/quick_start_yunwu.py --topic "自动文献综述生成"
python examples/ig_finder_examples/quick_start_yunwu.py --topic "知识图谱构建"
```

## ⏱️ 预期运行时间

- **阶段1**（认知基线构建）: 约2-5分钟
- **阶段2**（创新识别）: 约5-10分钟
- **报告生成**: 约1-2分钟

**总计**: 大约8-17分钟（取决于论文数量和网络速度）

## 📊 输出示例

完成后，您将看到类似以下的输出：

```
================================================================================
✨ KEY FINDINGS
================================================================================

🎯 Identified 3 innovation clusters:

1. Neural Architecture Search Automation
   📄 Papers: 5
   🔬 Dimensions: methodology, automation
   ⭐ Coherence: 0.85
   💡 Novel approaches using reinforcement learning for automated neural...

2. Efficient Training Methods
   📄 Papers: 4
   🔬 Dimensions: methodology, efficiency
   ⭐ Coherence: 0.78
   💡 New training paradigms that reduce computational costs by...

3. Multi-objective Optimization
   📄 Papers: 3
   🔬 Dimensions: theory, application
   ⭐ Coherence: 0.72
   💡 Frameworks that simultaneously optimize multiple objectives...
```

## 🛠️ 高级用法

### 使用环境变量（可选）

如果您想使用自己的API密钥：

```bash
# 使用配置脚本
source examples/ig_finder_examples/config_yunwu.sh

# 然后运行完整版本
python examples/ig_finder_examples/run_ig_finder_tavily.py \
    --topic "your topic"
```

### 增量执行

如果中途中断，可以跳过已完成的阶段：

```bash
# 只运行阶段1
python examples/ig_finder_examples/quick_start_yunwu.py \
    --topic "your topic" \
    --skip-phase2

# 稍后继续阶段2
python examples/ig_finder_examples/quick_start_yunwu.py \
    --topic "your topic" \
    --skip-phase1
```

## 🐛 常见问题

### Q: 运行时出现网络错误
**A**: 检查网络连接，确保可以访问 yunwu.ai 和 Tavily API

### Q: 没有找到综述论文
**A**: 尝试：
- 用英文描述主题
- 使用更通用的关键词
- 增加 `--top-k-reviews` 的值

### Q: 没有识别到创新簇
**A**: 这可能表示该领域比较成熟，创新较少。可以：
- 降低偏离阈值（但快速启动脚本已使用0.5的平衡值）
- 尝试更具体或更新的主题

### Q: 运行时间太长
**A**: 减少检索的论文数量：
```bash
python examples/ig_finder_examples/quick_start_yunwu.py \
    --topic "your topic" \
    --top-k-reviews 5 \
    --top-k-research 15
```

## 📖 详细文档

- **设计文档**: `../../IG_FINDER_DESIGN.md`
- **完整README**: `README.md`
- **使用指南**: `../../IG_FINDER_使用指南.md`

## 🎓 配置说明

### Tavily vs Bing/You.com

我们推荐使用Tavily的原因：

| 特性 | Tavily | Bing | You.com |
|------|--------|------|---------|
| **速度** | ⚡⚡⚡ | ⚡⚡ | ⚡⚡ |
| **准确性** | ✅✅✅ | ✅✅ | ✅✅ |
| **学术搜索优化** | ✅ | ⚠️ | ⚠️ |
| **API稳定性** | ✅✅✅ | ✅✅ | ✅ |
| **配置简单度** | ✅✅✅ | ✅✅ | ✅✅ |

### 云雾AI代理的优势

- ✅ **国内访问友好**: 无需特殊网络配置
- ✅ **API兼容**: 完全兼容OpenAI API格式
- ✅ **稳定可靠**: 提供稳定的服务
- ✅ **成本优化**: 可能提供更优惠的价格

## 🤝 技术支持

如有问题：
1. 查看详细日志输出
2. 检查 `ig_finder_output/` 目录中的中间结果
3. 参考主README文档
4. 在GitHub上提交Issue

## ✨ 开始探索！

现在您已经准备好使用IG-Finder发现研究领域的创新机会了！

```bash
cd /home/user/webapp
python examples/ig_finder_examples/quick_start_yunwu.py --topic "您感兴趣的研究主题"
```

祝您研究顺利！🎉
