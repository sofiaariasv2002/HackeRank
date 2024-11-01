##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (sorting)
# 31 oct 2024
##################################################################################################################

##################################################################################################################
#You are given q queries. Each query is of the form two integers described below:
# - 1x : Insert x in your data structure.
# - 2y : Delete one occurence of y from your data structure, if present.
# - 3z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

# The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, 
# and queries[i][1] contains the data element.
##################################################################################################################

def freqQuery(queries):
    Result=[]
    queriesDict={}
    for query, val in queries:
        if query==1:
            if val not in queriesDict:
                queriesDict[val]=1
            else:
                queriesDict[val]=queriesDict[val]+1
        elif query==2:
            if val in queriesDict:
                queriesDict[val]=queriesDict[val]-1
                if queriesDict[val]==0:
                    queriesDict.pop(val)
            else:
                continue
        else:
            cant=queriesDict.values()
            if val in cant:
                Result.append(1)
            else:
                Result.append(0)
    return Result

if __name__ == '__main__':
    queries=[(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]
    print(freqQuery(queries))