# Using Jupyter with RL4RS Environment

## Quick Start

Your `rl4rs` conda environment is now set up as a Jupyter kernel! 🎉

### Option 1: Using VS Code (Recommended)

1. **Open your notebook** (like `EDA.ipynb`)
2. **Click on the kernel selector** in the top-right corner of the notebook
3. **Select "Python (rl4rs)"** from the list of available kernels
4. You're ready to go!

### Option 2: Using Jupyter Lab/Notebook

1. **Activate the environment and start Jupyter**:
   ```bash
   conda activate rl4rs
   jupyter lab
   # or
   jupyter notebook
   ```

2. **When creating a new notebook or opening an existing one**:
   - Click on the kernel name in the top-right
   - Select "Python (rl4rs)" from the dropdown

3. **Or create a new notebook with the kernel**:
   - File → New → Notebook
   - Select "Python (rl4rs)" as the kernel

## Verify Installation

Run this in a notebook cell to verify you're using the correct environment:

```python
import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

# Check if key packages are available
try:
    import tensorflow as tf
    print(f"✓ TensorFlow {tf.__version__}")
except ImportError:
    print("✗ TensorFlow not found")

try:
    import torch
    print(f"✓ PyTorch {torch.__version__}")
except ImportError:
    print("✗ PyTorch not found")

try:
    import gym
    print(f"✓ Gym {gym.__version__}")
except ImportError:
    print("✗ Gym not found")
```

## Available Kernels

You can see all available Jupyter kernels by running:
```bash
jupyter kernelspec list
```

Your installed kernels include:
- **rl4rs** - Your RL4RS environment (Python 3.8)
- python3 - Default Python kernel
- (other environments you may have)

## Troubleshooting

### Kernel not showing up in VS Code
1. Reload VS Code window: `Cmd+Shift+P` → "Reload Window"
2. Make sure the Jupyter extension is installed
3. Try restarting VS Code

### Kernel not showing up in Jupyter Lab
1. Make sure you activated the environment before starting Jupyter Lab
2. Restart Jupyter Lab
3. Run: `jupyter kernelspec list` to verify the kernel is installed

### Wrong packages imported
If you're getting import errors:
1. Verify you've selected the "Python (rl4rs)" kernel
2. Restart the kernel: Kernel → Restart Kernel
3. Check the Python path in a cell: `import sys; print(sys.executable)`

### Reinstall the kernel
If something goes wrong, you can reinstall:
```bash
conda activate rl4rs
python -m ipykernel install --user --name=rl4rs --display-name="Python (rl4rs)" --force
```

### Remove the kernel
To remove the kernel if needed:
```bash
jupyter kernelspec uninstall rl4rs
```

## Your EDA Notebook

I've set up your `EDA.ipynb` notebook with:
- ✓ Markdown header
- ✓ Import statements for pandas, numpy, matplotlib, seaborn
- ✓ Code to load the item_info dataset
- ✓ Ready to run!

Just select the "Python (rl4rs)" kernel and start exploring your data!

## Next Steps

1. Open `EDA.ipynb` in VS Code or Jupyter
2. Select the "Python (rl4rs)" kernel
3. Run the cells to start your analysis
4. The notebook will load the `item_info.csv` dataset

Happy analyzing! 📊
