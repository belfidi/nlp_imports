# ============================================================
# nlp_imports.py — NLP Project Standard Imports
# ============================================================

# Standard library
import os, re, csv
from datetime import datetime
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Suppress tokenizer parallelism warnings

# Data manipulation
import pandas as pd        # Dataframes and tabular data
import numpy as np         # Numerical operations and array manipulation

# Visualization
import matplotlib.pyplot as plt   # Core plotting library
import matplotlib as mpl          # Matplotlib configuration and rcParams
import seaborn as sns             # Statistical visualization built on matplotlib

# Scikit-learn: data splitting and preprocessing
from sklearn.model_selection import train_test_split   # Train/validation split
from sklearn.preprocessing import LabelEncoder         # Encode string labels as integers

# Scikit-learn: evaluation metrics
from sklearn.metrics import (
    classification_report,      # Per-class precision, recall, F1
    confusion_matrix,           # Confusion matrix for multi-class evaluation
    ConfusionMatrixDisplay,     # Matplotlib-compatible confusion matrix display
    accuracy_score              # Overall accuracy score
)

# Scikit-learn: baseline models
from sklearn.feature_extraction.text import TfidfVectorizer   # TF-IDF text vectorizer
from sklearn.linear_model import LogisticRegression            # Logistic regression baseline

# PyTorch
import torch                                       # Core deep learning framework
from torch.utils.data import Dataset, DataLoader   # Custom dataset and batching utilities

# Hugging Face Transformers
from transformers import (
    AutoTokenizer,                        # Load tokenizer for any transformer model
    AutoModelForSequenceClassification,   # Load classification head on transformer
    TrainingArguments,                    # Training configuration (epochs, lr, batch size)
    Trainer                               # High-level training loop for transformer models
)

# Hugging Face Datasets
from datasets import load_dataset   # Load datasets directly from Hugging Face Hub

# Gradio
import gradio as gr   # Build interactive web interfaces for ML models

# Export
import dataframe_image as dfi   # Export styled pandas tables as PNG images

# Project utilities (palette + styling) — loaded from GitHub
import requests as _req
exec(_req.get("https://raw.githubusercontent.com/belfidi/nlp_imports/main/palette.py").text)
exec(_req.get("https://raw.githubusercontent.com/belfidi/nlp_imports/main/styling.py").text)
apply_style()

# Status
print("All imports loaded ✅")
print(f"PyTorch:      {torch.__version__}")
print(f"Transformers: {__import__('transformers').__version__}")
print(f"Pandas:       {pd.__version__}")
