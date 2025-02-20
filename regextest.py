import re

txt = "The rain in Spain hello"
x = re.search("^The.*Spain$", txt)

print(x)

txt1 = "The rain in spain"
y = re.search("\s", txt1)

print("the first whitespace char is located in position: ",y.start())
regex = r"([a-zA-Z]+) ([0-9]+)"
string = "The quick brown fox jumped over the lazy dog 3 times"
z = re.search(regex, string)
if z != None:
    print("Match at index %s, %s" % (z.start(), z.end()))
    print("Full match: %s" % (z.group(0)))
    print("Animal: %s" % (z.group(1)))
    print("Times: %s" % (z.group(2)))
else:
    print("The regex pattern does not match")