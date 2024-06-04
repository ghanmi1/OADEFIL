import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Rate constants (k) for red gram splits at different pH and temperatures
k_redgram = {
    4.5: [0.0030520972110602415, 0.005039374102028726, 0.006819297035216223, 
         0.010186841711395103, 0.012780020522184386, 0.022318532435006793, 
         0.035869097800339804],
    5.5: [0.0033105972671379274, 0.004973366967322911, 0.008625345126863183, 
         0.009818550314660474, 0.015322744289497923, 0.024240914928062733, 
         0.04540177501260745],
    6.5: [0.0036368538937002312, 0.005009430557419864, 0.008580397979481407, 
         0.01127220965076528, 0.017153300365533516, 0.027720265415081886, 
         0.04197795661832608]
}

# Rate constants (k) for pure solution at different pH and temperatures
k_pure_solution = {
    4.5: [0.004140805689573887, 0.005686332036459484, 0.0074844845293060005,
         0.009816815124220526, 0.01571179944742303, 0.024487960810648378, 
         0.04070427016954051],
    5.5: [0.004720285779367573, 0.005750060496710753, 0.008069250183014513, 
         0.012154303891993413, 0.016382787957166606, 0.025142044785042342, 
         0.044920942390759236],
    6.5: [0.0042574331054008345, 0.0049596879450099175, 0.00615283201620715, 
         0.013502860690331625, 0.019369200992839414, 0.03739910902827751, 
         0.07219377283083991]
}


# Temperatures in Celsius
temperatures_C = [50,60,70, 80,90,100, 120]

# Convert temperatures to Kelvin (1/T)
temperatures_K = np.array(temperatures_C) + 273.15

# Plot ln(k) versus 1/T for red gram splits and pure solution at different pH values
plt.figure(figsize=(10, 6))

# Plot red gram splits
for pH, k_values in k_redgram.items():
    ln_k_values = np.log(k_values)
    plt.plot(1 / temperatures_K, ln_k_values, marker='o', label=f'pH {pH} (Red Gram Splits)')

# Plot pure solution
for pH, k_values in k_pure_solution.items():
    ln_k_values = np.log(k_values)
    plt.plot(1 / temperatures_K, ln_k_values, marker='s', label=f'pH {pH} (Pure Solution)')

plt.xlabel('1/T (K^-1)')
plt.ylabel('ln(k)')
plt.title('ln(k) versus 1/T for Red Gram Splits and Pure Solution at Different pH')
plt.legend()
plt.grid(True)
plt.show()

# Iterate over different pH values
for pH, k_values_redgram in k_redgram.items():
    k_values_pure_solution = k_pure_solution[pH]
    
    # Calculate ln(k) and 1/T values for red gram splits
    ln_k_values_redgram = np.log(k_values_redgram)
    one_over_T_values = 1 / temperatures_K
    
    # Perform linear regression for red gram splits
    slope_redgram, intercept_redgram, r_value_redgram, p_value_redgram, std_err_redgram = linregress(one_over_T_values, ln_k_values_redgram)
    
    # Calculate ln(k) and 1/T values for pure solution
    ln_k_values_pure_solution = np.log(k_values_pure_solution)
    
    # Perform linear regression for pure solution
    slope_pure_solution, intercept_pure_solution, r_value_pure_solution, p_value_pure_solution, std_err_pure_solution = linregress(one_over_T_values, ln_k_values_pure_solution)
    
    # Print the equations of the lines for red gram splits
    print(f"For pH {pH} (Red Gram Splits):")
    print(f"    Equation of the line: ln(k) = {slope_redgram:.6f} / T + {intercept_redgram:.6f}")
    
    # Print the equations of the lines for pure solution
    print(f"For pH {pH} (Pure Solution):")
    print(f"    Equation of the line: ln(k) = {slope_pure_solution:.6f} / T + {intercept_pure_solution:.6f}")
    print()
