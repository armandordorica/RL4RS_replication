# RL4RS Environment Setup Guide

This guide helps you set up a Python environment for the RL4RS (Reinforcement Learning for Recommender Systems) project on macOS.

## Environment Overview

We've created a conda environment called `rl4rs` with Python 3.8 and all necessary packages for running the RL4RS project.

## Environment Details

- **Python Version**: 3.8.20
- **Environment Type**: Conda
- **Environment Name**: rl4rs

## Installed Packages

### Core Scientific Computing
- NumPy 1.24.3
- Pandas 2.0.3
- SciPy 1.10.1
- Matplotlib 3.7.3
- Scikit-learn 1.3.2
- H5py 3.11.0

### Deep Learning Frameworks
- TensorFlow 2.13.0 (with TensorFlow-macOS for Apple Silicon)
- PyTorch 2.4.1
- Keras 2.13.1

### Reinforcement Learning
- Gym 0.26.2 (note: original project used 0.19.0, but 0.26.2 is compatible)

### Jupyter and Development
- Jupyter Lab 4.2.5
- Jupyter Notebook 7.2.2
- IPython 8.12.2

### Utility Packages
- tqdm 4.67.1
- requests 2.32.3
- cloudpickle 3.1.1

## Activation Instructions

To activate the environment and start working:

```bash
# Activate the conda environment
conda activate rl4rs

# Navigate to the project directory
cd "/Users/armandoordoricadelatorre/Documents/U of T/PhD/PhD Research/RL4RS_replication"

# Test the environment (optional)
python test_environment.py
```

## Running Jupyter

To start Jupyter Lab or Notebook:

```bash
# Activate environment first
conda activate rl4rs

# Start Jupyter Lab
jupyter lab

# OR start Jupyter Notebook
jupyter notebook
```

## Environment Testing

We've included a test script (`test_environment.py`) that verifies all essential packages are working correctly. Run it with:

```bash
conda activate rl4rs
python test_environment.py
```

## Package Compatibility Notes

### Version Differences from Original
The original `environment.yml` was designed for Linux systems and used older package versions. Our setup includes:

1. **Gym**: Upgraded from 0.19.0 to 0.26.2 (the older version had build issues on macOS ARM64)
2. **TensorFlow**: Upgraded from 1.15.0 to 2.13.0 (TF 1.15 is not supported on Apple Silicon)
3. **Python**: Using 3.8 instead of 3.6 (3.6 is not available for macOS ARM64)

### Missing Packages from Original
Some packages from the original environment couldn't be installed due to compatibility issues:
- Ray: Version 1.5.1 has compatibility issues with Python 3.8 on ARM64
- d3rlpy: Version 0.91 may need to be installed separately if needed
- Some Keras extensions: May need manual installation if required

## Installing Additional Packages

If you need to install additional packages for the RL4RS project:

```bash
# Activate environment
conda activate rl4rs

# Install via conda (preferred)
conda install package_name

# Install via pip if not available in conda
pip install package_name
```

## Common Issues and Solutions

### Import Errors
If you get import errors when running RL4RS scripts:
1. Make sure the conda environment is activated: `conda activate rl4rs`
2. Check if additional packages need to be installed
3. Some scripts may need minor modifications for newer package versions

### Gym Deprecation Warning
You may see warnings about Gym being deprecated in favor of Gymnasium. For most RL4RS functionality, the current Gym version should work fine. If needed, you can install Gymnasium:

```bash
conda activate rl4rs
pip install gymnasium[classic-control]
```

### GPU Support
- PyTorch: Should work with Apple Silicon GPU automatically
- TensorFlow: Uses TensorFlow-macOS which has Apple Silicon optimization

## Deactivating the Environment

When you're done working:

```bash
conda deactivate
```

## Environment Backup

To export the current environment for sharing or backup:

```bash
conda activate rl4rs
conda env export > environment_macos_backup.yml
```

## Troubleshooting

If you encounter issues:

1. **Environment not found**: Make sure conda is properly installed and the environment was created successfully
2. **Package conflicts**: Try creating a fresh environment and installing packages one by one
3. **Performance issues**: Ensure you're using the native ARM64 version of conda/Python

For project-specific issues, refer to the original RL4RS documentation and adapt for the newer package versions as needed.
