import numpy as np
x = np.linspace(10,20,5)  # Took numbers from 10 to 20, both included and made them equally divide into 5 elements
print(x)

print(np.linspace(10,20,5,endpoint= False))  # Excluding last el


print(np.logspace(1.0,2.0,num=10, base=2))  #For log