
file = open("input1.txt", "r")
#output = open("output.txt", "w")

for i, line in enumerate(file):
    if i == 0:
        print("Algorithm used: ", line)
    
    elif i == 1:
        print("Size of the maze: ", line)
    
    elif i == 2:
        print("Entrance grid location: ", line)

    elif i == 3:
        print("Exit grid location: ", line)

    elif i == 4:
        print("Number of points where actions are available: ", line)
    
    else:
        print(line)
        #output.write(line)

#output.close()