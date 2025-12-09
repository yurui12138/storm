# IG-Finder Project Structure

## Directory Organization

```
ig-finder/
├── knowledge_storm/              # Core framework package
│   ├── __init__.py              # Package initialization
│   ├── dataclass.py             # Base data classes
│   ├── interface.py             # Module interfaces
│   ├── lm.py                    # Language model components
│   ├── rm.py                    # Retrieval module components
│   ├── encoder.py               # Text encoding utilities
│   ├── logging_wrapper.py       # Logging utilities
│   ├── utils.py                 # General utilities
│   └── ig_finder/               # IG-Finder implementation
│       ├── __init__.py
│       ├── dataclass.py         # IG-Finder specific data classes
│       ├── engine.py            # Main IGFinderRunner engine
│       └── modules/             # Core modules
│           ├── __init__.py
│           ├── cognitive_self_construction.py
│           ├── innovative_nonself_identification.py
│           ├── mind_map_manager.py
│           └── report_generation.py
│
├── examples/                    # Example scripts
│   └── ig_finder_examples/
│       ├── README.md
│       ├── SCRIPTS_COMPARISON.md
│       ├── quick_start_yunwu.py
│       ├── run_ig_finder_tavily.py
│       ├── run_ig_finder_gpt.py
│       ├── config_yunwu.sh
│       └── 快速开始_云雾AI.md
│
├── IG_FINDER_DESIGN.md          # Framework design document
├── IG_FINDER_IMPLEMENTATION_SUMMARY.md
├── IG_FINDER_使用指南.md
├── YUNWU_OPTIMIZATION_README.md
├── PROJECT_DELIVERY.md
├── CLEANUP_PLAN.md
├── PROJECT_STRUCTURE.md         # This file
├── README.md                    # Main project README
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── setup.py                     # Package installation script
├── MANIFEST.in                  # Package manifest
└── .gitignore                   # Git ignore rules

```

## Module Overview

### Core Modules

#### 1. Cognitive Self Construction
**File**: `knowledge_storm/ig_finder/modules/cognitive_self_construction.py`

Components:
- `ReviewRetriever`: Retrieves existing review papers
- `ConsensusExtractor`: Extracts consensus claims from reviews
- `CognitiveBaselineBuilder`: Builds the cognitive baseline model

Outputs:
- `cognitive_baseline.json`: Structured domain consensus knowledge

#### 2. Innovative Non-self Identification
**File**: `knowledge_storm/ig_finder/modules/innovative_nonself_identification.py`

Components:
- `FrontierPaperRetriever`: Retrieves recent research papers
- `ExpertPerspectiveGenerator`: Generates expert analysis perspectives
- `DifferenceAwareAnalyzer`: Analyzes deviations from baseline
- `InnovationClusterIdentifier`: Groups innovations into clusters

Outputs:
- `phase2_results.json`: Detailed analysis and cluster data

#### 3. Dynamic Mind Map Manager
**File**: `knowledge_storm/ig_finder/modules/mind_map_manager.py`

Components:
- `KnowledgeNode`: Represents concepts in the knowledge tree
- `MindMapManager`: Manages the dynamic mind map structure

Features:
- Hierarchical knowledge organization
- Evolution state tracking
- Innovation markers

#### 4. Report Generation
**File**: `knowledge_storm/ig_finder/modules/report_generation.py`

Components:
- `ReportGenerator`: Generates comprehensive innovation gap reports

Outputs:
- `innovation_gap_report.md`: Human-readable report
- `innovation_gap_report.json`: Machine-readable report

### Supporting Infrastructure

#### Language Model Interface (`lm.py`)
- Abstract LM interface
- LitellmModel implementation
- Support for OpenAI, Azure, and proxies

#### Retrieval Module (`rm.py`)
- TavilySearchRM: Tavily search integration
- BingSearch: Bing search integration
- YouRM: You.com search integration
- VectorRM: Vector database retrieval

