import pandas as pd
import re
import numpy as np
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# =======================================================
# First pass to create web scraping script
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
LacrosseMeet.columns = ["PL", "LASTNAME", "FIRSTNAME", "YEAR", "TEAM", "Avg. Mile", "TIME", "SCORE", "3K", "5.8K"]
LacrosseMeet["PL"] = LacrosseMeet["PL"].str.strip("[")
LacrosseMeet["5.8K"] = LacrosseMeet["5.8K"].str.strip("]")

# Adding column to designate meet name
rows = LacrosseMeet.shape
meet = ["Jim Drews Invitational (Lacrosse)"]*rows[0]
LacrosseMeet["MEET"] = meet

# Adding column to designate year of race
LacrosseMeet["DATE"] = 2019

# Saving new data set to only have Macalester runners
LacrosseMeet_Mac = LacrosseMeet[LacrosseMeet.TEAM == "Macalester"]

# Adding column to designate Team Place for each runner
shape = LacrosseMeet_Mac.shape
TeamPlace = list(range(1,shape[0]+1))
LacrosseMeet_Mac.insert(1, "TEAMPLACE", TeamPlace)


print(LacrosseMeet_Mac)

# =======================================================
# Function to Scrape Data
# =======================================================

def scrapeData(url, start, end, startCol):
    session = HTMLSession()
    resp = session.get(url)
    resp.html.render()
    soup = BeautifulSoup(resp.html.html, "lxml")

    # Get rows of data for all runners
    rows = soup.findAll('tr')
    table_rows = []
    for row in rows:
        row_td = row.find_all('td')
        str_cells = str(row_td)
        clean = BeautifulSoup(str_cells, "lxml")
        cleanText = clean.get_text(strip=True)
        table_rows.append(cleanText)

    # Extract men's race only
    start = start
    end = end
    individual_times = table_rows[start:end]

    # Create data frame
    df = pd.DataFrame(individual_times)
    df = df[0].str.split(',', expand=True)

    # Get column names for df
    columns = soup.findAll('thead')
    columnNames = []
    for col in columns:
        col_tr = col.find_all('tr')
        strCol = str(col_tr)
        cleanC = BeautifulSoup(strCol, "lxml")
        cleanCol = cleanC.get_text()
        columnNames.append(cleanCol)

    Columns = columnNames[startCol:startCol + 1]
    Columns1 = [x.split("\n") for x in Columns]
    Columns2 = Columns1[0][1::2]
    del Columns2[-1]
    Columns2[1] = "LASTNAME"
    Columns2.insert(2, "FIRSTNAME")

    # Change column names of df
    df.columns = Columns2

    # Remove extra brackets at either end
    df[df.columns[0]]= df[df.columns[0]].str.strip("[")
    df[df.columns[-1]] = df[df.columns[-1]].str.strip("]")

    return df

# =======================================================

# =======================================================
# Data on 2019 Meets (including the one above)
# =======================================================

TwinTwlightMeet = scrapeData("https://www.tfrrs.org/results/xc/15821/Twin_Cities_Twilight", 152, 361, 3)
#Start: 152, End: 361, 3

# Adding column to designate meet name
rows = TwinTwlightMeet.shape
meet = ["Twin Cities Invitational"]*rows[0]
TwinTwlightMeet["MEET"] = meet

# Adding column to designate year of race
TwinTwlightMeet["DATE"] = 2019

# Saving new data set to only have Macalester runners
TwinTwlightMeet_Mac = TwinTwlightMeet[TwinTwlightMeet.TEAM == "Macalester"]

# Adding column to designate Team Place for each runner
shape = TwinTwlightMeet_Mac.shape
TeamPlace = list(range(1,shape[0]+1))
TwinTwlightMeet_Mac.insert(1, "TEAMPLACE", TeamPlace)

print(TwinTwlightMeet_Mac)

# =======================================================
BlugoldMeet = scrapeData("https://www.tfrrs.org/results/xc/16404/Blugold_Invitational", 31, 478, 1)
# Start: 31, End: 478, 1

# Adding column to designate meet name
rows = BlugoldMeet.shape
meet = ["Blugold Invitational"]*rows[0]
BlugoldMeet["MEET"] = meet

# Adding column to designate year of race
BlugoldMeet["DATE"] = 2019

# Saving new data set to only have Macalester runners
BlugoldMeet_Mac = BlugoldMeet[BlugoldMeet.TEAM == "Macalester"]

# Adding column to designate Team Place for each runner
shape = BlugoldMeet_Mac.shape
TeamPlace = list(range(1,shape[0]+1))
BlugoldMeet_Mac.insert(1, "TEAMPLACE", TeamPlace)

