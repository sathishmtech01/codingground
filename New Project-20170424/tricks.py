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