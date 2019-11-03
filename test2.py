import pandas as pd
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# =======================================================
# First pass to create web scraping script
# =======================================================

session = HTMLSession()
resp = session.get("https://www.tfrrs.org/results/xc/16604/Jim_DrewsTori_Neubauer_Invitational")
resp.html.render()

soup = BeautifulSoup(resp.html.html, "lxml")

# Finding all rows
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

# Extracting only the men's meet
individual_times = table_rows[23:423]
# print(individual_times)

# Creating data frame with appropriate info
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


# print(LacrosseMeet_Mac)

# =======================================================
# Functions to Scrape Data
# =======================================================

def scrapeData(url, start, end, startCol):
    """This function uses Beautiful Soup to extract data from TFFRS website, selecting only the start and end
    of men's resuts. This alos extracts the column names and are added as the headers in the data frame it creates
    after extracting the appropriate data.
    Input: URL; start(int), indicates where the data should start being extracted;
    end(int), indicates where extracting of data should end; column to be extracted for headers
    Output: Returns created data frame from the web scraping results"""
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
    df = df[0].str.split(',', expand=True) # creating multiple columns from list

    # Get column names for df
    columns = soup.findAll('thead')
    columnNames = []
    for col in columns:
        col_tr = col.find_all('tr')
        strCol = str(col_tr)
        cleanC = BeautifulSoup(strCol, "lxml")
        cleanCol = cleanC.get_text()
        columnNames.append(cleanCol)

    # This takes all the rows the above loop finds, extracts the one that is associated with data in question
    # Preserves only every other element since some elements in list are merely white spaces or empty brackets
    # Because when we split the data frame above it split first and last name, we also create those columns to match
    # and then delete the original that came with the data (i.e. "Name")
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

def filterMac(df):
    """This function takes the data frame created in the function above and filters so that it only contains
    Macalester runners. It also creates new column to designate the place a runner got within the team. Does not
    return anything, it merely updates the data frame that is inputted."""
    # Saving new data set to only have Macalester runners
    df = df[df.TEAM == "Macalester"]

    # Adding column to designate Team Place for each runner
    shape = df.shape
    TeamPlace = list(range(1, shape[0] + 1))
    df.insert(1, "TEAMPLACE", TeamPlace)
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

# print(TwinTwlightMeet_Mac)

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

# print(BlugoldMeet_Mac)

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

# print(CarletonMeet_Mac)
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

# print(SummitCupMeet_Mac)

# =======================================================

MIACMeet = scrapeData("https://www.tfrrs.org/results/xc/16678/MIAC_Conference_Championships", 14, 234, 1)
# Start: 14, End: 234, 1

# Adding column to designate meet name
rows = MIACMeet.shape
race = ["MIAC"]*rows[0]
MIACMeet["MEET"] = race

# Adding column to designate year of race
MIACMeet["DATE"] = 2019

# Saving new data set to only have Macalester runners
MIACMeet_Mac = MIACMeet[MIACMeet.TEAM == "Macalester"]

# Adding column to designate Team Place for each runner
shape = MIACMeet_Mac.shape
TeamPlace = list(range(1,shape[0]+1))
MIACMeet_Mac.insert(1, "TEAMPLACE", TeamPlace)


print(MIACMeet_Mac)
# =======================================================
MeetTimes_19 = pd.concat([TwinTwlightMeet_Mac, SummitCupMeet_Mac, CarletonMeet_Mac, BlugoldMeet_Mac, LacrosseMeet_Mac,
                          MIACMeet_Mac],
                      sort=False)

MeetTimes_19.to_csv("MeetTimes_19.csv")


# =======================================================
# Data on 2018
# =======================================================

# Creating Dictionary of meet races and their links to be passed through web scraping function
# This will make the process of scraping more concise and have less code than above

Meets_18 = {"Twin Cities": "https://www.tfrrs.org/results/xc/14208/Twin_Cities_Twilight",
            "St. Olaf": "https://www.tfrrs.org/results/xc/14588/St._Olaf_Invitational",
            "Griak": "https://www.tfrrs.org/results/xc/14671/Roy_Griak_Invitational",
            "MIAC" : "https://www.tfrrs.org/results/xc/14944/MIAC_Championships",
            "Region": "https://www.tfrrs.org/results/xc/14517/NCAA_Division_III_Central_Region_Cross_Country_Championships"}

