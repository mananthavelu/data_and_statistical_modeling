import numpy as np
import pandas as pd

# Sample data
file_path = r"C:\Users\32470\Desktop\data"
file_name = file_path + "\\" + "house_prices.csv"
data = pd.read_csv(file_name)

# Dependent variable
input_variable = data['area']
# Independent variable
output_variable = data['price']

# Variance of area
variance = np.var(input_variable)
def calculate_variance(input_values):
    length = len(input_values)
    mean_of_input = np.mean(input_values)
    sum_of_squares = sum([(x-mean_of_input)**2 for x in input_values])
    return sum_of_squares/length

variance_by_calc_input = calculate_variance(input_variable)
variance_by_calc_output = calculate_variance(output_variable)

import matplotlib.pyplot as plt
plt.hist(input_variable, label = "Area", alpha = 0.6)
plt.show()

plt.hist(output_variable, label = "Price", alpha = 0.6)
plt.legend()
plt.show()

# Covariance
covariance = np.cov(input_variable, output_variable)

def calculate_covariance(input_variable, output_variable):
    length = len(input_variable)
    mean_of_input = np.mean(input_variable)
    mean_of_output = np.mean(output_variable)
    covariance = sum([(input_variable[i]-mean_of_input)*(output_variable[i]-mean_of_output) for i in range(length)])/length
    return covariance

covariance_by_calc = calculate_covariance(input_variable, output_variable)

correlation_coeff_built_in = np.corrcoef(input_variable, output_variable)
correlation_coeff = covariance_by_calc/np.sqrt(variance_by_calc_input *variance_by_calc_output)
