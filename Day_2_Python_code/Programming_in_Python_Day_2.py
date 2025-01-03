from datetime import datetime

date_creation = datetime.now().strftime("%Y-%m-%d")
Name_author= "@Mouliom Pagna"
script_Name = "Programming_in_python_Day_2"
purpose = "Given an integer array nums, find the subarray with the largest sum, and return its sum"
version = "2.0"
head = f"""
\"\"\"
==========================================================================================
Nom du Fichier : {script_Name}
Description    : {purpose}
Auteur         : {Name_author}
Date de création : {date_creation}
Version        : {version}
==========================================================================================
\"\"\"
"""
print(head)

def min_element(T_array):
    """
    This function take as input an array T_array and look for the minimum between the 
    elements of the  array and return it.

    min = min(T_array)
    """
    n = len(T_array)
    L = []
    min = T_array[0]

    for i in range(1,n):
        if (T_array[i] < min):
            min = T_array[i]
            index = i
        else:
            index = 0
    return min, index

def sub_array(T_array):
    """
    This function takes as an argument an arrya of integer and return a subarray of the initial array given.
    The subarray here is the array where the minimum of the elements has been drop.
    """

    T_array.pop(min_element(T_array)[1])

    return T_array

def sum_array(T_array):
    """
    This function take as argument an array and calculate the sum of the elements of the array and return it
    """

    n = len(T_array)
    sum = 0
    for i in range(0,n):
        sum += T_array[i]

    return sum

def display_result(array):
    """
    The aim of this function is to display the result
    """
    S = sub_array(array)
    print(f"==> For an array A = {array}, the subarray is S= {S}") 
    print(f"==> The sum of the subarray is: {sum_array(S)}")

# Application
T = [54,45,23,70,12]

display_result(T)