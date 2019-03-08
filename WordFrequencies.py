# Design a method to find the frequency of occurrences of any given word in a book.
# What if were running this algorithm multiple times?


book = '''Once upon a time, there was a little girl who lived in a village near the forest.  Whenever she went out, the 
little girl wore a red riding cloak, so everyone in the village called her Little Red Riding Hood.
One morning, Little Red Riding Hood asked her mother if she could go to visit her grandmother as it had been awhile 
since they'd seen each other. "That's a good idea," her mother said.  So they packed a nice basket for Little Red Riding 
Hood to take to her grandmother.'''
dictionary = {}
for word in book.split():
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
print (dictionary)
print (dictionary["Little"])