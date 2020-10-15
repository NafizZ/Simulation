arr = [[0, 1, 0],
       [0, 0, 1],
       [0, 0, 0]]
a1 = 0
a2 = 3
b1 = 0
b2 = 3
x = 1
y = 1
count_alive = 0
for i in range(a1, a2):
    print("first loop")
    for j in range(b1, b2):
        print("second loop")
        if i != x or j != y:
            print("i, j =", i, j, "  x, y", x, y)
            if arr[i][j] == 1:
                print("  !!   count e dhukse  !!" )
                count_alive = count_alive + 1
print("count_alive=", count_alive)