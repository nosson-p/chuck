# imports
import os
import requests
import time
import pyperclip



os.system("color 0d") # changeing color to purple (only windows)
Authors = ('''
############ Credits ############
#           Nosson-p            #
#      github.com/nosson-p/     #
#  made with api.chucknorris.io #
#################################
''')

print(Authors)
time.sleep(2)

# clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_screen()
users_name = input("NAME:\n")


# getting categorys from api
while True:
    try:
        
        number_of_jokes = int(input("Number of jokes\n"))# getting number of jokes
        clear_screen()
        print(requests.get("https://api.chucknorris.io/jokes/categories").json()) # printing joke categorys 
        user_category = input("\nplease select a catergory from above ^\n") # asking user to pick categorys
        # checks yo see if catogory_check caem back ok used to see if user put in a valid catogory 33333333333333333333333333333333333333333333333
        category_check = requests.get("https://api.chucknorris.io/jokes/random?category=" + user_category) 
        if category_check.ok:
            break
        else:
            clear_screen()
            print("please enter a valid value:")
            time.sleep(2)
            continue 


    except requests.exceptions.RequestException: # if any errors pop up with getting the joke
        clear_screen()
        print("An internet error acurred please try again later or check your connection:")
        time.sleep(2)
        exit()
        continue
    except ValueError: # if number_of_jokes is not a number(int)
        clear_screen()
        print("please enter a valid value:")
        continue

clear_screen()

# getting a cerrtent number of jokes 
for i in range(number_of_jokes):
    try:
        # getting joke with selected category piping into json and filtering "value" and replaceing any "Chuck Norris" or "chuck" with (user_name).
        joke_from_api_catogory = requests.get("https://api.chucknorris.io/jokes/random?category=" + user_category).json()["value"].replace("Chuck Norris",users_name).replace("Chuck",users_name)
        print(joke_from_api_catogory) # printing joke
    except requests.exceptions.RequestException: # if any errors pop up with getting the joke
        clear_screen()
        print("oops something went wrong try again later.")
        time.sleep(2)
        exit()


clear_screen()
pyperclip.copy(joke_from_api_catogory) # copying jokes to clipboard
input("done, run again to get more jokes")
