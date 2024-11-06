##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (sorting)
# 6 nov 2024
##################################################################################################################

##################################################################################################################
# A student is taking a cryptography class and has found anagrams to be very useful. 
# Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. 
# In other words, both strings must contain the same exact letters in the same exact frequency. 
# For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# he student decides on an encryption scheme that involves two large strings. 
# The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. 
# Determine this number.

# Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character 
# deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.
##################################################################################################################


def makeAnagram(a, b):
    adict={}
    bdict={}
    delete=0

    for char in a:
        if char in adict:
            adict[char]=adict[char]+1
        else:
            adict[char]=1

    for char in b:
        if char in bdict:
            bdict[char]=bdict[char]+1
        else:
            bdict[char]=1
    
    # print (adict)
    # print (bdict)
    adelete=adict.copy()
    bdelete=bdict.copy()

    for key in adict.keys():
        if key not in bdict.keys():
            delete += adelete[key]
            adelete.pop(key)
    
    for key in bdict.keys():
        if key not in adict.keys():
            delete += bdelete[key]
            bdelete.pop(key)
    
    for key in adelete.keys():
        delete+=abs(adelete[key]-bdelete[key])

    # print (adelete)
    # print (bdelete)
    # print (delete)

    return(delete)


if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
    print(makeAnagram(a, b))  
