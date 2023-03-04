
def reverse(num):
    revs_num = 0
    while num > 0:
        remainder = num % 10  
        revs_num = (revs_num * 10) + remainder  
        num = num // 10  
    return revs_num

def palindrome(num):
    rev = reverse(num)
    if rev == num:
        return True
    else:
        return False


#print(reverse(12345))
#print(palindrome(12321))
