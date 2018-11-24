wres_f = open("wres.txt", "r")

a = int(wres_f.readline())
A = int(wres_f.readline())

b = int(wres_f.readline())
B = int(wres_f.readline())

wres=A-a

if b>A:
    wres = wres + B-b
elif a<=b<=A and a<=B<=A:
    wres = wres + 0
else:
    wres = wres + B - A

while b!= 0:
    a = b
    A = B

    try:
        b = int(wres_f.readline())
        B = int(wres_f.readline())
    except ValueError:
        pass

    if b > A:
        wres = wres + B - b
    elif a <= b <= A and a <= B <= A:
        wres = wres + 0
    else:
        wres = wres + B - A

wres_f.close()
apotelesma_f = open("apotelesma.txt", "w")
apotelesma_f.write("to fws emine anameno " + str(wres) + " wres")
apotelesma_f.close()



