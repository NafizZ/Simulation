a = input("input string: ")
temp = list(a)

for b in range(1, len(a)):
    if(temp[0] == temp[b]):
        temp[b] = '$'
a = "".join(temp)
print(a)


