from sys import exit # comentariu
from random import randint
from textwrap import dedent

class DataAnalist(object):

    def enter(self):
        print("This is your objectif in the next year.")
        print("Try to lean every day a littly bit().")
        exit(1)

class PythonCours(object):

    def __init__(self, learn_python):
        self.learn_python = learn_python

    def play(self):
        current_cours = self.learn_python.opening_learn()
        last_cours = self.learn_python.next_cours()

        while current_cours != last_cours:
            next_cours_name = current_cours.enter()
            current_cours = self.learn_cours.next_cours(next_cours_name)

            #be sure to print out the last learn_python
        current_cours.enter()

class GitHub(object):

    quips = [
        " You have to do this work every day.",
        " Because is very important to you. ",
        " And helps you to became very good.",
        " And you have to do that very fast.",
        " Not mertherr what ."

    ]

    def enter(self):
        print(GitHub.quips[randint(0,len(self.quips) -1)])
        exit(1)

class Typing(DataAnalist):

    def enter(self):
        print(dedent("""
             Te first time when I'm try to type it was terifiants
             But I type every songle day
             and i start to undestannd that work
             Not because i love it , and because,
             I want to do something in my live.

             Now , to performe my work
             I have to type minimum 2h for day
             Because in that way i build the corect muscle
             And ia learn to type very faast
             So go back to work .
             """))

        action = input(">")

        if action == "shoot!":
            print(dedent("""
                  Quick on the draw you yank out you blaster and fire
                  it at the Gothon .His clown costume is flowing and
                  moving around hid body, which throws off your aim.
                  Your laser hits his costume but misses him entirely.
                  This complrtely ruins his brand new costume his mother
                  bought him, which makes him fly into an insane rage
                  and blast you repeatedly in the face until you are
                  dead.  Then he eats you.
                  """))
            return'death'

        elif action == "dodge!":
            print(dedent("""
                  Like a world class boxer you dodge , weave , slip and
                  slide right as the Gothon's blaster cranks a Laser
                  past your head. In the middle of your artful dodge
                  your foot slips and you bang your head on the metal
                  wall and pass out. You wake up chortly after only to
                  die as the Gothon stomps on your head eats you.
                  """))
            return 'death'

        elif action =="tell a joke":
            print(dedent("""
                  Lucky for you they made you learn Gothon insults in
                  the academy. You tell the one Gothon joke you know:
                  Lbhe zbgure vf fb sng , jura fur fvgf nebhaq gur ubhfr,
                  fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                  not to laugh, then busts out laughing and can't move.
                  While he's laughing you run up and shoot him square in
                  the head putting him down, then jump through the
                  Weapon Armory door.
                  """))
            return'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return'central_corridor'

class SearchJob(DataAnalist):

    def enter(self):
        print(dedent("""
              You do a drive roll into the Weapon Armory , crouch and scan
              the room for more Gothon that might be hiding . It's dead
              quiet, too quiet.You stand up and run to the far side of
              the room and find the neurton bomb in its container.
              There's a keypad lock on the box and you need the code to
              get the bomb out. If you get the code wrong 10 time then
              the lock closes forever and you can't get the bomb. The
              code is 3 digits.
              """))

        code ==f"{randint(1,9)} {randint(1,9)}{randint(1,9)}"
        guess = input("[keypad] >")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print (dedent("""
                  The container clicks open and the seal breaks , letting
                  gas out. You grab the neutron bomb and run as fast as
                  you can to the brige where you must place it in the
                  right spot.
                  """))
            return 'the_bridge'
        else:
            print(dedent("""
                 The lock buzzes one last time and then you hear a
                  sickening melting sound as the mechanism is fused
                  together.  You decide to sit there, and finally the
                  Gothons blow up the ship from their ship and you die.
                  """))
            return 'death'


class MovetoHague(DataAnalist):

    def enter(self):
        print (dedent("""
              You burst onto the Bridge with the netron destruct bomb
              under your arm and surprise 5 Gothons who are trying to
              take control of the ship.  Each of them has an even uglier
              clown costume than the last.  They haven't pulled their
              weapons out yet, as they see the active bomb under your
              arm and don't want to set it off.
              """))

        action = input ("> ")

        if action == "throw the bomb":
            print (dedent("""
                  In a panic you throw the bomb at the group of Gothons
                  and make a leap for the door.  Right as you drop it a
                  Gothon shoots you right in the back killing you.  As
                  you die you see another Gothon frantically try to
                  disarm the bomb. You die knowing they will probably
                  blow up when it goes off.
                  """))
            return 'death'

        elif action == "slowly place the bomb":
            print (dedent("""
                  You point your blaster at the bomb under your arm and
                  the Gothons put their hands up and start to sweat.
                  You inch backward to the door, open it, and then
                  carefully place the bomb on the floor, pointing your
                  blaster at it.  You then jump back through the door,
                  punch the close button and blast the lock so the
                  Gothons can't get out.  Now that the bomb is placed
                  you run to the escape pod to get off this tin can.
                  """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class StayinLiege(DataAnalist):

    def enter(self):
        print(dedent("""
              You rush through the ship desperately trying to make it to
              the escape pod before the whole ship explodes.  It seems
              like hardly any Gothons are on the ship, so your run is
              clear of interference.  You get to the chamber with the
              escape pods, and now need to pick one to take.  Some of
              them could be damaged but you don't have time to look.
              There's 5 pods, which one do you take?
              """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(dedent("""
                  You jump into pod {guess} and hit the eject button.
                  The pod escapes out into the void of space, then
                  implodes as the hull ruptures, crushing your body into
                  jam jelly.
                  """))
            return 'GitHub'
        else:
            print(dedent("""
                  You jump into pod {guess} and hit the eject button.
                  The pod easily slides out into space heading to the
                  planet below.  As it flies to the planet, you look
                  back and see your ship implode then explode like a
                  bright star, taking out the Gothon ship at the same
                  time.  You won!
                  """))

            return 'Happy'

class Happy(DataAnalist):

    def enter(self):
        print("You won! Good job.")
        return 'Happy'
class Map(object):

    scenes = {
        'Typing': Typing(),
        'SearchJob': SearchJob(),
        'MovetoHague': MovetoHague(),
        'StayinLiege': StayinLiege(),
        'GitHub': GitHub(),
        'Happy': Happy(),
    }

    def __init__(self, learn_python):
        self.learn_python  = learn_python

    def next_learn(self, cours_name):
        val = Map.scenes.get(cours_name)
        return val

    def opening_learn(self):
        return self.next_learn(self.learn_python)

a_map = Map('Typing')
a_game = PythonCours(a_map)
a_game.play()
