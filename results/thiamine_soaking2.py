import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def thiamine_decay(t, C0, k):
    return C0 * np.exp(-k * t)

def calculate_final_concentration(initial_concentration, k):
    time_hours = np.linspace(0, 9, 100)  # Time in hours
    final_concentration = thiamine_decay(time_hours, initial_concentration, k)
    return final_concentration, time_hours

def thiamine_concentration_at_time(t, C0, k):
    return C0 * np.exp(-k * t)

# Rate constants for each soaking method (replace with your obtained values)
k_citric_acid = 0.006335841328854233
k_water = 0.007153840933417455
k_sodium_bicarbonate = 0.011906487153782619

# Initial concentration
initial_concentration = 0.433

# Calculate final concentration for each soaking method
final_concentration_citric_acid, time_hours = calculate_final_concentration(initial_concentration, k_citric_acid)
final_concentration_water, _ = calculate_final_concentration(initial_concentration, k_water)
final_concentration_sodium_bicarbonate, _ = calculate_final_concentration(initial_concentration, k_sodium_bicarbonate)

# Plot concentration over time for each soaking method
plt.plot(time_hours, final_concentration_citric_acid, label='Citric Acid Soaking')
plt.plot(time_hours, final_concentration_water, label='Water Soaking')
plt.plot(time_hours, final_concentration_sodium_bicarbonate, label='Sodium Bicarbonate Soaking')

plt.title('Thiamine Concentration Over Time')
plt.xlabel('Time (hours)')
plt.ylabel('Thiamine Concentration')
plt.legend()
plt.grid(True)

plt.yscale('log')

# Define different time values and rate constants
time_values = [2, 4, 6 , 9]  # Time values in hours
rate_constants = [k_citric_acid, k_water, k_sodium_bicarbonate]  # Rate constants for different soaking methods

# Calculate and print thiamine concentrations at different times and for different rate constants
for t in time_values:
    for k in rate_constants:
        concentration_at_t = thiamine_concentration_at_time(t, initial_concentration, k)
        print(f"At time {t} hours and rate constant {k}: Thiamine concentration = {concentration_at_t}")


plt.legend()

plt.show()
