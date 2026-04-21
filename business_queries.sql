
-- Q1: What is the overall delinquency rate?
SELECT 
    COUNT(*) as Total_Customers,
    SUM(Delinquent_Account) as Total_Delinquents,
    (SUM(Delinquent_Account) * 100.0 / COUNT(*)) as Delinquency_Rate_Percent
FROM delinquency_data;

-- Q2: Average Credit Score & Income by Employment Status
SELECT Employment_Status, 
       COUNT(*) as Count, 
       ROUND(AVG(Credit_Score),0) as Avg_Score, 
       ROUND(AVG(Income),0) as Avg_Income
FROM delinquency_data
GROUP BY Employment_Status
ORDER BY Avg_Score DESC;

-- Q3: Who are the Top 5 Riskiest Customers? (High Debt + Low Credit Score)
SELECT Customer_ID, Credit_Score, Debt_to_Income_Ratio, Delinquent_Account
FROM delinquency_data
WHERE Credit_Score < 600
ORDER BY Debt_to_Income_Ratio DESC
LIMIT 5;

-- Q4: Does credit card type affect delinquency?
SELECT Credit_Card_Type, 
       SUM(Delinquent_Account) as Delinquencies,
       COUNT(*) as Total,
       (SUM(Delinquent_Account)*100.0 / COUNT(*)) as Risk_Percentage
FROM delinquency_data
GROUP BY Credit_Card_Type
ORDER BY Risk_Percentage DESC;