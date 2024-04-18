#Brian Nordlinger


def not_string(str):
    if(str[0:3] == "not"):
        return(str)
    else:
        return("not" + str)

    """
    Given a string, return a new string where "not" has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    not_string("cat") returns "notcat"
    not_string("not") returns not
    """
    pass


def swap(lst):
    min_int = min(lst)
    ind = lst.index(min_int)
    first_num = lst[0]
    lst[0] = min_int
    lst[ind] = first_num
    return(lst)
        
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    pass


def count_spaces(string):
    space = [space for space in string if space == ' ']
    return len(space)
    """
    Use comprehension to count the number of spaces in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_spaces("the cow jumped over the moon") returns 5
    Hint: your comprehension should return a new string (list of characters)
    with just spaces.
    """
    pass


def build_heights_dict():
    heights = {}
    with open("heights.txt") as file:
        for line in file:
            stripped_line=line.strip()
            token = stripped_line.split()
            heights[token[0] + " " + token[1]]= int(token[2])
            
    return heights
    '''
    Create a dictionary where the key is a person's name and the value is
    their height stored as an integer. 
    Read in the file, heights.txt, store the person's first name and 
    last name as the key (first and last name should have a space between them)
    and their height as the integer value.
    Your output should read:
     {'Thomas Jones': 70, 'Marcus Hansen': 68, 'Sarah Jenkins': 63, 
     'Abigail Ross': 65, 'Sebastian Adams': 70, 'Ella Rivera': 59, 
     'Luis Cruz': 71, 'Matt Patterson': 74, 'Jayden Cox': 67, 
     'Javier Alvaro': 69, 'Victoria Thompson': 62, 
     'Daniel Richardson': 68, 'Zoey Miller': 66}
    '''

print('not_string("cat") expected: notcat')
print('not_string("cat") actual:', not_string("cat"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print('count_spaces("the cow jumped over the moon") expected: 5')
print('count_spaces("the cow jumped over the moon") actual:', count_spaces("the cow jumped over the moon"))

print(build_heights_dict())