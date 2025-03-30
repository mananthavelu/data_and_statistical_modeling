# Import needed libraries
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

population_data = np.array(list(range(1000)))# Usually unknown
# sample_data = np.random.choice(population_data, size = 50, replace=True)

sample_data = np.array([1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0])# Unknown population data

print(f"The population mean is: {round(np.mean(sample_data), 2)} ")

# Sample once with replacement
sample = np.random.choice(sample_data, size = 5, replace=True)
print(f'The sample mean is: {round(np.mean(sample),2)}')
# They are not closer to each other given that the sample is small part of the population data

# Sampling distribution
mean_size_5 = []
sample_size = 5
for _ in range(10000):
    sample_draw = np.random.choice(sample_data, size = sample_size)
    mean_size_5.append(np.mean(sample_draw))

plt.hist(mean_size_5, alpha = 0.6, label = 'Sample size 5', bins = 10)
plt.show(block=False)

# Mean of the population vs mean of the sampling distribution
mean_of_population = np.mean(sample_data)
mean_of_sampling_distribution = np.mean(mean_size_5)
print(f"mean of the population: {mean_of_population},\nmean of the sampling distribution: {mean_of_sampling_distribution}")
# In this case however, we can infer that the mean of the sampling distribution obtained is closer to the population mean

# Variance and standard deviation of the population vs sampling distribution
mean_5 = np.mean(mean_size_5)
var_5 = np.var(mean_size_5)
std_5 = np.std(mean_size_5)

var_population = np.var(sample_data)
std_population = np.std(sample_data)
comparable_var = (mean_of_population*(1-mean_of_population))/sample_size
print(f"Variance of population:{comparable_var},\nVariance of sampling distribution: {var_5}\n")

