##################################################################################################################
# Sofia Arias villa
# HackerRank - interview preparation kit (hash Tables)
# 28 oct 2024
##################################################################################################################

##################################################################################################################
# Given two strings, determine if they share a common substring. A substring may be as small as one character.
##################################################################################################################

def twoStrings(s1, s2):
    s1Dict=dict()
    for letter in s1:
        s1Dict[letter]=None

    for letters2 in s2:
        if letters2 in s1Dict:
            return ("YES")
    return ("NO")

if __name__ == '__main__':
    s1="hello"
    s2 = "wrd"
    print (twoStrings(s1, s2))