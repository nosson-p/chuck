import requests
import time
import os



print("starting...")
Credits = ('''
############ Credits ############
#           Nosson-p            #
#################################
''')




# getting categorys from api
while True:
    try:
        print(requests.get("https://api.chucknorris.io/jokes/categories").json())
        user_category = input("please select a catergory:\n")
        category_check = requests.get("https://api.chucknorris.io/jokes/random?category=" + user_category)
        # checks yo see if catogory_check caem back ok used to see if user put in a valid catogory 
        if category_check.ok:
            break
        else:
            os.system("cls")
            print("hmmm looks like that is not a catogory lets try again.")
            time.sleep(3)
            continue
    except requests.exceptions.RequestException:
        os.system("cls")
        print("oops somthing went wrong try again later.")
        time.sleep(3)
        exit()
        continue

os.system("cls")



while True:
    try:
        # getting joke with selected category piing into json and filtering "value" and replaceing any "Chuck Norris" with "Nosson"
        time.sleep(3)
        joke_from_api = requests.get("https://api.chucknorris.io/jokes/random?category=" + user_category).json()["value"].replace("Chuck Norris","Nosson").replace("Chuck","Nosson")
        print(joke_from_api)
    except requests.exceptions.RequestException:
        os.system("cls")
        print("oops somthing went wrong try again later.")
        time.sleep(3)
        exit()
        continue
