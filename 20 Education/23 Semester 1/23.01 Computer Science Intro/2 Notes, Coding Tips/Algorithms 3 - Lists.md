#### Example 2: Create Snake
```python title:Lists2
arr = [[None] * cols for i in range(rows)] # Create an empty null 2d arr
    value = 1 # Starting value. Will be bumped by 1 for each index

    for col in range (-1, -(len(arr[0])) - 1, -1): # Run on columns from right to left
        for row in range(len(arr)): # Run on rows
            if col % 2 != 0: # Check if row is even or odd
                arr[-row - 1][col] = value
            else:
                arr[row][col] = value
            value += 1 # Bump value by 1. Now ready to insert into next index

    return arr
```
#### Example 3: Diagram Graph
```python title:Lists3
def diagram_graph(list):
    max_val = max(list) # Find the max value (highest graph bar)

    for row in range(max_val, 0, -1): # Run on rows from top to bottom
        for bar in range(len(list)): # Run on bars (columns)
            if list[bar] >= row: # Print '*' if bar reaches this row (height)
                print('*', end = ' ')
            else: # Skip/Print ' ' if bar doesn't reach this row (height)
                print(' ', end = ' ')
        print() # Proceed to next row

    #Cosmetic:
		# Add cosmetic lines here
```
#### Example 4: חיבור ארוך
```python title:Lists4
def sum_lists (list1, list2):
    longer_l, shorter_l = (list1, list2) if len(list1) >= len(list2) else (list2, list1)
    summed_list = [None] * (len(longer_l) + 1) # Define an empty list with +1 size
    leftover = 0 # Leftover will be 1 when sum of 2 nums is greater than 10

    for i in range(len(longer_l)): # Run on the longer list of the two
        item = longer_l[-i -1] + leftover # Get the items from right to left
        if i < (len(shorter_l)): # ONLY if this index exists in the shorter list
            item += shorter_l[-i -1] # Add the corresponding item from shorter lst
        if item > 9: # Define leftover if sum > 9
            item -= 10
            leftover = 1
        else:
            leftover = 0
        summed_list[-i -1] = item # Add the sum to result list

    if leftover == 1:
        summed_list[0] = 1
    else:
        summed_list.remove(None)

    return summed_list
```