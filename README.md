# Retail Sales Data Analysis - Python

## Objective:

The objective of this Python code is to perform data manipulation, analysis, and visualization on a retail transactions dataset. The analysis focuses on identifying patterns in transaction amounts, customer behavior, cohort segmentation, outlier detection, and churn analysis using various data processing and analytical techniques.


## Overview:

1. ***Data Loading and Merging:*** The code reads two CSV files containing retail transactions (`Retail_Data_Transactions.csv`) and customer responses (`Retail_Data_Response.csv`). These two datasets are merged based on `customer_id`, creating a single dataframe for further analysis.

2. ***Exploratory Data Analysis (EDA):***
   - Data types and basic statistics of the dataset are explored.
   - Missing values are checked and removed.
   - The data types of specific columns are converted for proper analysis.

3. ***Outlier Detection:*** The code applies Z-score to identify outliers in transaction amounts (`tran_amount`) and customer responses (`response`). Boxplots are also used for visualizing outliers in `tran_amount`.

4. ***Creating New Features:*** A new column `month` is extracted from the transaction date, allowing for monthly sales analysis.

5. ***Sales Analysis:***
   - The code identifies the top 3 months with the highest transaction amounts.
   - It determines the top 5 customers with the most orders and highest transaction values.

6. ***Advanced Analytics:***
   - ***Time Series Analysis:*** Monthly sales trends are plotted to analyze changes over time.
   - ***Cohort Segmentation:*** Customers are segmented based on recency, frequency, and monetary value (RFM analysis) to categorize them into different segments such as 'P0', 'P1', and 'P2'.
   - ***Churn Analysis:*** The code analyzes customer churn by counting the number of active and churned customers and visualizes the data using a bar plot.

7. ***Top Customer Analysis:*** The transaction behavior of the top 5 customers is plotted across different months.

8. ***Saving Results:*** The final datasets (including main data and RFM analysis) are saved into CSV files (`MainData.csv` and `AddAnlys.csv`) for further use.


## **Explanation of the Code:**

1. ***Data Reading and Merging:***
   - The transaction and response data are loaded using `pd.read_csv` and merged based on the `customer_id`. This combined dataset is then used for further analysis.
   
2. ***Missing Values Handling:***
   - Missing values in the dataset are identified using `df.isnull().sum()` and removed using `df.dropna()`.

3. ***Outlier Detection:***
   - Z-scores are computed to detect outliers in the `tran_amount` and `response` columns. Outliers are those data points where the Z-score is greater than 3.

4. ***Feature Engineering:***
   - New columns such as `month` (extracted from `trans_date`) and `month_year` are created for time-based analysis.

5. ***Monthly Sales Analysis:***
   - Monthly sales data are computed using `groupby` and sorted to find the top 3 months with the highest transaction values.
   - Top customers based on the number of orders and transaction values are identified using `value_counts` and `groupby`.

6. ***Cohort Segmentation:***
   - Customers are segmented into three categories (`P0`, `P1`, `P2`) based on recency, frequency, and monetary value in their transactions using an RFM model.

7. ***Churn Analysis:***
   - The number of active and churned customers is computed using `value_counts` on the `response` column, and visualized using a bar plot.

8. ***Time Series and Top Customer Analysis:***
   - Monthly sales trends are plotted over time, and the transaction behavior of the top 5 customers is analyzed and visualized using line plots.

9. ***Data Exporting:***
   - Final datasets are saved to CSV files for external use.


## Conclusion:

The code efficiently processes and analyzes retail transaction data to gain insights into customer behavior and sales trends. It highlights key metrics such as top-performing months, top customers by orders and sales value, and segments customers based on the RFM model. Outliers are detected and handled appropriately. Time series analysis provides a visual representation of sales over time, and churn analysis helps in understanding customer retention. The final outputs are saved for further analysis or reporting.
