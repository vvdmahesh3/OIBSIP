import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import string
import re
import os

# Create screenshots directory if it doesn't exist
os.makedirs("screenshots", exist_ok=True)

# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and special symbols
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # Basic stopword removal (hardcoded list to avoid requiring NLTK download for simplicity)
    stopwords = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])
    words = text.split()
    words = [w for w in words if w not in stopwords]
    return " ".join(words)

# Part 2: Load dataset
df = pd.read_csv("dataset/spam.csv", encoding='latin-1')
# Drop unnecessary columns often found in this dataset
df = df.iloc[:, :2]
df.columns = ['label', 'message']

# Save a plot for class distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='label', data=df, hue='label', palette='viridis', legend=False)
plt.title("Class Distribution (Spam vs Not Spam)")
plt.savefig("screenshots/class_distribution.png")
plt.close()

# Part 3: Preprocess Text
df['processed_message'] = df['message'].apply(preprocess_text)

# Part 4: Feature Extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['processed_message'])

# Convert labels to binary (1 for spam, 0 for ham)
y = df['label'].map({'spam': 1, 'ham': 0})

# Part 5: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Part 6: Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Part 7: Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=['Not Spam (Ham)', 'Spam'])

# Save Confusion Matrix Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("screenshots/confusion_matrix.png")
plt.close()

# Part 8: Custom Testing
custom_test = ["Congratulations! You won ₹10000"]
processed_custom_test = [preprocess_text(msg) for msg in custom_test]
custom_X = vectorizer.transform(processed_custom_test)
custom_pred = model.predict(custom_X)
custom_pred_label = "Spam" if custom_pred[0] == 1 else "Not Spam"

# Save outputs to text file
with open("screenshots/output.txt", "w", encoding='utf-8') as f:
    f.write("--- Model Evaluation ---\n")
    f.write(f"Accuracy: {accuracy:.4f}\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(conf_matrix) + "\n\n")
    f.write("Classification Report:\n")
    f.write(class_report + "\n\n")
    f.write("--- Custom Testing ---\n")
    f.write(f"Input: {custom_test[0]}\n")
    f.write(f"Prediction: {custom_pred_label}\n")

print("All tasks completed successfully. Outputs and screenshots saved.")
