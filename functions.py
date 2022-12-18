from csv import writer

import csv

import random

from termcolor import colored


class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return colored("\nTitle: ",  "red", attrs=["bold"]) + self.title + "\n" + colored("Genre: ", "green", attrs=["bold"]) + self.genre + "\n" + colored("Rating: ", "blue", attrs=["bold"]) + self.rating

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.title == other.title and self.genre == other.genre and self.rating == other.rating
        return False

def get_recommended_random_movie(csv_file):
    all_movies = list()
    with open(csv_file, "r", encoding="utf-8-sig") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            all_movies.append(row)
    movies_length = len(all_movies) - 1
    random_number = random.randint(0, movies_length)
    random_movie = all_movies[random_number]
    return Movie(random_movie[0], random_movie[1], random_movie[2])

def mark_movie_as_seen(csv_movie_list, csv_movie_seen_list, title):
    seen_movie = None

    with open(csv_movie_list, "r") as file:
        rows = csv.reader(file)
        for row in rows:
            if title.lower() == row[0].lower():
                seen_movie = row
    if seen_movie == None:
        return False

    with open(csv_movie_seen_list, "a") as file:
        writer_object = writer(file)
        writer_object.writerow(seen_movie)
        file.close()
    return True

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
            print(Movie(random_movie[0], random_movie[1], random_movie[2]))
            break


def recommend_movie_with_ratings_above(rating, csv_file):
    movies = get_list_movies_above_rating(csv_file, rating)
    if movies == None:
        return

    movies_length = len(movies) - 1
    random_number = random.randint(0, movies_length)
    random_movie = movies[random_number]
    return random_movie


def recommend_movie_through_genre(csv_file, movie_genre):
    movies_genre = list()
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        rows = csv.reader(file)
        for row in rows:
            if movie_genre == row[1]:
                movies_genre.append(row)
    if len(movies_genre) == 0:
        print(colored(
            "\nThat Genre Does Not Exist!", "red", attrs=["bold"]))
        print(colored("\nPlease select from:", "green", attrs=["bold"]))
        print("\nAnimation, Comedy, Crime, Documentary, Drama, Romance, Thriller, Sci-Fi\n")
    else:

        movies_length = len(movies_genre) - 1
        random_number = random.randint(0, movies_length)
        random_movie = movies_genre[random_number]
        return Movie(random_movie[0], random_movie[1], random_movie[2])


def list_all_movies(csv_file):
    all_movies = list()
    with open(csv_file, "r", encoding="utf-8-sig") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            all_movies.append(Movie(row[0], row[1], row[2]))
    return all_movies


def get_list_movies_above_rating(csv_file, rating):
    list_movies_above_rating = list()
    try:
        rating_as_number = float(rating)
        if rating_as_number > 5:
            print(colored("\nInput Invalid!\n", "red", attrs=["bold"]))
            print(colored("Please provide a number between: 0-5\n", "cyan"))
            return
    except:
        print(colored("\nInvalid Input!", "red", attrs=["bold"]))
        print(colored("\nPlease provide a number as input\n", "cyan"))
        return
    with open(csv_file, "r", encoding="utf-8-sig") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            found_rating = row[2]
            split_string_list = found_rating.split("/")
            if split_string_list[0] >= rating:

                list_movies_above_rating.append(Movie(row[0], row[1], row[2]))
    return list_movies_above_rating


def add_movie(csv_file, new_movie):
    with open(csv_file, "a", encoding="utf-8-sig") as file:
        writer_object = writer(file)
        writer_object.writerow(new_movie)
        file.close()


def delete_movie(csv_file, title):
    updated_movie_list = list()
    did_delete_movie = False

    with open(csv_file, "r", encoding="utf-8-sig") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            if title.lower() != row[0].lower():
                updated_movie_list.append(row)
            else:
                did_delete_movie = True

    with open(csv_file, 'w', encoding="utf-8-sig") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(updated_movie_list)
    if did_delete_movie == False:
        print(colored("\nDelete Failed. Film Not In Database!\n",
              "red", attrs=["bold"]))
        print(colored("Please select a film from the database\n", "cyan"))
    else:
        print(colored("\nFilm Deleted!\n", "green", attrs=["bold"]))
        print(title)
        print()
        return updated_movie_list


def update_rating(csv_file, title, rating):
    updated_movie_list = list()
    did_find_movie = False

    with open(csv_file, "r", encoding="utf-8-sig") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            if title.lower() == row[0].lower():
                updated_row = [row[0], row[1], rating]
                updated_movie_list.append(updated_row)
                did_find_movie = True
            else:
                updated_movie_list.append(row)

    with open(csv_file, "w", encoding="utf-8-sig") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(updated_movie_list)

    if did_find_movie == False:
        print()
        print(colored("Update Failed. Film Not In Database!\n",
              "red", attrs=["bold"]))
        print(colored("Please select a film from the database\n", "cyan"))
    else:
        print(colored("\nFilm Rating Updated To:\n", "green", attrs=["bold"]))
        print(rating)
        print()
    return updated_movie_list


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
        option = input(colored("Please select an option: \n", "cyan",))
        print()
        try:
            option_as_number = int(option)
            return option_as_number
        except:
            print(colored("Input Invalid!\n", "red", attrs=["bold"]))
            print(colored("Please type numbers only\n", "cyan"))


