import numpy as np
import matplotlib.pyplot as plt

# Histogram - frequency
# Probability Density Curve - shows the likelyhood of different outcomes
mu = 0
sigma = 1
sample_from_normal = np.random.normal(mu, sigma, 1000)

mu = sample_from_normal.mean()
sigma = sample_from_normal.std()
x = np.linspace(sample_from_normal.min(), sample_from_normal.max(), 100)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)# Probability density function

plt.plot(x, pdf, color='red')
plt.show()