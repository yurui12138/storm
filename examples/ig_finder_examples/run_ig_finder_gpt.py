"""
Example script for running IG-Finder with GPT models.

This script demonstrates how to use IG-Finder to identify innovation gaps
in a research domain by:
1. Constructing a cognitive baseline from review papers
2. Identifying innovative research clusters that deviate from consensus
3. Generating a comprehensive innovation gap report

Usage:
    python examples/ig_finder_examples/run_ig_finder_gpt.py --topic "automatic literature review generation"
"""

import os
import sys
import argparse
import logging

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from knowledge_storm.ig_finder import (
    IGFinderRunner,
    IGFinderLMConfigs,
    IGFinderArguments,
)
from knowledge_storm.rm import BingSearch, YouRM
from knowledge_storm.lm import LitellmModel

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description='Run IG-Finder with GPT models')
    parser.add_argument(
        '--topic',
        type=str,
        required=True,
        help='Research topic to analyze (e.g., "automatic literature review generation")'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./ig_finder_output',
        help='Output directory for results'
    )
    parser.add_argument(
        '--retriever',
        type=str,
        default='bing',
        choices=['bing', 'you'],
        help='Search engine to use (bing or you)'
    )
    parser.add_argument(
        '--top-k-reviews',
        type=int,
        default=10,
        help='Number of review papers to retrieve'
    )
    parser.add_argument(
        '--top-k-research',
        type=int,
        default=30,
        help='Number of research papers to retrieve'
    )
    parser.add_argument(
        '--min-cluster-size',
        type=int,
        default=2,
        help='Minimum number of papers to form a cluster'
    )
    parser.add_argument(
        '--deviation-threshold',
        type=float,
        default=0.5,
        help='Minimum deviation score (0-1) to consider'
    )
    parser.add_argument(
        '--skip-phase1',
        action='store_true',
        help='Skip Phase 1 (load from saved results)'
    )
    parser.add_argument(
        '--skip-phase2',
        action='store_true',
        help='Skip Phase 2 (load from saved results)'
    )
    
    args = parser.parse_args()
    
    # Check for API keys
    if not os.getenv('OPENAI_API_KEY'):
        logger.error("OPENAI_API_KEY environment variable not set")
        sys.exit(1)
    
    if args.retriever == 'bing' and not os.getenv('BING_SEARCH_API_KEY'):
        logger.error("BING_SEARCH_API_KEY environment variable not set")
        sys.exit(1)
    elif args.retriever == 'you' and not os.getenv('YDC_API_KEY'):
        logger.error("YDC_API_KEY environment variable not set")
        sys.exit(1)
    
    # Setup LM configs
    logger.info("Initializing language model configurations...")
    lm_configs = IGFinderLMConfigs()
    lm_configs.init(lm_type="openai", temperature=1.0, top_p=0.9)
    
    # You can also customize individual LMs:
    # openai_kwargs = {
    #     'api_key': os.getenv("OPENAI_API_KEY"),
    #     'temperature': 1.0,
    #     'top_p': 0.9,
    # }
    # custom_lm = LitellmModel(model='gpt-4o', max_tokens=3000, **openai_kwargs)
    # lm_configs.set_consensus_extraction_lm(custom_lm)
    
    # Setup retriever
    logger.info(f"Initializing retriever ({args.retriever})...")
    if args.retriever == 'bing':
        rm = BingSearch(
            bing_search_api_key=os.getenv('BING_SEARCH_API_KEY'),
            k=10
        )
    else:  # you
        rm = YouRM(
            ydc_api_key=os.getenv('YDC_API_KEY'),
            k=10
        )
    
    # Setup arguments
    ig_args = IGFinderArguments(
        topic=args.topic,
        output_dir=args.output_dir,
        top_k_reviews=args.top_k_reviews,
        top_k_research_papers=args.top_k_research,
        min_cluster_size=args.min_cluster_size,
        deviation_threshold=args.deviation_threshold,
        save_intermediate_results=True,
    )
    
    # Create runner
    logger.info("Creating IG-Finder runner...")
    runner = IGFinderRunner(
        args=ig_args,
        lm_configs=lm_configs,
        rm=rm,
    )
    
    # Run pipeline
    logger.info(f"\n{'='*80}")
    logger.info(f"Starting IG-Finder for topic: {args.topic}")
    logger.info(f"{'='*80}\n")
    
    try:
        report = runner.run(
            do_phase1=not args.skip_phase1,
            do_phase2=not args.skip_phase2,
            do_generate_report=True,
        )
        
        # Print summary
        runner.summary()
        
        # Print key results
        print("\n" + "="*80)
        print("KEY RESULTS")
        print("="*80)
        print(f"\nIdentified {len(report.identified_clusters)} innovation clusters:")
        for i, cluster in enumerate(report.identified_clusters, 1):
            print(f"\n{i}. {cluster.name}")
            print(f"   - Papers: {len(cluster.core_papers)}")
            print(f"   - Dimensions: {', '.join(cluster.innovation_dimensions)}")
            print(f"   - Coherence: {cluster.internal_coherence_score:.2f}")
            print(f"   - Summary: {cluster.cluster_summary[:200]}...")
        
        print("\n" + "="*80)
        print("INNOVATION GAP ANALYSIS")
        print("="*80)
        for dimension, gap in report.gap_analysis_by_dimension.items():
            print(f"\n{dimension}:")
            print(f"   - Evidence Strength: {gap.evidence_strength:.2f}")
            print(f"   - {gap.gap_description[:200]}...")
        
        print("\n" + "="*80)
        print(f"Full report saved to: {args.output_dir}/innovation_gap_report.md")
        print("="*80 + "\n")
        
        logger.info("IG-Finder execution completed successfully!")
        
    except Exception as e:
        logger.error(f"Error during execution: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
