from datetime import datetime

date_creation = datetime.now().strftime("%Y-%m-%d")
Name_author= "@Mouliom Pagna"
script_Name = "Programming_in_python_Day_1"
purpose = "Given an array of integers and an integer target, return indices of \n \t\t\t\t the two numbers such that they add up to target."
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

def search_index(T_array, target):
    """
    This function take as input an array T_array and a target and it returns
    two indices of the elements i and j of the Array such that
    Target = T_array[i] + T
    """
    n = len(T_array)
    L = []
    for i in range(0,n):
        for j in range(i,n):
            if(T_array[i]  + T_array[j] == target):
                L.append((i,j))

    if(len(L) != 0):
        return L            
    else:
        print("There is not a path for the target in the array !")
        return L

def display_result(array,Target):
    print(f"==> For an array ARRAY = {array} and a Target T = {Target}")
    index = search_index(array,Target)    
    print(f"==> Indices: {index}")

# Application
T = [2,4,5,7,12]
t = 9

display_result(T, 5)