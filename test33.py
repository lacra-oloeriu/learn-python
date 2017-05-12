password = ""
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print("Thank you. You have entered the correct password")
    else:
        print("Sorry the value entered in incorrecct")

i=0
numbers = []

while i < 6:
    print("At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print (" The numbers: ")

for num in numbers:
    print(num)

    def whilefunc(i):
        numbers = []
    for i in range(0,6):
        print ("At the top i is %d" %i)
        numbers.append(i)
        i += 1
        print ("Numbers now: ", numbers)
        print ("At the bottom, i is %d" %i)
    for num in numbers:
        print (num)
