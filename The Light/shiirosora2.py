#Φτιαχνει μια δισδιαστατη λιστα
list=[]
x=int(input("People entered: "))
for i in range(x):
    list.append([])
    var1=int(input("First: "))
    var2=int(input("Second: "))
    if var2<=var1:
        var2=int(input("Greater than first PLEASE: "))
    for j in range(var1,var2+1,1):
        list[i].append(j)
list.sort()

#Ελεγχει καθε λιστα στον πινακα με την επομενη και αν εχει
#κοινα στοιχεια τις ενωνει και διαγραφει την επομενη
i=0
while i <len(list)-1:
    j=0
    while j<len(list[i]):
        if list[i][j] in list[i+1]:
            list[i]=list[i]+list[i+1]
            list.pop(i+1)
            j-=1
        j+=1
    i+=1
list.sort()

#Ελεγχει τα στοιχεια καθε λιστας τη φορα.
#Αν υπαρχουν κοινα μεσα στη λιστα τα αφαιρει
i=0
while i<len(list):
    list[i].sort()
    j=1
    while j<len(list[i]):
        if list[i][j]==list[i][j-1]:
            temp=list[i][j]
            list[i].remove(temp)           
            j-=1
        j+=1
    i+=1

#Βρισκει τη λιστα με τα περισσοτερα στοιχεια    
max=list[0]
for i in range(len(list)):
    if len(list[i])>len(max):
        max=list[i]

#Η μεγιστη ωρα που η λαμπα ειναι αναμμενη
print (max[len(max)-1]-max[0])       

           

    
#print (list)
#print (max)
