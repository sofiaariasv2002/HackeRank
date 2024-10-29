##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (hash Tables)
# 28 oct 2024
##################################################################################################################

##################################################################################################################
# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him 
# through his handwriting. He found a magazine and wants to know if he can cut out whole words from 
# it and use them to create an untraceable replica of his ransom note. 
# The words in his note are case-sensitive and he must use only whole words available in the magazine. 
# He cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, 
# print Yes if he can replicate his ransom note exactly using whole words from the magazine; 
# otherwise, print No.
##################################################################################################################

def checkMagazine(magazine, note):
    magazineDict=dict()
    for word in magazine:
        if word not in magazineDict:
            magazineDict[word]=1
        else:
            magazineDict[word]= magazineDict[word]+1
    
    for wordNote in note:
        if wordNote not in magazineDict or magazineDict[wordNote]==0:
            print ("No")
            return 
        else:
            magazineDict[wordNote]= magazineDict[wordNote]-1
    print ("yes")

if __name__ == '__main__':
    magazine="give me one grand today night".rstrip().split()
    note = "give one grand today".rstrip().split()
    checkMagazine(magazine, note)