# crate1 = ["B", "G", "S", "C"]
# crate2 = ["T", "M", "W", "H", "J", "N", "V", "G"]
# crate3 = ["M", "Q", "S"]
# crate4 = ["B", "S", "L", "T", "W", "N", "M"]
# crate5 = ["J", "Z", "F", "T", "V", "G", "W", "P"]
# crate6 = ["C", "T", "B", "G", "Q", "H", "S"]
# crate7 = ["T", "J", "P", "B", "W"]
# crate8 = ["G", "D", "C", "Z", "F", "T", "Q", "M"]
# crate9 = ["N", "S", "H", "B", "P", "F"]

stacks = [[0, 0],
          ["B", "G", "S", "C"],
          ["T", "M", "W", "H", "J", "N", "V", "G"],
          ["M", "Q", "S"],
          ["B", "S", "L", "T", "W", "N", "M"],
          ["J", "Z", "F", "T", "V", "G", "W", "P"],
          ["C", "T", "B", "G", "Q", "H", "S"],
          ["T", "J", "P", "B", "W"],
          ["G", "D", "C", "Z", "F", "T", "Q", "M"],
          ["N", "S", "H", "B", "P", "F"]]

with open("day5.txt") as file:
    for line in file:
        action = line.strip()
        numberOfCrates = int((action.split(" from ")[0])[5:])
        crateFrom = int((action.split(" to ")[0])[12:])
        crateTo = int(action.split(" to ")[1])

        print(action)
        print(numberOfCrates)
        print(crateFrom)
        print(crateTo)
        print(stacks[crateFrom])
        print(stacks[crateTo])

        cratePackage = stacks[crateFrom][-(numberOfCrates):]
        print(cratePackage)
        for i in range(0, numberOfCrates):
            stacks[crateFrom].pop()
            stacks[crateTo].append(cratePackage[i])
        print(stacks[crateFrom])
        print(stacks[crateTo])

print("Stacks at the end:")
for i in range(1, 10):
    print(stacks[i])
