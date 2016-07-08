# First, calculate the fibonacci sequence by using a loop
def fibonacci_loop(number):
    ''' all fibonacci elements where element is <= n '''

    results = []
    first_element = 0
    second_element = 0
    # for element in range(0,number + 1):
    while True:
        sum = (first_element + second_element)

        if sum > number:
            break
        else:
            results.append(sum)

        if sum == 0:
            first_element = 1
        else:
            first_element = second_element

        second_element = sum

    return results

# Second, calculate the fibonacci sequence by using a loop. A better approach
def fibonacci_recurse(number, results = [], first_element = 0, second_element = 0):
    sum = (first_element + second_element)
    if sum > number:
        return results
    else:
        results.append(sum)
        if sum == 0:
            results.append(1)
            sum = 1
        return fibonacci_recurse(number, results, second_element, sum)
