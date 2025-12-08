# IG-Finder: Innovation Gap Finder Framework

## 概述

IG-Finder (Innovation Gap Finder) 是一个基于免疫系统"自我-非我识别"机制的科学知识建模框架。该框架通过构建领域认知基线并识别与之偏离的创新研究簇,显式发现可验证的创新性认知缺口,为下游自动综述系统提供高质量的创新引导。

## 核心设计理念

### 1. 免疫学隐喻

**自我-非我识别机制**:
- **认知自我 (Cognitive Self)**: 从已有综述中提取的领域共识和认知边界
- **创新非我 (Innovative Non-self)**: 偏离共识但内部逻辑自洽的新兴研究簇
- **差异感知推理 (Difference-aware Reasoning)**: 多视角专家代理在前沿文献与共识之间的对比分析

### 2. 两阶段工作流

#### 阶段一: 认知自我构建 (Cognitive Self Construction)
1. **综述检索**: 基于主题检索高质量的已有综述文献
2. **共识提取**: 从综述中结构化提取领域发展脉络、研究范式、主流方法论
3. **动态建模**: 将提取的共识填充到动态思维导图,建立认知基线

#### 阶段二: 创新非我识别 (Innovative Non-self Identification)
1. **前沿检索**: 检索最新的研究型论文(非综述)
2. **差异分析**: 多视角专家代理对比前沿文献与认知基线
3. **演化标注**: 在思维导图上标注知识演化状态(延续/偏离/创新)
4. **簇识别**: 识别内部逻辑自洽的创新研究簇
5. **缺口报告**: 生成面向创新性认知缺口的结构化报告

## 技术架构

### 核心组件设计

```
IG-Finder Framework
│
├── 1. CognitiveSelfConstructionModule (认知自我构建模块)
│   ├── ReviewRetriever (综述检索器)
│   ├── ConsensusExtractor (共识提取器)
│   └── CognitiveBaselineBuilder (认知基线构建器)
│
├── 2. InnovativeNonSelfIdentificationModule (创新非我识别模块)
│   ├── FrontierPaperRetriever (前沿论文检索器)
│   ├── DifferenceAwareAnalyzer (差异感知分析器)
│   ├── ExpertPerspectiveGenerator (专家视角生成器)
│   └── InnovationClusterIdentifier (创新簇识别器)
│
├── 3. DynamicMindMapManager (动态思维导图管理器)
│   ├── KnowledgeEvolutionTracker (知识演化追踪器)
│   ├── ConceptRelationshipGraph (概念关系图)
│   └── EvolutionStateAnnotator (演化状态标注器)
│
├── 4. InnovationGapReportGenerator (创新缺口报告生成器)
│   ├── GapSynthesizer (缺口综合器)
│   ├── EvidenceOrganizer (证据组织器)
│   └── ReportFormatter (报告格式化器)
│
└── 5. IGFinderRunner (主执行引擎)
    ├── Configuration Management
    ├── Pipeline Orchestration
    └── State Persistence
```

### 数据结构设计

#### 1. CognitiveBaseline (认知基线)
```python
@dataclass
class CognitiveBaseline:
    """表示从已有综述中提取的领域认知基线"""
    topic: str
    review_papers: List[ReviewPaper]  # 源综述列表
    consensus_map: KnowledgeBase  # 共识思维导图
    research_paradigms: List[ResearchParadigm]  # 研究范式
    mainstream_methods: List[Method]  # 主流方法
    knowledge_boundaries: Dict[str, Boundary]  # 知识边界
    temporal_coverage: TimeRange  # 时间覆盖范围
```

#### 2. EvolutionState (演化状态)
```python
class EvolutionState(Enum):
    """知识节点的演化状态"""
    CONSENSUS = "consensus"  # 共识:已有综述中的确立知识
    CONTINUATION = "continuation"  # 延续:继续深化共识内容
    DEVIATION = "deviation"  # 偏离:与共识不同但未形成体系
    INNOVATION = "innovation"  # 创新:偏离共识且内部自洽的新簇
    POTENTIAL_GAP = "potential_gap"  # 潜在缺口:需要进一步验证
```

