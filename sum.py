#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'find_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY lst as parameter.
#

def find_sum(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum
        
list1 = [1, 2, 3 , 5 ,6]

print(find_sum(list1))

        
