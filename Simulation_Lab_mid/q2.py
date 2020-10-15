import matplotlib.pyplot as plt
import random
random.seed(0)

trials = ['1000', '5000', '10000']
#square_side =
circle_radius = 2
square_height = 8
square_width = 6

# y-axis values for bar plot
y_pi, y_error_value, y_area_circle = [], [], []

for i in trials:
  hits = 0
  # x-axis values, y-axis values for scatter plot
  x_circle, y_circle, x_square, y_square  = [], [], [], []

  for j in range(int(i)):
      x = random.uniform(-8, -2)
      y = random.uniform(2, 10)


      if((x+5)**2 + (y-7)**2)**.5 <= circle_radius:
          hits = hits + 1
          x_circle.append(x)
          y_circle.append(y)
      else:
          x_square.append(x)
          y_square.append(y)

  area_circle = square_height * square_width
  area = (square_height * square_width) * (hits / int(i))
  pi = (area_circle/circle_radius**2)*(hits/j)    # here j=trails
  print("value of area :",area)

  error_value = abs(pi - 3.1416)


  # plotting points as a scatter plot
  plt.scatter(x_circle, y_circle, color="red", label="Hit points")
  plt.scatter(x_square, y_square, color="green", label="Miss points")

  plt.legend()
  plt.show()

  y_pi.append(pi)
  y_error_value.append(error_value)
  y_area_circle.append(area_circle)


