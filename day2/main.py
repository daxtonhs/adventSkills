with open("input.txt", "r") as file:
    for line in file:
        g_split = line.split(":") #split at the colon used for identifying games
        gid = ""
        for n in g_split[0]:
            if n.isdigit():
                gid += n
        gid = int(gid)

        
