# Photo Album Viewer
# Jacob Morningstar
# 12/06/2020
# Displays the photo id and title of photos from albums on the website 'https://jsonplaceholder.typicode.com/photos'

#imports
import requests
from bs4 import BeautifulSoup

# User inputs the album to view
while True:
    userQuery = 0
    while not 1 < userQuery < 101:
        try:
            userQuery = int(input("\nPlease enter the album ID of the album you would like to display (1-100)\n"))
            if 0 < userQuery < 101:
                break
            else:
                pass
        except:
            print("Please enter a numerical value")


    # Scraping the queried website for data
    url = 'https://jsonplaceholder.typicode.com/photos?albumId=' + str(userQuery)
    try:
        res = requests.get(url)
    except:
        print("Failed to connect to server please check your internet connection")
        input()
        quit(0)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')

    text = soup.findAll(text=True)

    # formatting data and making it into a list of dictionaries
    test = eval(str(text[0]).replace("\n", ""))

    print(f"\nDisplaying photo album {userQuery}\n")

    # Displaying all photo ids and titles
    ctr = 0
    for i in test:
        print(f"[{test[ctr]['id']}] {test[ctr]['title']}\n")
        ctr += 1

    # Asking the user if they would like to display another album
    keepGoing = ''
    while keepGoing != 'y' or 'n':
        keepGoing = input("\nWould you like to view another album (y/n)?\n")
        if keepGoing == 'y':
            break
        elif keepGoing == 'n':
            quit(0)
        else:
            print("\nPlease enter 'y' or 'n'")