#### Data Classes (`dataclass.py`)
- Base data structures
- Information storage models
- Configuration objects

## Key Files

### Configuration Files

1. **requirements.txt**: Python package dependencies
   - Core: dspy, litellm, tavily-python
   - ML: sentence-transformers
   - Utils: requests, toml

2. **setup.py**: Package installation configuration
   - Package name: `ig-finder`
   - Version: 0.1.0
   - Entry points for CLI

3. **MANIFEST.in**: Package distribution manifest

### Documentation Files

1. **IG_FINDER_DESIGN.md**: Comprehensive framework design
2. **IG_FINDER_IMPLEMENTATION_SUMMARY.md**: Implementation details
3. **IG_FINDER_使用指南.md**: Chinese user guide
4. **YUNWU_OPTIMIZATION_README.md**: Tavily + Yunwu AI guide
5. **PROJECT_DELIVERY.md**: Project delivery summary
6. **examples/ig_finder_examples/README.md**: Example usage guide
7. **examples/ig_finder_examples/SCRIPTS_COMPARISON.md**: Script comparison

## Example Scripts

### 1. quick_start_yunwu.py
**Purpose**: Zero-configuration quick start
**Features**:
- Pre-configured Tavily API key
- Pre-configured Yunwu AI endpoint
- Minimal command-line arguments
**Usage**: `python quick_start_yunwu.py --topic "your topic"`

### 2. run_ig_finder_tavily.py
**Purpose**: Full-featured production script
**Features**:
- Tavily search integration
- Comprehensive configuration options
- Environment variable support
**Usage**: Full parameter control

### 3. run_ig_finder_gpt.py
**Purpose**: Standard OpenAI + Bing/You.com
**Features**:
- Original configuration method
- Bing or You.com search
- Fallback option
**Usage**: For existing API users

### 4. config_yunwu.sh
**Purpose**: Environment variable setup
**Features**:
- Bash script for quick configuration
- Sets Tavily and Yunwu AI credentials
**Usage**: `source config_yunwu.sh`

## Data Flow

```
User Input (Topic)
    ↓
Phase 1: Cognitive Self Construction
    ↓
  ReviewRetriever → ConsensusExtractor → CognitiveBaselineBuilder
    ↓
cognitive_baseline.json + mind_map.json
    ↓
Phase 2: Innovative Non-self Identification
    ↓
  FrontierPaperRetriever → ExpertPerspectiveGenerator
    ↓
  DifferenceAwareAnalyzer → InnovationClusterIdentifier
    ↓
phase2_results.json + updated mind_map.json
    ↓
Report Generation
    ↓
innovation_gap_report.md + innovation_gap_report.json
```

## Output Files

### Standard Output Directory Structure

```
ig_finder_output/
├── cognitive_baseline.json       # Phase 1 output
├── mind_map.json                 # Dynamic knowledge map
├── phase2_results.json           # Phase 2 analysis
├── innovation_gap_report.json    # Structured report
└── innovation_gap_report.md      # Formatted report
```

## Dependencies

### Core Dependencies
- `dspy-ai`: LLM pipeline framework
- `litellm`: Multi-provider LLM interface
- `tavily-python`: Tavily search client
- `sentence-transformers`: Text embedding

### Optional Dependencies
- `qdrant-client`: Vector database
- `faiss-cpu`: Vector similarity search
- `streamlit`: Web UI (future feature)

## Version History

- **v0.1.0** (2024-12): Initial release
  - Two-phase IG-Finder framework
  - Tavily + Yunwu AI optimization
  - Comprehensive documentation
  - Example scripts

## Future Roadmap

1. **CLI Tool**: Complete command-line interface
2. **Web UI**: Interactive web-based interface
3. **Incremental Updates**: Support for continuous monitoring
4. **Multi-domain**: Cross-domain innovation detection
5. **Visualization**: Interactive mind map visualization
6. **Export Formats**: PDF, LaTeX, Word report generation

---

Last Updated: 2024-12-09
