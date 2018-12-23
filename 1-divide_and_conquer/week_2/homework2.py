"""This file contains all of the 100,000 integers between 1 and 100,000 
(inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the 
ith row of the file indicates the ith entry of an array.

Because of the large size of this array, you should implement the fast 
divide-and-conquer algorithm covered in the video lectures."""

def create_integer_array(filename):
    with open(filename) as f:
        integer_array = list(map(int, f.read().splitlines()))

    return integer_array


def splitArray(integer_array):
    
    mid = len(integer_array) // 2
    array_a = integer_array[:mid]
    array_b = integer_array[mid:] 
    
    return array_a, array_b


def mergeSort(sub_array):
    """ Takes in a list of integers and returns sorted list
    
    Args:
        alist - list of integers
        
    Returns:
        list
    """
    
    if len(sub_array) > 1:
        mid = len(sub_array) // 2
        lefthalf = sub_array[:mid]
        righthalf = sub_array[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                sub_array[k] = lefthalf[i]
                i += 1
            else:
                sub_array[k]=righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            sub_array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            sub_array[k] = righthalf[j]
            j += 1
            k += 1

    return sub_array


def counting_inversions(integer_array):
    
    inv_list = []
    
    array_a, array_b = splitArray(integer_array)
    
    sorted_a = mergeSort(array_a)
    sorted_b = mergeSort(array_b)
    i = 0
    j = 0
    k = 0
    inv = 0   
    
    for k in range(len(integer_array)):
        if len(integer_array) == 1:
            return 0
        
        while i < len(sorted_a) and j < len(sorted_b):
            if sorted_a[i] < sorted_b[j]:
                integer_array[k] = sorted_a[i]
                i += 1
            else: 
                integer_array[k] = sorted_b[j]
                j += 1
                inv += len(sorted_a) - i
                inv_list.append(len(sorted_a) - i)
            k += 1
            
        while j < len(sorted_b):
            integer_array[k] = sorted_b[j]
            j += 1
            k += 1
            
        while i < len(sorted_a):
            integer_array[k] = sorted_a[i]
            i += 1
            k += 1
     
    return integer_array, inv, inv_list, sorted_a, sorted_b
        

    
integer_array = create_integer_array('IntegerArray.txt')
#integer_array = [1, 3, 5, 2, 4, 6]
#integer_array = [8, 12, 3, 10, 15, 18]
sorted_list, inv, inv_list, sorted_a, sorted_b = counting_inversions(integer_array)
print('result', inv)
#1176350207

# =============================================================================
# file = open('results.txt', 'w')
# file.write(str(inv_list))
# file.close()
# 
# file = open('sub_array.txt', 'w')
# file.write(str(sorted_a))
# file.close()
# =============================================================================

#4,999,950,000

    