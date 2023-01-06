caloriesList = []
totalCalories = 0
with open("day1.txt") as file:
    for line in file:
        if line == "\n":
            caloriesList.append(totalCalories)
            totalCalories = 0
        else:
            totalCalories = totalCalories + int(line.strip())
caloriesList.sort()
print ("The elf with more calories has:", caloriesList[-1])
print ("The three elves carrying more calories have:", caloriesList[-1], caloriesList[-2], "and", caloriesList[-3])
totalThree = caloriesList[-1]+caloriesList[-2]+caloriesList[-3]
print ("The total calories carried by the three top calories elves is:", totalThree)

