from csv import writer

import csv

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
            # lines.append(row)
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
            # lines.append(row)
            if title == row[0]:
                updated_row = [row[0], row[1] ,rating]
                updated_movie_list.append(updated_row)
            else:
                updated_movie_list.append(row)

                
    with open('movie_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(updated_movie_list)


def recommend_movies():
    rating = input("Please select rating")
    with open("movie_list.csv", "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            found_rating = row[2]
            split_string_list = found_rating.split("/")
            # if rating == row[2]:
            if split_string_list[0] >= rating:
                print(row)

               


print("Welcome to Foreign and Indie Films!")
print("1. Create: add new movie")
print("2. Delete: delete movie")
print("3. Update: update rating")
print("4. Recommend Movies With Ratings Above:")

user_input = input()

if user_input == "1":
    add_movie()

if user_input == "2":
    delete_movie()

if user_input == "3":
    update_rating()

if user_input == "4":
    recommend_movies()



