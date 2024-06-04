import numpy as np 
import matplotlib.pyplot as plt 

def W(t,alpha,beta):
    return alpha*(1-beta**t)


temperatures = [20,50,85]

parametres = {
    20:(84.34,0.9874),
    50:(94.10,0.9739),
    85:(83.11,0.8947)
    }

plt.figure(figsize=(10,6))

for temp in temperatures:
    alpha,beta=parametres[temp]
    t=np.linspace(0, 200)
    plt.plot(t, W(t,alpha,beta), label=f'temperature {temp} °C')

plt.title('M vs Time for Different Temperatures boomer ')
plt.xlabel('Time(min)')
plt.ylabel('water uptake (g/100g)')
plt.legend()
plt.grid(True)
plt.show()