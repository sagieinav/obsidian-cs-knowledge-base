## 1. Recursion
#### Example 1: Max Couple at Inverted Indexes
```python title:Recursion1
def max_couple(list, length):
    return max_couple_helper(list, length) # Call the helper function

def max_couple_helper(list, length, max = 0, start = 0): # Helper with 2 new variables
    if length == 0 or (length == 1 and list[length + start - 1] <= max): # Stop condition case1
        return max
    
    if length == 1 and list[length + start - 1] > max: # Stop condition case2
        return list[length + start - 1]
    
    if list[start] + list[length + start - 1] > max: # Check if this pair is the new max value
        max = list[start] + list[length + start - 1]
    
    return max_couple_helper(list, length - 2, max, start + 1)
```
#### Example 2: Twin Neighbors
```python title:Recursion2_Sum
def twin_neighbours(my_list):
    return twin_helper(my_list, len(my_list) - 1)

# Helper for q1
def twin_helper(my_list, last_index, count=0):
    if last_index == 0: # Stop Condition - reached all items in the list
        return 0
    if my_list[last_index] == my_list[last_index - 1]: # When they are twins
        return 1 + twin_helper(my_list, last_index - 1) # Add to sum and continue
    else: # When they're NOT twins
        return twin_helper(my_list, last_index - 1)
```
#### Example 3: יעני פיבונצ׳י
```python title:Recursion3_Series
def like_fibo(nth):
	if nth <= 3: # Stop condition - reached the default [1, 2, 3] list
		return nth
	
	if nth % 2 == 0: # If index is even, return sum of prev 3 items
		return like_fibo(nth - 1) + like_fibo(nth - 2) + like_fibo(nth - 3)
	else: # Index is odd
		return abs(like_fibo(nth - 1) - like_fibo(nth - 3))
```
#### Example 4: מספר מתחלף
```python title:Recursion4
def is_switched_number(number):  
    if number < 10: # Stop condition
       return True  
    dig0 = number % 10 # Right dig
    dig1 = number // 10 % 10 # Left dig
    if (dig0 % 2 == 0 and dig1 % 2 == 0) or (dig0 % 2 != 0 and dig1 % 2 != 0): # Check condition
       return False
	   
    return is_switched_number(number // 10) # Cut last digit (it passed the test here)
```