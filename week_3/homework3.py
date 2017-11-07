def sort_by_pivot(pivot_type):
    if pivot_type == 'first':
        return quick_sort(input_array, 0, len(input_array))

    if pivot_type == 'last':
        input_array[0], input_array[-1] = input_array[-1], input_array[0]
        return quick_sort(input_array, 0, len(input_array))
        
    if pivot_type == 'median':
        med = (len(input_array) - 1) // 2
        input_array[0], input_array[med] = input_array[med], input_array[0]
        return quick_sort(input_array, 0, len(input_array))


def quick_sort(input_array, left, right):
    global count

    if left >= right:
        return
    
    pivot = input_array[left]
    i = left + 1
    
    for j in range(left+1, right):
        if input_array[j] < pivot:
            input_array[i] , input_array[j] = input_array[j], input_array[i]
            i = i + 1
            
    input_array[left] , input_array[i-1] = input_array[i-1], input_array[left]
    quick_sort(input_array, left, i-1)
    count += i-1-left
    quick_sort(input_array, i, right)
    count += right-i-1

    return pivot, count



count = 0
with open('quicksort.txt', 'r') as f:
    input_array = [int(line) for line in f]
    
    
''' first element of the array as the pivot element '''
#print(sort_by_pivot('first'))
# 152085


'''always using the final element of the given array as the pivot element
should exchange the pivot element (i.e., the last element) with the first element '''
#print(sort_by_pivot('last'))
# 149750


''' Compute the number of comparisons using the "median-of-three" pivot rule.'''
#print(sort_by_pivot('median'))
# 148773
