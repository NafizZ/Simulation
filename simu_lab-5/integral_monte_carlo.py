# Name: Shah Nafiz Monjoor
# ID:   011 163 096
import matplotlib.pyplot as plt
import random
random.seed(0)
import math

n = [500, 1000, 5000, 10000]       # trails

a = 0
b = 5

error_list = []

for i in n:

    f_sum = 0
    f_square_sum = 0

    for j in range(i):
        x = random.uniform(a, b)
        func_value = ((x**2) * (math.exp(-x)))

        f_sum = f_sum + func_value
        f_square_sum = f_square_sum + func_value ** 2

    f_avg = f_sum / i
    f_square_avg = f_square_sum / i

    integral_value = (b - a) * f_avg
    error = ((b - a) / math.sqrt(int(i))) * math.sqrt(f_square_avg - (f_avg ** 2))
    error_list.append(error)

    print("trials: ", i)
    print("integral value: ", integral_value)
    print("error: ", error, "\n")

n =['500','1000','5000','10000']
plt.bar(n, error_list)
plt.xlabel('Trials')
plt.ylabel('Error')
plt.title('Error Bar chart')
plt.show()
