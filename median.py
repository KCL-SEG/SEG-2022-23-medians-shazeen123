


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

lower_position = int(len(numbers)/2) - 1
upper_position = int(len(numbers)/2)


if len(numbers) % 2 == 0:
     median = (numbers[lower_position] + numbers[upper_position])/2
else:
    median = numbers[upper_position]

print(median)