
# ******************************
# Make your Code
# ******************************
numbers = []
sum = 0
for i in range(5):
    x = int(input())
    numbers.append(x)
    sum += x
average = sum/len(numbers)
for j in range(5):
    if numbers[j] > average:
        print(numbers[j], end=" ")