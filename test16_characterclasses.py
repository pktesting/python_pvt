import re

pattern = r"[aeiou]"

if re.search(pattern,"grey"):
    print("Got it")

if re.search(pattern,"hello"):
    print("Got it 2")

if re.search(pattern, "rtvs"):
    print("pergo")