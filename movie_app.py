from csv import writer

import csv
from functions import get_list_movies_above_rating, get_main_menu_option, update_rating, recommend_movie_with_ratings_above, recommend_movie_through_genre, delete_movie, add_movie, mark_movie_as_seen, get_recommend_unseen_movie, list_all_movies, get_recommended_random_movie
import random
import sys
import time

from termcolor import colored


f = open('bat.txt', 'r')


def print_ascii(fn):
    f = open(fn, 'r')
    print(''.join([line for line in f]))


print_ascii('bat.txt')
print()

option = get_main_menu_option()

while option != 0:
    if option == 1:
        print(colored('\nRecommend\n', 'red'))

        print("1. Random Film")
        print("2. Unseen Film")
        print("3. Film With Ratings Above: ")
        print("4. Film Through Genre")
        print("5. Go Back To Main Menu")
        user_input = input()
        if user_input == "1":
            print()
            result = get_recommended_random_movie("movie_list.csv")
            print(result)
        elif user_input == "2":
            print()
            get_recommend_unseen_movie("movie_list.csv", "movies_seen.csv")
        elif user_input == "3":
            rating = input("Please select rating ")
            result = recommend_movie_with_ratings_above(
                rating, "movie_list.csv")
            print(result)
            break
        elif user_input == "4":
            movie_genre = input("Please select genre ")
            result = recommend_movie_through_genre(
                "movie_list.csv", movie_genre)
            print(result)
        elif user_input == "5":
            print()
            option = get_main_menu_option()
        else:
            print("Invalid Option")

    elif option == 2:
        print("\nList:\n")
        print("1. All Films")
        print("2. Films With Ratings Above: ")
        print("3. Go Back To Main Menu: \n")
        user_input = input()
        if user_input == "1":
            movies = list_all_movies("movie_list.csv")
            for movie in movies:
                print(movie)
            print()
        if user_input == "2":
            rating = input("Please select rating ")
            movies = get_list_movies_above_rating("movie_list.csv", rating)
            for movie in movies:
                print(movie)
            print()
        if user_input == "3":
            print()
            option = get_main_menu_option()
    elif option == 3:
        print("\nModify:\n")
        print("1. Add New Film")
        print("2. Delete Film")
        print("3. Update Rating")
        print("4. Mark Film As Seen")
        print("5. Go Back To Main Menu")
        user_input = input()
        if user_input == "1":
            new_movie = []
            title = input("Please add a title\n")
            new_movie.append(title)
            genre = input("Please add a genre\n")
            new_movie.append(genre)
            rating = input("Please add a rating\n")
            new_movie.append(rating)
            add_movie("movie_list.csv", new_movie)
            print("Movie Added!")
        if user_input == "2":
            title = input("Which title would you like to delete?\n")
            delete_movie("movie_list.csv", title)
            print("Film Deleted!")
        if user_input == "3":
            title = input(
                "Which title would you like to change the rating for?\n")
            rating = input("What is your new rating?")
            update_rating("movie_list.csv", title, rating)
        if user_input == "4":
            title = input("Which title have you seen?\n")
            result = mark_movie_as_seen(
                "movie_list.csv", "movies_seen.csv", title)
            if result == True:
                print("Successfully Added!")
            else:
                print("Film Does Not Exist!")
        if user_input == "5":
            print()
            option = get_main_menu_option()
    elif option == 4:
        print("\n See You Next Time!")
        time.sleep(1)
        sys.exit()
        break
    else:
        print("Invalid Option")
