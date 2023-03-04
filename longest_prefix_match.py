def longestCommonPrefix(strs):
    first, last = min(strs), max(strs)
    print(first)
    print(last)
    prefix = ''
    for ind in range(min(len(first), len(last))):
        if first[ind] != last[ind]:
            break
        prefix += first[ind]

    return prefix

#strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
strs = ["pilot", "pills", "pillow", "piles"]

print(longestCommonPrefix(strs))