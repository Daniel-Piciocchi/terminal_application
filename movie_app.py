from csv import writer

import csv

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

def delete_movie():
    title = input("Which title would you like to delete?\n")
    updated_movie_list = list()
   
    with open("movie_list.csv", "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            if title != row[0]:
                updated_movie_list.append(row)
    with open('movie_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(updated_movie_list)

def update_rating():
    title = input("Which title would you like to change the rating for?\n")
    rating = input("What is your new rating?")
    updated_movie_list = list()
   
    with open("movie_list.csv", "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            if title == row[0]:
                updated_row = [row[0], row[1] ,rating]
                updated_movie_list.append(updated_row)
            else:
                updated_movie_list.append(row)

                
    with open('movie_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(updated_movie_list)


def get_list_movies_above_rating():
    rating = input("Please select rating")
    list_movies_above_rating = list()
    with open("movie_list.csv", "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            found_rating = row[2]
            split_string_list = found_rating.split("/")
            if split_string_list[0] >= rating:
                list_movies_above_rating.append(row)
    return list_movies_above_rating

def recommend_movie_with_ratings_above():
    movies = get_list_movies_above_rating()
    movies_length = len(movies) -1
    random_number = random.randint(0, movies_length)
    random_movie = movies[random_number]
    print(random_movie)

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

def recommend_movie_through_genre():
    movies_genre = list()
    genre = input("Which Genre Would You Like?")
    with open("movie_list.csv", "r") as file:
        rows = csv.reader(file)
        for row in rows:
            if genre == row[1]:
                movies_genre.append(row)
    movies_length = len(movies_genre) - 1
    random_number = random.randint(0, movies_length)
    random_movie = movies_genre[random_number]
    print(random_movie)

    


    
            

    

print("Welcome to Foreign and Indie Films!")
print("1. Create: add new movie")
print("2. Delete: delete movie")
print("3. Update: update rating")
print("4. List Movies With Ratings Above:")
print("5. Recommend Movies With Ratings Above:")
print("6. Mark Movie as Seen")
print("7. Recommend Unseen Movie")
print("8. Recommend Film Through Genre")

user_input = input()

if user_input == "1":
    add_movie()

if user_input == "2":
    delete_movie()

if user_input == "3":
    update_rating()

if user_input == "4":
    movies = get_list_movies_above_rating()
    # TODO: loop n print
    print(movies)

if user_input == "5":
    recommend_movie_with_ratings_above()

if user_input == "6":
    mark_movie_as_seen()

if user_input == "7":
    get_recommend_unseen_movie()

if user_input == "8":
    recommend_movie_through_genre()



