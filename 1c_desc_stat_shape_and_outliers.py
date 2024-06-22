
# Import needed libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm# For creating a sample from the normal distributions
np.random.seed(42)                                                  

alpha_values = [0, 10, -10]# Parameter for symmetric, right skewed, and left skewed distributions
size = 1000
for alpha in alpha_values:
    sample_drawn = skewnorm.rvs(a=alpha, size = size)#Draws randomly from a skewed normal distribution
    plt.hist(sample_drawn, bins = 25, color = 'blue')
    plt.show()

# Outliers
# 5 Number summary is important to identify the outliers
# Box plot - to understand the central tendency, spread and skewness of the data
# Outliers - below lower fence (Q1 - 1.5*IQR), above upper fence (Q3 + 1.5*IQR)
plt.boxplot(sample_drawn)
plt.show()




