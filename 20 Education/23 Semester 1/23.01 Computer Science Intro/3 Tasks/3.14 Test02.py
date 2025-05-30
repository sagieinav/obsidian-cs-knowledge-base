# Question 1 w/ Slicing
from tabnanny import check


def max_couple_v1(list, length):
    return max_couple_helper(list, length)

def max_couple_helper_v1(list, length, max = 0):
    if length == 0 or (length == 1 and list[0] <= max):
        return max
    
    if length == 1 and list[0] > max:
        return list[0]

    if list[0] + list[-1] > max:
        max = list[0] + list[-1]
    
    return max_couple_helper(list[1:length - 1], length - 2, max)


# Question 1 w/o Slicing
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


# ------------------------------------------------------------


# Question 2
def find_sequence_numbers(matrix, streak):
    new_list = []
    
    for i in range(len(matrix)):
        
        for j in range(len(matrix[0])):
            
            if i + streak <= len(matrix): # Checking Row Streak
                for s in range(1, streak):
                    if not (matrix[i][j] == matrix[i + s][j]):
                        break
                    if s == streak - 1:
                        new_list.append([matrix[i][j], i, j])
                        
            if j + streak <= len(matrix[0]): # Checking Column Streak
                for s in range(1, streak):
                    if not (matrix[i][j] == matrix[i][j + s]):
                        break
                    if s == streak - 1:
                        new_list.append([matrix[i][j], i, j])
                    
    return new_list
    
    
# --------------------------------------------------------------


# Question 4
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
    


if __name__ == '__main__':
    
    # Question 1
    list = [9, 8, 3, 1, 6, 2, 5, 6]
    length = len(list)
    
    # print(max_couple_loop(list, length))
    
    # print(max_couple(list, length))
    
    # Question 2
    list = [
        [1,2,3,4,1],
        [0,2,2,2,1],
        [1,2,9,0,1],
        [1,0,2,4,1],
        [4,2,1,1,1]
    ]
    
    # print(find_sequence_numbers(list, 4))
    
    
    # Question 4
    address = 'Jane@ivalid.2rq'
    print(is_valid_email(address))