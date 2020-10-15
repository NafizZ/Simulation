import copy   # for using deep copy.
# initial 2D array at time t=0
arr = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0]]

# this 2D array will keep the updated values
update_arr = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

r = len(arr) - 1  # length of row
c = len(arr[1]) - 1  # length of column


def check_neighbours(x, y, a1, a2, b1, b2):
    value = arr[x][y]
    count_alive = 0
    for k in range(a1, a2):
        for L in range(b1, b2):
            if k != x or L != y:
                if arr[k][L] == 1:
                    count_alive = count_alive + 1
    if value == 1:
        if count_alive == 2:
            return 1
        else:
            return 0
    else:
        if count_alive == 2 or count_alive == 3:
            return 1
        else:
            return 0


for t in range(21):
    print("time:", t)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()
    print()

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i != 0 and i != r and j != 0 and j != c:  #this one is for middle part
                update_arr[i][j] = check_neighbours(i, j, i-1, i+2, j-1, j+2)

            elif i == 0 and j == 0:                      # top left corner
                update_arr[i][j] = check_neighbours(i, j, i, i+2, j, j+2)

            elif i == r and j == 0:                      # bottom left corner
                update_arr[i][j] = check_neighbours(i, j, i-1, i+1, j, j+2)

            elif j == 0:                                 # left side
                update_arr[i][j] = check_neighbours(i, j, i-1, i+2, j, j+2)

            elif i == 0 and j == c:                      # top right corner
                update_arr[i][j] = check_neighbours(i, j, i, i + 2, j-1, j+1)

            elif i == r and j == c:                      # bottom right corner
                update_arr[i][j] = check_neighbours(i, j, i-1, i, j-1, j+1)

            elif j == c:                                 # right side
                update_arr[i][j] = check_neighbours(i, j, i-1, i+2, j-1, j+1)

            elif i == 0:                                 # top corner
                update_arr[i][j] = check_neighbours(i, j, i, i+2, j-1, j+2)

            elif i == r:                                 # bottom corner
                update_arr[i][j] = check_neighbours(i, j, i-1, i+1, j-1, j+2)

    arr = copy.deepcopy(update_arr)  # copy the updated array to the main array
