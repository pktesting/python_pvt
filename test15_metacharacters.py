import  re

pattern = r"^gray$"

if re.match(pattern , "wrey"):
    print ("hello")

if re.match(pattern, "wray"):
    print ("world")

if re.match(pattern, "blue"):
    print ("bye")