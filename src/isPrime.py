def is_prime(number):
    if number >= 2:
        for num in range(2, number):
            if not (number % num):
                return False
    else:
        return False
    return True


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if is_prime(num):
    print("Prime!")
else:
    print("Not Prime")
