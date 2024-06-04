import numpy as np 
import matplotlib.pyplot as plt 

def M(t,MS,M0,k):
    return MS-np.exp(-k*t)*(MS-M0)

'''
exponotiel model 
'''
M0 = 0.142
temperatures = [25, 32.5, 40, 55, 70, 85]

parametres = {
    25 : 1.41,
    32.5 : 1.421,
    40:1.797,
    55:2.665,
    70:4.836,
    85:5.612,
    }

plt.figure(figsize=(10,6))

for temp in temperatures:
    MS = 1.281 - 0.001 * temp
    k=parametres[temp]
    t=np.linspace(0, 200)
    plt.plot(t, M(t,MS,M0,k/60) , label=f'temperature {temp} °C')

plt.title('M vs Time for Different Temperatures(exponotiel model)')
plt.xlabel('Time(min)')
plt.ylabel('M')
plt.legend()
plt.grid(True)
plt.show()