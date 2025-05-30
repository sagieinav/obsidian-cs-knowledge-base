## Recursion
#### Example 1: Max Couple at Inverted Indexes
```python title:Recursion1
def max_couple(list, length):
    return max_couple_helper(list, length)

def max_couple_helper(list, length, max = 0, start = 0):
    if length == 0 or (length == 1 and list[length + start - 1] <= max):
        return max
    
    if length == 1 and list[length + start - 1] > max:
        return list[length + start - 1]
    
    if list[start] + list[length + start - 1] > max:
        max = list[start] + list[length + start - 1]
    
    return max_couple_helper(list, length - 2, max, start + 1)
```
#### Example 2: Twin Neighbors
```python title:Recursion2
def twin_neighbours(my_list):
    return twin_helper(my_list, len(my_list) - 1)

# Helper for q1
def twin_helper(my_list, last_index, count=0):
    if last_index == 0:
        return 0
    if my_list[last_index] == my_list[last_index - 1]:
        return 1 + twin_helper(my_list, last_index - 1)
    else:
        return twin_helper(my_list, last_index - 1)
```
#### Example 3: יעני פיבונצ׳י
```python title:Recursion3
def like_fibo(nth):
	if nth <= 3:
		return nth
	
	elif nth % 2 == 0:
		return like_fibo(nth - 1) + like_fibo(nth - 2) + like_fibo(nth - 3)
	else:
		return abs(like_fibo(nth - 1) - like_fibo(nth - 3))
```
#### Example 4: מספר מתחלף
```python title:Recursion4
def is_switched_number(number):  
    if number < 10:  
       return True  
    dig0 = number % 10  
    dig1 = number // 10 % 10  
    if (dig0 % 2 == 0 and dig1 % 2 == 0) or (dig0 % 2 != 0 and dig1 % 2 != 0):  
       return False
	   
    return is_switched_number(number // 10)
```
## Lists
#### Example 1: Rotate Matrix
כתבו הפונקציה המקבלת מטריצה ומסובבת אותה ב- 90 מעלות עם כיוון השעון (ימינה). אין להשתמש ברשימות עזר. יש לבצע הכל על המטריצה המקורית וללא slicing.
```python title:Lists1
def rotate_matrix_90_degrees_clockwise_v1(matrix):
    for i in range(len(matrix) // 2):
        for j in range(len(matrix) // 2):
            top_left = matrix[i][j]
            top_right = matrix[j][-i - 1]
            bottom_right = matrix[-i - 1][-j - 1]
            bottom_left = matrix[-j - 1][i]
            
            temp = top_left
            
            matrix[i][j] = bottom_left
            matrix[-j - 1][i] = bottom_right
            matrix[-i - 1][-j - 1] = top_right
            matrix[j][-i - 1] = temp
            
    return view_as_matrix(matrix)
```
#### Example 2: Has Path
```python title:Lists2
def has_path(matrix):
    row = 0
    col = -1
    while True:
        if matrix[row][col] == "|":
            if row == len(matrix) - 1:
                return True
            else:
                row += 1
        elif matrix[row][col] == "-" and col != -(len(matrix[0])):
                col -= 1
        else:
            return False
```
#### Example 3: Snake
```python title:Lists3
def create_snake(rows, cols):
    arr = [[None] * cols for i in range(rows)]
    value = 1
    col_index = -1

    for times in range (len(arr)):
        for row in range (len(arr)):
            if col_index % 2 != 0:
                arr[row * -1 - 1][col_index] = value
            else:
                arr[row][col_index] = value
            value += 1
        col_index -= 1
        if abs(col_index) > cols:
            break

    return arr
```
#### Example 4: Diagram Graph
```python title:Lists4
def diagram_graph(list):
    max_val = max(list)

    for row in range(max_val, 0, -1):
        for i in range(len(list)):
            if list[i] >= row:
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print()

    #Cosmetic:
		# Add cosmetic lines here
```
#### Example 5: חיבור ארוך
```python title:Lists5
def sum_lists (list1, list2):
    longer_l, shorter_l = (list1, list2) if len(list1) >= len(list2) else (list2, list1)
    summed_list = [None] * (len(longer_l) + 1)
    leftover = 0

    for i in range(len(longer_l)):
        item = longer_l[-i -1] + leftover
        if i < (len(shorter_l)):
            item += shorter_l[-i -1]
        if item > 9:
            item -= 10
            leftover = 1
        else:
            leftover = 0
        summed_list[-i -1] = item

    if leftover == 1:
        summed_list[0] = 1
    else:
        summed_list.remove(None)

    return summed_list
```
## String
#### Example 1: Check Email Address Validity
```python title:String1
def is_valid_email(address):
    username = address.split('@')[0]
    domain_name = address.split('@')[-1]
    country_code = domain_name.split('.')
    
    check1_at_symbol = address.count('@') == 1
    check2_length = len(address) >= 8 and len(address) <= 30
    check3_first_letter = (address[0]).isalpha()
    check4_lower_complexity = False
    check4_upper_complexity = False
    check5_server_validity = '.' in domain_name and len(country_code[-1]) >= 2
    check6_country_code_validity = True
    
    for letter in username:
        if letter.islower():
            check4_lower_complexity = True
        elif letter.isupper():
            check4_upper_complexity = True
    for letter in country_code[-1][-2:]:
        if not letter.isalpha():
            check6_country_code_validity = False
            
    is_valid = (check1_at_symbol and check2_length and check3_first_letter and check4_lower_complexity \
                and check4_upper_complexity and check5_server_validity and check6_country_code_validity)
    return is_valid
```
#### Example 2: Capitalize Words
```python title:String2
def capitalize_words(input_string):
    str_as_list = input_string.split(' ')
    str_as_list = [word for word in str_as_list if word != '']
    str_as_list = [word.capitalize() for word in str_as_list if word != '']
    # str_as_list = [word.capitalize() for word in input_string.split(' ') if word != '']

    res_str = ' '.join(str_as_list)
    return res_str
```

