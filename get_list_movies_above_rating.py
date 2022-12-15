import csv

def get_list_movies_above_rating(csv_file, rating):
    list_movies_above_rating = list()
    with open(csv_file, "r") as readFile:
        rows = csv.reader(readFile)
        for row in rows:
            found_rating = row[2]
            print(found_rating)
            split_string_list = found_rating.split("/")
            print(split_string_list[0] >= rating)
            if split_string_list[0] >= rating:
                print("appending row")
                print(row)
                list_movies_above_rating.append(row)
    return list_movies_above_rating
