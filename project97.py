a= 8
c= 0

while c < 5:
    g= int(input("enter a number from 1 to 9:   "))
    if(g < a):
        print("try entering a higher number")
        c= c+1
        print("chances left", 5-c)
    elif(g > a):
        print("try entering a lesser number ")
        c= c+1
        print("chances left", 5-c)
    else:
        print("congrats you won!")

print("sad u lost the number was: ", a)
    