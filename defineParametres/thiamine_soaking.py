import numpy as np

# Initial concentration and final concentration at t=9
C0 = 0.433
C9_citric_acid = 0.409
C9_water = 0.406
C9_sodium_bicarbonate = 0.389

# Time in hours
t = 9

# Calculate the rate constant for each soaking method
k_citric_acid = -np.log(C9_citric_acid / C0) / t
k_water = -np.log(C9_water / C0) / t
k_sodium_bicarbonate = -np.log(C9_sodium_bicarbonate / C0) / t

print("Rate constant k for citric acid soaking:", k_citric_acid)
print("Rate constant k for water soaking:", k_water)
print("Rate constant k for sodium bicarbonate soaking:", k_sodium_bicarbonate)
