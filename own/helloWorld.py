# Hello World in Python

# Your first Python program in this class
# Procedure-oriented Program
# Using function

# Function declaration. main: function name
def main():
    print("Hello, world")
    print("This program computes the average of the exam")

    score1, score2 = input("Enter exam scores by a comma: ").split(',')
    average = (float(score1) + float(score2)) / 2.0

    print("The average of the scores is: ", average)

main()