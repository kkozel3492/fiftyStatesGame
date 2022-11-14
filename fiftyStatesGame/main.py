import turtle

import pandas

from scoreboard import Scoreboard

screen = Scoreboard()
missingState = []

gameOn = True
while gameOn:
    screen.emptyPreviousMissed()
    go = screen.guessState()
    screen.missedState()
    if screen.score == 50 or go == False or screen.answerState == "Exit":
        gameOn = False

newData = pandas.DataFrame(screen.notGuessed)
newData.to_csv('statesToLearn.csv')

turtle.mainloop()
