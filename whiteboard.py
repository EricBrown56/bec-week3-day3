'''
# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

'''
# determine if the integer is positive, if so, we will count the numbers of integers. If its negative we will add them together

# if x > 0 count those numbers if x is <0 add them

def solution(integer):
    num = 0
    add = []
    if len(integer) == 0:
        return []
    for x in integer:
        if x > 0:
            num += 1
    
        else:
            add.append(x)
        

    return [num, sum(add)]


