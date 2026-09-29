# CS 1430 - Practice 1: Say It Again
#
# Ask for a whole number, then ask for a phrase, then print the phrase
# that many times. The steps are in README.md.
#
# Write your code below this comment.
number = input("Give a Number: ")
number = int(number)
phrase = input("Give a Phrase: ")

result = phrase * number

print(result)