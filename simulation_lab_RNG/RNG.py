import math
import numpy as np
import matplotlib.pyplot as plt

z=[3]
u=[]

for i in range(1, 100):
    new_z = ((z[i-1]**2) + 2*z[i-1]+5) % 127
    new_u = new_z/127

    z.append(new_z)
    u.append(new_u)

print(z)
print(u)

temp = []
for i in range(1, 100):
    temp.append(str(i))
plt.bar(temp, z[1:])
plt.show()


number = 5.55

result = ((number/1)-(number//1))

print(result)