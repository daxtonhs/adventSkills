replacements = [["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]]
number = 0
with open("input.txt", "r") as file:
    for line in file:
        temp = []
        for i in range(len(line)): 
            for rep in replacements: 
                if line.startswith(rep[0], i):
                    temp.append(rep[1])
            if line[i].isdigit():
                temp.append(i)

        print(temp, f"{temp[0]}{temp[-1]}")
        number += int(f"{temp[0]}{temp[-1]}")

print(number)