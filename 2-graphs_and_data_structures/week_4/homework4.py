"""
The goal of this problem is to implement a variant of the 2-SUM algorithm covered 
in this week's lectures.

The file contains 1 million integers, both positive and negative (there might be 
some repetitions!).This is your array of integers, with the ith row of the file 
specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval 
[-10000,10000] (inclusive) such that there are distinct numbers x,y in the input 
file that satisfy x+y=t.  (NOTE: ensuring distinctness requires a one-line addition 
to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your 
own hash table for it. For example, you could compare performance under the 
chaining and open addressing approaches to resolving collisions.
"""


def create_data_array(file):
    data_array = []
    with open(file) as f:
        data_array = list(map(int, f.read().splitlines()))
    return sorted(data_array)

data_array = create_data_array('2sum.txt')



def find_pairs(data_array, target):
    
    for x in data_array:
        y = target - x
        if y in data_array:
            return True
        
    return False


def find_answer(data_array):
    results = []
    
    for target in range(-10000, 10000):
        results.append(find_pairs(data_array, target))
        
    return sum(results)


print(find_answer(data_array))