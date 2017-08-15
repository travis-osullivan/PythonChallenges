import webbrowser

CIPHER_TEXT = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

TRANS = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                      "cdefghijklmnopqrstuvwxyzab")

PLAIN_TEXT = CIPHER_TEXT.translate(TRANS)

print("Cipher: \n%s\n" % CIPHER_TEXT)
print("Plain: \n%s\n" % PLAIN_TEXT)

URL_SECRET = "map"
webbrowser.open("http://www.pythonchallenge.com/pc/def/%s.html" % URL_SECRET.translate(TRANS))
