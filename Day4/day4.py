
overlaps = 0
moreOverlaps = 0
with open("day4.txt") as file:
    for line in file:
        pair = line.strip()
        pairRanges = pair.split(",")
        print(pairRanges)
        pairRange1 = pairRanges[0].split("-")
        pairRange2 = pairRanges[1].split("-")
        print(pairRange1,pairRange2)
        if (int(pairRange1[0]) <= int(pairRange2[0])) & (int(pairRange1[1]) >= int(pairRange2[1])):
            overlaps = overlaps + 1
            moreOverlaps = moreOverlaps + 1
            print("Yes")
        elif (int(pairRange2[0]) <= int(pairRange1[0])) & (int(pairRange2[1]) >= int(pairRange1[1])):
            overlaps = overlaps + 1
            moreOverlaps = moreOverlaps + 1
            print("Yes")
        elif (int(pairRange1[0]) <= int(pairRange2[0])) & (int(pairRange1[1]) >= int(pairRange2[0])):
            moreOverlaps = moreOverlaps + 1
            print("Yes 2")
        elif (int(pairRange2[0]) <= int(pairRange1[0])) & (int(pairRange2[1]) >= int(pairRange1[0])):
            moreOverlaps = moreOverlaps + 1
            print("Yes 2")
        else:
            print("No")
    print(overlaps)
    print(moreOverlaps)