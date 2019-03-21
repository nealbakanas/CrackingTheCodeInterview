input1 = 'pales'
input2 = 'bake'

# attempt 1
def count_dict(input):
    the_dict = {}
    for x in input:
        if x in the_dict.keys():
            the_dict[x]+=1
        else:
            the_dict[x]=1
    return the_dict

def compare_dicts(a,b):
    diff = 0
    for key in a:
        if key in b.keys():
            diff += abs(a[key] - b[key])
        else:
            diff += a[key]
    if diff > 1:
        return False
    else:
        return True
#
# input1 = count_dict(input1)
# input2 = count_dict(input2)
# print compare_dicts(input1,input2)


def compare_inputs(a,b):
    count=0
    if len(b) + 2 <= len(a) or len(b) - 2 >= len(a):
        return False
    else:
        for x in range(len(a)):
            try:
                if a[x]!=b[x]:
                    count+=1
            except IndexError:
                count+=1
    return count == 1

print compare_inputs(input1,input2)
