# IG-Finder Examples

This directory contains example scripts for running the Innovation Gap Finder (IG-Finder) framework.

## Overview

IG-Finder identifies innovation gaps in scientific research by:
1. **Phase 1**: Constructing a cognitive baseline from review papers (the "self")
2. **Phase 2**: Identifying innovation clusters from frontier research papers that deviate from consensus (the "non-self")
3. **Report Generation**: Creating a comprehensive innovation gap report

The output report can replace simple topic descriptions as input to downstream automatic review generation systems, enabling them to produce more innovative and valuable content.

## Installation

Ensure you have installed the `knowledge-storm` package:

```bash
cd /home/user/webapp
pip install -e .
```

## Setup API Keys

Create a `secrets.toml` file in the project root or set environment variables:

```bash
# OpenAI API (required for GPT models)
export OPENAI_API_KEY="your_openai_api_key"

# Search Engine API (choose one)
export BING_SEARCH_API_KEY="your_bing_api_key"  # for Bing
# OR
export YDC_API_KEY="your_you_api_key"  # for You.com
```

## Basic Usage

### Using GPT Models with Bing Search

```bash
python examples/ig_finder_examples/run_ig_finder_gpt.py \
    --topic "automatic literature review generation" \
    --output-dir ./output/auto_review \
    --retriever bing
```

### Customizing Parameters

```bash
python examples/ig_finder_examples/run_ig_finder_gpt.py \
    --topic "multi-agent reinforcement learning" \
    --output-dir ./output/marl \
    --retriever bing \
    --top-k-reviews 15 \
    --top-k-research 40 \
    --min-cluster-size 3 \
    --deviation-threshold 0.6
```

### Incremental Execution

If you want to run phases separately (useful for debugging or when API rate limits are hit):

```bash
# Run only Phase 1
python examples/ig_finder_examples/run_ig_finder_gpt.py \
    --topic "neural architecture search" \
    --output-dir ./output/nas \
    --skip-phase2

# Later, run Phase 2 using saved Phase 1 results
python examples/ig_finder_examples/run_ig_finder_gpt.py \
    --topic "neural architecture search" \
    --output-dir ./output/nas \
    --skip-phase1
```

## Command Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--topic` | str | required | Research topic to analyze |
| `--output-dir` | str | `./ig_finder_output` | Directory for saving results |
| `--retriever` | str | `bing` | Search engine (`bing` or `you`) |
| `--top-k-reviews` | int | 10 | Number of review papers to retrieve for baseline |
| `--top-k-research` | int | 30 | Number of research papers to analyze |
| `--min-cluster-size` | int | 2 | Minimum papers to form an innovation cluster |
| `--deviation-threshold` | float | 0.5 | Minimum deviation score (0-1) to consider |
| `--skip-phase1` | flag | false | Skip Phase 1 (load from saved results) |
| `--skip-phase2` | flag | false | Skip Phase 2 (load from saved results) |

## Output Files

After execution, the output directory will contain:

```
output/
├── cognitive_baseline.json          # Phase 1: Extracted consensus
├── phase2_results.json              # Phase 2: Identified clusters
├── innovation_gap_report.json       # Final report (JSON format)
└── innovation_gap_report.md         # Final report (Markdown format)
```

### Innovation Gap Report Structure

The generated report includes:

1. **Executive Summary**: Overview of findings
2. **Part I: Cognitive Baseline**: Established consensus from review papers
3. **Part II: Innovation Clusters**: Identified clusters with:
   - Core papers
   - Innovation dimensions
   - Deviation from consensus
   - Potential impact
4. **Part III: Gap Analysis by Dimension**: 
   - Methodological gaps
   - Data paradigm gaps
   - Theoretical gaps
   - Application domain gaps
5. **Part IV: Evolution Narrative**: Story of knowledge evolution
6. **Part V: Mind Map Visualization**: Evolution state distribution
7. **Part VI: Recommendations**: Guidance for review generation systems
8. **Appendix: Statistics**: Quantitative summary

## Programming API

You can also use IG-Finder programmatically:

```python
from knowledge_storm.ig_finder import (
    IGFinderRunner,
    IGFinderLMConfigs,
    IGFinderArguments,
)
from knowledge_storm.rm import BingSearch

# Setup
lm_configs = IGFinderLMConfigs()
lm_configs.init(lm_type="openai")

rm = BingSearch(bing_search_api_key="your_key", k=10)

args = IGFinderArguments(
    topic="automatic literature review generation",
    output_dir="./output",
    top_k_reviews=10,
    top_k_research_papers=30,
)

# Run
runner = IGFinderRunner(args, lm_configs, rm)
report = runner.run()

# Access results
print(f"Found {len(report.identified_clusters)} innovation clusters")
for cluster in report.identified_clusters:
    print(f"- {cluster.name}: {len(cluster.core_papers)} papers")
```

