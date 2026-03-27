import numpy as np
height = [1.60, 1.65, 1.70, 1.75, 1.80]
np_height= np.array(height)
print(np_height)
weight =[53,67,75,81,70]
np_weight = np.array(weight)
print(np_weight)
BMI=np_weight/np_height**2
print(BMI)

py_list = [1,2,3,5]
numpy_arrays= np.array( [3,7,8,1])
sum = py_list + numpy_arrays
print(sum)
print(BMI[1])
print(BMI > 23)
print(BMI[BMI > 23])
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

