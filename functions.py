from csv import writer

import csv

import random

from termcolor import colored


def get_recommended_random_movie(csv_file):
    all_movies = list()
    with open(csv_file, "r", encoding="utf-8-sig") as readFile:
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
    with open(csv_file, "r", encoding="utf-8-sig") as readFile:
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
    print(colored("Main Menu\n", "red", attrs=["bold", "underline"]))
    print(colored("1. Recommend", "green"))
    print(colored("2. List", "yellow"))
    print(colored("3. Modify", "blue"))
    print(colored("4. Exit Program", "magenta"))


def get_main_menu_option():
    while True:
        main_menu()
        print()
        option = input("Please Select An Option: \n")
        try:
            option_as_number = int(option)
            return option_as_number
        except:
            print("Option Invalid, Please Select Number from 1 - 4\n")


def recommend_movie_menu():
    print(colored("\nRecommend:\n", "green", attrs=["bold", "underline"]))

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
        return 1
    elif user_input == "2":
        print()
        get_recommend_unseen_movie("movie_list.csv", "movies_seen.csv")
        return 1
    elif user_input == "3":
        rating = input("Please select rating: ")
        print()
        result = recommend_movie_with_ratings_above(
            rating, "movie_list.csv")
        print(result)
        return 1
    elif user_input == "4":
        movie_genre = input("Please select genre: ")
        print()
        result = recommend_movie_through_genre(
            "movie_list.csv", movie_genre)
        print(result)
        return 1
    elif user_input == "5":
        print()
        return get_main_menu_option()
    else:
        print("Invalid Option")
        return 1
