##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (sorting)
# 6 nov 2024
##################################################################################################################

##################################################################################################################
# Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
# It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will 
# occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
##################################################################################################################

def alternatingCharacters(s):
    delete = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            delete += 1
    return delete


if __name__ == '__main__':
    s='BBBBB'
    print(alternatingCharacters(s))