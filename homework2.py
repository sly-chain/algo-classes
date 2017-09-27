"""This file contains all of the 100,000 integers between 1 and 100,000 
(inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the 
ith row of the file indicates the ith entry of an array.

Because of the large size of this array, you should implement the fast 
divide-and-conquer algorithm covered in the video lectures."""

def splitArray(integer_array):
    
    mid = integer_array // 2
    array_a = mergeSort(integer_array[:mid])
    array_b = mergeSort(integer_array[mid:])   
    
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
    
    array_a, array_b = splitArray(integer_array)
    
    sorted_a = mergeSort(array_a)
    sorted_b = mergeSort(array_b)
    
    sorted_list = []
    i = 0
    j = 0
    inv = 0   
    
    if not len(sorted_a):
        sorted_list.append(sorted_b[j])
        j += 1
    
    for i in len(range(sorted_a)):
        if sorted_a[i] < sorted_b[j]:
            sorted_list.append(sorted_a[i])
            i += 1
        else:
            sorted_list.append(sorted_b[j])
            j += 1
            inv += 1

    return sorted_list, inv 


    
#integer_array = 
#counting_inversions(integer_array)
    
    
    
    
    
    
    
    