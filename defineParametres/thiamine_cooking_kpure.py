import numpy as np
import matplotlib.pyplot as plt


#pure solution

def calculate_rate_constant(t, Ct, C0):
    ln_ratio = -np.log(np.array(Ct) / C0)
    ln_ratio = ln_ratio[~np.isnan(ln_ratio)]
    t = t[:len(ln_ratio)]
    slope, intercept = np.polyfit(t, ln_ratio, 1)
    return slope

def plot_degradation(t_values, ln_ratio_values, temperatures, ph_value):
    plt.figure()
    for i in range(len(temperatures)):
        plt.plot(t_values[i], ln_ratio_values[i], 'o-', label=f'Temperature {temperatures[i]}°C')
    plt.xlabel('Time (min)')
    plt.ylabel('Ln([C]t/[C]0)')
    plt.title(f'First-Order Degradation Kinetics pure solution (pH {ph_value})')
    plt.grid(True)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

t_values = [
    [5, 10, 15, 20, 30, 40, 50, 60],  
    [5, 10, 15, 20, 30, 40, 50, 60], 
    [5, 10, 15, 20, 30, 40, 50, 60],
    [5, 10, 15, 20, 30, 40, 50, 60],
    [5, 10, 15, 20, 30, 40, 50, 60],
    [5, 10, 15, 20, 30, 40, 50, 60],
    [5, 10, 15, 20, 30, 40, 50, 60],
]

temperatures = [50,60,70, 80,90,100, 120]  

C0_values = 0.38 

ph_data = {
    4.5: {'Ct_values': [
        [np.nan, 0.380, np.nan, 0.372, 0.365, 0.354, 0.340, 0.330],  
        [np.nan, 0.380, np.nan, 0.370, 0.352, 0.348, 0.330, 0.310], 
        [np.nan, 0.365, np.nan, 0.352, 0.328, 0.310, 0.298, 0.281],
        [np.nan, 0.342, np.nan, 0.326, 0.304, 0.282, 0.260, 0.245],
        [np.nan, 0.340, np.nan, 0.32, 0.292, 0.270, 0.230, 0.198],
        [np.nan, 0.310, np.nan, 0.282, 0.220, 0.191, 0.161, 0.133],
        [0.291, 0.229, 0.180, 0.160, np.nan, np.nan, np.nan, np.nan]
    ]},
    5.5: {'Ct_values': [
        [np.nan, 0.380, np.nan, 0.370, 0.360, 0.355, 0.340, 0.320],  
        [np.nan, 0.370, np.nan, 0.365, 0.360, 0.340, 0.325, 0.305], 
        [np.nan, 0.355, np.nan, 0.341, 0.318, 0.290, 0.281, 0.270],
        [np.nan, 0.340, np.nan, 0.321, 0.290, 0.271, 0.252, 0.220],
        [np.nan, 0.330, np.nan, 0.300, 0.272, 0.260, 0.213, 0.186],
        [np.nan, 0.308, np.nan, 0.271, 0.230, 0.205, 0.160, 0.128],
        [0.281, 0.230, 0.170, 0.147, np.nan, np.nan, np.nan, np.nan]
    ]},
    6.5: {'Ct_values': [
        [np.nan, 0.374, np.nan, 0.369, 0.360, 0.350, 0.338, 0.323],  
        [np.nan, 0.358, np.nan, 0.346, 0.340, 0.327, 0.315, 0.300],
        [np.nan, 0.350, np.nan, 0.341, 0.330, 0.310, 0.296, 0.285], 
        [np.nan, 0.340, np.nan, 0.319, 0.304, 0.270, 0.235, 0.217], 
        [np.nan, 0.330, np.nan, 0.304, 0.278, 0.239, 0.210, 0.167], 
        [np.nan, 0.300, np.nan, 0.264, 0.209, 0.149, 0.129, 0.080], 
        [0.310, 0.240, 0.172, 0.104, np.nan, np.nan, np.nan, np.nan]
    ]}
}

for ph, data in ph_data.items():
    Ct_values = data['Ct_values']
    ln_ratio_values = []
    for i in range(len(temperatures)):
        t = t_values[i]  # Using t_values[i] directly
        Ct = Ct_values[i]
        k = calculate_rate_constant(t, Ct, C0_values)
        ln_ratio = np.log(np.array(Ct) / C0_values)
        ln_ratio_values.append(ln_ratio)
        print(f"Rate constant (k) at pH {ph}, {temperatures[i]}°C: {k}")
    plot_degradation(t_values, ln_ratio_values, temperatures, ph)
