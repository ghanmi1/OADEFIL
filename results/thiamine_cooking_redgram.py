import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#### redgram spplits

# Define the function to calculate concentration at time t
def concentration(t, C0, k):
    return C0 * np.exp(-k * t)

# Define the time range
t_values = np.linspace(0,60)  # Adjust the time range as needed

# Define the initial concentration
C0 = 0.38  # Initial concentration, adjust as needed

# Define the rate constants (k values) for different pH and temperatures
rate_constants = {
    4.5: {50: 0.0030520972110602415, 60: 0.005039374102028726, 70: 0.006819297035216223, 
          80: 0.010186841711395103, 90: 0.012780020522184386, 100: 0.022318532435006793, 
          120: 0.035869097800339804},
    5.5: {50: 0.0033105972671379274, 60: 0.004973366967322911, 70: 0.008625345126863183, 
          80: 0.009818550314660474, 90: 0.015322744289497923, 100: 0.024240914928062733, 
          120: 0.04540177501260745},
    6.5: {50: 0.0036368538937002312, 60: 0.005009430557419864, 70: 0.008580397979481407, 
          80: 0.01127220965076528, 90: 0.017153300365533516, 100: 0.027720265415081886, 
          120: 0.04197795661832608}
}


# Plot concentration versus time for each pH and temperature
for ph, temp_k_values in rate_constants.items():
    plt.figure(figsize=(10, 8))
    i = 1  # Subplot index
    for temp, k in temp_k_values.items():
        Ct = concentration(t_values, C0, k)
        plt.subplot(3, 3, i)
        plt.plot(t_values, Ct, label=f'Temperature {temp}°C')
        
        half_concentration = C0 / 2
        half_life = fsolve(lambda t: concentration(t, C0, k) - half_concentration, 0)[0]
        plt.axvline(x=half_life, color='r', linestyle='--', label=f'Half-life: {half_life:.2f} min')
        
        plt.xlabel('Time (t)')
        plt.ylabel('Concentration (C)')
        plt.title(f'C vs. T at pH {ph}')
        plt.legend()
        plt.grid(True)
        i += 1
    plt.tight_layout()
    plt.show()

# Print half-life values for each pH and temperature
print("Half-life values:")
for ph, temp_k_values in rate_constants.items():
    for temp, k in temp_k_values.items():
        # Calculate the time to reach half of the initial concentration (half-life)
        half_concentration = C0 / 2
        half_life = fsolve(lambda t: concentration(t, C0, k) - half_concentration, 0)[0]
        print(f"pH {ph}, Temperature {temp}°C: Half-life = {half_life:.2f} min")
