# Compute the number of comparisons using the "median-of-three" pivot rule. 

"""
Consider the first, middle, and final elements of the given array. 
(If the array has odd length it should be clear what the "middle" element is; 
for an array with even length 2k, use the kth element as the "middle" element. 
So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 
6!) Identify which of these three elements is the median (i.e., the one whose 
value is in between the other two), and use this as your pivot.

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), 
middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, 
you would use 4 as your pivot element.
"""