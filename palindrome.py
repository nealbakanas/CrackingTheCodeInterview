import re

input = 'Never. odd. or .even.'


def Palindromes(in_here):
    count_dict = {}
    pattern = re.compile('[\W_]+',re.UNICODE)
    in_here = pattern.sub('',in_here).lower()

    for x in in_here:
        if x in count_dict.keys():
            count_dict[x] += 1
        else:
            count_dict[x] = 1

    odd_count = 0
    for k in count_dict:
        if count_dict[k] & 1:
            odd_count += 1
    if (odd_count>1):
        return False
    else:
        return True


print Palindromes(input)
