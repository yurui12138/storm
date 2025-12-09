# IG-Finder: Innovation Gap Finder

**Identifying Verifiable Innovation Gaps in Scientific Research**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 🌟 Overview

IG-Finder (Innovation Gap Finder) is an advanced AI framework designed to identify **verifiable innovation gaps** in scientific research by modeling cognitive baselines and detecting frontier research that deviates from established consensus. 

### The Problem
Existing automatic review generation systems suffer from **"lagging reviews"** - they fail to identify true innovations because they lack proper domain cognitive baseline modeling.

### The Solution
IG-Finder adapts the **immune system's self-nonself recognition mechanism** to scientific knowledge modeling:
- **"Cognitive Self"**: Consensus knowledge extracted from existing review papers
- **"Innovative Non-self"**: Emerging research clusters that logically deviate from the consensus

### Key Innovation
Instead of generating reviews directly, IG-Finder produces a **comprehensive innovation gap report** that can serve as enhanced input for downstream automatic review systems, dramatically improving their ability to recognize and articulate true innovation.

## 🏗️ Architecture

IG-Finder operates in two phases:

### Phase 1: Cognitive Self Construction
Build the domain's cognitive baseline by:
- Retrieving existing review papers
- Extracting consensus claims and domain development
- Structuring knowledge into a dynamic mind map

### Phase 2: Innovative Non-self Identification
Identify innovation gaps by:
- Retrieving frontier research papers
- Performing difference-aware analysis against the cognitive baseline
- Identifying emerging research clusters
- Marking evolution states on the mind map
- Generating comprehensive innovation gap reports

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yurui12138/storm.git
cd storm

# Install dependencies
pip install -r requirements.txt

# Or install as a package
pip install -e .
```

### Configure API Keys

Create a configuration file or set environment variables:

```bash
# For Tavily search (Recommended)
export TAVILY_API_KEY="your_tavily_api_key"

# For Yunwu AI (OpenAI-compatible proxy)
export OPENAI_API_KEY="your_api_key"
export OPENAI_API_BASE="https://yunwu.ai/v1/"

# Alternative: Bing or You.com search
export BING_SEARCH_API_KEY="your_bing_key"
# or
export YDC_API_KEY="your_you_key"
```

### Run IG-Finder

**Option 1: Quick Start (Recommended for testing)**

```bash
python examples/ig_finder_examples/quick_start_yunwu.py \
    --topic "transformer models in natural language processing"
```

**Option 2: Full Configuration**

```bash
python examples/ig_finder_examples/run_ig_finder_tavily.py \
    --topic "your research topic" \
    --output-dir ./output \
    --top-k-reviews 20 \
    --top-k-research 30 \
    --min-cluster-size 3
```

## 📊 Output

IG-Finder generates comprehensive outputs:

1. **Cognitive Baseline** (`cognitive_baseline.json`)
   - Domain consensus knowledge
   - Key concepts and relationships
   - Research paradigms

2. **Innovation Analysis** (`phase2_results.json`)
   - Difference perception records
   - Deviation analysis
   - Cluster identification

3. **Innovation Gap Report** (`innovation_gap_report.md`)
   - Executive summary
   - Identified innovation clusters
   - Detailed analysis with evidence
   - Recommendations for downstream systems

4. **Dynamic Mind Map**
   - Hierarchical knowledge structure
   - Evolution state tracking
   - Innovation markers

## 🎯 Use Cases

- **Automatic Review Generation**: Provide enhanced input to overcome "lagging review" problems
- **Literature Survey**: Quickly identify research gaps in a domain
- **Research Planning**: Discover emerging trends and unexplored areas
- **Innovation Assessment**: Evaluate novelty of research directions
- **Academic Intelligence**: Track domain evolution and paradigm shifts

## 🔧 Configuration

### Search Engines
- **Tavily** (Recommended): Fast, academic-focused, stable API
- **Bing Search**: Web-based search with academic sources
- **You.com**: Alternative web search engine

### Language Models
- OpenAI GPT-4/GPT-3.5
- Azure OpenAI
- Compatible OpenAI proxies (e.g., Yunwu AI)
- Other OpenAI-compatible endpoints

### Key Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--topic` | Research topic to analyze | Required |
| `--output-dir` | Output directory | `./ig_finder_output` |
| `--retriever` | Search engine: `tavily`, `bing`, `you` | `tavily` |
| `--top-k-reviews` | Number of review papers to retrieve | 15 |
| `--top-k-research` | Number of research papers to retrieve | 25 |
| `--min-cluster-size` | Minimum papers per innovation cluster | 3 |
| `--deviation-threshold` | Innovation detection threshold | 0.7 |