#### 3. InnovationCluster (创新簇)
```python
@dataclass
class InnovationCluster:
    """表示一个创新研究簇"""
    cluster_id: str
    name: str
    core_papers: List[ResearchPaper]  # 核心论文
    deviation_from_consensus: DeviationAnalysis  # 与共识的偏离分析
    internal_coherence_score: float  # 内部逻辑一致性得分
    innovation_dimensions: List[str]  # 创新维度(方法/数据/范式等)
    supporting_evidence: List[Evidence]  # 支撑证据
    knowledge_path: List[str]  # 在思维导图中的路径
```

#### 4. InnovationGapReport (创新缺口报告)
```python
@dataclass
class InnovationGapReport:
    """最终输出的创新缺口报告"""
    topic: str
    cognitive_baseline_summary: str  # 认知基线摘要
    identified_clusters: List[InnovationCluster]  # 识别的创新簇
    gap_analysis: Dict[str, GapAnalysis]  # 按维度的缺口分析
    evolution_narrative: str  # 知识演化叙述
    mind_map_visualization: Dict  # 思维导图可视化数据
    recommendation_for_review: str  # 给综述系统的建议
```

### 模块详细设计

#### Module 1: CognitiveSelfConstructionModule

**功能**: 从已有综述中构建领域认知基线

**子组件**:

1. **ReviewRetriever**
   - 检索策略: 优先选择高引用、近期发表的综述
   - 过滤条件: 排除研究型论文,只保留综述/Survey类文献
   - 输出: 排序的综述列表

2. **ConsensusExtractor**
   - 提取内容:
     - 领域发展历史和关键里程碑
     - 主流研究范式和方法论
     - 公认的挑战和未解决问题
     - 研究子领域的分类体系
   - 使用LLM进行结构化信息抽取

3. **CognitiveBaselineBuilder**
   - 将提取的共识组织到动态思维导图
   - 标记所有节点为CONSENSUS状态
   - 记录每个共识节点的来源综述

#### Module 2: InnovativeNonSelfIdentificationModule

**功能**: 识别偏离认知基线的创新研究簇

**子组件**:

1. **FrontierPaperRetriever**
   - 时间过滤: 检索认知基线时间范围之后的论文
   - 类型过滤: 排除综述,只保留研究型论文
   - 相关性排序: 确保与主题相关

2. **DifferenceAwareAnalyzer**
   - 多视角专家代理设计:
     - **方法论专家**: 关注研究方法的创新
     - **数据范式专家**: 关注数据和实验设计
     - **理论框架专家**: 关注概念和理论创新
     - **应用领域专家**: 关注应用场景扩展
   - 对比分析流程:
     ```
     For each paper:
       For each expert perspective:
         1. 提取论文核心主张
         2. 匹配认知基线中的相关节点
         3. 进行差异性分析
         4. 评估偏离程度和创新潜力
     ```

3. **ExpertPerspectiveGenerator**
   - 基于主题动态生成相关的专家视角
   - 参考STORM的perspective-guided机制

4. **InnovationClusterIdentifier**
   - 聚类算法: 基于语义相似度和共同偏离模式
   - 一致性验证: 检查簇内论文的逻辑自洽性
   - 标注策略:
     - 单篇偏离 → DEVIATION
     - 多篇形成簇且逻辑自洽 → INNOVATION
     - 与共识方向一致 → CONTINUATION

#### Module 3: DynamicMindMapManager

**功能**: 管理动态演化的思维导图

**特性**:
- 继承Co-STORM的KnowledgeBase结构
- 扩展功能:
  - 演化状态标注
  - 时间戳追踪
  - 多源信息关联(综述 vs 研究论文)
  - 偏离度量化

