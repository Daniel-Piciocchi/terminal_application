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


print("Welcome to Foreign and Indie Films!")
print("1. Create: add new movie")
print("2. Delete: delete movie")
print("3. Update: update rating")

user_input = input()

if user_input == "1":
    add_movie()

if user_input == "2":
    delete_movie()



