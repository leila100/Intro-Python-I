def is_prime(number):
    if number >= 2:
        for num in range(2, number):
            if not (number % num):
                return False
    else:
        return False
    return True


def removeNonPrime(numbers, num, i):
    # remove all multiples of the prime number
    if(i + 1) > len(numbers):
        return
    for i in range(i+1, len(numbers)):
        if (numbers[i][0] % num == 0) and (numbers[i][1]):
            numbers[i][1] = False


def soe(number):
    numbers = [[num, True] for num in range(2, number+1)]
    for i in range(0, len(numbers)):
        if(is_prime(numbers[i][0])):
            removeNonPrime(numbers, numbers[i][0], i)
    answer = [num[0] for num in numbers if num[1]]
    return answer


# Read a number from the keyboard
num = input("Up to how many numbers you wish to check? (>= 2) ")
num = int(num)

print(soe(num))
