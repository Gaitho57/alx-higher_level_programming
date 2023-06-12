#!/usr/bin/python3

def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence == "":
        # If the sentence is empty, return a tuple with 0 and None
        return 0, None

    # Return a tuple with the length of the sentence and its first character
    return len(sentence), sentence[0]

