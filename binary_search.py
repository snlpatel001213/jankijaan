import math
sorted_array = [i for i in range(0,1000)]
fixed = 67

min = 0
max = len(sorted_array)
n = 0
while True:
    guess = int((max+min)/2)
    if sorted_array[guess] == fixed:
        print(sorted_array[guess], n, math.log(1000,2))
        break
    if sorted_array[guess] < fixed:
        min = guess+1
    if sorted_array[guess] > fixed:
        max = guess
    n = n + 1