## Dictionary
___
```python title:Dictionary
def books_by_genre(books, the_genre): # Exercise 1's Function
    avg_pages = 0 # It's a sum for now
    books_from_this_genre = []
    for book in books:
        if book['genre'] == the_genre:
            books_from_this_genre.append(book['title'])
            avg_pages += book['pages']
    avg_pages = avg_pages / len(books_from_this_genre) if len(books_from_this_genre) != 0 else avg_pages # Now its the actual average
    return books_from_this_genre, avg_pages


def get_books_name_for_reader(books, readers, reader_name): # Exercise 2's Function
    leased_books = []
    for reader in readers:
        if reader['name'] == reader_name: # Found the dictionary of our reader
            for book_id in reader['borrowed']:
                for book in books:
                    if book_id == book['book_id']:
                        leased_books.append(book['title'])               
    return leased_books


def most_read_book(books, readers): # Exercise 3's Function
    most_leased = set()
    highest_votes = 0
    for book in books:
        book['votes'] = 0
        for reader in readers:
            for book_id in reader['borrowed']:
                if book_id == book['book_id']:
                    book['votes'] += 1
        highest_votes = book['votes'] if book['votes'] > highest_votes else highest_votes
    for book in books:
        if book['votes'] == highest_votes:
            most_leased.add(book['title'])
    return most_leased


def loan_book(books, readers, reader_name, book_name): # Exercise 4's Function
    book_id = 0
    for book in books:
        book_id = book['book_id'] if book['title'] == book_name else book_id
    if book_id == 0:
        return False
    for reader in readers:
        if reader['name'] == reader_name:
            for existing_book in reader['borrowed']:
                if existing_book == book_id:
                    return False
            reader['borrowed'].append(book_id)
            return True
    return False


def return_book(books, readers, reader_name, book_name): # Exercise 5's Function
    book_id = 0
    for book in books:
        book_id = book['book_id'] if book['title'] == book_name else book_id
    if book_id == 0:
        return False
    for reader in readers:
        if reader['name'] == reader_name:
            for existing_book in reader['borrowed']:
                if existing_book == book_id:
                    reader['borrowed'].remove(book_id)
                    return True
            return False
    return False


def readers_having_most_read_book(readers): # Exercise 6's Function
    books_by_id = []
    possessing_readers = set()
    highest_votes = 0
    for reader in readers: # Create a list with dicts containing book ID book's vote count
        for readers_book_id in reader['borrowed']:
            books_by_id.append(dict(book_id = readers_book_id, votes = 0))
            
    for book in books_by_id: # Count the votes and find the highest vote count
        for reader in readers:
            for readers_book_id in reader['borrowed']:
                if readers_book_id == book['book_id']:
                    book['votes'] += 1
        highest_votes = book['votes'] if book['votes'] > highest_votes else highest_votes
        
    for book in books_by_id: # Check which readers have the most-leased books
        if book['votes'] == highest_votes:
            for reader in readers:
                for readers_book_id in reader['borrowed']:
                    if readers_book_id == book['book_id']:
                        possessing_readers.add(reader['name'])

    return possessing_readers


if __name__ == '__main__':
	# Books List
	books = [dict(book_id=1001, title="Harry Potter", genre="fantasy", pages=500),
			 dict(book_id=1002, title="A song of Ice and Fire", genre="fantasy", pages=700),
			 dict(book_id=1003, title="1984", genre="classic", pages=800),
			 dict(book_id=1004, title="Attack on Titan", genre="manga", pages=1400),
			 dict(book_id=1005, title="One Piece", genre="manga", pages=12000)
	]
	# Readers List
	readers = [{"name": "Ichi", "borrowed": [1001, 1003]},
			   {"name": "Ni", "borrowed": [1002]},
			   {"name": "San", "borrowed": [1005, 1002]},
			   {"name": "Yon", "borrowed": [1005, 1002]},
			   {"name": "Go", "borrowed": [1005]}
	]
```