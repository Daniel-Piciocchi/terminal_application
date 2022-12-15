rm -f test_add_movie.csv test_movie_data.csv test_delete_movie.csv
echo -e -n "Armour,Romance,4/5\nBlue Is The Warmest Colour,Romance,5/5\nMonk,Animation,2/5" >> test_add_movie.csv
echo "" >> test_add_movie.csv

echo -e -n "Armour,Romance,4/5\nBlue Is The Warmest Colour,Romance,5/5\nMonk,Animation,2/5" >> test_delete_movie.csv
echo "" >> test_delete_movie.csv
echo -e "Armour,Romance,4/5\nBlue Is The Warmest Colour,Romance,5/5\nMonk,Animation,2/5\nFlee,Animation,4/5" >> test_movie_data.csv