## 📚 Documentation

- **[Design Document](IG_FINDER_DESIGN.md)**: Detailed framework design
- **[Implementation Summary](IG_FINDER_IMPLEMENTATION_SUMMARY.md)**: Technical implementation
- **[User Guide (中文)](IG_FINDER_使用指南.md)**: Chinese user guide
- **[Quick Start Guide (中文)](examples/ig_finder_examples/快速开始_云雾AI.md)**: Yunwu AI quick start
- **[Yunwu Optimization](YUNWU_OPTIMIZATION_README.md)**: Tavily + Yunwu AI optimization guide
- **[Scripts Comparison](examples/ig_finder_examples/SCRIPTS_COMPARISON.md)**: Comparison of example scripts
- **[Examples README](examples/ig_finder_examples/README.md)**: Detailed examples documentation

## 🛠️ Advanced Usage

### Incremental Execution

Run phases separately for debugging or iterative refinement:

```bash
# Phase 1 only: Build cognitive baseline
python examples/ig_finder_examples/run_ig_finder_tavily.py \
    --topic "your topic" \
    --skip-phase2

# Phase 2 only: Identify innovations (requires Phase 1 output)
python examples/ig_finder_examples/run_ig_finder_tavily.py \
    --topic "your topic" \
    --skip-phase1
```

### Python API

```python
from knowledge_storm.ig_finder.engine import IGFinderRunner
from knowledge_storm.ig_finder.dataclass import IGFinderRunnerArguments
from knowledge_storm.lm import LitellmModel
from knowledge_storm.rm import TavilySearchRM

# Configure language models
lm_configs = IGFinderLMConfigs()
openai_kwargs = {
    'api_key': 'your_api_key',
    'api_base': 'https://yunwu.ai/v1/',
    'temperature': 1.0,
}
lm = LitellmModel(model='gpt-4o', max_tokens=3000, **openai_kwargs)
lm_configs.set_all_models(lm)

# Configure retrieval
rm = TavilySearchRM(tavily_api_key='your_tavily_key', k=15)

# Create runner
args = IGFinderRunnerArguments(
    topic="your research topic",
    output_dir="./output",
)
runner = IGFinderRunner(args, lm_configs, rm)

# Execute
runner.run()
```

## 🤝 Contributing

We welcome contributions! Please see our contribution guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

IG-Finder builds upon concepts from the STORM project:
- **STORM Paper**: [Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](https://arxiv.org/abs/2402.14207)
- **Co-STORM Paper**: [Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations](https://arxiv.org/abs/2408.15232)

Special thanks to the STORM team at Stanford OVAL for their foundational work on knowledge curation systems.

## 📧 Contact

For questions, suggestions, or collaborations:
- **Project Repository**: https://github.com/yurui12138/storm
- **Issues**: https://github.com/yurui12138/storm/issues

## 📈 Citation

If you use IG-Finder in your research, please cite:

```bibtex
@software{ig_finder2024,
  title = {IG-Finder: Innovation Gap Identification Framework},
  author = {Your Name},
  year = {2024},
  url = {https://github.com/yurui12138/storm}
}
```

---

**Built with ❤️ to advance scientific knowledge discovery**
