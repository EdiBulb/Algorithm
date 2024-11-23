# Create a List of Numbers

# using a traditional for loop
numbers = []    
for i in range(4):
    numbers.append(i)
print(numbers)

# using a list comprehension
numbers = [i for i in range(5)]
print(numbers)

# adding a condition
even_numbers = []   
for i in range(10):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)