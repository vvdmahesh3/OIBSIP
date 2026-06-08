# Email Spam Detection

## Objective
Build a Machine Learning model that predicts whether an email or SMS message is "Spam" or "Not Spam" (Ham).

## Dataset
The dataset `spam.csv` contains SMS messages labeled as either `spam` or `ham`. It is stored in the `dataset/` directory. The data consists of the message text and its corresponding target label.

## Technologies Used
- Python
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- Jupyter Notebook

## Data Cleaning
- Loaded the dataset and removed unnecessary, unnamed columns.
- Renamed the primary columns to `label` and `message`.
- **Text Preprocessing**: 
  - Converted all text to lowercase.
  - Removed all punctuation and special symbols.
  - Removed common English stopwords to reduce noise in the data.

## Data Visualization
- **Class Distribution**: Plotted a countplot to show the imbalance between Spam and Not Spam messages.
- **Confusion Matrix Heatmap**: Visualized the performance of the predictive model, showing true positives, true negatives, false positives, and false negatives.

## Machine Learning Model
- **Feature Extraction**: Used `TfidfVectorizer` to convert the text messages into numerical TF-IDF feature vectors.
- **Data Splitting**: Split the dataset into 80% Training Data and 20% Testing Data.
- **Model Selection**: Trained a **Naive Bayes Model (MultinomialNB)**, which is highly effective and widely used for text classification and spam detection.

## Results
- The Naive Bayes model achieved a very high accuracy score on the testing dataset.
- Evaluated using a **Confusion Matrix** and **Classification Report**, showing excellent precision and recall for both Spam and Ham classes.
- **Custom Testing Example**:
  - *Input*: "Congratulations! You won ₹10000"
  - *Prediction*: Spam

## Screenshots
Screenshots of the data visualizations, confusion matrix, and model evaluation outputs have been successfully generated and saved inside the `screenshots/` directory.

## Conclusion
The project successfully demonstrates how Natural Language Processing (NLP) techniques and the Naive Bayes algorithm can be used to accurately detect spam messages. The model performs extremely well and effectively filters out unwanted spam content.
