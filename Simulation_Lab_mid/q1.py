import math

x_A = [10]
y_A = [0]
v_A = 3

x_B = [0]
y_B = [-10]
v_B = 5

x_C = [10]
y_C = [10]
v_C = 7

x_D = [0]
y_D = [0]
v_D = 4

dist_BC = []
dist_DB = []
dist_AD = []

A_got_shoot = 0
B_got_shoot = 0
C_got_shoot = 0
D_got_shoot = 0


# time variable t
for t in range(10):
    print("At time =", t)

    print("x_A =", x_A[t], " y_A =", y_A[t], "\n",
          "x_B =", x_B[t], "y_B =", y_B[t], "\n",
          "x_C =", x_C[t], "y_C =", y_C[t], "\n",
          "x_D =", x_D[t], "y_D =", y_D[t], "\n")

    dist_BC.append(math.sqrt(((x_B[t] - x_C[t]) ** 2) + ((y_B[t] - y_C[t]) ** 2)))
    dist_DB.append(math.sqrt(((x_D[t] - x_B[t]) ** 2) + ((y_D[t] - y_B[t]) ** 2)))
    dist_AD.append(math.sqrt(((x_A[t] - x_D[t]) ** 2) + ((y_A[t] - y_D[t]) ** 2)))

    print("C to B Distance =", dist_BC[t], "\n"
          "B to D Distance =", dist_DB[t], "\n"
          "D to A Distance =", dist_AD[t], "\n")

    if dist_BC[t] < 5:
        print("Car C shoots Car B at time =", t, "\n")
        B_got_shoot = B_got_shoot+1

    if dist_DB[t] < 5:
        print("Car B shoots Car D at time =", t, "\n")
        D_got_shoot = D_got_shoot+1

    if dist_AD[t] < 5:
        print("Car D shoots Car A at time =", t, "\n")
        A_got_shoot = A_got_shoot+1


    y_aNew = y_A[t] + v_A
    x_A.append(10)
    y_A.append(y_aNew)

    sin = (y_B[t] - y_C[t]) / dist_BC[t]
    cos = (x_B[t] - x_C[t]) / dist_BC[t]
    x_cNew = x_C[t] + v_C * cos
    y_cNew = y_C[t] + v_C * sin
    x_C.append(x_cNew)
    y_C.append(y_cNew)

    sin = (y_D[t] - y_B[t]) / dist_DB[t]
    cos = (x_D[t] - x_B[t]) / dist_DB[t]
    x_bNew = x_B[t] + v_B * cos
    y_bNew = y_B[t] + v_B * sin
    x_B.append(x_bNew)
    y_B.append(y_bNew)

    sin = (y_A[t] - y_D[t]) / dist_AD[t]
    cos = (x_A[t] - x_D[t]) / dist_AD[t]
    x_dNew = x_D[t] + v_D * cos
    y_dNew = y_D[t] + v_D * sin
    x_D.append(x_dNew)
    y_D.append(y_dNew)

print("Car A got shot ",  A_got_shoot, "times")
print("Car B got shot ",  B_got_shoot, "times")
print("Car C got shot ",  C_got_shoot, "times")
print("Car D got shot ",  D_got_shoot, "times")

