# running through tutorial https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
# from first import *

import math

def is_prime(number):
    """Return True if number is prime."""
    if number <= 1:
        return False

    max_element = int(math.ceil(math.sqrt(number)))
    # iterate through all elements from 2 through sqrt(n)
    for element in range(2,max_element + 1):
        if number % element == 0:
            return False

    return True

def return_primes_through_n(n):
    '''
    :param n: the max integer to look for primes through
    :return: An array of all primes <= n
    '''
    primes = []
    for element in range(0,n + 1):
        if is_prime(element):
            primes.append(element)

    return primes


def print_next_prime(number):
    """ Print the closest prime number larger than number.  """
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
