#!/bin/bash

# RL4RS Environment Activation Script
# This script activates the rl4rs conda environment and sets up the workspace

echo "🚀 Activating RL4RS Environment..."

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "❌ Error: conda not found. Please install Anaconda or Miniconda first."
    exit 1
fi

# Activate the rl4rs environment
echo "📦 Activating conda environment 'rl4rs'..."
conda activate rl4rs

# Check if activation was successful
if [[ "$CONDA_DEFAULT_ENV" != "rl4rs" ]]; then
    echo "❌ Error: Failed to activate rl4rs environment."
    echo "   Make sure the environment exists by running: conda env list"
    exit 1
fi

# Navigate to project directory
PROJECT_DIR="/Users/armandoordoricadelatorre/Documents/U of T/PhD/PhD Research/RL4RS_replication"
if [[ -d "$PROJECT_DIR" ]]; then
    cd "$PROJECT_DIR"
    echo "📁 Changed to project directory: $PROJECT_DIR"
else
    echo "⚠️  Warning: Project directory not found: $PROJECT_DIR"
fi

# Display environment info
echo ""
echo "✅ RL4RS Environment activated successfully!"
echo "🐍 Python version: $(python --version)"
echo "📦 Conda environment: $CONDA_DEFAULT_ENV"
echo "📁 Current directory: $(pwd)"
echo ""
echo "🔬 To test the environment, run: python test_environment.py"
echo "📓 To start Jupyter Lab, run: jupyter lab"
echo "📒 To start Jupyter Notebook, run: jupyter notebook"
echo "🔄 To deactivate when done, run: conda deactivate"
echo ""

# Keep the shell open with the environment activated
exec $SHELL
