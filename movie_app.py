from csv import writer

import csv
from functions import modify_movie_menu, list_movie_menu, recommend_movie_menu, get_list_movies_above_rating, get_main_menu_option, update_rating, recommend_movie_with_ratings_above, recommend_movie_through_genre, delete_movie, add_movie, mark_movie_as_seen, get_recommend_unseen_movie, list_all_movies, get_recommended_random_movie
import random
import sys
import time

from termcolor import colored


f = open('title.txt', 'r')


def print_ascii(fn):
    f = open(fn, 'r')
    print(''.join([line for line in f]))


print_ascii('title.txt')
print()

option = get_main_menu_option()

while option != 0:
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
        break
    else: 
        print(colored("Invalid Option!\n", "red", attrs=["bold"]))
        print(colored("Please Select A Number from 1 - 4", "cyan"))
        print()
        option = get_main_menu_option()
        
        
