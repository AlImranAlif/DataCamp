import numpy as np
height = [1.60, 1.65, 1.70, 1.75, 1.80]
weight =[53,67,75,81,70]
np_height= np.array(height)
np_weight = np.array(weight)
print(type(np_height))
print(type(np_weight))

np_2d =np.array ([
    [1,2,3,4,5,6],
    [7,8,9,0,11,21]
])
print(np_2d)
print(np_2d.shape)
print(np_2d[0])
print(np_2d[1][2])
print(np_2d[:,1:3])
print(np_2d[1,:])
print(np_2d[:,2:3])
