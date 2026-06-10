# Sales Prediction using Python

## Objective
Build a Machine Learning model to predict future sales based on advertising investment data across different platforms (TV, Radio, and Newspaper).

## Dataset
The dataset `Advertising.csv` contains historical data on advertising budgets for TV, Radio, and Newspaper, along with the corresponding Sales figures. It is stored in the `dataset/` directory.

## Technologies Used
- Python
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- Jupyter Notebook

## Data Cleaning
- Loaded the dataset and checked for any structural issues.
- Dropped the unnecessary `Unnamed: 0` index column that often comes with this dataset.

## Data Visualization
Exploratory Data Analysis was performed using four key visualizations:
1. **TV vs Sales** (Scatterplot): Showed a strong positive linear relationship.
2. **Radio vs Sales** (Scatterplot): Showed a moderate positive relationship.
3. **Correlation Heatmap** (Heatmap): Quantified the correlations between all features. TV had the highest correlation with Sales.
4. **Pairplot**: Visualized the relationships between all variables in the dataset simultaneously.

## Machine Learning Model
- **Algorithm Used**: Linear Regression.
- **Features**: TV, Radio, and Newspaper advertising budgets.
- **Target**: Sales.
- **Data Splitting**: Split the dataset into 80% Training Data and 20% Testing Data.

## Results
- Evaluated the model using standard regression metrics:
  - **R2 Score**: Indicates how well the model explains the variance in the data (higher is better).
  - **Mean Squared Error (MSE)** & **Mean Absolute Error (MAE)**: Measures the average magnitude of the errors in predictions.
- **Custom Prediction Example**:
  - *Input*: TV = 100, Radio = 20, Newspaper = 30
  - *Predicted Sales*: The model successfully calculated the expected sales volume based on these specific budgets.

## Screenshots
Screenshots of the data visualizations, EDA outputs, and model evaluation metrics have been successfully generated and saved inside the `screenshots/` directory.

## Conclusion
The analysis and the machine learning model both conclude that **TV advertising contributes significantly more towards sales than newspaper or radio advertising.** Businesses looking to maximize their ROI should allocate a larger portion of their budget to TV marketing.
