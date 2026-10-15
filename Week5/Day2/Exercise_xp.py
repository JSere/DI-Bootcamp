import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# --- Exercise 1: Basic Usage of SciPy ---
print("SciPy Version:", scipy.__version__)

# --- Exercise 2: Descriptive Statistics ---
data = [12, 15, 13, 12, 18, 20, 22, 21]
mean_val = np.mean(data)
median_val = np.median(data)
variance_val = np.var(data, ddof=1) # Sample variance
std_val = np.std(data, ddof=1)    # Sample standard deviation
print(f"Mean: {mean_val}, Median: {median_val}, Variance: {variance_val:.2f}, Std: {std_val:.2f}")

# --- Exercise 3: Understanding Distributions ---
mu, sigma = 50, 10
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.title("Normal Distribution (Mean=50, Std=10)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

# --- Exercise 4: T-Test Application ---
data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)
t_stat, p_value = stats.ttest_ind(data1, data2)
print(f"T-test -> T-statistic: {t_stat:.4f}, P-value: {p_value:.4e}")

# --- Exercise 5: Linear Regression Analysis ---
house_sizes = [50, 70, 80, 100, 120]
house_prices = [150000, 200000, 210000, 250000, 280000]

slope, intercept, r_value, p_val, std_err = stats.linregress(house_sizes, house_prices)
print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}")

# Predict price for 90 sqm
pred_90 = slope * 90 + intercept
print(f"Predicted price for 90 sqm: ${pred_90:,.2f}")
# Interpretation of slope: For every additional square meter, the house price increases by approximately $1,828.77.

# --- Exercise 6: Understanding ANOVA ---
fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]

f_val, p_val_anova = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)
print(f"ANOVA -> F-value: {f_val:.4f}, P-value: {p_val_anova:.6f}")
# Since p < 0.05, fertilizers have significantly different effects on plant growth.
# If p > 0.05, we would fail to reject the null hypothesis, meaning there is no statistically significant difference between group means.

# --- Exercise 7: Probability Distributions (Binomial) ---
# Probability of exactly 5 heads in 10 coin flips (p = 0.5)
binom_prob = stats.binom.pmf(5, 10, 0.5)
print(f"Probability of 5 heads in 10 flips: {binom_prob:.4f}")

# --- Exercise 8: Correlation Coefficients ---
age = [23, 25, 30, 35, 40]
income = [35000, 40000, 50000, 60000, 70000]

pearson_corr, _ = stats.pearsonr(age, income)
spearman_corr, _ = stats.spearmanr(age, income)
print(f"Pearson Correlation: {pearson_corr:.4f}")
print(f"Spearman Correlation: {spearman_corr:.4f}")