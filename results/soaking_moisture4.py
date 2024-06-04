import numpy as np 
import matplotlib.pyplot as plt 


'''
sigmoidal model
 describe a sigmoidal behaviour with an initial lag phase followed by a high absorption
rate phase and, finally, by a stationary phase
'''
def M(t,Meq,K3,tho):
    return Meq/(1+np.exp(-K3*(t-tho)))

temperatures = [25, 32.5, 40, 55, 70, 85]

parametres = {
    25 : (1.911,0.494),
    32.5 :(2.385,0.405),
    40:(3.011,0.335),
    55:(4.933,0.233),
    70:(8.549,0.142),
    85:(13.387,0.102),
    }


plt.figure(figsize=(10,6))

for temp in temperatures:
    Meq=1.281 - 0.001 * temp 
    K3,tho = parametres[temp]
    t=np.linspace(0, 200)
    plt.plot(t,M(t,Meq,K3/60,tho) , label=f'temperature {temp} °C')
    

plt.title('M vs Time for Different Temperatures(sigmoidal model)')
plt.xlabel('Time(min)')
plt.ylabel('M')
plt.legend()
plt.grid(True)
plt.show()