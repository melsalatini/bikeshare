import time
from matplotlib.style import available
import pandas as pd
import numpy as np

Debugging = True
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
Available_Months = ['january', 'february', 'march', 'april', 'may', 'june']
weekDays = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ""
    month = ""
    day = ""

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cityInput = input(
            '\nplease choose one of the following cities: chicago, new york city or Washington: .\n')
        if cityInput.lower() in CITY_DATA:
            city = cityInput.lower()
            break
        else:
            print("your entry is invalid. please try again")

     # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        monthInput = input('\nplease choose a filter for month: ' +
                           ', '.join([x.title() for x in Available_Months]) + ' or enter all to set no month filter:.\n')
        if monthInput.lower() in Available_Months or monthInput.lower() == 'all':
            month = monthInput.lower()
            break
        else:
            print("your entry is invalid. please try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        dayInput = input('\nplease choose a filter for day: ' +
                         ', '.join([x.title() for x in weekDays]) + ' or enter all to set no days filter:.\n')
        if dayInput.lower() in weekDays or dayInput.lower() == 'all':
            day = dayInput.lower()
            break
        else:
            print("your entry is invalid. please try again")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print(
        f"preparing dafaframe with your filters: City: '{city}' Month: '{month}' and day: '{day}' ")
    df = pd.read_csv(CITY_DATA[city])

    df['startTime'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['startTime'].dt.day_name()
    df['Month'] = df['startTime'].dt.month_name()

    if (month != 'all'):
        df = df[df['Month'] == month.title()]

    if(day != 'all'):
        df = df[df['day'] == day.title()]

    print(df.info())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(f" most frequent Month is: '{df['Month'].mode()[0]}'")
    # TO DO: display the most common day of week
    print(f" most common day of week is: '{df['day'].mode()[0]}'")
    # TO DO: display the most common start hour
    print(f" common start hour is: '{df['startTime'].dt.hour.mode()[0]}'")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(
        f" most commonly used start station is: '{df['Start Station'].mode()[0]}'")
    # TO DO: display most commonly used end station
    print(
        f" most commonly used end station is: '{df['End Station'].mode()[0]}'")
    # TO DO: display most frequent combination of start station and end station trip
    start_and_endStation = df.groupby(
        ['Start Station', 'End Station']).size().to_frame('size').sort_values("size", ascending=False).reset_index()

    print(
        f" most driven used bikes are from start station: '{start_and_endStation.iloc[0]['Start Station']}' and to end station: '{start_and_endStation.iloc[0]['End Station']}'")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    totalDuration = (df['Trip Duration'].sum() / 60) / 60
    # TO DO: display total travel time
    print(f"total travel time: {totalDuration} hours")
    # TO DO: display mean travel time

    meanDuration = (df['Trip Duration'].mean() / 60) / 60

    print(f"mean travel time: {meanDuration} hours")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print("user types are: ")
    print(df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if(city != "washington"):
        print("\n user genders are: ")
        print(df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    if (city == "new york city"):
        print(f"most common year of birth: {df['Birth Year'].mode()[0]}")

        earliestBY = df['Birth Year'].sort_values(
            ascending=True)
        print(f"\n earliest year of birth: {earliestBY.iloc[0]}")

        recentBY = df['Birth Year'].sort_values(
            ascending=False)
        print(f"\n most recent year of birth: {recentBY.iloc[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def showData(df):
    showRows = False
    RowCounter = 0
    userInput = input(
        "\n would you like to see first 5 rows of selected data? (yes/no)")
    if(userInput.lower() == "yes"):
        print(df.shape)
        rowCountToShow = 5
        print(df.iloc[RowCounter:rowCountToShow])
        RowCounter = RowCounter + rowCountToShow
        showRows = True

    while showRows:
        if df.iloc[RowCounter:RowCounter + rowCountToShow].empty:
           break
        userInput = input("\n would you like to see more 5 rows? (yes/no)")
        if(userInput.lower() == "no"):
            break

        print(df.iloc[RowCounter:RowCounter + rowCountToShow])
        RowCounter = RowCounter + rowCountToShow


def main():
    while True:
        if Debugging != True:
            city, month, day = get_filters()
        else:
            city = 'new york city'
            month = "may"
            day = "saturday"

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        showData(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
