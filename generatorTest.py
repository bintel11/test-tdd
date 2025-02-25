def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Create a generator object
# Test comment
counter = count_up_to(3)

# Use the generator with the next() method
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3

# Uncommenting the following line will raise StopIteration because the generator is exhausted
# print(next(counter))  # Raises StopIteration

# Alternatively, use the generator in a for loop
for number in count_up_to(3):
    print(number)