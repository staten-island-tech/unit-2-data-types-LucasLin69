import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
values = {}
if num1 > num2:
    values.append(num1)
elif num2 > num1:
    values.append(num2)
else:
    values.append(num1)
factors = []
for i in range(2, values+1):
    if values % i ==(0):
        factors.append(values)
print(f"The GCF of {num1} and {num2} is {factors}")
"""
verb = input("Say a verb: ")
noun = input("Say a noun: ")
past_tense_verb = input("Say a past tense verb: ")
number = input("Say a number: ")
celebrity = input("Say a celebrity: ")
MadLibs = (f"One day, I decided to {verb} to the park. \
To my surprise, I saw a {noun} there! Suddenly, I {past_tense_verb} and noticed that there were {number} people gathered around. \
 Among them was none other than {celebrity}! It was an unforgettable day!")
print(f"This is your story: {MadLibs}")"""

