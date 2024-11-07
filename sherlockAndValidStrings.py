def isValid(s):
    sdir={}
    for letter in s:
        if letter not in sdir:
            sdir[letter]=1
        else:
            sdir[letter]=sdir[letter]+1
        
    values=list(sdir.values())
    valuesset=set(sdir.values())

    if len(valuesset)==1:
        return ('YES')
    elif len(valuesset)>2:
        return('NO')
    else:
        maxi=max(list(valuesset))
        mini=min(list(valuesset))
        cantmini=values.count(mini)
        cantmaxi=values.count(maxi)

        if (mini-1 == 0 and cantmini==1)or (maxi-mini==1 and cantmaxi==1):
            return ('YES')
        else: 
            return('NO')

if __name__ == '__main__':
    #s='aabbc' #yes
    #s='abcdefghhgfedecba' #yes
    #s='abccc' #no
    #s='abcc' #yes
    s='aabbcd' #no
    print(isValid(s))