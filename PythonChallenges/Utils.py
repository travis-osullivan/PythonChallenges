import os
import webbrowser

__INPUT_DIRECTORY__ = "ChallengeInputs"
__CHALLENGE_URLS__ = "http://www.pythonchallenge.com/pc/def/"

def GetChallengeInput(n):
    inFile = os.path.join(os.path.dirname(__file__),
                          __INPUT_DIRECTORY__,
                          "Challenge.{0}.txt".format(n))

    print("Fetching input data from: {0}".format(inFile))
    with open(inFile) as inputFile:
        return inputFile.read()

def SubmitChallengeAnswer(ans):
    webbrowser.open(__CHALLENGE_URLS__ + ans + ".html")
