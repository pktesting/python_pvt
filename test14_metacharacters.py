import re

pattern = r"gr.y"

if re.match(pattern,"grey"):
    print ("Method 1")

if re.match(pattern , "gray"):
    print ("Method 2")

if re.match(pattern , "blue"):
    print ("Method 3")