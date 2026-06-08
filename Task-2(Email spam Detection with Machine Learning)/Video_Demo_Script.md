# Video Demo Script - Task 2: Email Spam Detection

## Intro
*(Camera on you / Screen recording starts)*

**You:** 
"Hello Everyone. I am Peruri Veera Venkata Durga Mahesh. This is Task 2 of my Oasis Infobyte Data Science Internship. The task is 'Email Spam Detection'. In this video, I will walk you through my machine learning project where I built a model to predict whether a message is Spam or Not Spam."

## Show Dataset
*(Open your dataset folder or show the CSV file in your IDE / Excel)*

**You:**
"First, let's look at the dataset. I used a CSV file `spam.csv` which contains a collection of text messages labeled as either 'spam' or 'ham' (which means not spam). This text data serves as the foundation for training our classification model."

## Show Code
*(Switch to Jupyter Notebook / `analysis.ipynb`)*

**You:**
"Here is the code I wrote for this project. 
- **Part 1 & 2:** I imported libraries like `pandas`, `sklearn`, and `matplotlib`, and loaded the dataset.
- **Part 3:** For text preprocessing, I converted all the text to lowercase and removed punctuations, special symbols, and common stopwords like 'the' or 'is'. This helps the model focus only on meaningful words.
- **Part 4 & 5:** I used `TfidfVectorizer` for feature extraction to convert the raw text into numerical data. Then, I split the dataset into 80% for training and 20% for testing.
- **Part 6:** Finally, I trained a Naive Bayes model using `MultinomialNB`, which is highly effective for text classification."

## Show Graphs
*(Scroll down the notebook or open the images from the `screenshots/` folder one by one)*

**You:**
"Let's look at the visualizations:
- **Class Distribution Plot:** This graph shows the balance of our dataset, highlighting that there are significantly more 'ham' messages than 'spam' messages.
- **Confusion Matrix:** This heatmap visualizes the performance of our model, showing exactly how many messages were correctly and incorrectly classified by the Naive Bayes algorithm."

## Show Model & Results
*(Show the README or the `output.txt` file)*

**You:**
"Moving on to the results: 
The Naive Bayes model achieved an excellent accuracy score. The Classification Report shows high precision and recall. 
To test it, I gave the model a custom input: 'Congratulations! You won ₹10000'. The model successfully predicted it as **Spam**, proving that it works perfectly."

## End
*(Look back at the camera / Wrap up)*

**You:**
"Thank you for watching. The GitHub repository link is available in the description."
