import sys
from src.asteroid import Asteroid, Asteroid2, Asteroid3
from src.player import Player
from Constants import *
from Weapon import *
import random
import os

class Score:
    def print_score(self):
        with open("Score_tracker.txt") as x:
            totals = []
            total = 0
            for line in x:
                totals.append(int(line))
        for y in totals:
            total = total + y
        print(total)
    def clear_score(self):
        score_file = open("Score_tracker.txt","w")
        score_file.truncate()
        score_file.close()