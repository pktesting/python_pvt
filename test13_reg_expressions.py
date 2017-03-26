import re

str = "My name is Puneet.Hi Puneet"
pattern = r"Puneet"
newstr = re.sub(pattern, "PK", str)
print(newstr)

'''
This program tells how to find & replace a string.
'''
