# Dataset Directory

This directory contains the datasets for the RL4RS project.

## Files

### Tracked Files (in Git)
- **item_info.csv** (86KB) - Item metadata and features

### Large Files (Not in Git)
The following large dataset files are excluded from Git tracking due to their size:

- **rl4rs_dataset_a_rl.csv** (~2.2GB) - RL training dataset A
- **rl4rs_dataset_a_sl.csv** (~2.7GB) - Supervised learning dataset A  
- **rl4rs_dataset_b_rl.csv** (~2.2GB) - RL training dataset B
- **rl4rs_dataset_b_sl.csv** (~2.7GB) - Supervised learning dataset B

**Total size:** ~9.8GB

## Downloading the Datasets

### Option 1: Original Source
Download the datasets from the original RL4RS data source:
```bash
# Add download instructions here when you have the source
# wget <download_url>
# or use the provided download script
```

### Option 2: Use Existing Files
If you already have the datasets locally (as in the original RL4RS folder), you can copy them:

```bash
# From your terminal in the RL4RS_replication directory
cp ../RL4RS/RL4RS/dataset/rl4rs_dataset_*.csv ./dataset/
```

### Option 3: Cloud Storage (Recommended for Collaboration)
For team collaboration, consider storing these large files on:
- **Google Drive** / **Dropbox** / **OneDrive**
- **AWS S3** / **Google Cloud Storage**
- **DVC (Data Version Control)** - Recommended for ML projects
- **Git LFS** - If you must track them in Git (not recommended for >1GB files)

## Dataset Structure

Each dataset CSV file contains user interaction data with columns such as:
- User ID
- Item ID
- Timestamp
- User features
- Item features
- Interaction type
- Rewards/Labels

For detailed schema information, refer to the original RL4RS documentation.

## Data Splitting

- **Dataset A**: One version for RL training and one for supervised learning
- **Dataset B**: One version for RL training and one for supervised learning

The differences between A and B datasets and RL/SL versions are documented in the RL4RS paper.

## Using DVC (Recommended)

If you want to track large files properly, consider using DVC:

```bash
# Install DVC
pip install dvc

# Initialize DVC in your repo
dvc init

# Add large files to DVC
dvc add dataset/rl4rs_dataset_a_rl.csv
dvc add dataset/rl4rs_dataset_a_sl.csv
dvc add dataset/rl4rs_dataset_b_rl.csv
dvc add dataset/rl4rs_dataset_b_sl.csv

# Set up remote storage (example with Google Drive)
dvc remote add -d myremote gdrive://<folder_id>

# Push data to remote
dvc push

# Now others can pull the data
# dvc pull
```

## Verification

After downloading/copying the datasets, verify their integrity:

```bash
# Check files exist
ls -lh dataset/

# Should see:
# - item_info.csv (~86KB)
# - rl4rs_dataset_a_rl.csv (~2.2GB)
# - rl4rs_dataset_a_sl.csv (~2.7GB)
# - rl4rs_dataset_b_rl.csv (~2.2GB)
# - rl4rs_dataset_b_sl.csv (~2.7GB)

# Optional: Verify data loads correctly
conda activate rl4rs
python -c "import pandas as pd; df = pd.read_csv('dataset/item_info.csv'); print(f'Loaded {len(df)} items')"
```

## Note on Git Tracking

These large CSV files are intentionally excluded from Git via `.gitignore` to:
1. Avoid exceeding GitHub's file size limits (100MB per file)
2. Keep the repository size manageable
3. Speed up clone and pull operations
4. Prevent Git LFS costs

The small `item_info.csv` file is tracked in Git for convenience.
