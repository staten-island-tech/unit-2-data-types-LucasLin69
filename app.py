num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def find_factors(num1num2):
    factors = []
    ball = []
    if num1 > num2:
        ball.append(num2)
    else:
        ball.append(num1)
    for i in range(2,ball+1):
        if ball % i == 0:
            factors.append(i)
    return factors
print(find_factors)
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

