import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#### pure solution 

# Define the function to calculate concentration at time t
def concentration(t, C0, k):
    return C0 * np.exp(-k * t)

# Define the time range
t_values = np.linspace(0,60)  # Adjust the time range as needed

# Define the initial concentration
C0 = 1.0  # Initial concentration, adjust as needed

# Define the rate constants (k values) for different pH and temperatures
rate_constants = {
    4.5: {50: 0.004140805689573887, 60: 0.005686332036459484, 70: 0.0074844845293060005,
          80: 0.009816815124220526, 90: 0.01571179944742303, 100: 0.024487960810648378,
          120: 0.04070427016954051},
    5.5: {50: 0.004720285779367573, 60: 0.005750060496710753, 70: 0.008069250183014513,
          80: 0.012154303891993413, 90: 0.016382787957166606, 100: 0.025142044785042342,
          120: 0.044920942390759236},
    6.5: {50: 0.0042574331054008345, 60: 0.0049596879450099175, 70: 0.00615283201620715,
          80: 0.013502860690331625, 90: 0.019369200992839414, 100: 0.03739910902827751,
          120: 0.07219377283083991}
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
