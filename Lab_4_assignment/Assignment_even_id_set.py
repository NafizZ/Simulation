import math
import matplotlib.pyplot as plt

x_A = [10]
y_A = [0]
v_A = 3

x_B = [0]
y_B = [10]
v_B = 5

x_C = [10]
y_C = [10]
v_C = 7

x_D = [0]
y_D = [0]
v_D = 2

dist_DC = []
dist_CB = []
dist_BA = []

# time variable t
for t in range(20):
    print("At time =", t)

    print("x_A =", x_A[t], " y_A =", y_A[t], "\n",
          "x_B =", x_B[t], "y_B =", y_B[t], "\n",
          "x_C =", x_C[t], "y_C =", y_C[t], "\n",
          "x_D =", x_D[t], "y_D =", y_D[t], "\n")

    dist_DC.append(math.sqrt(((x_D[t] - x_C[t]) ** 2) + ((y_D[t] - y_C[t]) ** 2)))
    dist_CB.append(math.sqrt(((x_C[t] - x_B[t]) ** 2) + ((y_C[t] - y_B[t]) ** 2)))
    dist_BA.append(math.sqrt(((x_B[t] - x_A[t]) ** 2) + ((y_B[t] - y_A[t]) ** 2)))

    print("D to C Distance =", dist_DC[t], "\n"
          "C to B Distance =", dist_CB[t], "\n"
          "B to A Distance =", dist_BA[t], "\n")

    if dist_DC[t] < 5:
        print("Car C shoots Car D at time =", t, "\n")
    if dist_CB[t] < 5:
        print("Car B shoots Car C at time =", t, "\n")
    if dist_BA[t] < 5:
        print("Car A shoots Car B at time =", t, "\n")


    y_dNew = y_D[t] + v_D
    x_D.append(0)
    y_D.append(y_dNew)

    sin = (y_D[t] - y_C[t]) / dist_DC[t]
    cos = (x_D[t] - x_C[t]) / dist_DC[t]
    x_cNew = x_C[t] + v_C * cos
    y_cNew = y_C[t] + v_C * sin
    x_C.append(x_cNew)
    y_C.append(y_cNew)

    sin = (y_C[t] - y_B[t]) / dist_CB[t]
    cos = (x_C[t] - x_B[t]) / dist_CB[t]
    x_bNew = x_B[t] + v_B * cos
    y_bNew = y_B[t] + v_B * sin
    x_B.append(x_bNew)
    y_B.append(y_bNew)

    sin = (y_B[t] - y_A[t]) / dist_BA[t]
    cos = (x_B[t] - x_A[t]) / dist_BA[t]
    x_aNew = x_A[t] + v_A * cos
    y_aNew = y_A[t] + v_A * sin
    x_A.append(x_aNew)
    y_A.append(y_aNew)


# multiline plot
# plotting the points
plt.plot(x_A, y_A, label="A")
plt.plot(x_B, y_B, label="B")
plt.plot(x_C, y_C, label="C")
plt.plot(x_D, y_D, label="D")
# naming the x axis
plt.xlabel('x axis')
# naming the y axis
plt.ylabel('y axis')
plt.legend()
plt.show()

# scatter plot
plt.scatter(x_A, y_A, label="A")
plt.scatter(x_B, y_B, label="B")
plt.scatter(x_C, y_C, label="A")
plt.scatter(x_D, y_D, label="B")
plt.legend()
plt.show()



