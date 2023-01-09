def intersection(lst1, lst2, lst3):
    return list(set(lst1) & set(lst2) & set(lst3))

items = [0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
         "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(len(items))
duplicate_char = []
allBackpacks = []
with open("day3.txt") as file:
    for line in file:

         # initializing the string
         backpack = line.strip()
         allBackpacks.append(backpack)
         print(backpack)
         quantityItems = len(backpack)
         sack1 = backpack[:quantityItems // 2]
         sack2 = backpack[quantityItems // 2:]
         # print(sack1, sack2)
         found = False
         for itemSack1 in sack1:
            if not found:
                for i in range(0, len(sack2)):
                    if itemSack1 == sack2[i]:
                        duplicate_char.append(itemSack1)
                        # print(itemSack1);
                        found = True
                        break
    print(duplicate_char)
    totalPriorities = 0
    for item in duplicate_char:
        totalPriorities = totalPriorities + items.index(item);
    print(totalPriorities)
    print(len(duplicate_char))
    badges = []
    for i in range (0, len(allBackpacks), 3):
        group = []
        group.append(allBackpacks[i])
        group.append(allBackpacks[i+1])
        group.append(allBackpacks[i+2])
        print(group)
        common = intersection(group[0], group[1], group[2])
        badges.append(common[0])
    print(badges)
    totalPriorities = 0
    for item in badges:
        totalPriorities = totalPriorities + items.index(item);
    print(totalPriorities)