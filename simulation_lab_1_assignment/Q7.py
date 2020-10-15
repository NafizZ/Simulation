listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = []
length = 0
if len(listOne) >= len(listTwo):
    length = len(listOne)
else:
    length = len(listTwo)

i=0
while i<length:
    if i%2 == 0:
        listThree.append(listTwo[i])
    else:
        listThree.append(listOne[i])
    i=i+1
   # print(i)
print(listThree)