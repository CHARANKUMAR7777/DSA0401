import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Clinical trial data
control = np.array([72, 75, 70, 68, 74, 73, 71, 69, 76, 72])
treatment = np.array([82, 85, 80, 88, 84, 86, 81, 83, 87, 85])

# Calculate means
control_mean = np.mean(control)
treatment_mean = np.mean(treatment)

# Hypothesis test
t_stat, p_value = ttest_ind(control, treatment)

print("Clinical Trial Analysis")
print("-----------------------")
print("Control Mean:", round(control_mean, 2))
print("Treatment Mean:", round(treatment_mean, 2))
print("T-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 6))

alpha = 0.05

if p_value < alpha:
    print("Result: Reject the Null Hypothesis")
    print("The treatment has a statistically significant effect.")
else:
    print("Result: Fail to Reject the Null Hypothesis")
    print("The treatment effect is not statistically significant.")

# Visualization
plt.boxplot(
    [control, treatment],
    labels=["Control", "Treatment"]
)
plt.ylabel("Treatment Outcome")
plt.title("Control vs Treatment Group")
plt.show()

# P-value visualization
plt.bar(["P-value", "Significance Level"], [p_value, alpha])
plt.ylabel("Value")
plt.title("P-value vs Significance Level")
plt.show()
