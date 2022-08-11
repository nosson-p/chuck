#from multiprocessing.sharedctypes import Value
from distutils.log import error
from unicodedata import category
import requests
import time
import os

Credits = ('''
############ Credits ############
#           Nosson-p            #
#################################
''')
print("starting...")
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
            print("something went wrong how about we try that again.")
            time.sleep(3)
            continue
    except requests.exceptions.RequestException:
        print("something went wrong how about we try that again.")
        os.system("cls")
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
        print("something went wrong how about we try that again.")
        continue
