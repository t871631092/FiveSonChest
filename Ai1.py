import random
import main

ScoreModel=[(10, (0,1,1,0,0)), #Model of chest 好像没什么卵用?
            (10, (0,0,1,1,0)),
            (20, (1,1,0,1,0)),
            (30, (0,0,1,1,1)),
            (30, (1,1,1,0,0)),
            (50, (0,1,0,1,1,0)),
            (50, (0,1,1,0,1,0)),
            (50, (1,1,1,0,1)),
            (50, (1,1,0,1,1)),
            (50, (1,0,1,1,1)),
            (50, (0,1,1,1,1)),
            (50, (1,1,1,1,0)),
            (100,(0,1,1,1,1,0)),
            (999,(1,1,1,1,1,1))]

def scan():
    score = 0
    #global chest_table
    x=0
    y=0
    count=0
    tablescore = [[[0 for count in range(5)] for x range(19)] for y in range(19)]
    print(tablesocore)
    # for a in range(0,19):
    #     for b in range(0,19):
    #         if chest_table[a][b] == 0:
    #             score += 0
    # break

scan()