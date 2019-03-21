

def string_compressor(input):
    seen = {}

    for i in input:
        if i in seen.keys():
            seen[i]+=1
        else:
            seen[i] = 1
