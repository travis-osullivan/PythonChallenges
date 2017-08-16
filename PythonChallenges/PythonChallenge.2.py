import Utils

CIPHER_TEXT = Utils.GetChallengeInput(2)

TRANS = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                      "cdefghijklmnopqrstuvwxyzab")

PLAIN_TEXT = CIPHER_TEXT.translate(TRANS)

print("Cipher: \n{0}\n\nPlain: \n{1}\n".format(CIPHER_TEXT, PLAIN_TEXT))

URL_SECRET = "map"
Utils.SubmitChallengeAnswer(URL_SECRET.translate(TRANS))
