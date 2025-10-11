#!/usr/bin/env python3
"""
Test script to verify the RL4RS environment is properly set up.
"""

def test_imports():
    """Test importing essential packages."""
    print("Testing essential package imports...")
    
    # Test basic packages
    try:
        import numpy as np
        print("✓ NumPy imported successfully")
    except ImportError as e:
        print(f"✗ NumPy import failed: {e}")
    
    try:
        import pandas as pd
        print("✓ Pandas imported successfully")
    except ImportError as e:
        print(f"✗ Pandas import failed: {e}")
    
    try:
        import matplotlib.pyplot as plt
        print("✓ Matplotlib imported successfully")
    except ImportError as e:
        print(f"✗ Matplotlib import failed: {e}")
    
    try:
        import sklearn
        print("✓ Scikit-learn imported successfully")
    except ImportError as e:
        print(f"✗ Scikit-learn import failed: {e}")
    
    # Test deep learning packages
    try:
        import torch
        print(f"✓ PyTorch {torch.__version__} imported successfully")
    except ImportError as e:
        print(f"✗ PyTorch import failed: {e}")
    
    try:
        import tensorflow as tf
        print(f"✓ TensorFlow {tf.__version__} imported successfully")
    except ImportError as e:
        print(f"✗ TensorFlow import failed: {e}")
    
    # Test RL packages
    try:
        import gym
        print(f"✓ Gym {gym.__version__} imported successfully")
    except ImportError as e:
        print(f"✗ Gym import failed: {e}")
    
    try:
        import h5py
        print("✓ H5py imported successfully")
    except ImportError as e:
        print(f"✗ H5py import failed: {e}")
    
    print("\nEnvironment test completed!")

def test_basic_functionality():
    """Test basic functionality of key packages."""
    print("\nTesting basic functionality...")
    
    try:
        import numpy as np
        arr = np.array([1, 2, 3])
        print(f"✓ NumPy basic test: {arr}")
    except Exception as e:
        print(f"✗ NumPy basic test failed: {e}")
    
    try:
        import pandas as pd
        df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        print(f"✓ Pandas basic test: DataFrame created with shape {df.shape}")
    except Exception as e:
        print(f"✗ Pandas basic test failed: {e}")
    
    try:
        import gym
        env = gym.make('CartPole-v1')
        print(f"✓ Gym basic test: Created CartPole-v1 environment")
        env.close()
    except Exception as e:
        print(f"✗ Gym basic test failed: {e}")

if __name__ == "__main__":
    test_imports()
    test_basic_functionality()
