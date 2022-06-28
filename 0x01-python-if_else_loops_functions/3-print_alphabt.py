#!/usr/bin/python3
for sletter in range(97, 123):
    if chr(sletter) is not 'q' and chr(sletter) != 'e':
        print("{}".format(chr(sletter)), end="")
