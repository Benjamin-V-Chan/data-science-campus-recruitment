import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Ensure output directory exists
os.makedirs("outputs", exist_ok=True)

# Histogram of numerical features
df.hist(figsize=(10, 8))
plt.savefig("outputs/numerical_histograms.png")

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")

# Bar plots for categorical variables
for col in ["gender", "workex", "specialisation", "status"]:
    plt.figure()
    sns.countplot(x=df[col])
    plt.title(f"Distribution of {col}")
    plt.savefig(f"outputs/{col}_distribution.png")
