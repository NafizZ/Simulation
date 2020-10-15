import matplotlib.pyplot as plt
import random
random.seed(0)

n = ["100", "1000", "5000", "10000"]       # trails
height = 5
width = 3
area_ractangle = height * width

x_hits, y_hits, x_miss, y_miss = [], [], [], []

for i in n:
    hits = 0

    for j in range(int(i)):
        x = random.uniform(0, width)
        y = random.uniform(0, height)

        y_limit = x + 2

        if y <= y_limit:
            hits = hits+1
            x_hits.append(x)
            y_hits.append(y)
        else:
            x_miss.append(x)
            y_miss.append(y)

    area = (area_ractangle * hits) / int(i)     # (area of selected part/ total area of ractangle) = (hits in the selected part/ total number of attemps)
    print(area)

    # plotting points as a scatter plot
    plt.scatter(x_hits, y_hits, color="red", label="Hit points")
    plt.scatter(x_miss, y_miss, color="green", label="Miss points")
    plt.legend()
    plt.show()
