
import pandas as pd

def getweeklyaverage(country):

    df1 = pd.read_csv(country + ' Cases.csv')
    df2 = pd.read_csv(country + ' Mobility.csv')

    date1 = df1.Date_reported
    date2 = df2.date

    df1.drop(df1.index[0:43], axis=0, inplace=True)
    df1.drop(df1.index[-6:], axis=0, inplace=True)
    df1 = df1.reset_index()
    df1.drop('index', axis=1, inplace=True)
    df1.drop('Cumulative_cases', axis=1, inplace=True)
    df1.drop('New_deaths', axis=1, inplace=True)
    df1.drop('Cumulative_deaths', axis=1, inplace=True)


    df2.drop('census_fips_code', axis=1, inplace=True)
    df2.drop('retail_and_recreation_percent_change_from_baseline', axis=1, inplace=True)
    df2.drop('grocery_and_pharmacy_percent_change_from_baseline', axis=1, inplace=True)
    df2.drop('parks_percent_change_from_baseline', axis=1, inplace=True)
    df2.drop('workplaces_percent_change_from_baseline', axis=1, inplace=True)
    df2.drop('residential_percent_change_from_baseline', axis=1, inplace=True)


    print(df1)
    print(df2)
    count = 0
    eplist = []
    datime = []
    necases = 0
    for index, row in df1.iterrows():
        necases = necases + row['New_cases']
        count += 1
        if count == 7:
            datime.append(row['Date_reported'])
            eplist.append(necases / 7)
            count = 0
            necases = 0

    mcount = 0
    meplist = []
    mdatime = []
    mnecases = 0
    for index, row in df2.iterrows():
        mnecases = mnecases + row['transit_stations_percent_change_from_baseline']
        mcount += 1
        if mcount == 7:
            mdatime.append(row['date'])
            meplist.append(mnecases / 7)
            mcount = 0
            mnecases = 0

    print (eplist)
    print (datime)

    df10 = pd.DataFrame({'date_time': datime, 'average_cases_7': eplist})
    df20 = pd.DataFrame({'date_time_for_mobility': mdatime, 'average_mobility_7': meplist})
    print(df10)
    print(df20)

    df20.to_csv(country + '_Weekly_average_data_Mobility.csv')
    df10.to_csv(country + '_Weekly_average_data_Cases.csv')

getweeklyaverage('Denmark')
getweeklyaverage('Colombia')
getweeklyaverage('Canada')
getweeklyaverage('Poland')
getweeklyaverage('Romania')