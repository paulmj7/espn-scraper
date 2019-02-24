# BeautifulSoup library to parse and scrape text from html pages
from bs4 import BeautifulSoup
# Requests library to retrieve information from the web
import requests

# Function to determine what sport and team to search for
def get_team():
    print("What sport does the team play?")
    sport = input("Enter 3 letter abbreviation: ")
    print("What team is it?")
    team = input("Enter 2 or 3 letter abbreviation: ")
    info = [sport, team]
    return info

# Variable saves the list object returned by the function call
info_list = get_team()

# Variable saves html page returned by the function call
response = requests.get("http://www.espn.com/" + info_list[0] + "/team/_/name/" + info_list[1])
# Parses html page
soup = BeautifulSoup(response.content, "html.parser")

# Finds information about the specified team
try:
  location = soup.find("span", class_="ClubhouseHeader__Location").text
  name = soup.find("span", class_="ClubhouseHeader__DisplayName").text
  # Prints the team information
  print(location + " " + name)
  record = [i.text for i in soup.find("ul", class_="ClubhouseHeader__Record").find_all('li')]
  print("Record: " + record[0])
  print("Standing: " + record[1])
except:
  print("Season has not started")