## Example Topics

Here are some interesting research topics to try:

### AI/ML Research
- "automatic literature review generation"
- "multi-agent reinforcement learning"
- "neural architecture search"
- "few-shot learning"
- "large language model reasoning"
- "diffusion models for image generation"

### Scientific Domains
- "CRISPR gene editing applications"
- "quantum computing algorithms"
- "exoplanet detection methods"
- "climate change mitigation strategies"

### Interdisciplinary
- "AI for drug discovery"
- "computational neuroscience models"
- "human-AI collaboration"
- "ethical AI frameworks"

## Understanding the Output

### Innovation Clusters

Each innovation cluster represents a group of papers that:
- **Deviate** from established consensus in specific dimensions
- **Maintain** internal logical coherence
- **Represent** potential new research directions

Key metrics:
- **Internal Coherence Score** (0-1): How well papers in the cluster support each other
- **Deviation Score** (0-1): How much the cluster deviates from baseline
- **Evidence Strength** (0-1): Confidence in the identified gap

### Evolution States

Nodes in the mind map are annotated with evolution states:
- **CONSENSUS**: Established knowledge from review papers
- **CONTINUATION**: New research continuing the consensus
- **DEVIATION**: Papers deviating but not forming coherent clusters
- **INNOVATION**: Clustered deviations with internal coherence
- **POTENTIAL_GAP**: Preliminary gaps requiring validation

## Tips for Better Results

1. **Topic Specificity**: Use specific topics rather than broad areas
   - Good: "transformer architectures for time series forecasting"
   - Too broad: "machine learning"

2. **Parameter Tuning**:
   - Increase `top-k-reviews` for more comprehensive baselines
   - Increase `top-k-research` to find more innovation signals
   - Adjust `deviation-threshold` based on your tolerance for novelty

3. **Quality Control**:
   - Review the cognitive baseline (check if captured well-known consensus)
   - Examine individual papers in clusters (verify they're truly innovative)
   - Read the evolution narrative to understand the field's progression

4. **Downstream Use**:
   - Feed the innovation gap report to review generation systems
   - Use identified clusters as seeds for literature search
   - Leverage gap analysis for research opportunity identification

## Troubleshooting

### No review papers found
- Try rephrasing your topic
- Add domain-specific keywords (e.g., "survey", "review")
- Check if your topic is too niche (may need broader search)

### No innovation clusters identified
- Lower `deviation-threshold`
- Lower `min-cluster-size` to 1 or 2
- Increase `top-k-research` to analyze more papers
- Your field may have very stable consensus (expected for mature fields)

### API Rate Limits
- Use incremental execution (`--skip-phase1` or `--skip-phase2`)
- Reduce `top-k-reviews` and `top-k-research`
- Add delays between API calls (modify source code if needed)

### Out of Memory
- Reduce the number of papers processed
- Process in smaller batches
- Use a machine with more RAM

## Integration with STORM

IG-Finder complements STORM by providing innovation-focused inputs:

```python
# 1. Generate innovation gap report with IG-Finder
ig_runner = IGFinderRunner(ig_args, lm_configs, rm)
gap_report = ig_runner.run()

# 2. Use gap report to guide STORM
from knowledge_storm import STORMWikiRunner, STORMWikiRunnerArguments

# Construct enhanced topic description from gap report
enhanced_topic = f"{topic}\n\nInnovation Focus:\n"
for cluster in gap_report.identified_clusters:
    enhanced_topic += f"- {cluster.name}: {cluster.cluster_summary}\n"

storm_args = STORMWikiRunnerArguments(
    output_dir="./storm_output"
)
storm_runner = STORMWikiRunner(storm_args, lm_configs, rm)
storm_runner.run(
    topic=enhanced_topic,
    do_research=True,
    do_generate_outline=True,
    do_generate_article=True,
)
```

## Citation

If you use IG-Finder in your research, please cite:

```bibtex
@software{igfinder2024,
  title={IG-Finder: Innovation Gap Finder for Scientific Knowledge Modeling},
  author={Your Name},
  year={2024},
  note={Built on the STORM framework by Shao et al.}
}
```

Also cite the original STORM papers that this framework builds upon:
- STORM: Shao et al., NAACL 2024
- Co-STORM: Jiang et al., EMNLP 2024

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check the main STORM repository for related discussions
- Review the design document: `IG_FINDER_DESIGN.md`

## License

This project inherits the license from the STORM project.
