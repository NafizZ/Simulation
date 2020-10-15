import math
import random
random.seed(0)

#Buffon's Needle for d=4 , l=2
d=4
l=2
hits= 0
n= 5000    #Number of trials
for i in range(n):
  D = random.uniform(0,d/2) # range of D is from 0 to half of 'd'
  theta= random.uniform(0, 180)
  # we have to check D <= {((1/2)*l) * sin(theta)}
  if D<=math.sin(theta*0.01745329251):  # 1 Degree = 0.0174533 Radian [so hare we converted the theta value from degree to radian]
    hits=hits+1
pi= (n/hits) #  pi = {(2l/d) * (trials/ hits)}   [here l=2 & d=4, so 2l/d = 1; trials = n;]
print(pi)


#Buffon needle scatter plot
import matplotlib.pyplot as plt
d=4
l=2
hits=0
n=1000
hit_x=[]
hit_y=[]
miss_x=[]
miss_y=[]
for i in range(0,n):
  D = random.uniform(0,d/2)
  theta= random.uniform(0,180)
  if D<=math.sin(theta*0.0174533):
    hits=hits+1
    hit_x.append(theta)
    hit_y.append(D)
  else:
    miss_x.append(theta)
    miss_y.append(D)
plt.scatter(hit_x, hit_y, color="red", label="Hit points")
plt.scatter(miss_x, miss_y, color="green", label="Miss points")

plt.ylabel('D')
plt.xlabel('Value theta')
plt.legend()
plt.show()