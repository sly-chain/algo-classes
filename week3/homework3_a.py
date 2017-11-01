"""
The file contains all of the integers between 1 and 10,000 (inclusive, with no 
repeats) in unsorted order. 

Your task is to compute the total number of comparisons used to sort the given 
input file by QuickSort. As you know, the number of comparisons depends on 
which elements are chosen as pivots, so we'll ask you to explore three 
different pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a recursive 
call on a subarray of length m, you should simply add m−1 to your running total 
of comparisons. (This is because the pivot element is compared to each of the 
other m−1 elements in the subarray in this recursive call.)
"""

# first element of the array as the pivot element

def partition(input_array, left_bound, right_bound):
    if len(input_array) == 1:
        return 0, input_array
    
    pivot = input_array[left_bound]
    i = left_bound + 1

    for j in range(left_bound + 1, right_bound):
        if input_array[j] < pivot:
            input_array[i], input_array[j] = input_array[j], input_array[i]
            i += 1
        print(i, j, input_array)
    input_array[left_bound], input_array[i-1] = input_array[i-1], input_array[left_bound]
    print('here', left_bound, i-1)
    return i-1, input_array


def sort_partition(unsorted_array):
    
    sorted_array = []
    
    for i in unsorted_array:
        
    
    return sorted_array
    

def quick_sort(input_array, left_bound, right_bound):
    
    pivot, partitioned_array = partition(input_array, left_bound, right_bound)
    
    Q = sort_partition(partitioned_array[:pivot])
    R = sort_partition(partitioned_array[pivot+1:])

    return Q + pivot + R
            
        

#input_array = [3, 8, 2, 5, 1, 4, 7, 6]
#quick_sort(input_array, 0, len(input_array)-1)
    
#print(partition(input_array, 0, len(input_array)-1))
    

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part
        
alist = [54,26,93,17,77,31,44,55,20]
quicksort(alist)
print(alist)