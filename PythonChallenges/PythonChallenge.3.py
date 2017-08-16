import Utils

INPUT_DATA = Utils.GetChallengeInput(3)

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

Utils.SubmitChallengeAnswer(ANSWER)
