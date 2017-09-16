import pickle
import urllib.request 
import Utils

###### BEWARE:  Python's Pickle module has security implications!!  ######
 
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = pickle.loads(urllib.request.urlopen(url).read())

# Can likely be cleaned up & made more pythonic
for line in data:
    lineOutput = ""
    for elt in line:
        lineOutput += (elt[0] * elt[1])
    print(lineOutput)

Utils.SubmitChallengeAnswer("channel")
