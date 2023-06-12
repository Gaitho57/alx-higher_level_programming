#!/usr/bin/python3

# Assign the value 89 to the variable 'a'
a = 89

# Assign the value 10 to the variable 'b'
b = 10

# Swap the values of 'a' and 'b' using tuple packing and unpacking
# The values of 'a' and 'b' are packed into a tuple (b, a), and then unpacked back into 'a' and 'b'
a, b = b, a

# Print the values of 'a' and 'b' using string formatting
print("a={:d} - b={:d}".format(a, b))

