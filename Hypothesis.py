import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Hello Files\Matplotlib and Seaborn\ab_test_data.csv")

# 3. Split control and test groups
control = df[df['group'] == 'control']['converted']
test = df[df['group'] == 'test']['converted']

# 4. Calculate conversion rates
control_rate = control.mean()
test_rate = test.mean()

print("Control Conversion Rate:", control_rate)
print("Test Conversion Rate:", test_rate)

# 5. Hypothesis Testing (t-test)
t_stat, p_value = ttest_ind(test, control)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# 6. Significance check
alpha = 0.05
if p_value < alpha:
    print("Result: Statistically Significant Difference")
else:
    print("Result: No Statistically Significant Difference")

# 7. Confidence Interval (difference in means)
diff = test_rate - control_rate
ci_low = diff - 1.96 * np.std(test) / np.sqrt(len(test))
ci_high = diff + 1.96 * np.std(test) / np.sqrt(len(test))

print("Confidence Interval:", (ci_low, ci_high))

# 8. Visualization
plt.bar(['Control', 'Test'], [control_rate, test_rate])
plt.title("A/B Test Conversion Rates")
plt.ylabel("Conversion Rate")
plt.show()

# 9. Save summary
summary = pd.DataFrame({
    'Group': ['Control', 'Test'],
    'Conversion_Rate': [control_rate, test_rate]
})
summary.to_csv("ab_test_summary.csv", index=False)