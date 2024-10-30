number = 0
with open("input.txt", "r") as file:
    for line in file:
        temp = [i for i in line if i.isdigit()]
        number += int(f"{temp[0]}{temp[-1]}")

print(number)