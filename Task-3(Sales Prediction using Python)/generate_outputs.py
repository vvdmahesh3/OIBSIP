import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import os
import io

# Create screenshots directory if it doesn't exist
os.makedirs("screenshots", exist_ok=True)

# Part 1: Load Dataset
print("Loading dataset...")
df = pd.read_csv("dataset/Advertising.csv")

# Clean column names (sometimes there's an 'Unnamed: 0' index column)
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

# Part 2: EDA
output_str = "--- Part 2: EDA ---\n\n"
output_str += "--- df.head() ---\n"
output_str += df.head().to_string() + "\n\n"
output_str += "--- df.info() ---\n"
buffer = io.StringIO()
df.info(buf=buffer)
output_str += buffer.getvalue() + "\n"
output_str += "--- df.describe() ---\n"
output_str += df.describe().to_string() + "\n\n"

# Part 3: Visualization

# Graph 1: TV vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(x='TV', y='Sales', data=df, color='blue')
plt.title("TV Advertising vs Sales")
plt.tight_layout()
plt.savefig("screenshots/graph_1_tv_vs_sales.png")
plt.close()

# Graph 2: Radio vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Radio', y='Sales', data=df, color='green')
plt.title("Radio Advertising vs Sales")
plt.tight_layout()
plt.savefig("screenshots/graph_2_radio_vs_sales.png")
plt.close()

# Graph 3: Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("screenshots/graph_3_heatmap.png")
plt.close()

# Graph 4: Pairplot
sns.pairplot(df)
plt.tight_layout()
plt.savefig("screenshots/graph_4_pairplot.png")
plt.close()

# Part 4: Train Model
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Part 5: Prediction
custom_input = pd.DataFrame({'TV': [100], 'Radio': [20], 'Newspaper': [30]})
custom_prediction = model.predict(custom_input)[0]

output_str += "--- Part 5: Prediction ---\n"
output_str += f"Input: TV=100, Radio=20, Newspaper=30\n"
output_str += f"Predicted Sales: {custom_prediction:.2f}\n\n"

# Part 6: Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

output_str += "--- Part 6: Evaluation ---\n"
output_str += f"R2 Score: {r2:.4f}\n"
output_str += f"Mean Squared Error: {mse:.4f}\n"
output_str += f"Mean Absolute Error: {mae:.4f}\n\n"

# Part 7: Conclusion
conclusion = """--- Part 7: Conclusion ---
TV advertising contributes significantly more towards sales than newspaper advertising.
This is evident from the high correlation coefficient in the heatmap and the visual trend in the scatterplots.
"""
output_str += conclusion

with open("screenshots/output.txt", "w") as f:
    f.write(output_str)

print("All tasks completed successfully. Outputs and screenshots saved.")
