from csv import writer

import csv
from functions import get_list_movies_above_rating, update_rating, recommend_movie_with_ratings_above, recommend_movie_through_genre, delete_movie
import random


def add_movie():
    add_movie = []
    title = input("Please add a film\n")
    add_movie.append(title)
    genre = input("Please add a genre\n")
    add_movie.append(genre)
    rating = input("Please add a rating\n")
    add_movie.append(rating)

    with open("movie_list.csv", "a") as file:
        writer_object = writer(file)
        writer_object.writerow(add_movie)
        file.close()

def mark_movie_as_seen():
    title = input("Which title have you seen?\n")
    seen_movie = None
    with open("movie_list.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            if title == row[0]:
                seen_movie = row
    with open("movies_seen.csv", "a") as file:
        writer_object = writer(file)
        writer_object.writerow(seen_movie)
        file.close()


def get_recommend_unseen_movie():
    all_movies = list()
    seen_movies = list()
    with open("movie_list.csv", "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            all_movies.append(row)
    with open("movies_seen.csv", "r") as readFile:
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


def get_recommended_random_movie():
    all_movies = list()
    with open("movie_list.csv", "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            all_movies.append(row)
    movies_length = len(all_movies) - 1
    random_number = random.randint(0, movies_length)
    random_movie = all_movies[random_number]
    print(random_movie)


def list_all_movies():
    all_movies = list()
    with open("movie_list.csv", "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            all_movies.append(row)
            print(all_movies)


print("Welcome to Foreign and Indie Films!")
print("1. Create: add new movie")
print("2. Delete: delete movie")
print("3. Update: update rating")
print("4. List Movies With Ratings Above:")
print("5. Recommend Movies With Ratings Above:")
print("6. Mark Movie as Seen")
print("7. Recommend Unseen Movie")
print("8. Recommend Film Through Genre")
print("9. Recommend Random Movie")
print("10. List All Movies")

user_input = input()

if user_input == "1":
    add_movie()

if user_input == "2":
    title = input("Which title would you like to delete?\n")
    delete_movie("movie_list.csv", title)
    result = delete_movie(title, "movie_list.csv")
    print(result)

if user_input == "3":
    title = input("Which title would you like to change the rating for?\n")
    rating = input("What is your new rating?")
    update_rating("movie_list.csv", title, rating)

if user_input == "4":
    rating = input("Please select rating")
    movies = get_list_movies_above_rating("movie_list.csv", rating)
    # TODO: loop n print
    print(movies)

if user_input == "5":
    rating = input("Please select rating")
    result = recommend_movie_with_ratings_above(rating, "movie_list.csv")
    print(result)


if user_input == "6":
    mark_movie_as_seen()

if user_input == "7":
    get_recommend_unseen_movie()

if user_input == "8":
    movie_genre = input("Please select genre")
    result = recommend_movie_through_genre("movie_list.csv", movie_genre)
    print(result)

if user_input == "9":
    get_recommended_random_movie()

if user_input == "10":
    list_all_movies()
