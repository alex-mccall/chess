from typing import Text

text = input("Brackets")

open = 0
closed = 0

for count in range(len(text)):
  if text[count] == "(":
    open = open + 1
  if text[count] == ")":
    closed = closed - 1
print(open, closed)