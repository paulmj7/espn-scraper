from bs4 import BeautifulSoup
import requests

def get_team():
    print("What sport does the team play?")
    sport = input("Enter 3-letter abbreviation: ")
    print("What team is it?")
    team = input("Enter 3-letter abbreviation: ")
    info = [sport, team]
    return info

info_list = get_team()

response = requests.get("http://www.espn.com/" + info_list[0] + "/team/_/name/" + info_list[1])
soup = BeautifulSoup(response.content, "html.parser")
location = soup.find("span", class_="ClubhouseHeader__Location").text
name = soup.find("span", class_="ClubhouseHeader__DisplayName").text
record = [i.text for i in soup.find("ul", class_="ClubhouseHeader__Record").find_all('li')]
print(location + " " + name)
print("Record: " + record[0])
print("Standing: " + record[1])
