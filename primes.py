"""List of prime numbers generator."""

def primes(number_of_primes):
    if (number_of_primes < 1):
        raise ValueError(" Cannot enter numbers less than 1")
    else:
        list = []

        count = 0 #to count the number of prime numbers found
        num = 0 #testing if number is prime
        while ( count < number_of_primes):
            if isprime(num) == True:
                count += 1
                list.append(num)
                num += 1
            else:
                num += 1

        return list

def isprime(num):

    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                return False
        return True
    else:
        return False
