# Descriptive statistics
import numpy as np
import statistics
import matplotlib.pyplot as plt

# Generate population date
population_data = np.array(list(range(1000)))# Usually unknown

# sample_data = np.random.choice(population_data, size = 50, replace=True)
sample_data = [15, 36, 39, 42, 48, 54, 57, 63, 72, 85, 89, 90, 91, 94, 99]

# Central tendency/ Measure of central value

# Sample mean
sample_mean = np.mean(sample_data)

def calculate_mean(input_data):
    "returns the mean of the input data"
    return sum(input_data)/len(input_data)

print(f"The mean using built-in function: {round(sample_mean, 2)}")
print(f"The mean using function: {round(calculate_mean(sample_data), 2)}")

# Sample median
sample_median = np.median(sample_data)

# Median calculation using the function
def calculate_median(input_data):
    "returns the median of the input data"
    input_data.sort()
    length_of_input_data = len(input_data)
    if len(input_data) % 2 == 0:
        return (input_data[length_of_input_data//2] + input_data[length_of_input_data//2 + 1])
    else:
        return input_data[len(input_data)//2]

print(f"The median using built-in function: {round(sample_median)}")
print(f"The median using function: {round(calculate_median(sample_data))}")

print("Successful" if calculate_median([1,2,3,4,5,6,7]) == 4 else "Error")
print("Successful" if calculate_median([10,28,38,4,95,6,57]) == 28 else "Error")

# Sample mode
sample_mode = statistics.mode(sample_data)

from collections import defaultdict
def calc_freq(input_data):
    "returns the mode of the input data"
    freq_values = defaultdict(int)
    for value in input_data:
        freq_values[value] += 1
    return freq_values

mode_using_function = max(calc_freq(sample_data), key = calc_freq(sample_data).get)
print(f"The mode using built-in function: {sample_mode}")
print(f"The mode using function: {mode_using_function}")

# Plot the sample data
plt.hist(sample_data, alpha = 0.6, label='Sample mean',bins=10)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()