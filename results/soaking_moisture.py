import numpy as np
import matplotlib.pyplot as plt

def moisture(t, A, k, MS, M0):
    return A * np.exp(k * t) * (MS - M0) + M0

M0 = 0.142  

'''
does give a bizare results 
 infinite series diffusion equation
 we can also program the same equation like this (we have all the value ):
     MR= 1-6/pi^2 exp(-De*pi^2*t/R^2) 
'''
temperatures = [25, 32.5, 40, 55, 70, 85]


parameters = {
    25: (0.996, 0.019 ),  
    32.5: (0.978, 0.023 ),
    40: (0.963, 0.032 ),
    55: (0.961, 0.048 ),
    70: (0.982, 0.087 ),
    85: (0.981, 0.092 )
}


plt.figure(figsize=(10, 6))

for temp in temperatures:
    MS = 1.281 - 0.001 * temp  
    A, k = parameters[temp]
    t = np.linspace(0, 200)  
    plt.plot(t, moisture(t/60, A, k, MS, M0), label=f'Temperature {temp} °C')

plt.title('Moisture Content vs Time for Different Temperatures')
plt.xlabel('Time (min)')
plt.ylabel('Moisture Content')
plt.legend()
plt.grid(True)
plt.show()