**核心方法**:
```python
class DynamicMindMapManager:
    def update_with_consensus(self, consensus_data):
        """用共识数据初始化思维导图"""
        
    def annotate_evolution_state(self, node, state, evidence):
        """标注节点的演化状态"""
        
    def track_deviation(self, node, baseline_node, deviation_metrics):
        """追踪偏离信息"""
        
    def identify_innovation_paths(self):
        """识别标记为INNOVATION的知识路径"""
        
    def export_visualization(self):
        """导出可视化数据"""
```

#### Module 4: InnovationGapReportGenerator

**功能**: 生成结构化的创新缺口报告

**报告结构**:
```
# Innovation Gap Report: [Topic]

## Executive Summary
- 认知基线概述
- 识别的创新簇数量
- 主要创新方向

## Part I: Cognitive Baseline
### 1.1 Field Development History
### 1.2 Established Research Paradigms
### 1.3 Mainstream Methodologies
### 1.4 Known Challenges

## Part II: Innovation Clusters
For each cluster:
  ### Cluster Name
  - Core Papers
  - Deviation Analysis
  - Innovation Dimensions
  - Internal Coherence Evidence

## Part III: Gap Analysis by Dimension
- Methodological Gaps
- Data Paradigm Gaps
- Theoretical Framework Gaps
- Application Domain Gaps

## Part IV: Knowledge Evolution Narrative
- 从共识到创新的演化路径
- 关键转折点分析
- 未来研究方向建议

## Part V: Mind Map Visualization
- 交互式思维导图数据
- 演化状态分布统计

## Part VI: Recommendations for Review Generation
- 建议的综述组织结构
- 需要重点阐述的创新点
- 引用证据的优先级
```

### 工作流程

```
Input: Topic (e.g., "自动综述生成")

┌─────────────────────────────────────────┐
│ Phase 1: Cognitive Self Construction   │
└─────────────────────────────────────────┘
  ↓
1.1 Retrieve Review Papers
  - Search Query: "[Topic] survey OR review"
  - Filter: publication_type=review
  - Sort: by citations and recency
  ↓
1.2 Extract Consensus from Reviews
  - For each review:
    - Extract: paradigms, methods, timeline, challenges
    - Organize: into hierarchical structure
  ↓
1.3 Build Cognitive Baseline
  - Initialize dynamic mind map
  - Populate with consensus nodes (state=CONSENSUS)
  - Record source reviews for each node

┌─────────────────────────────────────────┐
│ Phase 2: Innovative Non-self Identify  │
└─────────────────────────────────────────┘
  ↓
2.1 Retrieve Frontier Papers
  - Search Query: "[Topic]"
  - Filter: publication_type=research_article
  - Filter: date > cognitive_baseline.temporal_coverage.end
  ↓
2.2 Generate Expert Perspectives
  - Based on topic and cognitive baseline
  - Create specialized agents:
    - Methodology Expert
    - Data Paradigm Expert
    - Theory Expert
    - Application Expert
  ↓
2.3 Multi-perspective Difference Analysis
  - For each paper:
    - For each expert:
      - Extract paper's core claims
      - Match with baseline nodes
      - Analyze differences
      - Assess innovation potential
    - Aggregate expert opinions
  ↓
2.4 Update Mind Map with Evolution States
  - Add new nodes for frontier concepts
  - Annotate states: CONTINUATION/DEVIATION/INNOVATION
  - Record deviation metrics
  ↓
2.5 Identify Innovation Clusters
  - Cluster papers by:
    - Semantic similarity
    - Common deviation patterns
  - Validate internal coherence
  - Mark coherent clusters as INNOVATION
  ↓
2.6 Generate Innovation Gap Report
  - Synthesize cognitive baseline summary
  - Describe each innovation cluster
  - Provide gap analysis by dimensions
  - Construct evolution narrative
  - Export mind map visualization
  
Output: InnovationGapReport (替代简单的topic description)
```

