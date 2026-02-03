# Hypothesis-Testing-Analysis

## Project Overview
This project demonstrates how to perform **A/B Testing** using Python to evaluate whether a **new version (Test group)** performs better than an **existing version (Control group)** based on conversion rates.
The project follows a structured data analytics workflow, including hypothesis formulation, statistical testing, visualization, and business recommendations.

## Objective
To determine whether the **Test version** leads to a statistically significant improvement in conversion rate compared to the **Control version**.

## Project Structure
ab-testing-conversion-analysis-python/
│
├── ab_test_data.csv # Input dataset
├── ab_test_summary.csv # Output summary (conversion rates)
├── final_recommendation.txt # Business recommendation
├── ab_testing_analysis.ipynb # Jupyter Notebook (analysis code)
└── README.md # Project documentation

## Hypothesis Testing
- **Null Hypothesis (H₀):** There is no difference in conversion rates between Control and Test groups.
- **Alternative Hypothesis (H₁):** The Test group has a higher conversion rate than the Control group.
- **Significance Level (α):** 0.05

## Tools & Libraries Used
- Python  
- Pandas  
- NumPy  
- SciPy  
- Matplotlib  

## Analysis Steps
1. Load and inspect the dataset  
2. Split data into Control and Test groups  
3. Calculate conversion rates  
4. Perform a two-sample t-test  
5. Compute confidence intervals  
6. Visualize conversion rate comparison  
7. Draw statistical and business conclusions  

## Key Insights
- The Test group shows a higher conversion rate than the Control group.
- Statistical testing indicates that the observed difference is **statistically significant**.
- The null hypothesis is rejected at the 5% significance level.

## Conclusion
Based on the statistical evidence, the **Test version outperforms the Control version**.  
It is recommended to **deploy the Test version** to improve overall conversion rates.

Detailed findings are available in `final_recommendation.txt`.
