from functions import modify_movie_menu, list_movie_menu, recommend_movie_menu, get_main_menu_option

import sys
import time

from termcolor import colored

def print_ascii(fn):
    textWrapper = open(fn, 'r')
    print(''.join([line for line in textWrapper]))


print_ascii('title.txt')
print()

option = get_main_menu_option()

while True:
    if option == 1:
        option = recommend_movie_menu()
    elif option == 2:
            option = list_movie_menu()
    elif option == 3:
            option = modify_movie_menu()
    elif option == 4:
        print(colored("\nSee You Next Time!\n", "cyan", attrs=["bold"]))
        time.sleep(1)
        sys.exit()
    else: 
        print(colored("Invalid Option!\n", "red", attrs=["bold"]))
        print(colored("Please Select A Number from 1 - 4", "cyan"))
        print()
        option = get_main_menu_option()
        
        
