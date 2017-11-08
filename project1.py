import csv, datetime

f = open('full_data.csv', 'r')

data = list(csv.reader(f))
f.close()
# Extracting headers to a variable
headers = data[0]

# Removing the header row from data
data = data[1:]

# Saving each year in a list
years = [item[1] for item in data]
sex_data = [item[5] for item in data]
race_data = [item[7] for item in data]
intents = [item[3] for item in data]

#setting the dates
dates = [datetime.datetime(year=int(item[1]), month=int(item[2]), day=1) for item in data]

# counting the deaths by year, sex, race, and counting homicide by race
year_counts = {}
sex_counts = {}
race_counts = {}
homicide_race_counts = {}

# years first
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1

# sex count
for sex in sex_data:
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1

# counting the race data and homicide by race
for i, race in enumerate(race_data):
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
    if intents[i] == 'Homicide':
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1

# 'census.csv' is a data file which contains total number of people by race
f = open('census.csv', 'r')
census = list(csv.reader(f))
f.close()


race_per_hundredk = {}
for race in race_counts:
    if race == 'Asian/Pacific Islander':
        race_per_hundredk[race] = race_counts[race] / (int(census[1][14]) + int(census[1][15])) * 10000
        homicide_race_counts[race] = homicide_race_counts[race] / (int(census[1][14]) + int(census[1][15])) * 10000
    elif race == 'Black':
        race_per_hundredk[race] = race_counts[race] / int(census[1][12]) * 100000
        homicide_race_counts[race] = homicide_race_counts[race] / int(census[1][12]) * 100000
    elif race == 'Native American/Native Alaskan':
        race_per_hundredk[race] = race_counts[race] / int(census[1][13]) * 100000
        homicide_race_counts[race] = homicide_race_counts[race] / int(census[1][13]) * 100000
    elif race == 'Hispanic':
        race_per_hundredk[race] = race_counts[race] / int(census[1][11]) * 100000
        homicide_race_counts[race] = homicide_race_counts[race] / int(census[1][11]) * 100000
    elif race == 'White':
        race_per_hundredk[race] = race_counts[race] / int(census[1][10]) * 100000
        homicide_race_counts[race] = homicide_race_counts[race] / int(census[1][10]) * 100000


print(homicide_race_counts)
print(race_per_hundredk)