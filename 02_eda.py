import pandas as pd
import os

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Generate summary statistics
summary = df.describe(include="all")

# Ensure output directory exists
os.makedirs("outputs", exist_ok=True)

# Save summary statistics
summary.to_csv("outputs/eda_summary.csv")

# Display categorical value counts
categorical_cols = ["gender", "ssc_b", "hsc_b", "hsc_s", "degree_t", "workex", "specialisation", "status"]
category_counts = {col: df[col].value_counts().to_dict() for col in categorical_cols}

# Save category counts
pd.DataFrame(category_counts).to_csv("outputs/categorical_counts.csv")
