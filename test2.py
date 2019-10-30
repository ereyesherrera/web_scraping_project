import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# =======================================================
session = HTMLSession()
resp = session.get("https://www.tfrrs.org/results/xc/16604/Jim_DrewsTori_Neubauer_Invitational")
resp.html.render()


soup = BeautifulSoup(resp.html.html, "lxml")

table_rows = []

rows = soup.findAll('tr')
for row in rows:
    row_td = row.find_all('td')
    str_cells = str(row_td)
    clean = BeautifulSoup(str_cells, "lxml")
    cleanText = clean.get_text(strip=True)
    table_rows.append(cleanText)

# print(table_rows)
# print(table_rows[23])
# print(table_rows[422])

individual_times = table_rows[23:423]
# print(individual_times)


LacrosseMeet = pd.DataFrame(individual_times)

LacrosseMeet = LacrosseMeet[0].str.split(',', expand=True)
LacrosseMeet.columns = ["Place", "LastName", "FirstName", "Year", "Team", "AvgMile", "Time", "Score", "3k", "5.8k"]
LacrosseMeet["Place"] = LacrosseMeet["Place"].str.strip("[")
LacrosseMeet["5.8k"] = LacrosseMeet["5.8k"].str.strip("]")

# Saving new data set to only have Macalester runners
LacrosseMeet = LacrosseMeet[LacrosseMeet.Team == "Macalester"]
rows = LacrosseMeet.shape

# Adding column to designate meet name
meet = ["Jim Drews Invitational (Lacrosse)"]*rows[0]
LacrosseMeet["Meet"] = meet

# Adding column to designate Team Place for each runner
TeamPlace = list(range(1,rows[0]+1))
LacrosseMeet.insert(1, "TeamPlace", TeamPlace)


print(LacrosseMeet)

# =======================================================
def scrapeData(url, start, end):
    session = HTMLSession()
    resp = session.get(url)
    resp.html.render()
    soup = BeautifulSoup(resp.html.html, "lxml")

    rows = soup.findAll('tr')
    table_rows = []
    for row in rows:
        row_td = row.find_all('td')
        str_cells = str(row_td)
        clean = BeautifulSoup(str_cells, "lxml")
        cleanText = clean.get_text(strip=True)
        table_rows.append(cleanText)

    start = start
    end = end
    individual_times = table_rows[start:end]
    return individual_times

# =======================================================

TwinTwlight_list = scrapeData("https://www.tfrrs.org/results/xc/15821/Twin_Cities_Twilight", 152, 361)
#Start: 152, End: 361

# print(TwinTwlight_list)

TwinTwlightMeet = pd.DataFrame(TwinTwlight_list)
TwinTwlightMeet = TwinTwlightMeet[0].str.split(',', expand=True)
TwinTwlightMeet.columns = ["Place", "LastName", "FirstName", "Year", "Team", "AvgMile", "Time", "Score"]
TwinTwlightMeet["Place"] = TwinTwlightMeet["Place"].str.strip("[")
TwinTwlightMeet["Score"] = TwinTwlightMeet["Score"].str.strip("]")

# Saving new data set to only have Macalester runners

TwinTwlightMeet = TwinTwlightMeet[TwinTwlightMeet.Team == "Macalester"]
rows = TwinTwlightMeet.shape

# Adding column to designate meet name
meet = ["Twin Cities Invitational"]*rows[0]
TwinTwlightMeet["Meet"] = meet

# Adding column to designate Team Place for each runner
TeamPlace = list(range(1,rows[0]+1))
TwinTwlightMeet.insert(1, "TeamPlace", TeamPlace)

print(TwinTwlightMeet)

# =======================================================
Blugold_list = scrapeData("https://www.tfrrs.org/results/xc/16404/Blugold_Invitational", 31, 478)
# Start: 31, End: 478

# print(Blugold_list)

BlugoldMeet = pd.DataFrame(Blugold_list)
BlugoldMeet = BlugoldMeet[0].str.split(',', expand=True)
BlugoldMeet.columns = ["Place", "LastName", "FirstName", "Year", "Team", "AvgMile", "Time", "Score", "5k"]
BlugoldMeet["Place"] = BlugoldMeet["Place"].str.strip("[")
BlugoldMeet["5k"] = BlugoldMeet["5k"].str.strip("]")

# Saving new data set to only have Macalester runners

BlugoldMeet = BlugoldMeet[BlugoldMeet.Team == "Macalester"]
rows = BlugoldMeet.shape

# Adding column to designate meet name

race = ["Blugold Invitational"]*rows[0]
BlugoldMeet["Meet"] = race

# Adding column to designate Team Place for each runner
TeamPlace = list(range(1,rows[0]+1))
BlugoldMeet.insert(1, "TeamPlace", TeamPlace)

print(BlugoldMeet)

# =======================================================
Carleton_list = scrapeData("https://www.tfrrs.org/results/xc/16179/Running_of_the_Cows", 18, 244)
# Start: 18, End:244

# print(Carleton_list)

CarletonMeet = pd.DataFrame(Carleton_list)
CarletonMeet = CarletonMeet[0].str.split(',', expand=True)
CarletonMeet.columns = ["Place", "LastName", "FirstName", "Year", "Team", "AvgMile", "Time", "Score", "1k", "2.4k", "4.5k", "7k"]
CarletonMeet["Place"] = CarletonMeet["Place"].str.strip("[")
CarletonMeet["7k"] = CarletonMeet["7k"].str.strip("]")

# Saving new data set to only have Macalester runners
CarletonMeet = CarletonMeet[CarletonMeet.Team == "Macalester"]
rows = CarletonMeet.shape

# Adding column to designate meet name
race = ["Running of the Cows (Carleton)"]*rows[0]
CarletonMeet["Meet"] = race

# Adding column to designate Team Place for each runner
TeamPlace = list(range(1,rows[0]+1))
CarletonMeet.insert(1, "TeamPlace", TeamPlace)

print(CarletonMeet)

# =======================================================
SummitCup_list = scrapeData("https://www.tfrrs.org/results/xc/16025/Summit_Cup", 4, 40)
# Start: 4, End: 40

# print(SummitCup_list)

SummitCupMeet = pd.DataFrame(SummitCup_list)
SummitCupMeet = SummitCupMeet[0].str.split(',', expand=True)
SummitCupMeet.columns = ["Place", "LastName", "FirstName", "Year", "Team", "AvgMile", "Time", "Score"]
SummitCupMeet["Place"] = SummitCupMeet["Place"].str.strip("[")
SummitCupMeet["Score"] = SummitCupMeet["Score"].str.strip("]")

# Saving new data set to only have Macalester runners
SummitCupMeet = SummitCupMeet[SummitCupMeet.Team == "Macalester"]
rows = SummitCupMeet.shape


# Adding column to designate meet name
race = ["Summit Cup"]*rows[0]
SummitCupMeet["Meet"] = race

# Adding column to designate Team Place for each runner
TeamPlace = list(range(1,rows[0]+1))
SummitCupMeet.insert(1, "TeamPlace", TeamPlace)

print(SummitCupMeet)

# =======================================================


# =======================================================

MeetTimes = pd.concat([TwinTwlightMeet, SummitCupMeet, CarletonMeet, BlugoldMeet, LacrosseMeet], sort=False)

MeetTimes.to_csv("Meet.csv")