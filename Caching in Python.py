'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

'''
Problem Statement:
A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time. If the staircase has n steps, write a function to count the number of possible ways in which child can run up the stairs.
'''

import functools
@functools.lru_cache(maxsize=None)
def staircase(n):
	if n==0:
		return 1
	elif n<0:
		return 0
	climb_ways=0
	climb_ways+=staircase(n-1)
	climb_ways+=staircase(n-2)
	climb_ways+=staircase(n-3)
	return climb_ways
	
def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")
test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [3, 4]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)

