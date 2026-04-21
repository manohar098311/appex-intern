# Deliquency-Prediction
# Task 1: Data Immersion & Wrangling 📊

## 🚀 Project Overview
This project is part of the **ApexPlanet Internship** program. The objective was to take a raw, messy dataset simulating real-world financial data ("Delinquency Prediction"), assess its quality, and transform it into an analysis-ready format. 

The final output is a cleaned dataset with standardized formats and new engineered features suitable for risk modeling.

## 📂 Dataset Description
* **Name:** Delinquency Prediction Dataset
* **Domain:** Finance / Credit Risk
* **Rows:** 500 | **Columns:** 27 (After Engineering)
* **Goal:** Predict customer delinquency based on credit history and demographic data.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Libraries:** Pandas, NumPy
* **Tools:** Jupyter Notebook, Anaconda

## 📋 Steps Taken

### Phase 1: Data Quality Assessment (Profiling)
Before cleaning, I profiled the data to identify critical issues:
* **Missing Values:** Identified gaps in `Income` (~8% missing), `Loan_Balance`, and `Credit_Score`.
* **Inconsistent Text:** `Employment_Status` contained mixed casing ("EMP", "employed", "Self-employed").
* **Outliers:** Checked income distributions to ensure median-based imputation was appropriate.

### Phase 2: Data Cleaning
* **Imputation:**
    * Filled missing `Income` and `Loan_Balance` with **Median** values (robust against high-income outliers).
    * Dropped rows where `Credit_Score` was null (as this is a critical metric for the target variable).
* **Standardization:**
    * Normalized `Employment_Status` values to Title Case (e.g., converted "EMP" to "Employed").

### Phase 3: Feature Engineering (New Insights)
To enhance the dataset for future modeling, I created the following features:
1.  **`Recent_Risk_Score`**: Aggregated the payment history from the last 6 months (`Month_1` to `Month_6`) into a single numeric score (0-12), where higher scores indicate higher risk.
2.  **`High_Utilization`**: A binary flag (0/1) identifying customers using >80% of their credit limit.

## 📂 Project Structure

**Task-1-Data-Wrangling/**
* `data/`
    * 📄 **Delinquency_prediction_dataset.csv**: Raw, messy financial data
* `scripts/`
    * 🐍 **data_wrangling_task1.ipynb**: Python code for cleaning & profiling
* `output/`
    * 📊 **cleaned_delinquency_dataset.csv**: Final analysis-ready dataset
* 📝 **Data_Dictionary.md**: Column definitions & business relevance
* 📄 **README.md**: Project overview & documentation


## 💻 How to Run This Project
1.  Clone this repository.
2.  Install dependencies:
    ```bash
    pip install pandas numpy
    ```
3.  Open the Jupyter Notebook in the `scripts/` folder.
4.  Run all cells to generate the cleaned dataset in the `output/` folder.

## 🔍 Key Findings
* Customers with a `Recent_Risk_Score` above 5 showed a strong correlation with the `Delinquent_Account` target variable.
* Self-employed individuals had a higher variance in income reporting compared to employed individuals.

---
**Author:** [Shankar Reddy Mopur](https://github.com/Shankar007-pro)
**Date:** [01-01-2026]
