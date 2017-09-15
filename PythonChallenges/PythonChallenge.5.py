import re
import urllib.request
import Utils

SEED = '12345'

for x in range(0, 251):
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(SEED)) as response:

        html = str(response.read())
        print("Debug Iteration {0} -- seed: {1} -- html:\n{2}".format(x, SEED, html))
        regex = re.search("the next nothing is (\d+)", html)

        if(regex):
            SEED = int(regex.group(1))

        else:
            print("Iteration {0}: No next nothing. Possible result is -- \n{1}" .format(x, html))

            # Corner cases
            if("b'Yes. Divide by two and keep going.'"):
                SEED = int(SEED/2)

Utils.SubmitChallengeAnswer("peak")
