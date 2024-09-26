""" import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcf = math.gcd(num1, num2)
print(f"The greatest common factor of {num1} and {num2} is {gcf}.")
"""
verb = input("Say a verb: ")
noun = input("Say a noun: ")
past_tense_verb = input("Say a past tense verb: ")
number = input("Say a number: ")
celebrity = input("Say a celebrity: ")
MadLibs = (f"One day, I decided to {verb} to the park. To my surprise, I saw a {noun} there! Suddenly, I {past_tense_verb} and noticed that there were {number} people gathered around. Among them was none other than {celebrity}! It was an unforgettable day!")
print(f"This is your story: {MadLibs}")

