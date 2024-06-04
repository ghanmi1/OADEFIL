import numpy as np
import matplotlib.pyplot as plt


#### redgram splits 

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
    plt.title(f'First-Order Degradation Kinetics redgram splits (pH {ph_value})')
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
        [np.nan, 0.380, np.nan, 0.380, 0.370, 0.360, 0.353, 0.344],  
        [np.nan, 0.380, np.nan, 0.375, 0.370, 0.353, 0.340, 0.320],  
        [np.nan, 0.368, np.nan, 0.350, 0.330, 0.312, 0.301, 0.289],
        [np.nan, 0.357, np.nan, 0.332, 0.316, 0.291, 0.279, 0.245],
        [np.nan, 0.342, np.nan, 0.320, 0.293, 0.275, 0.246, 0.218],
        [np.nan, 0.321, np.nan, 0.299, 0.240, 0.216, 0.180, 0.149],
        [0.3, 0.256, 0.230, 0.171, np.nan, np.nan, np.nan, np.nan]
    ]},
    5.5: {'Ct_values': [
        [np.nan, 0.380, np.nan, 0.365, 0.360, 0.355, 0.345, 0.335],  
        [np.nan, 0.370, np.nan, 0.365, 0.354, 0.341, 0.329, 0.312],  
        [np.nan, 0.367, np.nan, 0.348, 0.328, 0.301, 0.292, 0.270],
        [np.nan, 0.350, np.nan, 0.328, 0.300, 0.284, 0.269, 0.245],
        [np.nan, 0.340, np.nan, 0.315, 0.281, 0.270, 0.225, 0.200],
        [np.nan, 0.325, np.nan, 0.300, 0.270, 0.225, 0.175, 0.145],
        [0.287, 0.246, 0.178, 0.150, np.nan, np.nan, np.nan, np.nan],
    ]},
    6.5: {'Ct_values': [
        [np.nan, 0.380, np.nan, 0.379, 0.368, 0.354, 0.342, 0.340],  
        [np.nan, 0.380, np.nan, 0.361, 0.345, 0.340, 0.327, 0.315],  
        [np.nan, 0.354, np.nan, 0.327, 0.302, 0.290, 0.270, 0.260],
        [np.nan, 0.342, np.nan, 0.298, 0.257, 0.241, 0.231, 0.224],
        [np.nan, 0.329, np.nan, 0.264, 0.222, 0.198, 0.189, 0.170],
        [np.nan, 0.299, np.nan, 0.235, 0.169, 0.149, 0.126, 0.109],
        [0.257, 0.194, 0.157, 0.137, np.nan, np.nan, np.nan, np.nan],
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
