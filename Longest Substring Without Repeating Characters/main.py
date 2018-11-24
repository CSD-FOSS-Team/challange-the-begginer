file = open("input.txt")
s = file.read()
file.close()
maxstreak = 0
streak = 1
letters = tuple(s)
leng = len(set(letters))
for i in range(len(letters)):
    prevletters = set(letters[i])
    for j in range(i + 1, len(letters)):
        letter = letters[j]
        if letter not in prevletters:
            streak += 1
            prevletters.add(letter)
        else:
            if streak > maxstreak:
                maxstreak = streak
            streak = 1
    if streak > maxstreak:
        maxstreak = streak
    streak = 1
    if maxstreak >= leng:
        break
file = open("output.txt", "w")
file.write(str(maxstreak))
file.close()
