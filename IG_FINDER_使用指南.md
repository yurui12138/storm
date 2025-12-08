# IG-Finder 使用指南

## 什么是 IG-Finder？

IG-Finder (Innovation Gap Finder，创新缺口发现器) 是一个自动识别科研领域创新缺口的框架。它通过两个阶段的分析：

1. **认知自我构建**：分析已有综述，建立领域共识基线
2. **创新非我识别**：分析最新研究论文，识别偏离共识但内部逻辑自洽的创新研究簇

最终生成一份详细的**创新缺口报告**，可作为自动综述生成系统的高质量输入。

## 核心理念

借鉴免疫系统的"自我-非我识别"机制：
- **认知自我 (Self)** = 已有综述中的共识知识
- **创新非我 (Non-self)** = 偏离共识的新兴研究簇
- **目标** = 识别真正的创新，而非重复已知内容

## 快速开始

### 1. 安装

```bash
cd /home/user/webapp
pip install -e .
```

### 2. 配置 API 密钥

```bash
# OpenAI API (必需)
export OPENAI_API_KEY="your_openai_api_key"

# 搜索引擎 API (选择其一)
export BING_SEARCH_API_KEY="your_bing_api_key"
# 或
export YDC_API_KEY="your_you_api_key"
```

### 3. 运行示例

```bash
python examples/ig_finder_examples/run_ig_finder_gpt.py \
    --topic "自动综述生成" \
    --output-dir ./output \
    --retriever bing
```

## 详细使用

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--topic` | 研究主题（必需） | - |
| `--output-dir` | 输出目录 | `./ig_finder_output` |
| `--retriever` | 搜索引擎（bing/you） | `bing` |
| `--top-k-reviews` | 检索综述数量 | 10 |
| `--top-k-research` | 检索研究论文数量 | 30 |
| `--min-cluster-size` | 最小簇大小 | 2 |
| `--deviation-threshold` | 偏离阈值(0-1) | 0.5 |

### Python API 使用

```python
from knowledge_storm.ig_finder import (
    IGFinderRunner,
    IGFinderLMConfigs,
    IGFinderArguments,
)
from knowledge_storm.rm import BingSearch
import os

# 配置语言模型
lm_configs = IGFinderLMConfigs()
lm_configs.init(lm_type="openai")

# 配置检索器
rm = BingSearch(
    bing_search_api_key=os.getenv('BING_SEARCH_API_KEY'),
    k=10
)

# 配置参数
args = IGFinderArguments(
    topic="自动综述生成",
    output_dir="./output",
    top_k_reviews=10,
    top_k_research_papers=30,
)

# 创建并运行
runner = IGFinderRunner(args, lm_configs, rm)
report = runner.run()

# 查看结果
print(f"识别到 {len(report.identified_clusters)} 个创新簇")
for cluster in report.identified_clusters:
    print(f"- {cluster.name}: {len(cluster.core_papers)} 篇论文")
