# IG-Finder Framework Summary

## 框架核心流程总结

### 整体架构

```
IG-Finder = Phase 1 (认知自我构建) + Phase 2 (创新非我识别) + 报告生成
```

### Phase 1: 认知自我构建 (Cognitive Self Construction)

**目标**: 从综述论文中提取共识知识，构建认知基线

**流程**:
1. **ReviewRetriever**: 检索综述论文
   - 使用多个查询: "{topic} survey/review/overview"
   - 去重、过滤、按相关度排序
   - 返回 top-k 综述论文

2. **ConsensusExtractor**: 提取结构化共识
   - 使用 LLM (GPT-4o) 分析每篇综述
   - 提取: 研究范式、主流方法、知识边界、概念层次
   - 输出 ReviewPaper 对象

3. **CognitiveBaselineBuilder**: 构建认知基线
   - 聚合所有综述的共识知识
   - 构建动态思维导图 (KnowledgeBase)
   - 所有节点标记为 CONSENSUS 状态
   - 输出 CognitiveBaseline 对象

**输出**: 
- cognitive_baseline.json
- 包含: 研究范式、方法、边界、思维导图

### Phase 2: 创新非我识别 (Innovative Non-self Identification)

**目标**: 识别偏离共识但具有内在逻辑一致性的创新簇

**流程**:
1. **FrontierPaperRetriever**: 检索前沿研究论文
   - 排除综述类论文
   - 按时效性排序 (优先最新)
   - 返回 top-k 研究论文

2. **ExpertPerspectiveGenerator**: 生成专家视角
   - 方法学专家 (Methodology Expert)
   - 数据范式专家 (Data Paradigm Expert)
   - 理论框架专家 (Theoretical Framework Expert)
   - 应用领域专家 (Application Domain Expert)

3. **DifferenceAwareAnalyzer**: 差异感知分析
   - 对每篇论文从多个专家视角分析
   - 计算与认知基线的偏离度 (0-1)
   - 识别偏离维度 (方法、数据、理论、应用)
   - 输出 DeviationAnalysis 对象

4. **InnovationClusterIdentifier**: 识别创新簇
   - 按偏离维度分组
   - 过滤显著偏离 (deviation > threshold)
   - LLM 验证内在一致性
   - 创建 InnovationCluster 对象

**输出**:
- phase2_results.json
- 包含: 创新簇、偏离分析、聚类数据

### 思维导图管理

**EvolutionStateAnnotator**: 标注演化状态
- CONSENSUS: 共识知识 (来自综述)
- CONTINUATION: 延续共识的研究
- DEVIATION: 孤立的偏离
- INNOVATION: 成簇的一致性偏离
- POTENTIAL_GAP: 潜在缺口

**DynamicMindMapManager**: 管理动态演化
- 更新思维导图节点状态
- 附加偏离度量
- 跟踪创新路径
- 导出可视化数据

### 报告生成

**InnovationGapReportGenerator**: 生成创新缺口报告

1. **认知基线摘要**: 总结共识知识 (3-5段)
2. **维度缺口分析**: 按维度分析创新缺口
3. **演化叙事**: 生成知识演化故事 (5-7段)
4. **评审建议**: 为下游评审系统提供建议
5. **统计数据**: 编译关键指标

**输出**:
- innovation_gap_report.json (结构化)
- innovation_gap_report.md (可读)

## 核心数据结构

```python
# Phase 1 输出
CognitiveBaseline:
    - review_papers: List[ReviewPaper]
    - consensus_map: KnowledgeBase (思维导图)
    - research_paradigms: List[ResearchParadigm]
    - mainstream_methods: List[Method]
    - knowledge_boundaries: Dict[Boundary]
    - temporal_coverage: TimeRange

# Phase 2 输出  
InnovationCluster:
    - cluster_id: str
    - name: str
    - core_papers: List[ResearchPaper]
    - deviation_from_consensus: DeviationAnalysis
    - internal_coherence_score: float (0-1)
    - innovation_dimensions: List[str]
    - supporting_evidence: List[Evidence]
    - cluster_summary: str
    - potential_impact: str

# 最终报告
InnovationGapReport:
    - cognitive_baseline_summary: str
    - identified_clusters: List[InnovationCluster]
    - gap_analysis_by_dimension: Dict[GapAnalysis]
    - evolution_narrative: str
    - mind_map_visualization_data: Dict
    - recommendations_for_review: str
    - statistics: Dict
```

