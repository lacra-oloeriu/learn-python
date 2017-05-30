from sys import exit#comentariu
from random import randint
from textwrap import dedent

class Stage (object):
    def enter(self):
        print ("This stage is very important.")
        print ("Subclass it that implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, stage_map):
        self.stage_map = stage_map

    def play (self):
        current_stage = self.stage_map.opening_stage()
        last_stage = self.stage_map.next_stage("succeeded")

        while current_stage != last_stage:
            next_stage_name = current_stage.enter()
            current_stage = self.stage_map.next_stage(next_stage_name)
        # be sure to print out the last stage
        current_stage.enter()
class Price(Stage):
    quips = [
        " You finish the championchip in the 3 position.",
        " Your Mom would be very proud of you. ",
        " The result is amaising.",
        " Because the competiotion was verry difficult.",
        " Good job! ."

    ]
    def enter(self):
        print(Price.quips[randint(0,len(self.quips) -1)])
        exit(1)
class Game(Stage):
    def enter(self):
        print(dedent("""
             You start the conpetition in the 64 position
             That isn't so nice for you.
             You have to work hard.
             After the first 3 ronds you are in the first 20 players.
             and after one more 3 tyou are in the first 10.
             At the finish line you are in the 3 position .Good job!
             """))

        action = input(">")

        if action == "good!":
            print(dedent("""
                  This conpetition it's very hard for you
                  You after do your best this year:
                  Try to earn even 5 points ,
                  and next year you can become campion
                  In the mind time .
                  Work hard every single day
                  and try to do your best
                  go go go.
                  """))
            return'iupii'

        elif action == "game!":
            print(dedent("""
                  You start the conpetition in the 64 position
                  That isn't so nice for you.
                  You have to work hard.
                  After the first 3 ronds you are in the first 20 players.
                  and after one more 3 tyou are in the first 10.
                  At the finis line the are in the 3 position .Good job!
                  """))
            return 'not bad'

        elif action =="this is not for you":
            print(dedent("""
                  This conpetition it was very hard for you
                  You are di=o your best:
                  You earn 5 points ,
                  and next year you can become campion
                  In the mind time .
                  Work hard every single day
                  and try to do your best
                  go go go.
                  """))
            return'faild'

        else:
            print("DOES NOT COMPUTE!")
            return'game_stage'

class RankCv(Stage):
    def enter(self):
        print(dedent("""
            You finished the national chqmpionchip whit 6.5 points
            what do you do?
            """))
        action = input("> ")

        if action == "wait":
            print(dedent("""
                You do not go to the international championchip in Romania
                You wait one more year and then you go to the mondials
                """))
            return "not so good"

        elif action =="go to the championchip":
            print (dedent("""
                You are finished at fourd and you have the right to go.
                They have invided you for the championchip!
                """))
            return "initial_inscription";

        else:
            print ("DOES NOT COMPUTE")
            return 'rank_cv'
class Result(Stage):
    def enter(self):
        print (dedent("""
             The result of the competition helps you to
             analuysis your game and
             to become betterr in the futur .
              """))

        action = input ("> ")

        if action == "get to work":
            print (dedent("""
                  You have to work every singer day
                  To do three probleme and to play two game
                  Like that you caan become the next champion of the word.
                  """))
            return 'rank_cv'

        elif action == "step by step":
            print (dedent("""
                  The game is very simple and verry complex
                  You have to learn how every pice move and a lot of strategy
                  The rest is gest matematiques things.
                  """))

            return 'game'
        else:
            print("DOES NOT COMPUTE!")
            return "price"

class Map(object):
    stages = {
        'rank_cv': RankCv(),
        'price':Price(),
        'game':Game(),
    }

    def __init__(self, start_stage):
        self.start_stage = start_stage

    def next_stage(self, stage_name):
        val = Map.stages.get(stage_name)
        return val

    def opening_stage(self):
        return self.next_stage(self.start_stage)
print ("Hello from my game")
a_map = Map('price')
a_game = Engine(a_map)
a_game.play()
