import Utils
import re

INPUT_DATA = Utils.GetChallengeInput(4)

'''
Pattern matches:
    - at least 1 non-captialized followed by --  [^A-Z]+
    - exactly 3 capitalized followed by      --  [A-Z]{3}
    - exactly 1 lowercase followed by        --  ([a-z])
    - exactly 3 capitalized followed by      --  [A-Z]{3}
    - at least 1 non capitalized             --  [^A-Z]+
'''
pattern = re.compile(''.join(['[^A-Z]+', '[A-Z]{3}', '([a-z])', '[A-Z]{3}', '[^A-Z]+']))
matches = pattern.findall(INPUT_DATA)

print("Results matching the regex pattern are: {0}".format(matches))
ANSWER = ''.join(matches)

Utils.SubmitChallengeAnswer(ANSWER)
