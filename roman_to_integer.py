def roman_to_integer(s):
    d = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    s = s[::-1]
    integer = 0
    integer += d[s[0]]
    for i in range(1, len(s)):
        if d[s[i]] >= d[s[i-1]]:
            integer += d[s[i]]
        else:
            integer -= d[s[i]]
    
    return integer

print(roman_to_integer("MCMXCIV"))
