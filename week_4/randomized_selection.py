from random import randrange

def partition(x, pivot_index = 0):
    """
    takes in array x 
    and pivot index, with default = 0
    returns partitioned array with lower values to left of pivot and higher
    values to the right - not necessarily sorted. 
    """
    i = 0
    len_x = len(x)
    if pivot_index !=0: 
        x[0], x[pivot_index] = x[pivot_index], x[0]
        
    for j in range(len_x-1):
        if x[j+1] < x[0]:
            x[j+1], x[i+1] = x[i+1], x[j+1]
            i += 1
    x[0], x[i] = x[i], x[0]
    
    return x, i


def random_select(x, k):
    """
    takes x array and uses a random integer k as the pivot index
    returns the kth order statistic/ k index value
    """
    len_x = len(x)
    if len_x == 1:
        return x[0]
    
    else:
        xpart, j = partition(x, randrange(len_x))

        if j == k:
            return xpart[j]
        elif j > k:
            return random_select(xpart[:j], k)
        else:
            k = k - j - 1                           
            return random_select(xpart[(j+1):], k)
        
x = [3,1,8,4,7,9]
for i in range(len(x)):
    print(random_select(x, i))

