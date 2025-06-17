import pandas as pd
import numpy as np
# Replace with your actual file path
file_path = "data/discover_analytics_2025-01-01_to_2025-06-04.csv"

try:
    df = pd.read_csv(file_path)
except pd.errors.ParserError:
    df = pd.read_csv(file_path, delimiter='\t')

# Convert to numeric and protect against divide-by-zero
df["Clicks"] = pd.to_numeric(df["Clicks"], errors="coerce")
df["Impressions"] = pd.to_numeric(df["Impressions"], errors="coerce")
df["Impressions"] = df["Impressions"].replace(0, np.nan)

# Calculate true Google-style CTR
df["URL CTR"] = (df["Clicks"] / df["Impressions"]).round(6)

# Create required columns
df["Landing Page"] = df["URL"]
df["Url Clicks"] = df["Clicks"]

# Define strict output column order
final_columns = ["Landing Page", "Impressions", "Url Clicks", "URL CTR"]
output_df = df[final_columns]

# Preview
print("✅ Final CSV Preview:")
print(output_df.head())

# Save to CSV (comma-separated)
output_df.to_csv("ctr_final_output.csv", index=False)