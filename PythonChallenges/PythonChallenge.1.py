import webbrowser

result = pow(2, 38)
print("Result of 2^38 is %d. Now navigating to next level using calculated answer" % result)

webbrowser.open("http://www.pythonchallenge.com/pc/def/%d.html" % result)
