# Terminal Application

The following 'Indie Film Generator' terminal application was designed and implemented using the Python programming language in order to showcase a thorough understanding of 
working with industry standard developer tools.

## Table of Contents

- Github repistory and project link
- Styling guide and styling convetions
- Features of application
- Implementation plan
- Installation Instructions
- Presentation
- References

## Github

Here is a link to the github repoistory and terminal application project

- https://github.com/Daniel-Piciocchi/terminal_application

## Styling Guide

The styling guide of choice was PEP 8, selected for optimizing readability across applications and platforms

- https://peps.python.org/pep-0008/

## Features

### Main Menu:

- When starting the program the user is initially presented with a title screen of the application followed by a 'Main Menu' with 4 options to choose from:

### Recommend: 

- The 'Recommend' feature selects a film for the user depending on one of the following option selected from the list/menu below: 

#### 1. Random Film

- recommends a random film from the entire database. 

#### 2. Unseen Film

- recommends a random film from the database that the user has not seen yet (user's can modify films in a selection below by marking them as seen).

#### 3. Film With Ratings Above

- users are asked to select a rating from 1 - 5 resulting in a film recommendation based on their input.

#### 4. Film Through Genre

- users are asked to input a genre from 'Animation, Comedy, Crime, Documentary, Drama, Romance, Thriller, Sci-fi' resulting in a film recommendation based on their input.

#### 5. Go Back To Main Menu

brings the user back to the 'Main Menu'.

### List:

- the 'List' feature presents films to the user depending on the following options selected from the list/menu below:

#### 1. All Films

- lists all films from the entire database to the user.

#### 2. Films With Ratings Above

- asks the user to input a rating resuling in a list of all films from that genre.

#### 3. Go Back To Main Menu

- brings the user back to the 'Main Menu'.

### Modify

- the 'Modify' feature allows the user to modify (add, delete, update rating, mark film as seen) depending on one of the options selected from the list/menu below:

#### 1. Add New Film

- ask's the user to input a title of a film, the genre, and the rating to add to the database.

#### 2. Delete Film

- ask's the user to input a title of a film to delete that film from the database.

#### 3. Updating Rating

- ask's the user to input a title of a film followed by a new rating selection.

#### 4. Mark Film As Seen

- ask's the user to input a title of a film to mark the film as seen (removing the film from selected lists for future film recommendation choices).

#### 5. Go Back To Main Menu

- brings the user back to the 'Main Menu'.

### Exit Program

- exit's the program.

## Implementation Plan

Here is a link to the implementation plan:

https://trello.com/b/4BqNwoGK/terminal-application

## Installation Instructions

User needs to install python 3:

https://www.python.org/downloads/

User needs to type 'make build' into a terminal to install external module used in application.

### Hardware requirements

This application has only been tested on a mac and therefore a mac OS is recommended.

## How To Run Program

User needs to type in 'make run' into a terminal to run the 'Indie Film Generator' application.

## How To Run Tests

User needs to type 'make test' into a terminal to run tests.

## Presentation

Here is a link to the overview and presentation of the project:

https://youtu.be/dt42LjHHEV8

## References 

https://peps.python.org/pep-0008/

https://realpython.com/python-pep8/

https://codefather.tech/blog/write-unit-test-python/

https://pypi.org/project/termcolor/

https://termcolor.readthedocs.io/

http://patorjk.com/software/taag/#p=testall&h=1&v=1&f=ANSI%20Shadow&t=Foreign%20and%20Indie%20Films%20Generator