from csv import writer

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



print("Welcome to Foreign and Indie Films!")
print("1. Create: add new movie")
print("2. Delete: delete movie")
print("3. Update: update rating")

user_input = input()

if user_input == "1":
    add_movie()



