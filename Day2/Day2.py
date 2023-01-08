
totalPoints = 0
with open("day2.txt") as file:
    for line in file:
        if line.strip()[-1] == "X":             # means I put rock
            totalPoints = totalPoints + 1       # get 1 point for rock
            if line.strip()[0] == "A":          # opponent has rock
                totalPoints = totalPoints + 3   # get 3 points for draw
            if line.strip()[0] == "C":          # opponent has scissors
                totalPoints = totalPoints + 6   # get 6 points for winning
        if line.strip()[-1] == "Y":             # means I put paper
            totalPoints = totalPoints + 2       # get 2 points for paper
            if line.strip()[0] == "A":          # opponent has rock
                totalPoints = totalPoints + 6   # get 6 points for winning
            if line.strip()[0] == "B":          # opponent has paper
                totalPoints = totalPoints + 3   # get 3 points for draw
        if line.strip()[-1] == "Z":             # means I put scissors
            totalPoints = totalPoints + 3       # get 3 points for scissors
            if line.strip()[0] == "B":          # opponent has paper
                totalPoints = totalPoints + 6   # get 6 point for winning
            if line.strip()[0] == "C":          # opponent has scissors
                totalPoints = totalPoints + 3   # get 3 points for draw
print("The total points following the first assumption is:", totalPoints)
totalPoints = 0
with open("day2.txt") as file:
    for line in file:
        if line.strip()[-1] == "X":             # means I need to lose
            if line.strip()[0] == "A":              # opponent has rock
                totalPoints = totalPoints + 3           # I should put scissors (3 points) and lose
            if line.strip()[0] == "B":              # opponent has paper
                totalPoints = totalPoints + 1           # I should put rock (1 point) and lose
            if line.strip()[0] == "C":              # opponent has scissors
                totalPoints = totalPoints + 2           # I should put paper (2 points) and lose
        if line.strip()[-1] == "Y":             # means draw
            totalPoints = totalPoints + 3           # 3 points for draw
            if line.strip()[0] == "A":              # opponent has rock
                totalPoints = totalPoints + 1           # I should put rock (1 point)
            if line.strip()[0] == "B":              # opponent has paper
                totalPoints = totalPoints + 2           # I should put paper (2 points)
            if line.strip()[0] == "C":              # opponent has scissors
                totalPoints = totalPoints + 3           # I should put scissors (3 points)
        if line.strip()[-1] == "Z":             # means I have to win
            totalPoints = totalPoints + 6           # 6 points for draw
            if line.strip()[0] == "A":              # opponent has rock
                totalPoints = totalPoints + 2            # I should put paper (2 points)
            if line.strip()[0] == "B":              # opponent has paper
                totalPoints = totalPoints + 3           # I should put scissors (3 points)
            if line.strip()[0] == "C":              # opponent has scissors
                totalPoints = totalPoints + 1           # I should put rock (1 point)
print("The total points following the second assumption is:", totalPoints)
