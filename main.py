
file = open("input1.txt", "r")
lines = file.readlines()

output = open("output.txt", "w")

size = int(lines[4])
algorithm = lines[0].rstrip("\n")

start = lines[2].rstrip("\n")
end = lines[3].rstrip("\n")

header = 5

adj_list = {}

for i in range(header, size+header):
    line = lines[i].rstrip("\n").split()
    point = line[0] + " " + line[1] + " " + line[2]

    line_len = len(line)

    adj_list[point] = []

    for move in range(3, line_len):
        if line[move] == "1":
            adj_list[point].append(str(int(line[0])+1) + " " + line[1] + " " + line[2])
        elif line[move] == "2":
            adj_list[point].append(str(int(line[0])-1) + " " + line[1] + " " + line[2])
        elif line[move] == "3":
            adj_list[point].append(line[0] + " " + str(int(line[1])+1) + " " + line[2])
        elif line[move] == "4":
            adj_list[point].append(line[0] + " " + str(int(line[1])-1) + " " + line[2])
        elif line[move] == "5":
            adj_list[point].append(line[0] + " " + line[1] + " " + str(int(line[2])+1))
        elif line[move] == "6":
            adj_list[point].append(line[0] + " " + line[1] + " " + str(int(line[2])-1))
        elif line[move] == "7":
            adj_list[point].append(str(int(line[0])+1) + " " + str(int(line[1])+1) + " " + line[2])
        elif line[move] == "8":
            adj_list[point].append(str(int(line[0])+1) + " " + str(int(line[1])-1) + " " + line[2]) 
        elif line[move] == "9":
            adj_list[point].append(str(int(line[0])-1) + " " + str(int(line[1])+1) + " " + line[2])
        elif line[move] == "10":
            adj_list[point].append(str(int(line[0])-1) + " " + str(int(line[1])-1) + " " + line[2])
        elif line[move] == "11":
            adj_list[point].append(str(int(line[0])+1) + " " + line[1] + " " + str(int(line[2])+1))
        elif line[move] == "12":
            adj_list[point].append(str(int(line[0])+1) + " " + line[1] + " " + str(int(line[2])-1))
        elif line[move] == "13":
            adj_list[point].append(str(int(line[0])-1) + " " + line[1] + " " + str(int(line[2])+1))
        elif line[move] == "14":
            adj_list[point].append(str(int(line[0])-1) + " " + line[1] + " " + str(int(line[2])-1))
        elif line[move] == "15":
            adj_list[point].append(line[0] + " " + str(int(line[1])+1) + " " + str(int(line[2])+1))
        elif line[move] == "16":
            adj_list[point].append(line[0] + " " + str(int(line[1])+1) + " " + str(int(line[2])-1))
        elif line[move] == "17":
            adj_list[point].append(line[0] + " " + str(int(line[1])-1) + " " + str(int(line[2])+1))
        elif line[move] == "18":
            adj_list[point].append(line[0] + " " + str(int(line[1])-1) + " " + str(int(line[2])-1))

def use_bfs(adjacency_list, start_node, end_node):

    visited_nodes = []
    queue = [[start_node]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited_nodes:
            adjacent_nodes = adjacency_list[node]

            for adjacent_node in adjacent_nodes:
                new_path = list(path)
                new_path.append(adjacent_node)
                queue.append(new_path)

                if adjacent_node == end_node:
                    output.write(str(len(new_path)-1) + "\n")
                    output.write(str(len(new_path)))
                    for node in new_path:
                        if node == start:
                            value = 0
                        else:
                            value = 1
                        output.write("\n" + node + " " + str(value))
                    return
            
            visited_nodes.append(node)
    
    output.write("FAIL")

use_bfs(adj_list, start, end)

output.close()
