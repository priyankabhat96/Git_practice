list1 = [73, 12, 9, 65, 5, 26]

for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] >= list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(list1)            