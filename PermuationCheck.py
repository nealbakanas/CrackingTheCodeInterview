first_string = 'racecar'
second_string = 'acercar'


def Check_Perm(first,second):

    if len(first)!=len(second):
        return False


    if sorted(first) == sorted(second):
        return True
    else:
        return False


if Check_Perm(first_string,second_string):
    print first_string, 'and ', second_string, 'are permutations!'
else:
    print 'Nope!'
