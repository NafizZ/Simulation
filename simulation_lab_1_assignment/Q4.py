l = [1, 3, 4, 2, 4, 5 ,6 , 7]
print(len(l))
even_count =0
odd_count=0
i=0
while i < len(l):
    print(i)
    if (l[i]) % 2 == 0:
        print("l[i]", i)
        even_count += 1
        del(l[i])
        print("lenth of list:", len(l))
    else:
        odd_count += 1
        i += 1
print("even number:", even_count," odd number:", odd_count, " updated list:",  l)