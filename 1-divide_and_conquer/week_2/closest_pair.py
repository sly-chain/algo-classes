"""
presort outside of function that will be called recursively 
==> smaller time complexity
"""


import math
def find_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def brute(x_sort):
    coord_x = x_sort[0]
    coord_y = x_sort[1]
    min_dist = find_dist(coord_x, coord_y)
    len_sorted_x = len(x_sort)
    
    if len_sorted_x == 2:
        return coord_x, coord_y, min_dist
    for i in range(len_sorted_x - 1):
        for j in range(i + 1, len_sorted_x):
            if i != 0 and j != 1:
                current_dist = find_dist(x_sort[i], x_sort[j])
                if current_dist < min_dist:  # Update min_dist and points
                    min_dist = current_dist
                    coord_x, coord_y = x_sort[i], x_sort[j]
                    
    return coord_x, coord_y, min_dist



def closest_split_pair(x_sort, y_sort, delta, best_pair):
    len_x_sort = len(x_sort)  
    mid_x_sort = x_sort[len_x_sort // 2][0]  # select midpoint on x-sorted array

    # Create a subarray of points not further than delta from
    # midpoint on array sorted by x

    sub_array = [x for x in y_sort if mid_x_sort - delta <= x[0] <= x_sort + delta]
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



def closest_pair(x_sort, y_sort):
    len_x_sort = len(x_sort)  
    if len_x_sort <= 3:
        return brute(x_sort) 
    mid = len_x_sort // 2 
    Qx = x_sort[:mid]  
    Rx = x_sort[mid:]

    # Determine midpoint on x-axis

    midpoint = x_sort[mid][0]  
    Qy = []
    Ry = []
    
    for i in y_sort:  # split sorted_y into 2 arrays using midpoint
        if i[0] <= midpoint:
           Qy.append(i)
        else:
           Ry.append(i)

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

    (p3, q3, mi3) = closest_split_pair(x_sort, y_sort, d, mn)

    # Determine smallest distance for the array

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3



def solution(P):
    sorted_by_x = sorted(P, key=lambda x: x[0])  
    sorted_by_y = sorted(P, key=lambda x: x[1])  
    p1, p2, mi = closest_pair(sorted_by_x, sorted_by_y)  
    return mi
