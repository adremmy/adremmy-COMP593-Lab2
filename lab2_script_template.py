def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Remy Adepetun',
        'student_id': 10327073,
        'pizza_toppings': ['OLIVES', 'MUSHROOM', 'SAUSAGE'],
        'movies': [
         {'title': 'chuck', 'genre' :'comedy',
         'title': 'you got served', 'genre' : 'dance-drama'

         }   
        ],

    }

    # TODO: Step 3 - Add another movie to the data structure
    another_movie = {
        'title': 'stomp the yard', 'genre' : 'dance-romance'
    }
    about_me['movies'].append(another_movie)
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(
        f"My name is {full_name}, but you can call me Mr {first_name}.\nMy student ID is {student_id}."
    )
    print(f"My student ID is {student_id}.\n")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].append(toppings)
    about_me['pizza_toppings']= sorted(about_me['pizza_toppings'])
    about_me['pizza_toppings']= [topping.lower() for topping in
     about_me['pizza_toppings'] ]               
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favorite pizza toppings are:")
    for toppings in about_me['pizza_toppings']:
        print(f"- {toppings}") 
        print()
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movies']]
    print(f"I like to watch {', '.join(genres)} movies.\n")
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie['title'].title() for movie in movie_list]
    print(f"Some of my favorite movies are {','.join(titles)}!\n")
    return
    
if __name__ == '__main__':
    main()