input = "Mr Neal Bakanas"




def urlifier(in_here):
    split = in_here.split()

    urlified = '%20'.join(split)

    return urlified

print urlifier(input)