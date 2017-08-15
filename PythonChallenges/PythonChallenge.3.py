import webbrowser
import os

SCRIPT_DIR = os.path.dirname(__file__) #<-- absolute dir the script is in
REL_PATH = "ChallengeInputs\\Challenge.3.txt"
INPUT_PATH = os.path.join(SCRIPT_DIR, REL_PATH)

with open(INPUT_PATH) as inputFile:
    INPUT_DATA = inputFile.read()

COUNT_DICT = {}
for elt in INPUT_DATA:
    if elt not in COUNT_DICT:
        COUNT_DICT[elt] = 1
    else:
        COUNT_DICT[elt] = COUNT_DICT[elt] + 1

ANSWER = ""
for entry in COUNT_DICT:
    print("{0}: {1}".format(entry, COUNT_DICT[entry]))
    if COUNT_DICT[entry] == 1:
        ANSWER += entry

webbrowser.open("http://www.pythonchallenge.com/pc/def/{0}.html".format(ANSWER))
