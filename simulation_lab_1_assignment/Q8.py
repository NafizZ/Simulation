import matplotlib.pyplot as plt

# Toothpaste points
x1 = [1, 2, 3, 4, 5, 6]
y1 = [2500, 2630, 2140, 3400, 3600, 2760]
# plotting the line 1 points
plt.plot(x1, y1,  label="Toothpaste")

# Facewash points
x2 = [1, 2, 3, 4, 5, 6]
y2 = [1500, 1200, 1340, 1130, 1740, 1555]
# plotting the line 2 points
plt.plot(x2, y2, label="Facewash")

# Shampoo points
x3 = [1, 2, 3, 4, 5, 6]
y3 = [5200, 5100, 4550, 5870, 4560, 4890]
# plotting the line 2 points
plt.plot(x3, y3, label="Shampoo")

# Moisturizer points
x4 = [1, 2, 3, 4, 5, 6]
y4 = [9200, 6100, 9550, 8870, 7760, 7490]
# plotting the line 2 points
plt.plot(x4, y4, label="Moisturizer")

# Soap points
x5 = [1, 2, 3, 4, 5, 6]
y5 = [1200, 2100, 3550, 1870, 1560, 1890]
# plotting the line 2 points
plt.plot(x5, y5, label="Soap")

# naming the x axis
plt.xlabel('Month no.')
# naming the y axis
plt.ylabel('Sales Unit')

# i)ans:
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()



# ii) ans:

# plotting points as a scatter plot
plt.scatter(x2, y2, label="Moisturizer")

plt.legend()
plt.show()



#iii) ans:
x = [1,2,3,4,5]
y = []
for i in range(5):
    y.append(y1[i] + y2[i] + y3[i] + y4[i] + y5[i])
plt.bar(x,y)
plt.show()