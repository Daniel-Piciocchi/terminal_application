from csv import writer

import csv

import random

from termcolor import colored



def get_recommended_random_movie(csv_file):
    all_movies = list()
    with open(csv_file, "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            all_movies.append(row)
    movies_length = len(all_movies) - 1
    random_number = random.randint(0, movies_length)
    random_movie = all_movies[random_number]
    return random_movie

def get_recommend_unseen_movie(csv_movie_list, csv_movie_seen):
    all_movies = list()
    seen_movies = list()
    with open(csv_movie_list, "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            all_movies.append(row)
    with open(csv_movie_seen, "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            seen_movies.append(row)
    while True:
        movies_length = len(all_movies) - 1
        random_number = random.randint(0, movies_length)
        random_movie = all_movies[random_number]
        if random_movie not in seen_movies:
            print(random_movie)
            break
        

def recommend_movie_with_ratings_above(rating, csv_file):
    movies = get_list_movies_above_rating(csv_file, rating)
    movies_length = len(movies) - 1
    random_number = random.randint(0, movies_length)
    random_movie = movies[random_number]
    return random_movie

def recommend_movie_through_genre(csv_file, movie_genre):
    movies_genre = list()
    with open(csv_file, "r") as file:
        rows = csv.reader(file)
        for row in rows:
            if movie_genre == row[1]:
                movies_genre.append(row)
    movies_length = len(movies_genre) - 1
    random_number = random.randint(0, movies_length)
    random_movie = movies_genre[random_number]
    return random_movie

def list_all_movies(csv_file):
    all_movies = list()
    with open(csv_file, "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            all_movies.append(row)
    return all_movies


def get_list_movies_above_rating(csv_file, rating):
    list_movies_above_rating = list()
    with open(csv_file, "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            found_rating = row[2]
            split_string_list = found_rating.split("/")
            if split_string_list[0] >= rating:
                list_movies_above_rating.append(row)
    return list_movies_above_rating

def add_movie(csv_file, new_movie):
    with open(csv_file, "a") as file:
        writer_object = writer(file)
        writer_object.writerow(new_movie)
        file.close()

def delete_movie(csv_file, title):
    updated_movie_list = list()
    
    with open(csv_file, "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            if title != row[0]:
                updated_movie_list.append(row)
    with open(csv_file, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(updated_movie_list)
    return updated_movie_list

def update_rating(csv_file, title, rating):
    updated_movie_list = list()

    with open(csv_file, "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            if title == row[0]:
                updated_row = [row[0], row[1], rating]
                updated_movie_list.append(updated_row)
            else:
                updated_movie_list.append(row)

    with open(csv_file, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(updated_movie_list)

    return updated_movie_list

def mark_movie_as_seen(csv_movie_list, csv_movie_seen_list, title):
    seen_movie = None

    with open(csv_movie_list, "r") as file:
        rows = csv.reader(file)
        for row in rows:
            if title == row[0]:
                seen_movie = row
    if seen_movie == None:
        return False

    with open(csv_movie_seen_list, "a") as file:
        writer_object = writer(file)
        writer_object.writerow(seen_movie)
        file.close()
    return True


def main_menu():
    print(colored("Main Menu\n", "red"))
    print("1. Recommend")
    print("2. List")
    print("3. Modify")
    print("4. Exit Program")


def get_main_menu_option():
    main_menu()
    print()
    option = int(input("Please Select An Option: \n"))
    return option





