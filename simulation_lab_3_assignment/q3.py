import matplotlib.pyplot as plt
import random
import math
random.seed(0)

n = ["100", "1000", "5000", "10000"]       # trails
height = 4
width = 8
area_ractangle = height * width

x_hits, y_hits, x_miss, y_miss = [], [], [], []

for i in n:
    hits = 0

    for j in range(int(i)):
        x = random.uniform(0, width)
        y = random.uniform(0, height)

        if x <= 4:
            y_limit = math.sqrt(4*x)
            if y <= y_limit:
                hits = hits+1
                x_hits.append(x)
                y_hits.append(y)
            else:
                x_miss.append(x)
                y_miss.append(y)

        else:
                y_limit = 8-x
                if y <= y_limit:
                    hits = hits + 1
                    x_hits.append(x)
                    y_hits.append(y)
                else:
                    x_miss.append(x)
                    y_miss.append(y)


    area = (area_ractangle * hits) / int(i)
    print(area)

    # plotting points as a scatter plot
    plt.scatter(x_hits, y_hits, color="red", label="Hit points")
    plt.scatter(x_miss, y_miss, color="green", label="Miss points")
    plt.legend()
    plt.show()
