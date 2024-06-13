
def display_menu():
    print("The Movie List Program")
    print("/n)
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()


def list(movie_list):
    for i, movie in enumerate(movie_list, start= 1):
        print (f"{i}. {movie}")
    print()

def add(movie_list):
    movie= input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("invalid movie number.\n")

    else:
        movie= movie_list.pop(number-1)
        print(f"{movie} was deleted.\n")

def main():
    movie_list =[ "Bride Wars", 
                 "The Devil Wears Prada",
                "National Treasure"]
    display_menu()

    while True:
        command = input ("Command: ")
        if command.lower() =="list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "delete":
            delete(movie_list)
        elif command.lower()== "exit":
            break
        else:
            print("not a valid comman. Please try again. \n")

    print("Goodbye!")

if __name__ == "__main__":
    main("/n)
