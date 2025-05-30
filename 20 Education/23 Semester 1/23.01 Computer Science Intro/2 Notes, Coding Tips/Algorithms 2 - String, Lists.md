## 2. String
#### Example 1: Check Email Address Validity
```python title:String1
def is_valid_email(address):
    username = address.split('@')[0] # Extract the username
    domain_name = address.split('@')[-1] # Extract the domain name
    country_code = domain_name.split('.') # Extrace the country code
    
    check1_at_symbol = address.count('@') == 1 # Check if there's 1 '@' symbol
    check2_length = len(address) >= 8 and len(address) <= 30 # Check length validity
    check3_first_char = (address[0]).isalpha() # Check that first char is a letter
    check4_lower_complexity = False # Complexity - lowercase. False by default
    check4_upper_complexity = False # Complexity - uppercase. False by default
    check5_server_validity = '.' in domain_name and len(country_code[-1]) >= 2 # Serv validity
    check6_country_code_validity = True # Country code validity. True by default
    
    for letter in username: # Check complexity validity
        if letter.islower():
            check4_lower_complexity = True
        elif letter.isupper():
            check4_upper_complexity = True
    for letter in country_code[-1][-2:]: # Check country code validity
        if not letter.isalpha():
            check6_country_code_validity = False
            
    is_valid = (check1_at_symbol and check2_length and check3_first_char and check4_lower_complexity \
                and check4_upper_complexity and check5_server_validity and check6_country_code_validity)
    return is_valid
```
#### Example 2: Capitalize Words
```python title:String2
def capitalize_words(input_string):
    str_as_list = input_string.split(' ') # Split the words into a list
    str_as_list = [word.capitalize() for word in str_as_list if word != ''] # Capitalize each word and remove empty words

    res_str = ' '.join(str_as_list) # Convert from list to string
    return res_str
```
## 3. Lists
#### Example 1: Rotate Matrix
כתבו הפונקציה המקבלת מטריצה ומסובבת אותה ב- 90 מעלות עם כיוון השעון (ימינה). אין להשתמש ברשימות עזר. יש לבצע הכל על המטריצה המקורית וללא slicing.
```python title:Lists1
def rotate_matrix_90_degrees_clockwise_v1(matrix):
    for i in range(len(matrix) // 2): # Run on first half of rows
        for j in range(len(matrix) // 2): # Run on first half of columns
		# together it runs on the frames from outside -> inside
            top_left = matrix[i][j] # Top left item
            top_right = matrix[j][-i - 1] # Top right item
            bottom_right = matrix[-i - 1][-j - 1] # Bottom right item
            bottom_left = matrix[-j - 1][i] # Bottom left item
            
            temp = top_left # Save top left into a temp, to perform the rotation
            
            matrix[i][j] = bottom_left # Bot left into Top left
            matrix[-j - 1][i] = bottom_right # Bot right into Bot left
            matrix[-i - 1][-j - 1] = top_right # Top right into Bot right
            matrix[j][-i - 1] = temp # Top left into Top right
            
    return matrix
```