## 与STORM/Co-STORM的关系

### 借鉴的组件

1. **从STORM借鉴**:
   - 整体Pipeline架构 (STORMWikiRunner → IGFinderRunner)
   - 多视角专家机制 (perspective-guided question asking)
   - 信息检索和引用管理
   - 模块化设计理念

2. **从Co-STORM借鉴**:
   - 动态思维导图 (KnowledgeBase)
   - 知识节点的层级组织
   - 协作式信息整合
   - 实时状态更新机制

### 关键创新点

1. **两阶段认知模型**: 区分"已知共识"和"创新偏离"
2. **演化状态标注**: 显式追踪知识演化信号
3. **差异感知推理**: 专家代理在共识与前沿之间进行对比
4. **创新簇识别**: 不仅发现单点创新,还识别系统性创新模式
5. **输出重定位**: 生成面向创新缺口的报告而非综述文章

## 实现计划

### Phase 1: 核心数据结构
- [ ] 实现CognitiveBaseline
- [ ] 实现InnovationCluster
- [ ] 扩展KnowledgeNode支持EvolutionState

### Phase 2: 认知自我构建模块
- [ ] ReviewRetriever
- [ ] ConsensusExtractor
- [ ] CognitiveBaselineBuilder

### Phase 3: 创新非我识别模块
- [ ] FrontierPaperRetriever
- [ ] ExpertPerspectiveGenerator
- [ ] DifferenceAwareAnalyzer
- [ ] InnovationClusterIdentifier

### Phase 4: 思维导图管理
- [ ] DynamicMindMapManager
- [ ] EvolutionStateAnnotator

### Phase 5: 报告生成
- [ ] InnovationGapReportGenerator
- [ ] 可视化导出

### Phase 6: 主执行引擎
- [ ] IGFinderRunner
- [ ] IGFinderLMConfigs
- [ ] 配置和参数管理

### Phase 7: 示例和文档
- [ ] 示例脚本
- [ ] 使用文档
- [ ] 测试用例

## 使用示例

```python
from knowledge_storm.ig_finder import IGFinderRunner, IGFinderLMConfigs
from knowledge_storm.lm import LitellmModel
from knowledge_storm.rm import BingSearch

# 配置LLM
lm_configs = IGFinderLMConfigs()
lm_configs.init(lm_type="openai")

# 配置检索器
rm = BingSearch(api_key=os.getenv('BING_API_KEY'))

# 创建Runner
runner = IGFinderRunner(
    topic="自动综述生成",
    lm_configs=lm_configs,
    rm=rm,
    output_dir="./results"
)

# 执行两阶段流程
# Phase 1: 构建认知自我
cognitive_baseline = runner.run_cognitive_self_construction()

# Phase 2: 识别创新非我
innovation_clusters = runner.run_innovative_nonself_identification(
    cognitive_baseline
)

# 生成报告
gap_report = runner.generate_innovation_gap_report(
    cognitive_baseline,
    innovation_clusters
)

# 保存结果
runner.save_report(gap_report)
```

## 性能优化建议

1. **并行处理**: 多篇论文的分析可并行执行
2. **缓存机制**: 缓存已提取的共识和论文分析结果
3. **增量更新**: 支持基于已有基线的增量更新
4. **语义索引**: 使用向量数据库加速相似度检索

## 评估指标

1. **认知基线质量**:
   - 共识覆盖完整性
   - 知识组织合理性

2. **创新识别准确性**:
   - 创新簇的准确率和召回率
   - 人工评估的创新价值得分

3. **下游任务提升**:
   - 基于报告生成的综述创新性评分
   - 与直接生成综述的对比

## 总结

IG-Finder通过引入免疫学的"自我-非我识别"机制,解决了现有自动综述系统缺乏认知基线建模的问题。该框架不生成综述本身,而是为下游综述系统提供高质量的创新引导,使其能够跳出"滞后性综述"的陷阱,真正反映领域前沿动态。
