import numpy as np
import matplotlib.pyplot as plt

def gab_isotherm(a_w, C, K, M0):
    denominator = (1 - K * a_w) * (1 - K * a_w + C * K * a_w)
    m = C * K * M0 * a_w / denominator
    return m


a_w_values = np.linspace(0.20, 0.85, 100)  # Water activity values

# Define parameters for each case: (C, K, M0)
parameters = {
    'Raw Lentil Flour': (155.37, 0.89, 5.17),
    'Germination 2 days': (11.92, 0.86, 6.53),
    'Germination 4 days': (86.04, 0.85, 7.81),
    'Germination 6 days': (141.96, 0.90, 6.32)
}



plt.figure(figsize=(10, 6))

for case, (C, K, M0) in parameters.items():
    moisture_contents = gab_isotherm(a_w_values, C, K, M0)
    print(moisture_contents)
    plt.plot(a_w_values, moisture_contents, label=case)

plt.xlabel('Water Activity (a_w)')
plt.ylabel('Moisture Content (g/100 solid' )
plt.title('GAB Isotherm Model')
plt.legend()
plt.grid(True)
plt.show()
