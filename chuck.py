# imports
import os # os commands for changing color and clearing screen 
import requests 
import time # sleeps
import pyperclip # copy to cliperboard


os.system("color 0d") # changeing color to purple (only windows)
Info = ('''
############ Credits ############
#           Nosson-p            #
#      github.com/nosson-p/     #
#  made with api.chucknorris.io #
#             v1.0              #
#################################
''')

print(Info)
time.sleep(2)

# clear screen
def Clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


Clear_screen()
#getting username ether from pc or user
while True:
    try:
        y_n = input("Is this your name " + os.getlogin() + " y/n :\n")
        if y_n == "y":
            Username = os.getlogin()
            break
        else:
            Username = input("What is your name then:\n")
            break
    except ValueError:
        print("Please enter only y/n:")
        continue

# getting categorys from api
while True:
    try:
        
        Number_of_jokes = int(input("Number of jokes\n"))# getting number of jokes
        Clear_screen()
        print(requests.get("https://api.chucknorris.io/jokes/categories").json()) # printing joke categorys 
        User_joke_category = input("\nplease select a catergory from above ^\n") # asking user to pick categorys
        # checks yo see if catogory_check caem back ok used to see if user put in a valid catogory
        User_category_check = requests.get("https://api.chucknorris.io/jokes/random?category=" + User_joke_category) 
        if User_category_check.ok:
            break
        else:
            Clear_screen()
            print("Please enter a valid value:")
            time.sleep(2)
            continue 


    except requests.exceptions.RequestException: # if any errors pop up with getting the joke
        Clear_screen()
        print("An internet error acurred please try again later or check your connection:")
        time.sleep(2)
        exit()
        continue 
    except ValueError: # if number_of_jokes is not a number(int)
        Clear_screen()
        print("Please enter a valid value:")
        continue

Clear_screen()
All_api_jokes = ""
# getting a cerrtent number of jokes 
for i in range(Number_of_jokes):
    try:
        # getting joke with selected category piping into json and filtering "value" and replaceing any "Chuck Norris" or "chuck" with (username).
        Jokes_from_api_catogory = requests.get("https://api.chucknorris.io/jokes/random?category=" + User_joke_category).json()["value"].replace("Chuck Norris",Username).replace("Chuck",Username)
        print(Jokes_from_api_catogory) # printing joke
        All_api_jokes += str(Jokes_from_api_catogory) + '\n' # Have a variable that changes value and then store all values in a multi line var and then copy to clipboard
    except requests.exceptions.RequestException: # If any errors pop up with getting the joke
        Clear_screen()
        print("Oops something went wrong try again later.")
        time.sleep(2)
        exit()


pyperclip.copy(All_api_jokes) # Copying jokes to clipboard
input("Done, run again to get more jokes") # Asking user to run again to get more jokes
