A = [50]
B = [50]
C = [30]
kf = 0.05
kb = 0.01
dt = 0.2

for i in range(5):
    dA = 2 * kb * C[i] - kf * A[i]**2 * B[i]
    dB = 2 * kb * C[i] - kf * A[i]**2 * B[i]
    dC = kf * A[i]**3 * B[i] - kb * C[i]
    print()
    print("  time", i)
    print("dA", dA)
    print("dB", dB)
    print("dC", dC)
    print()

    new_A = A[i] + dA * dt
    new_B = B[i] + dB * dt
    new_C = C[i] + dC * dt
    print("new_A", new_A)
    print("new_B", new_B)
    print("new_C", new_C)
    print()

    A.append(new_A)
    B.append(new_B)
    C.append(new_C)

    deffer_A = abs(A[i+1] - A[i])
    deffer_B = abs(B[i+1] - B[i])
    deffer_C = abs(C[i+1] - C[i])
    print("deffer_A", deffer_A)
    print("deffer_B", deffer_B)
    print("deffer_C", deffer_C)
    print()

    if deffer_A < 0.1 and deffer_B < 0.1 and deffer_C < 0.1:
        print(" Equilibrium!! ")
        break


