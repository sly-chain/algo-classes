"""
The file contains all of the integers between 1 and 10,000 (inclusive, with no 
repeats) in unsorted order. 

Your task is to compute the total number of comparisons used to sort the given 
input file by QuickSort. You should not count comparisons one-by-one. Rather, when there is a recursive 
call on a subarray of length m, you should simply add m−1 to your running total 
of comparisons. (This is because the pivot element is compared to each of the 
other m−1 elements in the subarray in this recursive call.)
"""

# first element of the array as the pivot element

def partition(input_array, left, right):
    if len(input_array) == 0 or len(input_array) == 1:
        return 0, input_array
    
    pivot = input_array[left]
    i = left + 1

    for j in range(i, right):
        if input_array[j] < pivot:
            input_array[i], input_array[j] = input_array[j], input_array[i]
            i += 1
    input_array[left], input_array[i-1] = input_array[i-1], input_array[left]

    return i-1, input_array



def sort(partitioned_array, sorted_array=[]):
    global count
    len_array= len(partitioned_array)
    
    if len_array == 1:
        return sorted_array.append(partitioned_array[0])
    
    else:
        k = 0
        for j in range(len_array-1):
            if partitioned_array[j+1] < partitioned_array[k]:
                partitioned_array[j+1], partitioned_array[k] = partitioned_array[k], partitioned_array[j+1]
                k += 1
        sorted_array.append(partitioned_array[0])
        sort(partitioned_array[1:])
        count += len_array-1
        
    return count, sorted_array



def quick_sort(input_array):
    if len(input_array) == 0 or len(input_array) == 1:
        return 0, input_array
    
    pivot_index, partitioned_array = partition(input_array, left, right)

    Q_count, Q = sort(partitioned_array[:pivot_index])
#    R_count, R = sort(partitioned_array[pivot_index+1:])
    
#    return Q + [input_array[pivot_index]] + R
#    return Q_count + R_comparisons, R
    return Q_count, Q
#    return R_count, R

            
count = 0
#input_array = [3, 8, 2, 5, 1, 4, 7, 6]
with open('quicksort.txt', 'r') as f:
    input_array = [int(line) for line in f]
left = 0 
right = len(input_array) - 1
print(quick_sort(input_array))
    
    
