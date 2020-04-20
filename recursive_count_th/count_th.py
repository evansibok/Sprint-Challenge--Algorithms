'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# Function should take in a string of words
# Must return a count of how the total number of times *th* occurs within the input.
# Case matters ->
# If you check for lower case, the count should only be lowercase found in the input
# If you check for upper case, the count should only be uppercase found in the input
# No loops contained, it must call itself

# UPER
#   Understand
#   Plan
# 1. If string is empty return 0
# 2. If string has one character return 0
# 3. If char at current index + char at current+1 equals phrase count
# 4. move forward one iteration and start from 3 above


def count_th(word):
    phrase = "th"

    # TBC

    if len(word) <= 1:
        return 0
    elif word[:2] == phrase:
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
