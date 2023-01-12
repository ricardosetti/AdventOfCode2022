
file1 = [char for char in open("day6.txt").read()]
# print(file1)
length = len(file1)
print(length)
code = 0
codeFound = False
for i in range(0, length-13):
    tempSequence = ""
    for f in range(0, 14):
        tempSequence = tempSequence+str(file1[i+f])
    print(tempSequence)
    duplicateChar = []
    for character in tempSequence:
        if tempSequence.count(character) > 1:
            if character not in duplicateChar:
                duplicateChar.append(character)
    print(duplicateChar)
    if len(duplicateChar)==0:
        code = i+14
        break

print(code)