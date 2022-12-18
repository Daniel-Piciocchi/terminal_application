import unittest
from functions import get_list_movies_above_rating, update_rating, recommend_movie_with_ratings_above, recommend_movie_through_genre, delete_movie, add_movie, Movie

import csv


class Test_Movie(unittest.TestCase):
    def test_get_list_movies_above_rating(self):
        resultOne = get_list_movies_above_rating("test_movie_data.csv", "4")
        resultTwo = get_list_movies_above_rating("test_movie_data.csv", "5")
        resultThree = get_list_movies_above_rating(
            "test_movie_data.csv", "2.5")

        expectedOne = list()
        expectedOne.append(Movie("Armour", "Romance", "4/5"))
        expectedOne.append(
            Movie("Blue Is The Warmest Colour", "Romance", "5/5"))
        expectedOne.append(Movie("Flee", "Animation", "4/5"))

        expectedTwo = list()
        expectedTwo.append(
            Movie("Blue Is The Warmest Colour", "Romance", "5/5"))

        expectedThree = list()
        expectedThree.append(Movie("Armour", "Romance", "4/5"))
        expectedThree.append(Movie(
            "Blue Is The Warmest Colour", "Romance", "5/5"))
        expectedThree.append(Movie("Flee", "Animation", "4/5"))

        self.assertEqual(expectedOne, resultOne)
        self.assertEqual(expectedTwo, resultTwo)
        self.assertEqual(expectedThree, resultThree)
        pass

    def test_update_rating(self):
        updated_movies = update_rating("test_movie_data.csv", "Flee", "4/5")
        expectedResult = [['Armour', 'Romance', '4/5'], ['Blue Is The Warmest Colour',
                                                         'Romance', '5/5'], ['Monk', 'Animation', '2/5'], ['Flee', 'Animation', '4/5']]

        self.assertEqual(updated_movies, expectedResult)
        pass

    def test_recommend_movie_with_ratings_above(self):
        resultOne = recommend_movie_with_ratings_above(
            "5", "test_movie_data.csv")
        expectedOne = Movie("Blue Is The Warmest Colour", "Romance", "5/5")

        self.assertEqual(expectedOne, resultOne)

    def test_recommend_movie_through_genre(self):
        resultOne = recommend_movie_through_genre(
            "genre_lists.csv", "Thriller")
        expectedOne = Movie("Phoenix", "Thriller", "2.5/5")

        self.assertEqual(expectedOne, resultOne)

    def test_delete_movie(self):
        resultOne = delete_movie("test_delete_movie.csv", "Monk")
        expectedOne = [['Armour', 'Romance', '4/5'],
                       ['Blue Is The Warmest Colour', 'Romance', '5/5']]

        resultTwo = delete_movie("test_delete_movie.csv", "Armour")
        expectedTwo = [['Blue Is The Warmest Colour', 'Romance', '5/5']]

        self.assertEqual(expectedOne, resultOne)
        self.assertEqual(expectedTwo, resultTwo)

    def test_add_movie(self):
        add_movie("test_add_movie.csv", ['new title', 'genre', '4/5'])
        expectedOne = ['new title', 'genre', '4/5']
        lastItem = None

        with open("test_add_movie.csv", "r") as readFile:
            rows = csv.reader(readFile)
            for row in rows:
                lastItem = row

        self.assertEqual(lastItem, expectedOne)


print(__name__)
if __name__ == "__main__":
    unittest.main()
