# Video Demo Script - Task 3: Sales Prediction Using Python

## Intro
*(Camera on you / Screen recording starts)*

**You:** 
"Hello Everyone! I am Peruri Veera Venkata Durga Mahesh. This is Task 3 of my Oasis Infobyte Data Science Internship. The task is 'Sales Prediction Using Python'. In this video, I will walk you through my machine learning project where I built a model to predict future sales based on advertising investments."

## Show Dataset
*(Open your dataset folder or show the CSV file in your IDE / Excel)*

**You:**
"First, let's look at the dataset. I used an advertising dataset that contains historical data on budgets allocated to TV, Radio, and Newspaper advertising, along with the corresponding sales figures. Our goal is to find out which advertising medium drives the most sales."

## Show Code
*(Switch to Jupyter Notebook / `analysis.ipynb`)*

**You:**
"Here is the code I wrote for this project using Jupyter Notebook. 
- **Part 1 & 2:** I imported essential libraries like `pandas`, `scikit-learn`, and `seaborn`. Then, I loaded the dataset and performed basic Exploratory Data Analysis using `head()`, `info()`, and `describe()` to understand the data distribution.
- **Part 3:** I created several visualizations to uncover relationships between advertising platforms and sales.
- **Part 4:** For the machine learning part, I chose a Linear Regression model since we are predicting continuous numerical values. I trained the model on 80% of the data.
- **Part 5 & 6:** I then passed a custom input to the model to predict sales and evaluated the model's accuracy using metrics like the R2 Score and Mean Absolute Error."

## Show Graphs
*(Scroll down the notebook or open the images from the `screenshots/` folder one by one)*

**You:**
"Let's look at the visualizations:
- **TV vs Sales Scatterplot:** This graph shows a very strong linear relationship. As TV advertising increases, sales clearly increase.
- **Radio vs Sales Scatterplot:** This shows a more scattered but positive trend.
- **Heatmap & Pairplot:** The correlation heatmap proves that TV has the highest correlation with sales, while Newspaper has the lowest."

## Show Model & Results
*(Show the notebook prediction cell or the `output.txt` file)*

**You:**
"Moving on to the results: 
The Linear Regression model performed very well with a high R2 score. I tested the model with a custom input: TV=100, Radio=20, and Newspaper=30, and the model instantly predicted the expected sales. 

## Conclusion
*(Show the README Conclusion or the `output.txt` file)*

**You:**
To conclude: The data clearly shows that TV advertising contributes significantly more towards sales than newspaper advertising. Businesses should focus their budgets on TV and Radio to maximize their ROI."

## End
*(Look back at the camera / Wrap up)*

**You:**
"Thank you for watching. The GitHub repository link is available in the description below."
