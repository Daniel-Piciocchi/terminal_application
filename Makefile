build: 
	pip3 install termcolor
run:
	python3 movie_app.py
test: 
	bash ./setup-test.sh
	python3 -m unittest test_movie.py