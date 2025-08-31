import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user.
7) Search movies.
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"--{heading} MOVIES--")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        formatted_date = movie_date.strftime("%b %d, %Y")
        print(f"{_id}: {title} (on {formatted_date})")
    print("---- \n")


def prompt_watch_movie():
    username = input("Enter your name: ")
    movie_id = int(input("Enter the movie ID you just watched: "))
    database.watch_movie(username, movie_id)


def prompt_show_watched_movies():
    user_name = input("Enter your name: ")
    movies = database.get_watched_movies(user_name)
    if movies:
        print_movie_list("Watched", movies)
    else:
        print("User haven't watched any movies yet!\n")


def prompt_search_movies():
    search_term = input("Enter partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Search results", movies)
    else:
        print("No movies found with that title!\n")


def prompt_add_user():
    username = input("Enter your name: ")
    database.add_user(username)


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(upcoming=True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")