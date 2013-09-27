"""
open file named on command line
for loop:
    count how many times each letter occurs in the file
print results of counting in alphabetical order
visualize with spark
"""

from sys import argv
# import locale 



script, input_file = argv

txt = open(input_file)
first_letter = txt.read()
first_letter = first_letter.lower()
# lower appears to take a string...?



letter_count = [0] * 26


for i in first_letter:
    index = ord(i) - 97
    # if 0 <= index <= 26:
    if index >= 0 and index <= 26:
        letter_count[index] += 1
    #index[letter_count] += 1

for i in letter_count:
    print i