
file = open("input1.txt", "r")
lines = file.readlines()

size = int(lines[4])
algorithm = lines[0].rstrip("\n")

start = lines[2].rstrip("\n")
end = lines[3].rstrip("\n")

header = 5

adj_list = {}

for i in range(header, size+header):
    line = lines[i].rstrip("\n").split()
    point = line[0] + " " + line[1] + " " + line[2]

    adj_list[point] = len(line)-3

print(adj_list)