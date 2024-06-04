from scipy.optimize import minimize


coefficients_TI = [380.52, 1.41, 6.04, -16.26, 6.12, -1.08, -18.16, -13.71, 3.04]

coefficients_F = [150.07, 2.37, -0.39, -2.97, 3.87, 2.49, -2.27, -6.60, 1.45]

coefficients_G = [3.24, 0.37, -0.02, -0.15, 0.10, -0.30, -0.26, -0.01, 0.08]



def scale_to_real(x_bounded, lower_bound, upper_bound):
    return lower_bound + ((x_bounded + 1) * (upper_bound - lower_bound)) / 2

def Ti(params , coefficients_TI):
    T, L, W = params
    a, b1, b2, b3, b4, b5, b6, b7, c = coefficients_TI
    return a + b1*T + b2*L + b3*W + b4*T*L + b5*T*W + b6*L*W + b7*T*L*W + c

initial_guess = [0, 0, 0]  
bounds_real = [(25, 35), (0, 12), (80, 120)]  

bounds = ((-1,1), (-1, 1), (-1,1 ))

result = minimize(lambda x: -Ti(x , coefficients_TI), initial_guess, bounds=bounds)


optimal_values_real = [scale_to_real(result.x[i], bounds_real[i][0], bounds_real[i][1]) for i in range(len(result.x))]

print("Optimal values for thiamine (Temperature, Light, Water):", optimal_values_real)
print("Maximum value of the function thiamine:", -result.fun)


print("####################")
#print ("now we will maximize the equation of folate ")
print("####################")

def F(params , coefficients_F):
    T, L, W = params
    a, b1, b2, b3, b4, b5, b6, b7, c = coefficients_F
    return a + b1*T + b2*L + b3*W + b4*T*L + b5*T*W + b6*L*W + b7*T*L*W + c

initial_guess = [0, 0, 0]  
bounds_real = [(25, 35), (0, 12), (80, 120)]  

bounds = ((-1,1), (-1, 1), (-1,1 ))

result = minimize(lambda x: -F(x , coefficients_F), initial_guess, bounds=bounds)




optimal_values_real = [scale_to_real(result.x[i], bounds_real[i][0], bounds_real[i][1]) for i in range(len(result.x))]

print("Optimal values for folate  (Temperature, Light, Water):", optimal_values_real)
print("Maximum value of the function folate :", -result.fun)


print("####################")
#print ("now we will minimize the equation of alpha-galactoside ")
print("####################")


def g(params , coefficients_G):
    T, L, W = params
    a, b1, b2, b3, b4, b5, b6, b7, c = coefficients_G
    return a + b1*T + b2*L + b3*W + b4*T*L + b5*T*W + b6*L*W + b7*T*L*W + c



initial_guess = [0, 0, 0]  
bounds_real = [(25, 35), (0, 12), (80, 120)]  

bounds = ((-1,1), (-1, 1), (-1,1 ))

result = minimize(lambda x: g(x , coefficients_G), initial_guess, bounds=bounds)


optimal_values_real = [scale_to_real(result.x[i], bounds_real[i][0], bounds_real[i][1]) for i in range(len(result.x))]

print("Optimal values for alpha-galactoside (Temperature, Light, Water):", optimal_values_real)
print("Maximum value of the function alpha-galactoside:", result.fun)


print("####################")
#print("now let us see the combined objectives ")
print("####################")

def combined_objective(params, weights):
    T, L, W = params
    return weights[0] * Ti(params) + weights[1] * F(params) - weights[2] * g(params)


initial_guess = [0, 0, 0]  
bounds_real = [(25, 35), (0, 12), (80, 120)]  

bounds = ((-1,1), (-1, 1), (-1,1 ))

optimal_values_real = [scale_to_real(result.x[i], bounds_real[i][0], bounds_real[i][1]) for i in range(len(result.x))]


print("Optimal values for reach the objectif (T, L, W):", optimal_values_real , Ti(result.x , coefficients_TI) , F(result.x , coefficients_F) , g(result.x , coefficients_G))
