##### Create / clone lists using List Comprehension:
- **Null 1D List:** `{python icon title:} empty_arr = [None] * length`
- **Null 2D List:** `{python icon title:} empty_2d_arr = [[None] * columns for row in range(rows)]`
- **Clone a 1D List:** `{python icon title:1D} cloned_arr = [item for item in arr1] # Create a CLONE of arr1`
- **Clone a 2D List:** `{python icon title:2D} cloned_arr = [x[:] for x in arr1] # Create a CLONE of arr1`
- **1D with condition:** `{python icon title:List_Comprehension} new_arr = [item for item in arr1 if (var satisfies this condition)]`
###### The following list comprehension will transpose rows and columns:
`{python icon title:Input} # Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]`
`{python icon title:Transpose} transposed = [[row[i] for row in matrix] for i in range(4)]`
`{python icon title:Output} # Output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]`
##### Useful list-building functions
```python title:Input_List
def input_list(length = 6): # Create a user-input list
	print(f'Forming a list. Please enter {length} numbers: ')
	list = [int(input()) for item in range(length)]
	return list
```

```python title:Random_List
def random_list(length = 6, max = 100): # Create a random list
	list = [random.randint(0, max) for item in range(length)]
	return list
```

```python title:Random_into_2D_List
# This function overwrites the original list!
def rng_into_2d_arr(two_d_arr): # Insert random values into en empty 2D list
	for row in range(len(arr)):  
	    for column in range(len(arr[row])):  
	        arr[row][column] = random.randint(1, 99)
```

```python title:View_as_Matrix
def view_as_matrix(two_d_arr): # View a 2D List as a Matrix
    matrix = ''
    for i in range(len(two_d_arr)):
        for j in range(len(two_d_arr[i])):
            matrix += f'{str(two_d_arr[i][j]).rjust(3)} '
        matrix += '\n'
    return matrix
```
## 3. Tuple
###### Creating / packing
`{python icon title:opt1} tuple = num1, num2, num3` `{python icon title:opt2} tuple = (num1, num2)` `{python icon title:empty} tuple = ()` 
###### Unpacking
```python title:Tuple_Unpacking
t1 = (10, 20, 30)
num1, num2, num3 = t1
print(num1 + num2 + num3) # Output will be: 60
```
##### Convert from List to Tuple
`{python icon title:List_To_Tuple} tup1 = tuple(list1)`
`{python icon title:Set_To_Tuple} tup1 = tuple(set1)`