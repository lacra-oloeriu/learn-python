from sys import exit
from random import randint
from textwrap import dedent

class Stage (object):
    def enter(self):
        print ("This stage is note yet cofigure.")
        print ("Subclass it tand implement enter().")
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

class SendCv(Stage):
    def enter(self):
        print(dedent("""
            You are looking at a job description that is perfect for you
            what do you do?
            """))
        action = input("> ")

        if action == "wait":
            print(dedent("""
                You spend to much time deding if you are ok for the job
                and you missed the oportunity
                """))
            return "fail_interview"

        elif action =="send cv":
            print (dedent("""
                You are brave and your cv made a good inprestion on this conpany.
                They have invided you for an interview!
                """))
            return "initial_screaning";

        else:
            print ("DOES NOT COMPUTE")
            return 'send_cv'

class Map(object):
    stages = {
        'send_cv': SendCv()
    }

    def __init__(self, start_stage):
        self.start_stage = start_stage

    def next_stage(self, stage_name):
        val = Map.stages.get(stage_name)
        return val

    def opening_stage(self):
        return self.next_stage(self.start_stage)

print ("Hello from my game")
a_map = Map('send_cv')
a_game = Engine(a_map)
a_game.play()
