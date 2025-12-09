#!/bin/bash
# Configuration for IG-Finder with Tavily and YunWu.ai proxy
# 
# Usage:
#   source examples/ig_finder_examples/config_yunwu.sh
#   python examples/ig_finder_examples/run_ig_finder_tavily.py --topic "your topic"

# Tavily API Key
export TAVILY_API_KEY="tvly-dev-lcV5zvU7Tusx4YefEyQHi0pRfnEna"

# OpenAI API Key (via YunWu.ai proxy)
export OPENAI_API_KEY="sk-QkPuzan6xUAa4q9Ae47OZUak6nz4Yq35dvXrg2KNHwXLM"

# OpenAI API Base (YunWu.ai proxy endpoint)
export OPENAI_API_BASE="https://yunwu.ai/v1"

echo "✅ Environment configured for IG-Finder:"
echo "   - Tavily Search Engine: Enabled"
echo "   - OpenAI Proxy: yunwu.ai"
echo "   - API Keys: Configured"
echo ""
echo "You can now run:"
echo '  python examples/ig_finder_examples/run_ig_finder_tavily.py --topic "your topic"'
