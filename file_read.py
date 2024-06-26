file = open('test.txt')
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()

file = open('test.txt')
line = file.readlines()
for itr in line:
    print(itr)

file.close()
