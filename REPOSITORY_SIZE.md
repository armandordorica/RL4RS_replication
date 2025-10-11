# Repository Size Management

This document explains which files are tracked in Git and which are excluded to keep the repository manageable.

## Summary

- **Tracked files**: ~15-20 MB (code, configs, documentation, small data files)
- **Excluded files**: ~9.8 GB (large datasets)
- **GitHub limits**: 100 MB per file, recommended repo size < 1 GB

## Tracked Files (In Git)

### Code and Scripts
- `rl4rs/` - Core library code
- `script/` - Training and evaluation scripts  
- `reproductions/` - Reproduction bash scripts

### Documentation
- `README.md` - Main repository README
- `REPLICATION_README.md` - Detailed replication guide
- `ENVIRONMENT_SETUP.md` - Environment setup instructions
- `LICENSE` - License file
- `RL4RS_appendix.pdf` - Additional documentation (~1 MB)
- `tutorial.ipynb` - Tutorial notebook (~124 KB)

### Configuration
- `environment.yml` - Original Linux environment file
- `environment_macos.yml` - macOS-compatible environment file
- `activate_rl4rs.sh` - Environment activation script
- `test_environment.py` - Environment verification script
- `.gitignore` - Git ignore rules

### Small Data Files
- `dataset/item_info.csv` - Item metadata (86 KB)
- `dataset/README.md` - Dataset documentation

### Assets
- `assets/` - Images and other small assets
- `index.html` - Project webpage

## Excluded Files (Not in Git)

### Large Datasets (~9.8 GB total)
These are excluded via `.gitignore`:
- `dataset/rl4rs_dataset_a_rl.csv` (~2.2 GB)
- `dataset/rl4rs_dataset_a_sl.csv` (~2.7 GB)
- `dataset/rl4rs_dataset_b_rl.csv` (~2.2 GB)
- `dataset/rl4rs_dataset_b_sl.csv` (~2.7 GB)

**How to get these files:**
See `dataset/README.md` for download instructions.

### Generated Files
Also excluded to keep the repo clean:
- Python cache: `__pycache__/`, `*.pyc`
- Jupyter checkpoints: `.ipynb_checkpoints/`
- Virtual environments: `.venv/`, `env/`
- macOS files: `.DS_Store`

### Experiment Outputs
- Model checkpoints: `*.pth`, `*.pt`, `*.ckpt`, `*.h5`
- Results directories: `results/`, `outputs/`, `runs/`
- Logs: `*.log`, `wandb/`, `tensorboard_logs/`
- Large HDF5 files: `*.h5`, `*.hdf5`

## File Size Thresholds

We use the following guidelines:
- **< 1 MB**: Always track (code, configs, small data)
- **1-10 MB**: Track if informative (documentation, small checkpoints)
- **10-50 MB**: Generally exclude unless essential
- **> 50 MB**: Always exclude (use external storage)

## Alternative Storage for Large Files

For large files, consider these options:

### 1. DVC (Recommended for ML Projects)
```bash
pip install dvc
dvc init
dvc add dataset/rl4rs_dataset_*.csv
dvc remote add -d storage s3://your-bucket/path
dvc push
```

### 2. Git LFS (Not recommended for multi-GB files)
```bash
git lfs install
git lfs track "dataset/*.csv"
git add .gitattributes
```
**Note**: Git LFS has bandwidth limits and costs.

### 3. Cloud Storage Links
Store data on Google Drive/Dropbox/S3 and include download links in `dataset/README.md`.

### 4. Local Copying
For personal use, copy files locally:
```bash
cp ../RL4RS/RL4RS/dataset/rl4rs_dataset_*.csv ./dataset/
```

## Checking Repository Size

```bash
# Check current repo size (excluding .git)
du -sh --exclude=.git .

# Check .git directory size
du -sh .git/

# List largest files
find . -type f -size +10M ! -path "./.git/*" -exec ls -lh {} \;

# Check what git will track
git status
git status --ignored
```

## Before First Commit

Before making your first commit, verify:

1. ✅ Large CSV files are in `.gitignore`
2. ✅ Only `item_info.csv` is tracked from dataset/
3. ✅ No files over 50 MB are being tracked
4. ✅ Repository size < 100 MB

```bash
# Verify with:
git add .
git status
git diff --cached --stat
```

## Cleaning Up Accidentally Tracked Large Files

If you accidentally committed large files:

```bash
# Remove from Git but keep locally
git rm --cached dataset/rl4rs_dataset_*.csv

# Remove from history (if already committed)
git filter-repo --path dataset/rl4rs_dataset_a_rl.csv --invert-paths
# OR use BFG Repo-Cleaner
java -jar bfg.jar --delete-files rl4rs_dataset_*.csv
```

## Collaborator Instructions

When cloning this repository:

1. Clone the repo (will be fast without large files):
   ```bash
   git clone <repo-url>
   cd RL4RS_replication
   ```

2. Download the large datasets separately (see `dataset/README.md`)

3. Set up the environment:
   ```bash
   conda env create -f environment_macos.yml
   conda activate rl4rs
   ```

4. Verify everything works:
   ```bash
   python test_environment.py
   ```

## Questions?

- For dataset download issues, see `dataset/README.md`
- For environment setup, see `ENVIRONMENT_SETUP.md`
- For general questions, open an issue in this repository
