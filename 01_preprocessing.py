import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/Placement_Data_Full_Class.csv")

# Drop irrelevant column
df.drop(columns=["sl_no"], inplace=True)

# Handle missing values in salary (fill with median)
df["salary"].fillna(df["salary"].median(), inplace=True)

# Encode categorical variables
categorical_cols = ["gender", "ssc_b", "hsc_b", "hsc_s", "degree_t", "workex", "specialisation", "status"]
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Ensure output directory exists
os.makedirs("outputs", exist_ok=True)

# Save cleaned data
df.to_csv("outputs/cleaned_data.csv", index=False)
