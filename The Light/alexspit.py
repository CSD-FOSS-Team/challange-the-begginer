
##NumOfPeople = int(input("How Many people??? \n ammount:"))
f = open("alexspit.in","r")
if f.mode != 'r':
    f.close()
    exit()
contents = f.read().split()
NumOfPeople = int(len(contents)/2)

x = [[0 for x in range(2)] for y in range(NumOfPeople)]
y1 = 0
y2 = 0
for j in contents:
    ##arrival = int(input("Time of arrival:"))
    ##deport = int(input("Time left:"))
    if(j.isdigit() == True):
        x[y1][y2]= int(j)
        y2+=1
        if(y2 ==2):
            y2 = 0
            y1 +=1
f.close()
x.sort()
if NumOfPeople ==0:
    print(0)
    exit()
max = x[0][1]-x[0][0]
i = 1
max2 = 0
if NumOfPeople ==1:
    print(max+1)
    exit()
while  x[i-1][1] >= x[i][0]:
    max += x[i][1] - x[i-1][1]
    i+=1
    if (i == NumOfPeople):
        break
while i < NumOfPeople:
    max2 = x[i][1] - x[i][0]
    i+=1
    if(i == NumOfPeople):
        if max2 > max:
            max = max2
        break
    while x[i - 1][1] >= x[i][0]:
        max2 += x[i][1] - x[i - 1][1]
        i += 1
        if(i== NumOfPeople):
            break
    if (max2 > max):
        max = max2
f = open("alexspit.out","w")
f.write(str(max+1))