def recommend_movie_menu():
    print(colored("Recommend\n", "green", attrs=["bold", "underline"]))
    print("1. Random Film")
    print("2. Unseen Film")
    print("3. Film With Ratings Above: ")
    print("4. Film Through Genre")
    print("5. Go Back To Main Menu\n")
    user_input = input(colored("Please select an option: \n", "cyan",))
    if user_input == "1":
        result = get_recommended_random_movie("movie_list.csv")
        print(result)
        print()
        return 1
    elif user_input == "2":
        get_recommend_unseen_movie("movie_list.csv", "movies_seen.csv")
        print()
        return 1
    elif user_input == "3":
        rating = input(colored("\nPlease select rating: ", "cyan"))
        result = recommend_movie_with_ratings_above(
            rating, "movie_list.csv")
        if result != None:
            print(result)
            print()
        return 1
    elif user_input == "4":
        movie_genre = input("\nPlease select genre: ")
        result = recommend_movie_through_genre(
            "movie_list.csv", movie_genre)
        if result != None:
            print(result)
            print()
        return 1
    elif user_input == "5":
        print()
        return get_main_menu_option()
    else:
        print(colored("\nInvalid Option\n", "red", attrs=["bold"]))
        return 1


def list_movie_menu():
    print(colored("List\n", "yellow", attrs=["bold", "underline"]))
    print("1. All Films")
    print("2. Films With Ratings Above: ")
    print("3. Go Back To Main Menu: \n")
    user_input = input(colored("Please select an option: \n", "cyan",))
    if user_input == "1":
        movies = list_all_movies("movie_list.csv")
        for movie in movies:
            print(movie)
        print()
        return 2
    if user_input == "2":
        rating = input(colored("\nPlease select rating: ", "cyan"))
        movies = get_list_movies_above_rating("movie_list.csv", rating)
        if movies != None:
            for movie in movies:
                print(movie)
        print()
        return 2
    if user_input == "3":
        print()
        return get_main_menu_option()
    else:
        print(colored("\nInvalid Option!\n", "red", attrs=["bold"]))
        print(colored("Please select a number from 1 - 3\n", "cyan"))
        return 2


def modify_movie_menu():
    print(colored("Modify\n", "blue", attrs=["bold", "underline"]))
    print("1. Add New Film")
    print("2. Delete Film")
    print("3. Update Rating")
    print("4. Mark Film As Seen")
    print("5. Go Back To Main Menu\n")
    user_input = input(colored("Please select an option: \n", "cyan",))
    if user_input == "1":
        new_movie = []
        title = input(colored("\nPlease add a title:\n", "cyan"))
        new_movie.append(title)
        genre = input(colored("\nPlease add a genre:\n", "cyan"))
        new_movie.append(genre)
        rating = input(colored("\nPlease add a rating:\n", "cyan"))
        formatted_rating = rating + '/5'
        new_movie.append(formatted_rating)
        add_movie("movie_list.csv", new_movie)
        print(colored("\nMovie Added:", "green", attrs=["bold"]))
        print(Movie(new_movie[0], new_movie[1], new_movie[2]))
        print()
        return 3
    if user_input == "2":
        title = input(
            colored("\nWhich title would you like to delete?\n", "cyan"))
        delete_movie("movie_list.csv", title)
        return 3
    if user_input == "3":
        title = input(colored(
            "\nWhich title would you like to change the rating for?\n", "cyan"))
        rating = input(colored("\nWhat is your new rating?\n", "cyan"))
        try:
            rating_as_number = float(rating)
            if rating_as_number > 5:
                print(colored("\nInput Invalid!", "red", attrs=["bold"]))
                print(colored("\nPlease provide number between 0-5\n", "cyan"))
                return 3
        except:
            print(colored("\nInvalid Option!\n", "red", attrs=["bold"]))
            print(colored("Please provide a number as input\n", "cyan"))
            return 3
        formatted_rating = rating + '/5'
        update_rating("movie_list.csv", title, formatted_rating)
        return 3
    if user_input == "4":
        title = input(colored("\nWhich title have you seen?\n", "cyan"))
        result = mark_movie_as_seen(
            "movie_list.csv", "movies_seen.csv", title)
        if result == True:
            print()
            print(title, colored(
                "\n\nSuccessfully Added " + title + " To Films Seen List!\n", "green", attrs=["bold"]))
        else:
            print(colored("\nFilm Does Not Exist!", "red", attrs=["bold"]))
            print(colored("\nPlease select a film from the database\n", "cyan"))
        return 3
    if user_input == "5":
        print()
        return get_main_menu_option()

    else:
        print(colored("\nInvalid Option!\n", "red", attrs=["bold"]))
        print(colored("Please select a number from 1 - 3\n", "cyan"))
        return 3
