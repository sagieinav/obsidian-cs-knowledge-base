# your id: 207456047

def view_as_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j]).rjust(3), end = ' ')
        print()
            

# --------------------------------------------


# Question 1
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


# --------------------------------------------


# Question 2
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


# Question 2
def rotate_matrix_90_degrees_clockwise(matrix):
    
    for i in range(len(matrix) // 2):
        for j in range(len(matrix) // 2):
            matrix[i][j], matrix[j][-i - 1], matrix[-i - 1][-j - 1], matrix[-j - 1][i] \
                = matrix[-j - 1][i], matrix[i][j], matrix[j][-i - 1], matrix[-i - 1][-j - 1]
        
    return view_as_matrix(matrix)


# ----------------------------------------------


# Question 3 part 1
def distance_of_number_in_list (lst, num):
    distance_from_start = len(lst) - 1
    distance_from_end = len(lst) - 1
    for i in range(len(lst)):
        if lst[i] == num:
            if distance_from_start >= i:
                distance_from_start = i
            if distance_from_end >= len(lst) - 1 - i:
                distance_from_end = len(lst) - 1 - i
                
    min_distance = distance_from_start + distance_from_end
    if min_distance > len(lst):
        return -1
    
    return min_distance
    

# Question 3 part 2
def find_minimal_distance_number(the_list):
    min_value = distance_of_number_in_list(the_list, the_list[0])
    winner = the_list[0]
    for i in range(1, len(the_list)):
        if distance_of_number_in_list(the_list, the_list[i]) < min_value:
            winner = the_list[i]
    
    return winner
    
    
# --------------------------------------------


#Question 4
def capitalize_words(input_string):
    str_as_list = input_string.split(' ')
    str_as_list = [word for word in str_as_list if word != '']
    str_as_list = [word.capitalize() for word in str_as_list if word != '']
    
    #The 3 above in 1 line: str_as_list = [word.capitalize() for word in input_string.split(' ') if word != '']

    res_str = ' '.join(str_as_list)

    return res_str
    


# ------------------------



# Main Function
def main():
    return


if __name__ == '__main__':
    list1 = [1,1]
    list2 = [1,2,1]
    list3 = [1,1,1,1,1]
    list4 = [1,1,42,42]
    list5 = [1]
    
    # print(twin_neighbours(list3))
    
    
    matrix = [[1,2,3,4,5,6], [20,21,22,23,24,7], [19,32,33,34,25,8], [18,31,36,35,26,9], [17,30,29,28,27,10], [16,15,14,13,12,11]]
    # print(rotate_matrix_90_degrees_clockwise(matrix))
    
    q3_check = [4,10,13,71,10,10,71,71,2]
    # print(distance_of_number_in_list(q3_check, 71))
    
    # print(find_minimal_distance_number(q3_check))
    
    string1 = 'welcome       to my blog'
    string2 = "this 2Nd OPTION wITh feW SPACES and $#COMBOs"
    print(capitalize_words(string1))
    print(capitalize_words(string2))
    
    l2 = [10, 20, 30, 40, 50]
    print(l2[1:3])