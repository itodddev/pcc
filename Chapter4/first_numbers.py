for value in range(1, 5): # starting range, ending range (not inclusive), range(6) will go from 0..5
    print(value)

numbers = list(range(1, 6)) # Create a list of numbers 1..5
print(numbers)

even_numbers = list(range(2, 11, 2)) # Even numbers 1..10, 3rd param is step
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(f'Squares: { squares }')

# Using list comprehension
squares = [value ** 2 for value in range(1, 11)]
print(f'List Comprehension Squares: { squares }')

# Simple Statistics with List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(f'Min: { min(digits) }')
print(f'Max: { max(digits) }')
print(f'Sum: { sum(digits) }')