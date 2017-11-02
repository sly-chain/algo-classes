"""
The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. 

Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m−1 to your running total of comparisons. (This is because the pivot element is compared to each of the other m−1 elements in the subarray in this recursive call.)
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
    input_array[left_bound], input_array[i-1] = input_array[i-1], input_array[left_bound]

    return i-1, input_array



def sort(partitioned_array, sorted_array=[], comparisons=0):
    len_array= len(partitioned_array)
    
    if len_array == 1:
        return sorted_array.append(partitioned_array[0])
    
    else:
        
        k = 0
        print('array length', len_array-1)
        
        for j in range(len_array-1):
            
            
            if partitioned_array[k] > partitioned_array[j+1]:
                partitioned_array[j+1], partitioned_array[k] = partitioned_array[k], partitioned_array[j+1]
                k += 1
             
#            print(j, comparisons)
        sorted_array.append(partitioned_array[0])
        sort(partitioned_array[1:])
    comparisons += (len_array-1)   
    return comparisons, sorted_array



def quick_sort(input_array):
    
    if len(input_array) == 0:
        return 0, input_array
    
    pivot, partitioned_array = partition(input_array, left_bound, right_bound)

#    Q_comparisons, Q = sort(partitioned_array[:pivot])
    R_comparisons, R = sort(partitioned_array[pivot+1:])
    
#    return Q + [input_array[pivot]] + R
#    return Q_comparisons + R_comparisons, R
#    return Q_comparisons, Q
    return R_comparisons, R

            
        

input_array = [3, 8, 2, 5, 1, 4, 7, 6]
left_bound = 0 
right_bound = len(input_array) - 1
print(quick_sort(input_array))

    
    

