from turtle import Turtle, Screen
import pandas

# Read the csv file
data = pandas.read_csv('50_states.csv')

# Save state names to iterate
stateList = data['state'].to_list()


class Scoreboard(Turtle):
    stateList = data['state'].to_list()

    # initialize the screen and the score
    def __init__(self):
        super().__init__()
        self.newScreen = Screen()
        self.score = 0
        self.newScreen.title("U.S States Game")
        self.newScreen.setup(725, 500)
        self.newScreen.bgpic('blank_states_img.gif')
        self.answerState = ''
        self.notGuessed = []

    # Guess the state
    def guessState(self):
        self.answerState = self.newScreen.textinput(title=f'Guess the state {self.score}/50',
                                                    prompt="What's another state's name")
        if self.answerState != None:
            self.answerState = self.answerState.title()
        elif self.answerState == None:
            return False

        if self.answerState in stateList:
            index = stateList.index(self.answerState)
            self.score += 1
            self.getSpot()
            stateList.pop(index)
        else:
            pass

    # Create the state name
    def createStates(self, x, y, name):
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x, y)
        state.write(name)

    # move the name of the state
    def getSpot(self):
        state = data[data['state'] == self.answerState]
        x = int(state['x'])
        y = int(state['y'])
        print(x)
        print(y)
        self.createStates(x, y, name=self.answerState)

    def missedState(self):
        self.notGuessed = [state for state in stateList]

    def emptyPreviousMissed(self):
        self.notGuessed = []
