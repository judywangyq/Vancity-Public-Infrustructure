'''
Judy Wang
Fall 2022 CS5001
Final Project Milstone 1 
input file
'''


def loop_input():

    user_choices = 0

    while user_choices != "E":

        user_choices = str(input("Which option would you like? type 1 for 'Public School'\n, 2 for 'Independent School'\n, 3 for 'StrongStart BC'\n, or 4 for 'Any Type of School'\n, choose E to exit \n"))
        if user_choices == 'E':
            print("Thanks for analyzing!")
            break
        
        return user_choices
