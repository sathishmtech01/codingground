'''
Fun with for loop
'''
def trick01():
    # for loop in single line
    # Using one line code dictonary and array
    
    # dictonary with key value, for loop
    dict1 = {x: 10 * x for x in range(5)}
    # dictonary with only value, basically a set operation, for loop
    dict2 = {10 * x for x in range(5)}
    #array with values, for loop
    array1 = [10 * x for x in range(5)]
    
    return dict1,dict2,array1

'''
Fun with zip
'''
def trick02():
    # Zip function
    l = [[1, 2, 3], [4, 5, 6]]
    # Transpose
    Transpose = [x for x in zip(*l)]
    
    # Dividing the list in group of n
    l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
    
    Dividing = [x for x in zip(*[iter(l)] * 3)]
    iteration = [i for i in iter(l)]
    return Transpose,Dividing,iteration
    
