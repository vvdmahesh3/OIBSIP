# 🔄 Project Workflow & Architecture

This document outlines the step-by-step implementation plan for **CrisisSignal AI Lite**.

## 📅 Phased Implementation Plan

### Phase 1: Planning & Setup (Week 1)
- [x] Define project scope and objectives.
- [x] Set up GitHub repository structure.
- [x] Create initial documentation (`README.md`, `Project_Planning.md`, `Project_Workflow.md`).
- [ ] Finalize dataset selection.

### Phase 2: Data Collection & EDA (Week 2)
- [ ] Load the selected dataset (Disaster Tweets).
- [ ] Perform Exploratory Data Analysis (EDA) to understand data distribution.
- [ ] Identify missing values, class imbalances, and data patterns.
- [ ] Visualize word frequencies and category counts.

### Phase 3: Data Preprocessing (Week 2-3)
- [ ] Text cleaning: Lowercasing, removing punctuation, and special characters.
- [ ] Tokenization: Splitting text into individual words.
- [ ] Stop-word removal: Filtering out common words (e.g., 'the', 'is', 'in').
- [ ] Stemming/Lemmatization: Reducing words to their root forms.
- [ ] Vectorization: Converting text to numerical features (TF-IDF or CountVectorizer).

### Phase 4: Model Building & Training (Week 3)
- [ ] Split dataset into training and testing sets.
- [ ] Train baseline models (Naive Bayes, Logistic Regression).
- [ ] Evaluate models using Accuracy, Precision, Recall, and F1-Score.
- [ ] Select the best-performing model and tune hyperparameters.
- [ ] Save the trained model as a `.pkl` file.

### Phase 5: UI Development & Integration (Week 4)
- [ ] Design a simple, intuitive web interface using Streamlit.
- [ ] Integrate the saved ML model with the Streamlit app.
- [ ] Implement features: Text input, Prediction display, Confidence score, and Suggested action.
- [ ] Test the application locally.

### Phase 6: Finalization & Deployment (Week 4)
- [ ] Record a demo video and capture screenshots of the working application.
- [ ] Update `README.md` with installation and usage instructions.
- [ ] Push final code to GitHub.
- [ ] Submit project deliverables for the internship evaluation.

## 🏗️ System Architecture
1. **User Input:** User enters a text message via the Streamlit UI.
2. **Preprocessing:** Text is cleaned and vectorized using the same methods applied during training.
3. **Prediction:** The processed text is fed into the loaded Scikit-Learn model.
4. **Output:** The model returns the predicted category and confidence score, displayed to the user.
