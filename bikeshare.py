import time
import pandas as pd
import numpy as np

from colorama import init
import calendar

# Initialization
# initialize colorama to enable windows terminal compatability for colors. 
init()


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

DIVDER_WIDTH = 80

def color_message(color_class, message):
    """
    Attache color ANSI codes into messages based on color_class

    Receives:
        (str) color_class -- requested color class (as defined in color_pallet dic)
        (str) message -- message before adding color ANSI codes

    Returns: 
        (str) message -- message after adding color ANSI codes.
    """
    colors = {
        'PROMPT':       '\033[94m',    # BLUE
        'RESULT':       '\033[92m',    # GREEN
        'BOLDRESULT':   '\033[92;0m',  # GREEN;BOLD
        'WARNING':      '\033[93m',    # YELLOW
        'FAIL':         '\033[91;4m',  # RED;UNDERLINE
        'RESET':        '\033[0m',     # TERMINAL DEFAULT
    }

    try:
        return colors[color_class.upper()] + message + colors['RESET']
    except:
        return message
    
def get_input(choices, message, color_class = 'prompt'):
    """
    Inquiry user input with validation

    Receives:
        (list) choices -- multiple choices user can select from.
        (str) message -- message to be sent to user.
        (str) color_class -- color to be used for output message (default is 'prompt').

    Returns: 
        (str) choice -- user's input (has to be in choices)
    """
    while True:
        choice = input(color_message(color_class, message)).lower()
        if choice in choices:
            # correct input, break loop & continue
            return choice
        else:
            # incorrect input, prompt & loop
            print(color_message('warning', 'Warning: invalid entry'))
            print()

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    message = ('Would you like to see data for Chicago, New York, or Washington? ')
    city = get_input(CITY_DATA.keys(), message)
    
    # get user input on filter choice.
    message = ('Would you like to filter the data by "month", "day", "both" or "none"? ')
    filter_choice_options = ['month', 'day', 'both', 'none']
    filter_choice = get_input(filter_choice_options, message)

    # get user input for month (all, january, february, ... , june)
    month_message = ('Which month? January, February, March, April, May, or June? ')
    month_choices =['january', 'february', 'march', 'april', 'may', 'june']
    month = get_input(month_choices, month_message) if (filter_choice == "month") else 'all'

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_message = ('Which day? Please type your response as an integer (e.g., 1=Sunday)? ')
    day_choices = [str(x) for x in range(1,8)]
    day = get_input(day_choices, day_message) if (filter_choice == "day") else 'all'

    # get user input for both month & day in case of both.
    if filter_choice == 'both':
        month = get_input(month_choices, month_message)
        day = get_input(day_choices, day_message)

    # convert day to string
    # note: day-2 due to start of week@ Sunday + list starts at 0 'not 1'
    day = calendar.day_name[int(day) - 2] if day != 'all' else day
    
    message = ('-'*DIVDER_WIDTH + '\n' 
        + 'Data is filtered to city: {}, month: {}, day: {}\n'.format(
            city.title(), 
            month.title(), 
            day.title())
        + '-'*DIVDER_WIDTH
        )

    print(color_message('result', message))

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
    print(color_message('warning','\nLoading data with selected filters...'), end ='')

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df.month == month]
        print(color_message('warning','...'), end = '')

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week == day.title()]
        print(color_message('warning','...'), end = '')

    print(color_message('result','[DONE]\n'))

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print(color_message('warning','Calculating The Most Frequent Times of Travel...'))
    start_time = time.time()

    # TO DO: display the most common month
    # FIXME: What if month is set to a specific value?


    # TO DO: display the most common day of week
    # FIXME: What if day is set to a specific value?


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = str(df['hour'].mode()[0])
    print(color_message('result','Most Popular Start Hour: '), color_message('boldresult',popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        #restart = input('\nWould you like to restart? Enter yes or no.\n')
        #if restart.lower() != 'yes':
        #    break


if __name__ == "__main__":
	main()
    ## get_filters()
    ## df = load_data('new york', 'march', 'monday')
    # city, month, day = get_filters()
    # df = load_data(city, month, day)