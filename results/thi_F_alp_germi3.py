from scipy.optimize import minimize


def Ti(params):
    T, L, W = params
    return 380.52 + 1.41*T + 6.04*L - 16.26*W + 6.12*T*L - 1.08*T*W - 18.16*L*W - 13.71*T*L*W + 3.04


initial_guess = [0, 0, 0]

 
bounds = ((-1,1), (-1, 1), (-1,1 ))

result = minimize(lambda x: -Ti(x), initial_guess, bounds=bounds )


print ("now we will maximize the equation of thiamine ")
print("Optimal values (Temperature, Light, Water):", result.x)
print("Maximum value of the function:", -result.fun)

print ("now we will maximize the equation of folate ")


def F(params):
    T, L, W = params
    return 150.07 + 2.37*T -0.39*L - 2.97*W + 3.87*T*L +2.49*T*W -2.27*L*W - 6.60*T*L*W + 1.45


initial_guess = [0,0 ,0]


bounds = ((-1,1), (-1, 1), (-1,1 ))


result = minimize(lambda x: -F(x), initial_guess, bounds=bounds )


print("Optimal values (Temperature, Light, Water):", result.x)
print("Maximum value of the function:", -result.fun)


print ("now we will minimize the equation of alpha-galactoside ")


def g(params):
    T, L, W = params
    return 3.24 + 0.37*T -0.02*L - 0.15*W + 0.10*T*L -0.30*T*W -0.26*L*W - 0.01*T*L*W + 0.08



initial_guess = [0, 0, 0]


bounds = ((-1,1), (-1, 1), (-1,1 ))


result = minimize(lambda x: g(x), initial_guess, bounds=bounds )


print("Optimal values (Temperature, Light, Water):", result.x)
print("Minimum value of the function:", result.fun)



print("now let us see the combined objectives ")


def combined_objective(params, weights):
    T, L, W = params
    return weights[0] * Ti(params) + weights[1] * F(params) - weights[2] * g(params)


initial_guess = [0, 0, 0]
bounds = ((-1, 1), (-1, 1), (-1,1))  


weights = [1, 1, 1] 

result = minimize(combined_objective, initial_guess, args=(weights,) , bounds=bounds)


optimal_values = result.x


print("Optimal values (T, L, W):", optimal_values , Ti(result.x) , F(result.x) , g(result.x))



































