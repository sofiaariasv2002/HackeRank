# There is a collection of input strings and a collection of query strings. 
# For each query string, determine how many times it occurs in the list of input strings. 
# Return an array of the results.

def matchingStrings(stringList, queries):
    result=[]
    for query in queries:
        cont=0
        for listElement in stringList:
            if listElement== query:
                cont=cont+1
        result.append(cont)
    return result

if __name__ == '__main__':
    stringList=['ab', 'ab', 'abc']
    queries=['ab', 'abc','bc']
    #result=[2,1,0]

    print(matchingStrings(stringList, queries))
