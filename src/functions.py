"""
------------------------------------------------------------------------
list of callable functions
------------------------------------------------------------------------
Author: Katrina Co
ID: 200804230
Email:  coxx4230@mylaurier.ca
__updated__ = "2020-04-20"
------------------------------------------------------------------------
"""

def read_positive():
    """
    -------------------------------------------------------
    Asks user for numbers, returns a list of only positive 
    numbers given, user types in "0" to stop prompt
    Use: read_positive()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        positive_list - list of positive numbers
    ------------------------------------------------------
    """
    positive_list = []
    user_num = int(input("Enter a positive integer number: "))
    while (user_num != 0): 
        if user_num > 0:
            positive_list.append(user_num)
            user_num = int(input("Enter a positive integer number: "))
        else:
            user_num = int(input("Enter a positive integer number: ")) 
    
    return positive_list


def find_target(num_list, target):
    """
    -------------------------------------------------------
    Finds all indexes in which the target is in the list
    Use: indexes = find_target(num_list, target)
    -------------------------------------------------------
    Parameters:
        num_list - list positive numbers to search through 
        target - number to search for in the list 
    Returns:
        indexes - list of indexes where target is found
    ------------------------------------------------------
    """
    indexes = []
    length = len(num_list)
    i = 0
    
    while i < length:
        if num_list[i] == target:
            indexes.append(i)
            i = i + 1
        else:
            i = i + 1
    
    return indexes


def largest_odd(integers):
    """
    -------------------------------------------------------
    Calculates the largest odd number in given list, 
    if no odd numbers returns -1
    Use: largest = largest_odd(integers)
    -------------------------------------------------------
    Parameters:
        integers - list of positive numbers
    Returns:
        largest - largest odd number in list 
    ------------------------------------------------------
    """
    largest = -1
    length = len(integers)
    
    for i in range (length):
        if integers[i] % 2 == 0:
            largest = largest
        else:
            if integers[i] > largest:
                largest = integers[i]       
    
    return largest

def reverse_list(num_list):
    """
    -------------------------------------------------------
    Mutates given list such that all elements are reversed
    Use: reverse_list(num_list)
    -------------------------------------------------------
    Parameters:
        num_list - list of positive integers
    Returns:
        None
    ------------------------------------------------------
    """
    length = len(num_list)
    counter = 0
    
    for i in range (length): 
        element = num_list.pop(length-1)
        num_list.insert(counter, element)
        counter = counter + 1
    
    print("List reversed: {}".format(num_list))
    
    return 