import Utils

INPUT_DATA = Utils.GetChallengeInput(3)

COUNT_DICT = {}
for elt in INPUT_DATA:
    # Fancy, Pythonic upsert. Returns count, if key exists, or defaults to 0 if key not found
    # Then increments in either case
    COUNT_DICT[elt] = COUNT_DICT.setdefault(elt, 0) + 1

ANSWER = ""
# TODO: clean this up as well. Dictionary Comprehensions look promising
for entry in COUNT_DICT:
    print("{0}: {1}".format(entry, COUNT_DICT[entry]))
    if COUNT_DICT[entry] == 1:
        ANSWER += entry

Utils.SubmitChallengeAnswer(ANSWER)