## 关键算法

### 偏离度计算
```python
deviation_score = mean([
    d(paper, expert_i, baseline) 
    for expert_i in expert_perspectives
])

where d() ∈ [0, 1]
```

### 创新簇识别
```python
1. Filter: papers with deviation_score > threshold
2. Group: by deviation_dimensions
3. Validate: LLM coherence test
4. Create: InnovationCluster if coherent
```

### 演化状态分配
```python
if paper in cluster_papers:
    state = INNOVATION
elif deviation > 0.7:
    state = DEVIATION  
elif deviation > 0.3:
    state = POTENTIAL_GAP
else:
    state = CONTINUATION
```

## 技术栈

- **Framework**: DSPy (模块化 LLM 编程)
- **LLM**: GPT-4o, Azure OpenAI, Together AI
- **Retrieval**: Tavily, Bing, You.com
- **Data**: 层次化知识图、时序追踪

## 性能指标

- **Phase 1**: 5-10分钟 (10篇综述)
- **Phase 2**: 10-15分钟 (30篇论文)
- **报告生成**: 2-3分钟
- **总计**: 17-28分钟

- **LLM调用**: 50-100次
- **Token使用**: 200K-500K
- **内存**: <2GB
- **存储**: <10MB/报告

## 核心创新点

1. **认知基线建模**: 显式构建领域共识知识
2. **多视角分析**: 4个专家视角全面评估
3. **簇验证**: 内在一致性验证而非单纯新颖性
4. **动态演化**: 5状态知识演化追踪
5. **结构化报告**: 为下游系统提供增强输入

## 与相关工作对比

| 特性 | STORM | Co-STORM | IG-Finder |
|------|-------|----------|-----------|
| 目标 | 生成类维基文章 | 协作知识整理 | 识别创新缺口 |
| 基线建模 | ❌ | ❌ | ✅ |
| 创新检测 | ❌ | 有限 | ✅ (核心) |
| 偏离分析 | ❌ | ❌ | ✅ |
| 下游使用 | 直接消费 | 直接消费 | 增强输入 |

## 应用场景

1. **自动评审生成**: 提供增强型主题输入
2. **文献综述**: 快速识别研究缺口
3. **研究规划**: 发现新兴趋势
4. **创新评估**: 评价研究方向新颖性
5. **学术情报**: 追踪领域演化

## 文档资源

- **IG_FINDER_FRAMEWORK_ANALYSIS.md**: 完整技术分析 (23KB)
- **IG_FINDER_PAPER_ABSTRACT.md**: 学术论文摘要 (14KB)
- **IG_FINDER_DESIGN.md**: 设计文档
- **IG_FINDER_IMPLEMENTATION_SUMMARY.md**: 实现总结
- **IG_FINDER_使用指南.md**: 中文使用指南

## 快速开始

```bash
# 安装
pip install -r requirements.txt

# 运行 (零配置)
python examples/ig_finder_examples/quick_start_yunwu.py \
    --topic "your research topic"

# 输出目录
./ig_finder_output/
    ├── cognitive_baseline.json
    ├── phase2_results.json
    ├── innovation_gap_report.json
    └── innovation_gap_report.md
```

## 论文投稿建议

**适合会议/期刊**:
- SIGIR, WWW, ACL (信息检索、NLP)
- NeurIPS, ICML (机器学习应用)
- AAAI, IJCAI (AI应用)
- CHI (人机交互)
- JAIR, TACL (期刊)

**核心卖点**:
1. 首次形式化"滞后评审"问题
2. 免疫系统隐喻的创新应用
3. 多智能体协作框架
4. 可验证的创新识别
5. 完整的端到端系统

---

**Last Updated**: 2024-12-09
**Framework Version**: 0.1.0
**Status**: Complete and Documented
