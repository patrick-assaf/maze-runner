
file = open("input1.txt", "r")
output = open("output.txt", "w")

for line in file:
    print(line)
    output.write(line)

output.close()