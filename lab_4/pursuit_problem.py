import math
import matplotlib.pyplot as plt

x_T = [100, 110, 120, 129, 140, 149, 158, 168, 179, 188, 198, 209, 219, 226, 234, 240]
y_T = [0, 3, 6, 10, 15, 20, 26, 32, 37, 34, 30, 27, 23, 19, 16, 14]
x_D = [0]
y_D = [60]
v_D = 20
dist_TD = []
for t in range(13):
    print("time t = ", t)
    dist_TD.append(math.sqrt(((x_T[t] - x_D[t]) ** 2) + ((y_T[t] - y_D[t]) ** 2)))  #distance calculation at time t
    sin = (y_T[t] - y_D[t]) / dist_TD[t]
    cos = (x_T[t] - x_D[t]) / dist_TD[t]
    x_dNew = x_D[t] + v_D * cos
    y_dNew = y_D[t] + v_D * sin
    x_D.append(x_dNew)
    y_D.append(y_dNew)
    #dist_update =
    print(dist_TD[t])
    if dist_TD[t] <10:
        print("Booom!!")
        break


# multiline plot
# plotting the points
plt.plot(x_T, y_T, label="Target")
plt.plot(x_D, y_D, label="Defender")
# naming the x axis
plt.xlabel('x axis')
# naming the y axis
plt.ylabel('y axis')
plt.legend()
plt.show()

# scatter plot
plt.scatter(x_T, y_T, label="Target")
plt.scatter(x_D, y_D, label="Defender")
plt.legend()
plt.show()