import matplotlib.pyplot as plt

trials = ['100', '1000', '5000', '10000']
for t in trials:
    z1 = [12, 7]
    z2 = [3, 5]
    z3 = [2, 7]
    u1 = [0, 0]
    u2 = [0, 0]
    u3 = [0, 0]
    u = [0, 0]
    temp = []
    for i in range(2, int(t)):
        new_z = ((13*z1[i-1])+(11*z1[i-2]) + 3) % 16
        new_u = new_z/16
        z1.append(new_z)
        u1.append(new_u)

        new_z = ((12 * (z2[i - 1]**2)) + (13 * z1[i - 2])) % 17
        new_u = new_z / 17
        z2.append(new_z)
        u2.append(new_u)

        new_z = ((z1[i - 1])**3 + (z1[i - 2]**2)) % 15
        new_u = new_z / 15
        z3.append(new_z)
        u3.append(new_u)

        temp1 = u1[i] + u2[i] + u3[i]
        value = (temp1/1)-(temp1//1)
        u.append(value)

        temp.append(str(i))
    plt.bar(temp, u[2:])
    plt.show()