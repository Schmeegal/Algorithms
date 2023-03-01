def sum(numbers):
    '''
    Uncomment print statements to help understand recursion process
    recursive function must have a break condition (the if statement)
    '''
    if not numbers:
        return 0
    #print("Calling sum(%s)" % numbers[1:])
    remaining_sum = sum(numbers[1:])
    #print("Call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum


print(sum([1,6,3,15,8,14]))