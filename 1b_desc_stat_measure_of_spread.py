# Descriptive statistics
import numpy as np
import statistics
import matplotlib.pyplot as plt
import random

# Generate population date
population_data = np.array(list(range(1000)))# Usually unknown
# sample_data = np.random.choice(population_data, size = 50, replace=True)
sample_data = [15, 36, 39, 42, 48, 54, 57, 63, 72, 85, 89, 90, 91, 94, 99]

# Dispersion
# Range
range_of_sample = max(sample_data) - min(sample_data)
print(f"Range is {range_of_sample}")

# Inter quartile range-1
def calculate_median(input_data):
    length_of_input_data = len(input_data)
    if length_of_input_data % 2 == 0:
        return (input_data[length_of_input_data // 2 - 1] + input_data[length_of_input_data // 2]) / 2
    else:
        return input_data[length_of_input_data // 2]
def calculate_iqr(input_data):
    input_data.sort()
    length_of_input_data = len(input_data)
    if length_of_input_data % 2 == 0:
        q1 = calculate_median(input_data[:length_of_input_data // 2])
        q3 = calculate_median(input_data[length_of_input_data // 2:])
    else:
        q1 = calculate_median(input_data[:length_of_input_data // 2])
        q3 = calculate_median(input_data[length_of_input_data // 2 + 1:])
    return q3 - q1

print(calculate_iqr(sample_data))

# Inter quartile range-2
q1 = calculate_median(sample_data[:len(sample_data)//2])# Median of the first half of the ordered data
q3 = calculate_median(sample_data[len(sample_data)//2 +1 :])# MEdian of the second half of the ordered data
iqr = q3 - q1
print(f"IQR is: {iqr}")

# Variance and standard deviation
var_sample = np.var(sample_data)
std_sample= np.std(sample_data)
print(f"Variance of the sample data :{round(var_sample, 3)}, Std. deviation of the sample data : {round(std_sample, 3)}")