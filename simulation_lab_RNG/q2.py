import matplotlib.pyplot as plt

r = 3
q = 5

b = [1, 1, 1, 1, 1]
l = 4
w = []
u = []
x_axis = []

for i in range(5, 1000):
    b_xor = b[i - r] ^ b[i - q]
    b.append(b_xor)

for i in range(0, 1000, l):
    x_axis.append(i / 4)
    bit_segment = b[i:i + l]
    str1 = ''
    for j in bit_segment:
        str1 = str1 + str(j)
    # print(str1)
    new_w = int(str1, 2)
    #print(new_w)

    temp_u = new_w / (2 ** l)
    u.append(temp_u)
print(u)


#this function is to finding number of elements in a sequance in a list
def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) / 2
    for x in range(2, int(max_len)):
        if seq[0:x] == seq[x:2 * x]:
            return x

    return guess


number_of_elements = guess_seq_len(u)  # number of elements in a cycle
number_of_cycles = len(u) / number_of_elements
# print(guess_seq_len(u))
# print(guess_seq_len(range(500)))
print("\nThere are total", number_of_cycles, "cycles in this graph. Each cycle contains",
      number_of_elements, "elements.","Number of full cycles =", int(number_of_cycles))

plt.bar(x_axis, u)
plt.show()



