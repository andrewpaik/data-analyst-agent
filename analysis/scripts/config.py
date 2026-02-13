"""
Default configuration and imports for the Data Analyst project.
Usage: from config import *
"""

# Core
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Statistical Analysis
from scipy import stats
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

# Machine Learning
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    r2_score,
    mean_squared_error,
    mean_absolute_error,
)

# Utilities
import warnings
warnings.filterwarnings("ignore")

# --- Pandas display settings ---
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)
pd.set_option("display.float_format", "{:.2f}".format)

# --- Matplotlib / Seaborn defaults ---
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("muted")
plt.rcParams["figure.figsize"] = (12, 7)
plt.rcParams["figure.dpi"] = 300
plt.rcParams["font.size"] = 12

# --- Project paths ---
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_RAW = os.path.join(PROJECT_ROOT, "data", "raw")
DATA_CLEANED = os.path.join(PROJECT_ROOT, "data", "cleaned")
OUTPUT_CHARTS = os.path.join(PROJECT_ROOT, "output", "charts")
OUTPUT_REPORTS = os.path.join(PROJECT_ROOT, "output", "reports")
