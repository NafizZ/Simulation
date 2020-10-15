import matplotlib.pyplot as plt
import random
random.seed(0)

trials = ['100', '1000', '5000', '10000']
square_side = 2
circle_radius = 1.5
square_height = 4
square_width = 4

# y-axis values for bar plot
y_pi, y_error_value, y_area_circle = [], [], []

for i in trials:
  hits = 0
  # x-axis values, y-axis values for scatter plot
  x_circle, y_circle, x_square, y_square  = [], [], [], []

  for j in range(int(i)):
      x = random.uniform(0, square_height)
      y = random.uniform(0, square_width)


      if((x-square_side)**2 + (y-square_side)**2)**.5 <= circle_radius:
          hits = hits + 1
          x_circle.append(x)
          y_circle.append(y)
      else:
          x_square.append(x)
          y_square.append(y)

  area_circle = square_height * square_width
  pi = (area_circle/circle_radius**2)*(hits/j)    # here j=trails
  print("value of pi :",pi)

  error_value = abs(pi - 3.1416)


  # plotting points as a scatter plot
  plt.scatter(x_circle, y_circle, color="red", label="Hit points")
  plt.scatter(x_square, y_square, color="green", label="Miss points")

  plt.legend()
  plt.show()

  y_pi.append(pi)
  y_error_value.append(error_value)
  y_area_circle.append(area_circle)

# bar plot for trials vs pi values
plt.bar(trials, y_pi)
plt.show()

# bar plot for trials vs error values
plt.bar(trials, y_error_value)
plt.show()

# bar plot for trials vs area of circle
plt.bar(trials, y_area_circle)
plt.show()
