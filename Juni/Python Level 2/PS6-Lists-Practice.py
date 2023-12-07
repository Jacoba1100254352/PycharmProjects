# Create a list called nums. Add the numbers 10 to 0 to the list using a loop. Then, print out nums.

nums = []
for i in range(10, -1, -1):
    nums.append(i)
print(nums)

# Ask the user for a word. Create a list of all of the letters in the word. Then, print out the list.

word = input("Type in a word: ")
letters = []
for letter in word:
    letters.append(letter)
print(letters)

# Create a list of all of the perfect squares between 1 to 10,000. Then, print out the list.

squares = []
for i in range(1, 101):
    squares.append(i * i)
print(squares)

# Take your list of perfect squares and remove the numbers any numbers between 2000 and 3000. Then, print out the list.

for i in range(2000, 3001):
    if i in squares:
        squares.remove(i)
print(squares)


# Copy and paste your factorial function from the other day. Use that function to create a list of all the factorials from 1! to 25!. Then, print out the list.

def factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


factorials = []
for i in range(1, 26):
    factorials.append(factorial(i))
print(factorials)


# Write a function that takes in a list and returns the sum of the numbers.

def sumList(x):
    answer = 0
    for num in x:
        answer += num
    return answer


print(sumList(factorials))


# Challenge: Write a function that takes in a list and returns the largest number in the list. Don't forget that lists can have all negative numbers!

def findMaxNum(x):
    maxNum = x[0]
    for num in x:
        if num > maxNum:
            maxNum = num
    return maxNum


print(findMaxNum(factorials))
