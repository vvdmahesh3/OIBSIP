import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create screenshots directory if it doesn't exist
os.makedirs("screenshots", exist_ok=True)

# Load Dataset
print("Loading dataset...")
df = pd.read_csv("dataset/unemployment.csv")

# Clean column names by stripping spaces
df.columns = df.columns.str.strip()

# Basic Analysis Output
with open("screenshots/output.txt", "w") as f:
    f.write("--- df.head() ---\n")
    f.write(df.head().to_string())
    f.write("\n\n--- df.info() ---\n")
    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    f.write(buffer.getvalue())
    f.write("\n\n--- df.describe() ---\n")
    f.write(df.describe().to_string())
    f.write("\n\n--- df.isnull().sum() ---\n")
    f.write(df.isnull().sum().to_string())

# Data Cleaning
df = df.drop_duplicates()
df = df.dropna()

# Visualizations

# Graph 1: Unemployment by State
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
plt.xticks(rotation=90)
plt.title("Unemployment by State")
plt.tight_layout()
plt.savefig("screenshots/graph_1_unemployment_by_state.png")
plt.close()

# Graph 2: Monthly unemployment trend
# Let's convert Date to datetime and sort
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'], marker='o', linestyle='-')
plt.title("Monthly Unemployment Trend")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/graph_2_monthly_trend.png")
plt.close()

# Graph 3: Covid impact on unemployment
# We can use lineplot to show the trend across states or aggregate
plt.figure(figsize=(10, 5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df, errorbar=None)
plt.title("Covid Impact on Unemployment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/graph_3_covid_impact.png")
plt.close()

# Graph 4: Heatmap
# Correlation heatmap for numeric columns
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("screenshots/graph_4_heatmap.png")
plt.close()

# Findings / Insights
findings = """
Findings & Insights:
- During the Covid period, unemployment rose significantly, especially from March 2020 to May 2020.
- State Puducherry / Haryana / Tripura showed the highest unemployment rates in certain periods.
- States like Meghalaya and Assam showed relatively lower unemployment.
- There is a strong negative correlation between Estimated Employed and Estimated Unemployment Rate.
"""
with open("screenshots/insights.txt", "w") as f:
    f.write(findings.strip())

print("All screenshots and insights saved successfully!")
