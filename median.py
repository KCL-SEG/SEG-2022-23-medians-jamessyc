"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers = sorted(numbers)
        length = len(numbers)
        if length % 2 == 0:
            middle = length / 2
            middle_l, middle_r = int(middle - 1), int(middle) 
            numbers = (numbers[middle_l] + numbers[middle_r]) / 2
        elif length % 2 == 1:
            middle = int(length / 2 - 0.5)
            numbers = numbers[middle]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
