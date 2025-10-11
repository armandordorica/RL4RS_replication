# RL4RS Replication Study

This repository contains a replication study of the RL4RS (Reinforcement Learning for Recommender Systems) project, adapted for macOS Apple Silicon (ARM64).

## 📋 Overview

RL4RS is a comprehensive platform for training and evaluating Reinforcement Learning models in recommender systems. This replication aims to reproduce the results and experiments from the original work while adapting the codebase for modern macOS systems.

## 🚀 Quick Start

### Prerequisites

- macOS (preferably with Apple Silicon/ARM64)
- Anaconda or Miniconda installed
- Git

### Environment Setup

1. **Clone this repository** (if you haven't already):
   ```bash
   git clone <your-repo-url>
   cd RL4RS_replication
   ```

2. **Create the conda environment**:
   ```bash
   conda env create -f environment_macos.yml
   ```
   
   Note: The original `environment.yml` is included for reference but won't work on macOS ARM64.

3. **Activate the environment**:
   ```bash
   conda activate rl4rs
   ```
   
   Or use the convenience script:
   ```bash
   source activate_rl4rs.sh
   ```

4. **Test the installation**:
   ```bash
   python test_environment.py
   ```

For detailed setup instructions, see [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md).

## 📁 Repository Structure

```
RL4RS_replication/
├── README.md                    # This file
├── ENVIRONMENT_SETUP.md         # Detailed environment setup guide
├── LICENSE                      # License information
├── activate_rl4rs.sh           # Convenience activation script
├── test_environment.py         # Environment verification script
├── environment.yml             # Original environment file (Linux)
├── environment_macos.yml       # macOS-compatible environment file
├── tutorial.ipynb              # Tutorial notebook
├── RL4RS_appendix.pdf         # Additional documentation
├── index.html                  # Project webpage
│
├── dataset/                    # Dataset files
│   ├── item_info.csv
│   ├── rl4rs_dataset_a_rl.csv
│   ├── rl4rs_dataset_a_sl.csv
│   ├── rl4rs_dataset_b_rl.csv
│   └── rl4rs_dataset_b_sl.csv
│
├── rl4rs/                      # Core RL4RS library
│   ├── env/                    # Environment implementations
│   ├── nets/                   # Neural network models
│   ├── policy/                 # Policy implementations
│   ├── mdpchecker/            # MDP verification tools
│   ├── server/                # Server components
│   └── utils/                 # Utility functions
│
├── script/                     # Training and evaluation scripts
│   ├── batchrl_train.py
│   ├── simulator_eval.py
│   ├── supervised_train.py
│   └── ...
│
├── reproductions/             # Reproduction scripts
│   ├── run_simulator_train.sh
│   ├── run_batch_rl.sh
│   └── ...
│
└── assets/                    # Images and other assets
```

## 🔬 Running Experiments

### 1. Training the Simulator

```bash
conda activate rl4rs
# Run simulator training
bash reproductions/run_simulator_train.sh
```

### 2. Supervised Learning

```bash
# Train supervised models
bash reproductions/run_supervised_slate.sh
```

### 3. Batch RL Training

```bash
# Train batch RL models
bash reproductions/run_batch_rl.sh
```

### 4. Evaluation

```bash
# Evaluate trained models
bash reproductions/run_simulator_eval.sh
```

## 📊 Datasets

The `dataset/` directory contains:
- **item_info.csv**: Item metadata
- **rl4rs_dataset_a_rl.csv**: RL dataset A
- **rl4rs_dataset_a_sl.csv**: Supervised learning dataset A
- **rl4rs_dataset_b_rl.csv**: RL dataset B
- **rl4rs_dataset_b_sl.csv**: Supervised learning dataset B

## 🛠️ Key Modifications for macOS ARM64

This replication includes several adaptations for Apple Silicon compatibility:

1. **Python Version**: Upgraded to 3.8 (from 3.6)
2. **TensorFlow**: Using TensorFlow 2.13 with TensorFlow-macOS
3. **PyTorch**: Using PyTorch 2.4 with Apple Silicon support
4. **Gym**: Upgraded to 0.26.2 (from 0.19.0)
5. **Package Manager**: Using conda-forge channel for ARM64 packages

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for complete details.

## 📝 Jupyter Notebooks

To explore the tutorial and run experiments interactively:

```bash
conda activate rl4rs
jupyter lab
# or
jupyter notebook
```

Open `tutorial.ipynb` to get started.

## 🐛 Troubleshooting

### Common Issues

1. **Environment activation fails**:
   - Ensure conda is properly installed
   - Try: `conda env list` to see available environments

2. **Import errors**:
   - Make sure the conda environment is activated
   - Some scripts may need minor modifications for newer package versions

3. **GPU/Metal support**:
   - PyTorch should automatically use Apple Silicon GPU
   - TensorFlow-macOS includes Metal acceleration

4. **Gym deprecation warnings**:
   - These are expected; Gym 0.26.2 shows warnings about Gymnasium
   - The code should still work correctly

For more issues and solutions, see [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md).

## 📖 Original Paper & Citation

If you use this code or replicate these experiments, please cite the original RL4RS paper:

```bibtex
@article{rl4rs2022,
  title={RL4RS: A Real-World Benchmark for Reinforcement Learning based Recommender System},
  author={[Original Authors]},
  journal={[Journal/Conference]},
  year={2022}
}
```

## 🤝 Contributing

Contributions to improve the replication or fix compatibility issues are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project maintains the original license from the RL4RS project. See [LICENSE](LICENSE) for details.

## 🔗 Resources

- **Original RL4RS Repository**: [Link to original repo if available]
- **Paper**: [Link to paper if available]
- **Documentation**: See `RL4RS_appendix.pdf` and `ENVIRONMENT_SETUP.md`

## 📧 Contact

For questions about this replication:
- Open an issue in this repository
- [Your contact information if you want to include it]

---

**Note**: This is a replication study adapted for macOS Apple Silicon. Some results may differ slightly from the original due to:
- Different package versions
- Hardware differences (Apple Silicon vs x86_64)
- Random seed variations

Always compare results with the original paper and document any differences.