```

## 输出结果

运行完成后，输出目录包含：

```
output/
├── cognitive_baseline.json          # 认知基线（可复用）
├── phase2_results.json              # 第二阶段结果
├── innovation_gap_report.json       # 完整报告(JSON)
└── innovation_gap_report.md         # 完整报告(Markdown)
```

### 报告内容

创新缺口报告包括：

1. **概述摘要**：识别的创新簇数量和主要方向
2. **认知基线**：领域发展历史、研究范式、主流方法
3. **创新簇详情**：
   - 核心论文列表
   - 创新维度（方法论/数据/理论/应用）
   - 偏离分析
   - 潜在影响
4. **缺口分析**：按不同维度分析创新机会
5. **演化叙述**：从共识到创新的知识演化路径
6. **推荐建议**：给下游综述生成系统的指导

## 适用场景

### 学术研究
- 📚 文献综述准备：快速了解领域前沿
- 🔍 研究选题：发现尚未充分探索的方向
- 📝 论文写作：理解自己工作的创新定位

### 科研管理
- 💰 基金评审：识别真正创新的项目
- 🎯 战略规划：确定研究优先级
- 👥 人才评估：评估研究者的创新贡献

## 推荐研究主题

### AI/机器学习
- "自动综述生成"
- "多智能体强化学习"
- "神经架构搜索"
- "少样本学习"
- "大语言模型推理"

### 交叉领域
- "AI药物发现"
- "计算神经科学"
- "人机协作"
- "可解释AI"

## 参数调优建议

### 1. 主题描述
- ✅ **推荐**：具体明确，如"Transformer在时间序列预测中的应用"
- ❌ **避免**：过于宽泛，如"机器学习"

### 2. 检索数量
- **综述少**：增加 `--top-k-reviews` 到 15-20
- **论文少**：增加 `--top-k-research` 到 40-50
- **成本控制**：减少检索数量，但可能影响全面性

### 3. 阈值设置
- **保守策略**：`--deviation-threshold 0.7`（只识别显著创新）
- **激进策略**：`--deviation-threshold 0.3`（识别更多潜在创新）
- **平衡策略**：`--deviation-threshold 0.5`（默认）

### 4. 簇大小
- **严格要求**：`--min-cluster-size 3`（需要3+篇论文支撑）
- **宽松要求**：`--min-cluster-size 1`（接受单篇创新论文）
- **推荐设置**：`--min-cluster-size 2`（默认）

## 与 STORM 集成

IG-Finder 可以为 STORM 提供更好的输入：

```python
# 第一步：识别创新缺口
from knowledge_storm.ig_finder import IGFinderRunner
ig_runner = IGFinderRunner(ig_args, lm_configs, rm)
gap_report = ig_runner.run()

# 第二步：构建增强的主题描述
enhanced_topic = f"{topic}\n\n重点关注以下创新方向：\n"
for cluster in gap_report.identified_clusters:
    enhanced_topic += f"\n## {cluster.name}\n"
    enhanced_topic += f"{cluster.cluster_summary}\n"
    enhanced_topic += f"关键论文：\n"
    for paper in cluster.core_papers[:3]:
        enhanced_topic += f"- {paper.title} ({paper.year})\n"

# 第三步：使用 STORM 生成创新型综述
from knowledge_storm import STORMWikiRunner
storm_runner = STORMWikiRunner(storm_args, lm_configs, rm)
storm_runner.run(
    topic=enhanced_topic,
    do_research=True,
    do_generate_article=True,
)
```

## 常见问题

### Q1: 没有找到综述怎么办？
- 尝试用英文描述主题
- 添加领域关键词（如"survey", "review"）
- 扩大搜索范围（增加 `top-k-reviews`）

### Q2: 没有识别到创新簇？
- 降低 `deviation-threshold`
- 减小 `min-cluster-size`
- 检查是否是成熟稳定的领域（可能确实缺少创新）

### Q3: API 调用太多成本高？
- 减少检索数量
- 使用分阶段执行（`--skip-phase1` 或 `--skip-phase2`）
- 复用认知基线（同一领域多次查询）

### Q4: 内存不足？
- 减少 `top-k-research`
- 分批处理
- 使用更大内存的机器

## 技术支持

- **设计文档**：查看 `IG_FINDER_DESIGN.md` 了解详细架构
- **实现总结**：查看 `IG_FINDER_IMPLEMENTATION_SUMMARY.md` 了解技术细节
- **示例文档**：查看 `examples/ig_finder_examples/README.md` 了解更多用法
- **GitHub**: https://github.com/yurui12138/storm
- **Pull Request**: https://github.com/yurui12138/storm/pull/1

## 贡献指南

欢迎贡献改进！可以：
- 报告 bug 或提出功能请求
- 改进文档和示例
- 优化算法和提示词
- 添加新的检索后端
- 实现可视化界面

## 许可证

继承 STORM 项目的许可证。

## 致谢

IG-Finder 基于以下优秀工作：
- **STORM** (Shao et al., NAACL 2024): 提供了基础框架和多视角机制
- **Co-STORM** (Jiang et al., EMNLP 2024): 提供了动态思维导图的灵感
- **DSPy**: 提供了优雅的 LLM 编程范式

---

**开始使用 IG-Finder，发现科研创新的新机会！** 🚀
