"""
Script Name: reconstructSentence.py
Description: This script reads two text files and reconstructs/combines their contents in a specific order to produce a complete output sentence.
Command Line Arguments: Two text files names (e.g. input1.txt input2.txt)
Example Invocation: python3 reconstructSentence.py input1.txt input2.txt
"""

import sys

def reconstruct_sentence(file1, file2):

    # Open and read the files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        list1 = f1.read().strip().split()
        list2 = f2.read().strip().split()

    print("list1 is:", list1)
    print("list2 is:", list2)

    list1Length = len(list1)
    list2Length = len(list2)

    print("list1Length:", list1Length)
    print("list2Length:", list2Length)

    # Initialize the output list
    out = []

    # Loop until both lists are empty
    while list1 or list2:
        if list1:
            out.append(list1.pop())  # Get the last word from list1
        if list2:
            out.append(list2.pop())  # Get the last word from list2

    print("The list out is:", out)

    # Write the output list to a file
    with open("output.txt", "w") as f3:
        for word in out:
            f3.write(word + ' ')
        
if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    reconstruct_sentence(file1, file2)
