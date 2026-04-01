#import numpy as np
#a = np.array([1,2,3])
#print(a)
#from numpy import array
import numpy_test as np
fam=["alif",1.75,"samim",1.70,"abbu",1.68,"ammu",1.65,"dadi",1.50]
extra_fam=fam +["me",1.78]
print(str(len(extra_fam))+ "element in extra_fam")

# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))