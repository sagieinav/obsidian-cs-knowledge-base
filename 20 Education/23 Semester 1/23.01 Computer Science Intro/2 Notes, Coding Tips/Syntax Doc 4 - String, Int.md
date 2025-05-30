## 6. Integer
- **absolute:** `{python icon title:Example} to_user = (abs(user_floor - elevator_floor))`

- **random:** `{python icon title:Import} import random # First we need to import the library` ; `{python icon title:Example} bingo = random.randint(1,100)`
## 7. String

##### String Operations
**NOTE: For some of these, we need to import the library:** `{python icon title:} import string`
###### Search
- **var.find() / var.rfind():** Searches the string for a specified value and returns the position of where it was found
- **var.index():** Searches the string for a specified value and returns the position of where it was found
- **var.count():** Returns the number of times a specified value occurs in a string
###### Format / Split / Replace
- **var.rjust():** `{python icon title:syntax} num = num.rjust(width, 'fillchar')`     `{python icon title:example} num = num.rjust(2, '0')`
- **var.join():** `{python icon title:} var += ''.join('Enter text here')`
- **var.partition(): / var.rpartition()** Returns a tuple where the string is parted into three parts
- **var.split() / var.rsplit():** Splits the string at the specified separator, and returns a list
- **var.splitlines():** Splits the string at line breaks and returns a list
- **var.rstrip() / var.lstrip():** Returns a right/left trim version of the string
- **var.replace:** Returns a string where a specified value is replaced with a specified value
- **remove:** `{python icon title:remove_ALL_OCCURENCES_of_'a'} st = st.replace('a', '')` ; `{python icon title:remove_2_OCCURENCES_of_'d'} st = st.replace('d', '', 2)`
###### Lowercase / Uppercase Conversion
- **var.upper():** Convert a string to uppercase
- **var.lower():** Convert a string to lowercase
- **var.capitalize():** Capitalizes the string. First letter is CAPITAL, rest are small letters
- **var.swapcase():** Swaps cases, lower case becomes upper case and vice versa
- **var.title():** Converts the first character of each word to upper case
- **var.casefold():** Converts string into lower case
###### Boolean Checks
- **var.startswith():** Returns true if the string starts with the specified value
- **var.endswith():** Returns true if the string ends with the specified value
- **var.istitle():** Returns True if the string follows the rules of a title
- **var.isalnum():** Returns True if all characters in the string are alphanumeric
- **var.isalpha():** Returns True if all characters in the string are in the alphabet
- **var.isnumeric():** Returns True if all characters in the string are numeric
- **var.isascii():** Returns True if all characters in the string are ascii characters
- **var.isdigit():** Returns True if all characters in the string are digits
- **var.isspace():** Returns True if all characters in the string are whitespaces
- **'text' in var:** Check if a letter/symbol exists in a string. returns True/False `{python icon title:} check_sym = '@' in address`
##### Slicing
```python title:String_Slicing
st = "Hello, World!"  

# Get the characters from position 2 to position 5 (not included):
print(st[2:5]) # Output: "ell"

# Get the characters from position -5 to position -2 (not included):
print(st[-5:-2]) # Output: "orl"

# Combined Slicing: Remove characters in the middle of the string; lets say length = 2
st = st[0:length - 1] + st[length:] # Removes the char in index {length - 1} = 1 = 'e'
```