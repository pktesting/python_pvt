import re

pattern = r"[^A-Z]"
if re.search(pattern , "this is all quite"):
    print ("Match 1")

if re.search(pattern,"AfhnoD123"):
    print ("Match 2")

if re.search(pattern,"DHUFIHGOSHVBGOS"):
    print("Match 3")