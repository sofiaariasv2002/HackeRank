import math


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]  
    answer = []  
    lastAnswer = 0

    for query in queries:
        x = query[1]  
        y = query[2]  
        idx = (x ^ lastAnswer) % n  
        if query[0] == 1:  
            arr[idx].append(y)  
        elif query[0] == 2:  
            lastAnswer = arr[idx][y % len(arr[idx])]  
            answer.append(lastAnswer)  

    return answer

if __name__ == '__main__':
    n=2
    queries = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0]
    ]

    result = dynamicArray(n, queries)
    print(result)