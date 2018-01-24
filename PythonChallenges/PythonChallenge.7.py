import os
import re
import zipfile

import Utils

sourceZip =  os.path.join(os.path.dirname(__file__),
                          Utils.__INPUT_DIRECTORY__, 
                          "Challenge.7.channel.zip")

with zipfile.ZipFile(sourceZip) as archive:
    with archive.open("readme.txt") as readme:
        print(readme.read())


    SEED = "90052.txt"
    for i in range(0, 1000):
        with archive.open(SEED) as seedContents:
            seed_str = seedContents.read().decode('utf-8')
            #print("Debug Iteration {0} -- seed: {1} -- contents:\n{2}".format(i, SEED, seed_str))
            #print(seed_str)
            regex = re.search("Next nothing is (\d+)", seed_str)
            
            if regex:
                SEED = regex.group(1) + ".txt"

    # "46145.txt" is final --->> "Collect the comments."
    # archive.comment() is a thing...
