import pandas as pd
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def missing_meets():
    """This function is used to extract information on the two meets that were missing from the
    TFRRS website, explained above and below. This function call is placed in the main_script.py file
    to be run with the other function calls to get data on all meets."""

    #####################################
    #####Getting Missing Meet in 2017####
    #####################################
    session = HTMLSession()
    resp2 = session.get("http://www.fastfinishtiming.com/2017RoadandCC/17Results/MIACMen.html")
    resp2.html.render()


    soup2 = BeautifulSoup(resp2.html.html, "lxml")

    table_rows2 = []

    rows2 = soup2.findAll('tr')
    for row in rows2:
        row_td2 = row.find_all('td')
        str_cells2 = str(row_td2)
        clean2 = BeautifulSoup(str_cells2, "lxml")
        cleanText2 = clean2.get_text(strip=True)
        table_rows2.append(cleanText2)

    individual_times2 = table_rows2[31:236]

    MIAC17 = pd.DataFrame(individual_times2)

    MIAC17 = MIAC17[0].str.split(',', expand=True)

    MIAC17.columns = ["PL", "X1", "X2", "NAME", "TEAM", "TIME", "PACE", "YEAR", "X3"]
    MIAC17["PL"] = MIAC17["PL"].str.strip("[")

    # Adding column to designate meet name
    rows = MIAC17.shape
    meet = ["MIAC"]*rows[0]
    MIAC17["MEET"] = meet

    # Adding column to designate year of race
    MIAC17["DATE"] = 2017

    # Filtering out Macalester runners
    MIAC17 = MIAC17[MIAC17.TEAM == "Macalester"]

    # Adding column to designate Team Place for each runner
    shape = MIAC17.shape
    TeamPlace = list(range(1, shape[0] + 1))
    MIAC17.insert(1, "TEAMPLACE", TeamPlace)

    # Adding column to designate Avg. mile for each runner
    MIAC17["Avg. Mile"] = ["5:21.3", "5:22.5", "5:27.6", "5:29.4", "5:32.1",
                             "5:35.5", "5:37.6", "5:39.4", "5:46.1", "5:47.5",
                             "5:47.7", "5:50.8", "5:57.9", "6:01.8", "6:03.9",
                             "6:07.7", "6:21.2", "6:34.2", "6:35.9"]

    splitName = MIAC17["NAME"].str.split(" ", n = 1, expand = True)
    MIAC17["FIRSTNAME"] = splitName[0]
    MIAC17["LASTNAME"] = splitName[1]
    MIAC17.drop(columns =["NAME", "X1", "X2", "X3"], inplace = True)

    print(MIAC17)

    MIAC17.to_csv("data/MIAC17.csv")

    ######################################
    #####Getting Missing Meet for 2016####
    ######################################
    session = HTMLSession()
    resp3 = session.get("http://wayzatatiming.com/crosscountry/2016/AugsburgAlumni/")
    resp3.html.render()


    soup3 = BeautifulSoup(resp3.html.html, "lxml")

    table_rows3 = []

    rows3 = soup3.findAll('tr')
    for row in rows3:
        row_td3 = row.find_all('td')
        str_cells3 = str(row_td3)
        clean3 = BeautifulSoup(str_cells3, "lxml")
        cleanText3 = clean3.get_text(strip=True)
        table_rows3.append(cleanText3)

    individual_times3 = table_rows3[8:88]

    Augsburg16 = pd.DataFrame(individual_times3)

    Augsburg16 = Augsburg16[0].str.split(',', expand=True)
    Augsburg16.columns = ["PL", "NAME", "YEAR", "TEAM", "SCORE", "TIME", "GAP", "Avg. Mile", "Avg. K"]
    Augsburg16["PL"] = Augsburg16["PL"].str.strip("[")
    Augsburg16["Avg. K"] = Augsburg16["Avg. K"].str.strip("]")

    # Adding column to designate meet name
    rows = Augsburg16.shape
    meet = ["Augsburg Open"]*rows[0]
    Augsburg16["MEET"] = meet

    # Adding column to designate year of race
    Augsburg16["DATE"] = 2016

    # Filtering out Macalester runners
    Augsburg16 = Augsburg16[Augsburg16.TEAM == "Macalester College"]

    # Adding column to designate Team Place for each runner
    shape = Augsburg16.shape
    TeamPlace = list(range(1, shape[0] + 1))
    Augsburg16.insert(1, "TEAMPLACE", TeamPlace)

    splitName = Augsburg16["NAME"].str.split(" ", n = 1, expand = True)
    Augsburg16["FIRSTNAME"] = splitName[0]
    Augsburg16["LASTNAME"] = splitName[1]
    Augsburg16.drop(columns =["NAME"], inplace = True)

    print(Augsburg16)

    Augsburg16.to_csv("data/Augsburg16.csv")
