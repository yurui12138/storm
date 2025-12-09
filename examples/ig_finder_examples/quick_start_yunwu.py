"""
Quick start script for IG-Finder with pre-configured YunWu.ai proxy and Tavily search.

This script has your API keys pre-configured. Just run:
    python examples/ig_finder_examples/quick_start_yunwu.py

Or specify a custom topic:
    python examples/ig_finder_examples/quick_start_yunwu.py --topic "your custom topic"
"""

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import argparse
import logging
from knowledge_storm.ig_finder import (
    IGFinderRunner,
    IGFinderLMConfigs,
    IGFinderArguments,
)
from knowledge_storm.rm import TavilySearchRM
from knowledge_storm.lm import LitellmModel

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# PRE-CONFIGURED API KEYS
# ============================================================================
TAVILY_API_KEY = "tvly-dev-lcV5zvU7Tusx4YefEyQHi0pRfnEna"
OPENAI_API_KEY = "sk-QkPuzan6xUAa4q9Ae47OZUak6nz4Yq35dvXrg2KNHwXLM"
OPENAI_API_BASE = "https://yunwu.ai/v1"
# ============================================================================


def main():
    parser = argparse.ArgumentParser(description='Quick start IG-Finder with YunWu.ai')
    parser.add_argument(
        '--topic',
        type=str,
        default='automatic literature review generation',
        help='Research topic (default: "automatic literature review generation")'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./ig_finder_output',
        help='Output directory'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='gpt-4o',
        help='Model name (default: gpt-4o)'
    )
    parser.add_argument(
        '--top-k-reviews',
        type=int,
        default=10,
        help='Number of review papers'
    )
    parser.add_argument(
        '--top-k-research',
        type=int,
        default=30,
        help='Number of research papers'
    )
    
    args = parser.parse_args()
    
    print("\n" + "="*80)
    print("🚀 IG-Finder Quick Start - YunWu.ai Edition")
    print("="*80)
    print(f"📖 Topic: {args.topic}")
    print(f"🤖 Model: {args.model}")
    print(f"🔍 Search: Tavily")
    print(f"🌐 API: yunwu.ai")
    print(f"📂 Output: {args.output_dir}")
    print("="*80 + "\n")
    
    logger.info("Initializing IG-Finder...")
    
    # Setup language models
    lm_configs = IGFinderLMConfigs()
    
    openai_kwargs = {
        'api_key': OPENAI_API_KEY,
        'api_base': OPENAI_API_BASE,
        'temperature': 1.0,
        'top_p': 0.9,
    }
    
    # Create models for different tasks
    consensus_lm = LitellmModel(model=args.model, max_tokens=3000, **openai_kwargs)
    deviation_lm = LitellmModel(model=args.model, max_tokens=2000, **openai_kwargs)
    cluster_lm = LitellmModel(model=args.model, max_tokens=1500, **openai_kwargs)
    report_lm = LitellmModel(model=args.model, max_tokens=4000, **openai_kwargs)
    
    lm_configs.set_consensus_extraction_lm(consensus_lm)
    lm_configs.set_deviation_analysis_lm(deviation_lm)
    lm_configs.set_cluster_validation_lm(cluster_lm)
    lm_configs.set_report_generation_lm(report_lm)
    
    logger.info("✓ Language models configured")
    
    # Setup Tavily search
    rm = TavilySearchRM(
        tavily_search_api_key=TAVILY_API_KEY,
        k=10,
        include_raw_content=False,
    )
    
    logger.info("✓ Tavily search configured")
    
    # Setup arguments
    ig_args = IGFinderArguments(
        topic=args.topic,
        output_dir=args.output_dir,
        top_k_reviews=args.top_k_reviews,
        top_k_research_papers=args.top_k_research,
        min_cluster_size=2,
        deviation_threshold=0.5,
        save_intermediate_results=True,
    )
    
    # Create and run
    runner = IGFinderRunner(args=ig_args, lm_configs=lm_configs, rm=rm)
    
    logger.info("✓ IG-Finder initialized")
    logger.info("\n" + "="*80)
    logger.info("Starting analysis... This may take several minutes.")
    logger.info("="*80 + "\n")
    
    try:
        report = runner.run(
            do_phase1=True,
            do_phase2=True,
            do_generate_report=True,
        )
        
        # Display results
        runner.summary()
        
        print("\n" + "="*80)
        print("✨ KEY FINDINGS")
        print("="*80)
        
        if report.identified_clusters:
            print(f"\n🎯 Identified {len(report.identified_clusters)} innovation clusters:\n")
            for i, cluster in enumerate(report.identified_clusters, 1):
                print(f"{i}. {cluster.name}")
                print(f"   📄 Papers: {len(cluster.core_papers)}")
                print(f"   🔬 Dimensions: {', '.join(cluster.innovation_dimensions[:3])}")
                print(f"   ⭐ Coherence: {cluster.internal_coherence_score:.2f}")
                if cluster.cluster_summary:
                    summary = cluster.cluster_summary[:150] + "..." if len(cluster.cluster_summary) > 150 else cluster.cluster_summary
                    print(f"   💡 {summary}")
                print()
        else:
            print("\nNo innovation clusters identified.")
            print("Try adjusting --deviation-threshold or --min-cluster-size")
        
        if report.gap_analysis_by_dimension:
            print("\n" + "="*80)
            print("🔍 GAP ANALYSIS BY DIMENSION")
            print("="*80 + "\n")
            for dimension, gap in report.gap_analysis_by_dimension.items():
                print(f"📊 {dimension}")
                print(f"   Evidence: {gap.evidence_strength:.2f}")
                desc = gap.gap_description[:120] + "..." if len(gap.gap_description) > 120 else gap.gap_description
                print(f"   {desc}")
                print()
        
        print("="*80)
        print(f"📁 Full report: {args.output_dir}/innovation_gap_report.md")
        print(f"📊 JSON data: {args.output_dir}/innovation_gap_report.json")
        print("="*80 + "\n")
        
        print("✅ IG-Finder completed successfully!")
        print("\n💡 Next steps:")
        print("   1. Review the generated report")
        print("   2. Explore identified innovation clusters")
        print("   3. Use findings to guide your research\n")
        
    except Exception as e:
        logger.error(f"\n❌ Error: {e}", exc_info=True)
        print("\n💡 Troubleshooting tips:")
        print("   - Check your internet connection")
        print("   - Verify API keys are valid")
        print("   - Try with a different topic")
        print("   - Reduce --top-k-reviews and --top-k-research")
        sys.exit(1)


if __name__ == "__main__":
    main()
