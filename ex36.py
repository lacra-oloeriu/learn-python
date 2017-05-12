from sys import exit

def gold_room():
    print (" This is full of gold.I have to find the lamp!")

    choice= input (">")
    if "0" in choice or "1" in choice:
        how_much = int ( choice)
    else :
        dead ("Man , there are so many.")

    if how_much < 50 :
        print(" Nice , What can I do now?")
        exit(0)
    else :
        dead("You have to run!")


def aladin_room():
    print ("Aladin isn't a prince.")
    print (" He fool in love .He love the princese")
    print ("The princese didn't know that.")
    print ("What he can do?")
    aladin_moved = False

    while True:
        choice= input ("> ")

        if choice == " take  the princese":
            dead("the princese looks at you then kiss you.")
        elif choice =="kiss him" and not aladin_moved:
            print(" the princese don't want you.")
            print("You say tanks and you")
            aladin_moved = True
        elif choice=="kiss him" and aladin_moved:
            dead ("the princese gets pissed off and chews your leg off.")
        elif choice =="open door" and aladin_moved:
            gold_room()
        else :
            print(" I got no idea what that means.")


def sorcerer_room():
    print ("Here you see the great evil Sorcerer.")
    print(" He , it , whatever stares at you and you go insane.")
    print(" do you flee for your life or eat your head?")

    choice = input (">")

    if "flee " in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else :
        sorcerer_room()


def dead (why):
    print (why, "Good job!")
    exit(0)

def start():
    print(" You are in a dark room.")
    print (" There is a door to your right and left.")
    print (" Which one do you take?")

    choice = input (">")

    if choice =="left":
        aladin_room()
    elif choice == "right":
        sorcerer_room()
    else :
        dead (" You stumble around the room until you starve.")


start()