# Missing Meet: "Oshkosh". This was manually inputted into a csv file.""

# Create empty list, which will hold all the data frames that are created by for loop below
dfList_meets18 = []

# Loops over key in dictionary of meets, sets specific parameters for web scraping function for each meet
# Appends to list to create collection of data frames for this particular year
for key in Meets_18.keys():
    if key == "Twin Cities":
        df = scrapeData(Meets_18[key], 9, 109, 1)
        rows = df.shape
        race = ["Twin Cities Invitational"]*rows[0]
        df["MEET"] = race
        df["DATE"] = 2018
        dfMac = filterMac(df) # Using function that filters Macalester runners here and throughout
        dfList_meets18.append(dfMac)
    elif key == "St. Olaf":
        df = scrapeData(Meets_18[key], 183, 305, 3)
        rows = df.shape
        race = ["St. Olaf Invitational"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2018
        dfMac = filterMac(df)
        dfList_meets18.append(dfMac)
    elif key == "Griak":
        df = scrapeData(Meets_18[key], 813, 1164, 9)
        rows = df.shape
        race = ["Griak"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2018
        dfMac = filterMac(df)
        dfList_meets18.append(dfMac)
    elif key == "MIAC":
        df = scrapeData(Meets_18[key], 13, 213, 1)
        rows = df.shape
        race = ["MIAC"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2018
        dfMac = filterMac(df)
        dfList_meets18.append(dfMac)
    elif key == "Region":
        df = scrapeData(Meets_18[key], 271, 483, 3)
        rows = df.shape
        race = ["Central Region"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2018
        dfMac = filterMac(df)
        dfList_meets18.append(dfMac)

# Saving each data frame in the list in their own objects
df1_18 = pd.DataFrame(dfList_meets18[0])
df2_18 = pd.DataFrame(dfList_meets18[1])
df3_18 = pd.DataFrame(dfList_meets18[2])
df4_18 = pd.DataFrame(dfList_meets18[3])
df5_18 = pd.DataFrame(dfList_meets18[4])
df6_181 = pd.read_csv("OSHKOSH.csv") # This is the data that was manually inputted since it was not available
df6_18 = pd.DataFrame(df6_181) # Missing data read in, then passed through to be created as Data Frame

# Putting all the data frames that represent meets of the year into one larger one, export to csv
MeetTimes_18 = pd.concat([df1_18, df2_18, df3_18, df4_18, df5_18, df6_18], sort=False)
MeetTimes_18.to_csv("MeetTimes_18.csv")

# =======================================================
# Data on 2017 Meets
# =======================================================

# Creating Dictionary of meet races and their links to be passed through web scraping function
Meets_17 = {"Augsburg":"https://www.tfrrs.org/results/xc/12042/Augsburg_Open",
            "River Falls":"https://www.tfrrs.org/results/xc/11951/Falcon_Invitational",
            "St. Olaf":"https://www.tfrrs.org/results/xc/12550/St._Olaf_Invitational",
            "Summit Cup":"https://www.tfrrs.org/results/xc/12804/Summit_Cup",
            "Carleton":"https://www.tfrrs.org/results/xc/12950/Carleton_Running_of_the_Cows",
            "Lacrosse": "https://www.tfrrs.org/results/xc/13226/UW_La_Crosse_Jim_DrewsTori_Neubauer_Invitational",
            "Region": "https://www.tfrrs.org/results/xc/13031/NCAA_Division_III_Central_Region_Cross_Country_Championships"}

# Missing: "MIAC":"http://www.fastfinishtiming.com/2017RoadandCC/17Results/MIACMen.html"
# Will need to do separate web scraping commands since it is in a different website

# Create empty list, which will hold all the data frames that are created by for loop below
dfList_meets17 = []

# Loops over key in dictionary of meets, sets specific parameters for web scraping function for each meet
# Appends to list to create collection of data frames for this particular year
for key in Meets_17.keys():
    if key == "Augsburg":
        df = scrapeData(Meets_17[key], 7, 61, 1)
        rows = df.shape
        race = ["Augsburg Open"]*rows[0]
        df["MEET"] = race
        df["DATE"] = 2017
        dfMac = filterMac(df) # Using function that filters Macalester runners here and throughout
        dfList_meets17.append(dfMac)
    elif key == "River Falls":
        df = scrapeData(Meets_17[key], 10, 86, 1)
        rows = df.shape
        race = ["Falcon Invite"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2017
        dfMac = filterMac(df)
        dfList_meets17.append(dfMac)
    elif key == "St. Olaf":
        df = scrapeData(Meets_17[key], 366, 644, 3)
        rows = df.shape
        race = ["St. Olaf Invitational"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2017
        dfMac = filterMac(df)
        dfList_meets17.append(dfMac)
    elif key == "Summit Cup":
        df = scrapeData(Meets_17[key], 4, 33, 1)
        rows = df.shape
        race = ["Summit Cup"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2017
        dfMac = filterMac(df)
        dfList_meets17.append(dfMac)
    elif key == "Region":
        df = scrapeData(Meets_17[key], 281, 483, 3)
        rows = df.shape
        race = ["Central Region"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2017
        dfMac = filterMac(df)
        dfList_meets17.append(dfMac)
    elif key == "Carleton":
        df = scrapeData(Meets_17[key], 14, 193, 1)
        rows = df.shape
        race = ["Running of the Cows (Carleton)"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2017
        dfMac = filterMac(df)
        dfList_meets17.append(dfMac)
    elif key == "Lacrosse":
        df = scrapeData(Meets_17[key], 23, 380, 1)
        rows = df.shape
        race = ["Jim Drews Invitational (Lacrosse)"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2017
        dfMac = filterMac(df)
        dfList_meets17.append(dfMac)

'''
################################
#####Getting Missing Meet#######
################################

# As mentioned above, there was data on one meet that could only be found on another website different than the one
# in which the function was created to scrape from. As such, the code below shows how to web scrape this particular
# page. It is saved to a csv file so that these commands only need to be executed once, then they are commented out.
# Note that this can only be run by itself, everything else has to be commented out for it to work. This is because
# it is pulling from a different website than the rest, so the connection gets lost if everything else is included.

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

splitName = MIAC17["NAME"].str.split(" ", n = 1, expand = True)
MIAC17["FIRSTNAME"] = splitName[0]
MIAC17["LASTNAME"] = splitName[1]
MIAC17.drop(columns =["NAME", "X1", "X2", "X3"], inplace = True)

MIAC17.to_csv("MIAC17.csv")
'''

# Saving each data frame in the list in their own objects
df1_17 = pd.DataFrame(dfList_meets17[0])
df2_17 = pd.DataFrame(dfList_meets17[1])
df3_17 = pd.DataFrame(dfList_meets17[2])
df4_17 = pd.DataFrame(dfList_meets17[3])
df5_17 = pd.DataFrame(dfList_meets17[4])
df6_17 = pd.DataFrame(dfList_meets17[5])
df7_17 = pd.DataFrame(dfList_meets17[6])
df8_171 = pd.read_csv("MIAC17.csv") # Reading in data web scraped from different source
df8_17 = pd.DataFrame(df8_171) # Converting data from different source into data frame

# Putting all the data frames that represent meets of the year into one larger one, export to csv
MeetTimes_17 = pd.concat([df1_17, df2_17, df3_17, df4_17, df5_17, df6_17, df7_17, df8_17], sort=False)
MeetTimes_17.to_csv("MeetTimes_17.csv")

# =======================================================
# Data on 2016 Meets
# =======================================================

# Creating Dictionary of meet races and their links to be passed through web scraping function
Meets_16 = {"River Falls": "https://www.tfrrs.org/results/xc/9999/Falcon_Invitational",
           "Summit Cup": "https://www.tfrrs.org/results/xc/10620/Summit_Cup",
            "Griak": "https://www.tfrrs.org/results/xc/10762/ROY_GRIAK_INVITATIONAL",
            "Blugold": "https://www.tfrrs.org/results/xc/10836/Blugold_Invitational",
            "Lacrosse": "https://www.tfrrs.org/results/xc/11045/Jim_DrewsTori_Neubauer_Invitational",
            "MIAC":"https://www.tfrrs.org/results/xc/11198/MIAC_Championships",
            "Region":"https://www.tfrrs.org/results/xc/11018/NCAA_Division_III_Central_Region_Cross_Country_Championships"}

# Missing Meet: "Augsburg":"http://wayzatatiming.com/crosscountry/2016/AugsburgAlumni/"
# Will need to do separate commands to web scrape differemt website in which data is found

# Create empty list, which will hold all the data frames that are created by for loop below
dfList_meets16 = []

# Loops over key in dictionary of meets, sets specific parameters for web scraping function for each meet
# Appends to list to create collection of data frames for this particular year
for key in Meets_16.keys():
    if key == "River Falls":
        df = scrapeData(Meets_16[key], 12, 117, 1)
        rows = df.shape
        race = ["River Falls"]*rows[0]
        df["MEET"] = race
        df["DATE"] = 2016
        dfMac = filterMac(df) # Using function to filter Macalester runners
        dfList_meets16.append(dfMac)
    elif key == "Griak":
        df = scrapeData(Meets_16[key], 1538, 1628, 9)
        rows = df.shape
        race = ["Griak"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2016
        dfMac = filterMac(df)
        dfList_meets16.append(dfMac)
    elif key == "Blugold":
        df = scrapeData(Meets_16[key], 250, 536, 3)
        rows = df.shape
        race = ["Blugold Invitational"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2016
        dfMac = filterMac(df)
        dfList_meets16.append(dfMac)
    elif key == "Summit Cup":
        df = scrapeData(Meets_16[key], 4, 49, 1)
        rows = df.shape
        race = ["Summit Cup"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2016
        dfMac = filterMac(df)
        dfList_meets16.append(dfMac)
    elif key == "Region":
        df = scrapeData(Meets_16[key], 285, 493, 3)
        rows = df.shape
        race = ["Central Region"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2016
        dfMac = filterMac(df)
        dfList_meets16.append(dfMac)
    elif key == "MIAC":
        df = scrapeData(Meets_16[key], 275, 484, 3)
        rows = df.shape
        race = ["MIAC"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2016
        dfMac = filterMac(df)
        dfList_meets16.append(dfMac)
    elif key == "Lacrosse":
        df = scrapeData(Meets_16[key], 22, 391, 1)
        rows = df.shape
        race = ["Jim Drews Invitational (Lacrosse)"] * rows[0]
        df["MEET"] = race
        df["DATE"] = 2016
        dfMac = filterMac(df)
        dfList_meets16.append(dfMac)


'''
################################
#####Getting Missing Meet#######
################################

# As mentioned above, there was data on one meet that could only be found on another website different than the one
# in which the function was created to scrape from. As such, the code below shows how to web scrape this particular
# page. It is saved to a csv file so that these commands only need to be executed once, then they are commented out.
# Note that this can only be run by itself, everything else has to be commented out for it to work. This is because
# it is pulling from a different website than the rest, so the connection gets lost if everything else is included.

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

Augsburg16.to_csv("Augsburg16.csv")
'''

# Saving each data frame in the list in their own objects
df1_16 = pd.DataFrame(dfList_meets16[0])
df2_16 = pd.DataFrame(dfList_meets16[1])
df3_16 = pd.DataFrame(dfList_meets16[2])
df4_16 = pd.DataFrame(dfList_meets16[3])
df5_16 = pd.DataFrame(dfList_meets16[4])
df6_16 = pd.DataFrame(dfList_meets16[5])
df7_16 = pd.DataFrame(dfList_meets16[6])
df8_161 = pd.read_csv("Augsburg16.csv") # Reading in data web scraped from different source
df8_16 = pd.DataFrame(df8_161) # Converting data from different source into data frame

# Putting all the data frames that represent meets of the year into one larger one, export to csv
MeetTimes_16 = pd.concat([df1_16, df2_16, df3_16, df4_16, df5_16, df6_16, df7_16, df8_16], sort=False)
MeetTimes_16.to_csv("MeetTimes_16.csv")

# =======================================================
# Putting them all together
# =======================================================

# Compiling the four csv files created above into a full one to have all data from four years in one, saved to csv
MeetALL = pd.concat([MeetTimes_16, MeetTimes_17, MeetTimes_18, MeetTimes_19], sort= False)
MeetALL.to_csv("MeetALL.csv")

