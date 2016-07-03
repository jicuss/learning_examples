def pascal_triangle_recursive(result_array = [],max_depth = 1):
    '''  Generate an entire Pascal triangle to a depth of N  '''
    print 'result_array: ', result_array
    if result_array == []:
        result_array.append([1])
    if len(result_array) > max_depth:
        return result_array
    else:
        last_row = result_array[len(result_array) - 1]
        new_row = pascal_triangle_row(last_row)
        result_array.append(new_row)
        return pascal_triangle_recursive(result_array,max_depth)

def pascal_triangle_row(last_row):
    '''  Generate a row of the Pascal triangle given the previous row'''
    new_row = []
    for index in range(0,len(last_row) + 1):
        try:
            if index == 0:
                prev = 0
            else:
                prev = last_row[index - 1]
            next = last_row[index]
            new_row.append(prev + next)
        except IndexError:
            new_row.append(1)
    return new_row

def display_pascal_triangle(triangle):
    ''' print a nicely formatted pascal triangle  '''
    str_triangle = map(lambda row: ' '.join(map(lambda element: str(element), row)), triangle)
    max_length = len(str_triangle[len(str_triangle) - 1])
    output = map(lambda row: row.center(max_length),str_triangle)
    for row in output:
        print row

def print_triangle(depth):
    display_pascal_triangle(pascal_triangle_recursive([],depth))