print(BlugoldMeet_Mac)

# =======================================================
CarletonMeet = scrapeData("https://www.tfrrs.org/results/xc/16179/Running_of_the_Cows", 18, 244, 1)
# Start: 18, End:244, 1

# Adding column to designate meet name
rows = CarletonMeet.shape
meet = ["Running of the Cows (Carleton)"]*rows[0]
CarletonMeet["MEET"] = meet

# Adding column to designate year of race
CarletonMeet["DATE"] = 2019

# Saving new data set to only have Macalester runners
CarletonMeet_Mac = CarletonMeet[CarletonMeet.TEAM == "Macalester"]

# Adding column to designate Team Place for each runner
shape = CarletonMeet_Mac.shape
TeamPlace = list(range(1,shape[0]+1))
CarletonMeet_Mac.insert(1, "TEAMPLACE", TeamPlace)

print(CarletonMeet_Mac)
# =======================================================
SummitCupMeet = scrapeData("https://www.tfrrs.org/results/xc/16025/Summit_Cup", 4, 40, 1)
# Start: 4, End: 40, 1

# Adding column to designate meet name
rows = SummitCupMeet.shape
race = ["Summit Cup"]*rows[0]
SummitCupMeet["MEET"] = race

# Adding column to designate year of race
SummitCupMeet["DATE"] = 2019

# Saving new data set to only have Macalester runners
SummitCupMeet_Mac = SummitCupMeet[SummitCupMeet.TEAM == "Macalester"]

# Adding column to designate Team Place for each runner
shape = SummitCupMeet_Mac.shape
TeamPlace = list(range(1,shape[0]+1))
SummitCupMeet_Mac.insert(1, "TEAMPLACE", TeamPlace)

print(SummitCupMeet_Mac)

# =======================================================
# Data on 2018, 2017, 2016 Meets
# =======================================================

Meets_18 = {"Twin Cities": "https://www.tfrrs.org/results/xc/14208/Twin_Cities_Twilight",
            "St. Olaf": "https://www.tfrrs.org/results/xc/14588/St._Olaf_Invitational",
            "Griak": "https://www.tfrrs.org/results/xc/14671/Roy_Griak_Invitational",
            "Oshkosh":"",
            "MIAC" : "https://www.tfrrs.org/results/xc/14944/MIAC_Championships",
            "Region": "https://www.tfrrs.org/results/xc/14517/NCAA_Division_III_Central_Region_Cross_Country_Championships"}

Meets_17 = {"Augsburg":"https://www.tfrrs.org/results/xc/12042/Augsburg_Open",
            "River Falls":"https://www.tfrrs.org/results/xc/11951/Falcon_Invitational",
            "St. Olaf":"https://www.tfrrs.org/results/xc/12550/St._Olaf_Invitational",
            "Summit Cup":"https://www.tfrrs.org/results/xc/12804/Summit_Cup",
            "Carleton":"https://www.tfrrs.org/results/xc/12950/Carleton_Running_of_the_Cows",
            "Lacrosse": "https://www.tfrrs.org/results/xc/13226/UW_La_Crosse_Jim_DrewsTori_Neubauer_Invitational",
            "MIAC":"http://www.fastfinishtiming.com/2017RoadandCC/17Results/MIACMen.html",
            "Region": "https://www.tfrrs.org/results/xc/13031/NCAA_Division_III_Central_Region_Cross_Country_Championships"}

Meets_16 = {"Augsburg":"http://wayzatatiming.com/crosscountry/2016/AugsburgAlumni/",
            "River Falls": "https://www.tfrrs.org/results/xc/9999/Falcon_Invitational",
           "Summit Cup": "https://www.tfrrs.org/results/xc/10620/Summit_Cup",
            "Griak": "https://www.tfrrs.org/results/xc/10762/ROY_GRIAK_INVITATIONAL",
            "Blugold": "https://www.tfrrs.org/results/xc/10836/Blugold_Invitational",
            "Lacrosse": "https://www.tfrrs.org/results/xc/11045/Jim_DrewsTori_Neubauer_Invitational",
            "MIAC":"https://www.tfrrs.org/results/xc/11198/MIAC_Championships",
            "Region":"https://www.tfrrs.org/results/xc/11018/NCAA_Division_III_Central_Region_Cross_Country_Championships"}
# =======================================================
# Putting them all together
# =======================================================
MeetTimes = pd.concat([TwinTwlightMeet_Mac, SummitCupMeet_Mac, CarletonMeet_Mac, BlugoldMeet_Mac, LacrosseMeet_Mac],
                      sort=False)

MeetTimes.to_csv("Meet.csv")