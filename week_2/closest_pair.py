"""
presort outside of function that will be called recursively 
==> smaller time complexity
"""


import math
def find_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def brute(sort_by_x):
    coord_x = sort_by_x[0]
    coord_y = sort_by_x[1]
    min_dist = find_dist(coord_x, coord_y)
    len_sorted_x = len(sort_by_x)
    
    if len_sorted_x == 2:
        return coord_x, coord_y, min_dist
    for i in range(len_sorted_x - 1):
        for j in range(i + 1, len_sorted_x):
            if i != 0 and j != 1:
                current_dist = find_dist(sort_by_x[i], sort_by_x[j])
                if current_dist < min_dist:  # Update min_dist and points
                    min_dist = current_dist
                    coord_x, coord_y = sort_by_x[i], sort_by_x[j]
                    
    return coord_x, coord_y, min_dist



def closest_split_pair(sort_by_x, sort_by_y, delta, best_pair):
    len_sort_by_x = len(sort_by_x)  
    sort_by_x_mid = sort_by_x[len_sort_by_x // 2][0]  # select midpoint on x-sorted array

    # Create a subarray of points not further than delta from
    # midpoint on array sorted by x

    sub_array = [x for x in sort_by_y if sort_by_x_mid - delta <= x[0] <= sort_by_x + delta]
    min_dist = delta  
    len_sub_array = len(sub_array)  
    
    for i in range(len_sub_array - 1):
        for j in range(i + 1, min(i + 7, len_sub_array)):
            p, q = sub_array[i], sub_array[j]
            current_dist = find_dist(p, q)
            if current_dist < min_dist:
                best_pair = p, q
                min_dist = current_dist
    return best_pair[0], best_pair[1], min_dist



def closest_pair(sorted_x, sorted_y):
    len_sorted_x = len(sorted_x)  
    if len_sorted_x <= 3:
        return brute(sorted_x) 
    mid = len_sorted_x // 2 
    Qx = sorted_x[:mid]  
    Rx = sorted_x[mid:]

    # Determine midpoint on x-axis

    midpoint = sorted_x[mid][0]  
    Qy = []
    Ry = []
    
    for x in sorted_y:  # split sorted_y into 2 arrays using midpoint
        if x[0] <= midpoint:
           Qy.append(x)
        else:
           Ry.append(x)

    # Call recursively both arrays after split

    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)

    # Determine smaller distance between points of 2 arrays

    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    # Call function to account for points on the boundary

    (p3, q3, mi3) = closest_split_pair(sorted_x, sorted_y, d, mn)

    # Determine smallest distance for the array

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3



def solution(x, y):
    a = list(zip(x, y))
    sorted_x = sorted(a, key=lambda x: x[0])  
    sorted_y = sorted(a, key=lambda x: x[1])  
    p1, p2, mi = closest_pair(sorted_x, sorted_y)  
    return mi
