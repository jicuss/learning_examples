
def find_indices(element,array):
    ''' return the indices of all instances of an element in an array '''
    indices = [i for i, x in enumerate(array) if x == element]
    return indices

def find_first_non_repeated_character_in_a_string(string):
    ''' string_operation: find first non repeated character in a string '''
    character_array = list(string)
    non_repeating_characters = filter(lambda c: len(find_indices(c,character_array)) == 1,character_array)
    try:
        return non_repeating_characters[0]
    except IndexError:
        print 'No non repeating characters'

def reverse_a_string_iteratively(string):
    ''' string_operation: reverse a string iteratively '''
    output = []
    for index in range(1,len(string) + 1):
        output.append(string[-index])
    return ''.join(output)

def reverse_a_string_recursively(string,output = []):
    ''' string_operation: find first non repeated character in a string '''
    if len(string) == 0:
        return ''.join(output)
    else:
        output.append(string[len(string) - 1])
        string = string[:(len(string) - 1)]
        return reverse_a_string_recursively(string,output)

def determine_if_strings_are_anagrams(string_a,string_b):
    array_string_a = list(string_a); array_string_a.sort()
    array_string_b = list(string_b); array_string_b.sort()
    if array_string_a == array_string_b:
        return True

def determine_if_string_is_palindrome(string):
    no_spaces = string.replace(' ','')
    if no_spaces == reverse_a_string_recursively(no_spaces,[]):
        return True

def determine_if_string_is_all_unique_characters(string):
    character_array = list(string)
    repeating_characters = filter(lambda c: len(find_indices(c,character_array)) > 1,character_array)
    if len(repeating_characters) == 0:
        return True

def determine_if_string_is_a_int_or_double(string):
    response = 'neither'
    try:
        if str(float(string)) == string:
            response = 'double'
    except:
        ''

    try:
        if str(int(string)) == string:
            response = 'int'
    except:
        ''

    return response
