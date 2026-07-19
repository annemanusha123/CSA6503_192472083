file = open("sample.txt", "r")
for line in file:
    print(line, end="")
file.close()