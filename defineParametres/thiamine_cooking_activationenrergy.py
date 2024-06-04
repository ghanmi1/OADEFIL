import numpy as np
from scipy.stats import linregress

# Function to calculate activation energy (Ea) and pre-exponential constant (A0)
def calculate_Ea_A0(pH_slope, pH_intercept, gas_constant):
    # Slope of ln(k) vs 1/T gives -Ea/R
    activation_energy = -pH_slope * gas_constant /1000
    # Intercept gives ln(A0)
    pre_exponential_constant = np.exp(pH_intercept)
    return activation_energy, pre_exponential_constant

# Given pH values and their corresponding slope and intercept data
pH_values = [4.5, 5.5, 6.5]
slope_data = {
    'Red Gram Splits': [-4466.881669, -4724.109313, -4636.154514],
    'Pure Solution': [-4272.760087, -4240.105305, -5551.316398]
}
intercept_data = {
    'Red Gram Splits': [8.054667, 8.892385, 8.700876],
    'Pure Solution': [7.634716, 7.627644, 11.428945]
}

# Gas constant (input your specific value)
gas_constant = 1.987  # Units: cal/(mol*K)

# Calculate activation energy (Ea) and pre-exponential constant (A0) for each pH value and solution type
for solution_type, slope_data_type in slope_data.items():
    print(f"For {solution_type}:")
    for pH, slope, intercept in zip(pH_values, slope_data_type, intercept_data[solution_type]):
        Ea, A0 = calculate_Ea_A0(slope, intercept, gas_constant)
        print(f"\tFor pH {pH}:")
        print(f"\t\tActivation energy (Ea): {Ea} kcal/mol")
        print(f"\t\tPre-exponential constant (A0): {A0}\n")
