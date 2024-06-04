import numpy as np 
import matplotlib.pyplot as plt 

'''
Weibull model
'''

def M(t,MS,M0, alpha, beta):
    exp_term = -t / beta
    return MS - np.exp(exp_term)**alpha * (MS - M0)

temperatures = [25, 32.5, 40, 55, 70, 85]

M0 = 0.142

parameters = {
    25 : (1.629, 0.886),
    32.5 :(1.661, 0.590),
    40:(1.994, 0.394),
    55:(2.393, 0.281),
    70:(2.871, 0.187),
    85:(3.445, 0.125),
}

plt.figure(figsize=(10, 6))

for temp in temperatures:
    MS = 1.281 - 0.001 * temp
    alpha, beta = parameters[temp]
    t = np.linspace(0, 200)
    plt.plot(t, M(t, MS,M0,alpha, beta*60), label=f'Temperature {temp} °C')

plt.title('M vs Time for Different Temperatures(Weibull model)')
plt.xlabel('Time')
plt.ylabel('M')
plt.legend()
plt.grid(True)
plt.show()
