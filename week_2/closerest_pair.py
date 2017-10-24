import math
def find_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def form_sorted_lists(P):
    Px = sorted(P, key=lambda x: x[0])  
    Py = sorted(P, key=lambda x: x[1]) 
    
    mid = len(P) // 2

    left_x_sort = Px[:mid]
    left_y_sort = Py[:mid]
    
    right_x_sort = P[mid:]
    right_y_sort = Py[mid:]

    return Px, Py, left_x_sort, left_y_sort, right_x_sort, right_y_sort


def closest_split_pair(x_sort, y_sort, delta, best_pair):
    len_x_sort = len(x_sort)  
    mid_x_sort = x_sort[len_x_sort // 2][0]  

    split_array = [x for x in y_sort if mid_x_sort - delta <= x[0] <= x_sort + delta]
    best_dist = delta  
    len_split_array = len(split_array)  
    
    for i in range(len_split_array - 1):
        for j in range(i + 1, min(i + 7, len_split_array)):
            p, q = split_array[i], split_array[j]
            current_dist = find_dist(p, q)
            if current_dist < best_dist:
                best_pair = p, q
                best_dist = current_dist
    return best_pair[0], best_pair[1], best_dist


def closest_pair(x_sort, y_sort):

    coord1 = x_sort[0]
    coord2 = x_sort[1]
    min_dist = find_dist(coord1, coord2)
    len_sorted_x = len(x_sort)
    
    if len_sorted_x == 2:
        return coord1, coord2, min_dist
    
    for i in range(len_sorted_x - 1):
        for j in range(i + 1, len_sorted_x):
            if i != 0 and j != 1:
                current_dist = find_dist(x_sort[i], x_sort[j])
                if current_dist < min_dist:  # Update min_dist and points
                    min_dist = current_dist
                    coord1, coord2 = x_sort[i], x_sort[j]
                    
    return coord1, coord2, min_dist

    
    
def solution(P):
    Px, Py, Qx, Qy, Rx, Ry = form_sorted_lists(P)

    p1, q1, mi1 = closest_pair(Qx, Qy)  
    p2, q2, mi2 = closest_pair(Rx, Ry) 
    delta = min(mi1, mi2)
    best_pair = min((p1, q1), (p2, q2), key=lambda x: find_dist(x[0], x[1]))
    p3, q3 = closest_split_pair(Px, Py, delta, best_pair)
    
    return min(best_pair, (p3, q3), key=lambda x: find_dist(x[0], x[1]))
