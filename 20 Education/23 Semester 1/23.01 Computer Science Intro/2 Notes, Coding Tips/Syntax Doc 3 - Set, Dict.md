## 4. Set
##### Set creation
`{python icon title:opt1} set1 = {10, 20, 30}` ; `{python icon title:opt2} set1 = set(10, 20, 30)` ; `{python icon title:empty} set1 = set()`
`{python icon title:set_from_list} set1 = set([2, 4, 5, 1])` `{python icon title:set_from_list} set1 = {[2, 4, 5, 1]}`
`{python icon title:set_from_str} set1 = set("hello")`
##### Set Comprehension
`{python icon title:} set1 = set(n for n in range(10)) # Output will be {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`
##### Set Operations
- **Add item:** `{python icon title:add_to_set} the_set.add("this", 8)`
- **Remove / Pop item:** `{python icon title:remove_from_set} the_set.remove(8, "Yon")` ; `{python icon title:pop_from_set} the_set.pop(index_num)`
- **Get length/size of a set:** `{python icon title:len_of_set} set1_len = len(set1)`
- **Intersect 2 sets:** `{python icon title:intersect_sets} intersected = set1 & set2`
- **Union 2 sets:** `{python icon title:unioned_sets} unioned = set1 | set2`
- **XOR 2 sets:** `{python icon title:xor_sets} xor_set = set1 ^ set2`
- **Diff 2 sets:** `{python icon title:diff_sets} unioned = set1 - set2`
- **Check if subset (contained)**: `{python icon title:is_subset} print(set1 <= set2) # True/False`
## 5. Dictionary
##### Dictionary creation
`{python icon title:option1} dict1 = dict(book_id = var_id, title='AOT', votes = 0)`
`{python icon title:option2} dict1 = {"book_id":var_id, "title":"AOT", "votes":0}`
##### Dict's keys
`{python icon title:get_keys_into_set} keys_set = set(dict1.keys() ` ; `{python icon title:get_keys_into_list} keys_list = list(dict1.keys() `
`{python icon title:loop_on_keys} for key in dict1.keys(): `
##### Dict's values
`{python icon title:get_values_into_set} values_set = set(dict1.values()) ` ; `{python icon title:get_values_into_list} values_list = list(dict1.values()) `
`{python icon title:loop_on_values} for value in dict1.values(): `
##### Dict's pairs / items
`{python icon title:get_pairs_into_list} pairs_list = list(dict1.items)` ; `{python icon title:get_pairs_into_set} pairs_list = set(dict1.items)`
**USEFUL:** `{python icon title:loop_on_pairs} for key, value in dict1.items(): ` `{python icon title:example} for album, songs_list in LinkinPark.items(): `

```python title:Dictionary_Operations
# Define a dict
tel = {'Sagi': 4098, 'Amit': 4139}

# Create / add an item
tel['Ilay'] = 4127

# Get value of a key
tel['Sagi'] # Output: 4098

# Delete an item
del tel['Amit'] # opt1
tel.pop('Amit') # opt2

# View the dictionary's keys
list(tel) # Output: ['Sagi', 'Amit', 'Ilay']

# View the dictionary's keys, sorted
sorted(tel) # Output: ['Amit', 'Ilay', 'Sagi']

# Check if a key exists in the dict
'Sagi' in tel # Output: True
'Amit' not in tel # Output: False
```