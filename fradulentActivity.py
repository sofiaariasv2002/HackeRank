##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (sorting)
# 1 nov 2024
##################################################################################################################

##################################################################################################################
# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
# If the amount spent by a client on a particular day is greater than or equal to 2x the client's median 
# spending for a trailing number of days, they send the client a notification about potential fraud. 
# The bank doesn't send the client any notifications until they have at least that trailing number of prior days' 
# transaction data.

#Given the number of trailing days d and a client's total daily expenditures for a period of n days, 
# determine the number of times the client will receive a notification over all n days.
##################################################################################################################

# def activityNotifications(expenditure, d):
#     median=[]
#     day= expenditure[d]
#     notifications=0
    
#     for i in range(len(expenditure)-d):
#         for j in range(i,d):
#             median.append(expenditure[j])
#         median.sort()  

#         if len(median)==0:
#             tam=len(median)
#             med=(median[tam//2]+median[(tam//2)-1])/2
#         else:
#             tam=len(median)
#             med=median[(tam//2)]

#         day=expenditure[d]
#         if day >=med*2:
#             notifications+=1

#         median.clear()
#         d=d+1
    
#     return (notifications)

######################################################################################

from bisect import bisect, insort

def activityNotifications(expenditures, d):
    res = 0
    vals = sorted(expenditures[:d])
    
    for first_val, cur_val in zip(expenditures, expenditures[d:]):
        if d % 2:
            median2 = 2 * vals[d//2]
        else:
            median2 = vals[d//2] + vals[d//2-1]
            
        if cur_val >= median2:
            res += 1
            
        vals.pop(bisect(vals, first_val) - 1)
        insort(vals, cur_val)
        
    return res

################################################################################

# def activityNotifications(expenditure, d):
#     notifications = 0
    
#     for i in range(len(expenditure) - d):
#         # Toma el subconjunto deslizante de tamaño d
#         window = expenditure[i:i + d]
#         window.sort()
        
#         # Calcula la mediana dependiendo de si d es par o impar
#         if d % 2 == 0:
#             med = (window[d // 2 - 1] + window[d // 2]) / 2
#         else:
#             med = window[d // 2]
        
#         # Revisa si el gasto actual es al menos el doble de la mediana
#         day = expenditure[i + d]
#         if day >= 2 * med:
#             notifications += 1

#     return notifications


if __name__ == '__main__':
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

    d=5
    (activityNotifications(expenditure, d))