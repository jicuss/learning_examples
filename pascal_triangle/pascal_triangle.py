'''
Objective:
    Write a program to calculate the Pascal triangle to a given depth

Example Triangle of Depth 5:
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1

'''

def pascal_triangle_recursive(result_array = [],max_depth = 1):
    '''
    Generate an entire Pascal triangle to a depth of N
    return an array of arrays, each child array contains integer elements of the row
    '''
    print 'result_array: ', result_array

    ''' as a starting point if the result_array is blank, populate it with the first row (1) '''
    if result_array == []:
        result_array.append([1])

    ''' if the result_array is already of greater or equal depth then specified, return it '''
    if len(result_array) > max_depth:
        return result_array

    else:
        last_row = result_array[len(result_array) - 1]
        new_row = pascal_triangle_row(last_row)
        result_array.append(new_row)
        return pascal_triangle_recursive(result_array,max_depth)

def pascal_triangle_row(last_row):
    '''  Generate a row of the Pascal triangle given the previous row '''
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
    '''
        Output: print a nicely formatted pascal triangle
        TODO: This looks great for shorter depths but as the triangle gets longer it gets skewed.
              A future improvement would be to determine that max character length of an element
              then base the centering strategy for all elements on that.
    '''
    str_triangle = map(lambda row: ' '.join(map(lambda element: str(element), row)), triangle)
    max_length = len(str_triangle[len(str_triangle) - 1])
    output = map(lambda row: row.center(max_length),str_triangle)
    for row in output:
        print row

def print_triangle(depth):
    display_pascal_triangle(pascal_triangle_recursive([],depth))