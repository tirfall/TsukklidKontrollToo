from random import *

#variant 4, ulesanne 1

#while True:
#    try:
#        catnumber = int(input("Tere! Kui palju kassid sa tahad? Vali number 1-9:"))
#        break
#    except ValueError:
#        print("See pole täisarv")
#if catnumber<1 or catnumber>9:
#    print("Vali õige number")
#else:
#    x = 0
#    for x in range (catnumber):
#        print("  ^---^  ", end=" ")
#    print("\n", end="")
#    for x in range (catnumber):
#        print(" ( o o ) ", end=" ")
#    print("\n", end="")
#    for x in range (catnumber):
#        print("  ! = !/)", end=" ")
#    print("\n")

#variant 4, ulesanne 2

#while True:
#    try:
#        number = int(input("Tere! Sisesta number:"))
#        kraad = int(input("Sisesta kraad:"))
#        break
#    except ValueError:
#        print("See pole täisarv")
#ans = number**kraad
#print("Siin on sinu vastus:", ans)

#variant 4, ulesanne 3

#while True:
#    try:
#        yesno = str(input("Tere! Kas sa tahad alustada programmi?  jah või ei: "))
#        break
#    except ValueError:
#        print("Vali õige vastu")
#if yesno == "jah":
#    hinnelist = []
#    student = randint(1,30)
#    for x in range (student):
#        hinne = randint(1,100)
#        print (hinne, end=", ")
#        hinnelist.append (hinne)
#    print("\n")
#    print(max(hinnelist),"Maksimaalne hinne")
#    print(min(hinnelist) ,"Minimaalne hinne")
#else:
#    print("Head aega!")

#variant 4, ulesanne 4

#amyoba = 1
#while True:
#    try:
#        yesno2 = str(input("Tere! Kas sa tahad alustada programmi?  jah või ei: "))
#        break
#    except ValueError:
#        print("Vali õige vastu")
#if yesno2 == "jah":
#    numb = 0
#    while numb!=8:
#        amyoba = amyoba*2
#        print(amyoba, end=" amyobad parast kolm tundi, ")
#        numb += 1
#    print("\n Head aega")
#else:
#    print("Head aega")


