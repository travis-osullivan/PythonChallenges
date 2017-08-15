import webbrowser

result = pow(2, 38)
print("Result of 2^38 is {0}. Now navigating to next level using calculated answer".format(result))

webbrowser.open("http://www.pythonchallenge.com/pc/def/{0}.html".format(result))
