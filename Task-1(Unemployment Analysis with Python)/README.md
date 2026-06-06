# Unemployment Analysis with Python

## Objective
Analyze unemployment trends during Covid and identify patterns. This project performs an exploratory data analysis on unemployment data in India, examining the impact of the Covid-19 pandemic on employment across various states.

## Dataset
The dataset provides historical information about the unemployment rate, labor participation rate, and employment numbers in different regions of India during the Covid-19 pandemic. It is stored in the `dataset/` directory.

## Technologies Used
- Python
- pandas
- numpy
- matplotlib
- seaborn
- Jupyter Notebook

## Data Cleaning
- Loaded the dataset `unemployment.csv`.
- Handled missing data by dropping null values (`df.dropna()`).
- Removed duplicate records to ensure data integrity (`df.drop_duplicates()`).

## Data Visualization
Exploratory Data Analysis was performed using four key visualizations:
1. **Unemployment by State** (Barplot): Comparing the unemployment rate across different states.
2. **Monthly Unemployment Trend** (Lineplot): Tracking the rate of unemployment over time.
3. **Covid Impact on Unemployment Rate** (Lineplot): Visualizing the specific spikes during the pandemic months.
4. **Correlation Heatmap** (Heatmap): Highlighting the negative correlation between employment and unemployment rates.

## Machine Learning Model
*Note: This specific task focuses purely on Exploratory Data Analysis (EDA) and data visualization. No predictive Machine Learning model was required or implemented.*

## Results
- During the Covid period, the unemployment rate rose significantly, with massive spikes between March and May 2020.
- Certain states (such as Puducherry, Haryana, and Tripura) showed extremely high unemployment rates during the lockdown, while others (like Meghalaya and Assam) managed to maintain relatively lower rates.
- There is a noticeable and strong negative correlation between the Estimated Employed numbers and the Estimated Unemployment Rate.

## Screenshots
Screenshots of the data visualizations, data head, data info, and insights have been successfully generated and saved inside the `screenshots/` directory. 

## Conclusion
The analysis clearly demonstrates the severe economic impact of the Covid-19 lockdowns on employment in India. The visualizations effectively map out the sudden rise in unemployment rates and highlight the disproportionate effects experienced by different states.
