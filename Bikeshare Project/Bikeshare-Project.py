## TODO: import all necessary packages and functions

import csv
from datetime import datetime
import time

# Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

month_list=['january','jan','february','feb','march','mar','april','apr','may','june','jun']
day_list=['monday','mon','tuesday','tue','wednesday','wed','thursday','thurs','friday','fri','saturday','sat','sunday','sun']

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    # TODO: handle raw input and complete function
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 '\nWould you like to see data for Chicago, New York, or Washington?\n')
        if city.lower() not in ('chicago','ny','new york','washington'):
            print("Please enter a valid choice from the list")
        else:
            break

    if city.lower() in ('chicago','chi'):
        return chicago
    elif city.lower() in ('new york','ny'):
        return new_york_city
    elif city.lower() in ('washington','wash'):
        return washington

    else:
        get_city()

def load_city_data(city_file,time_period):
    '''Take the input from get_city function and return the corresponding csv file for R/W .

    Args: city name
        City file and time_period filter
    Returns:
        Return the corresponding CSV/filtered CSV file based on time filter
    '''
    #months = ['January', 'February', 'March', 'April','May','June']
    #week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    city_data=[]

    if time_period=='none':
        print("\nOne moment please! Reading from requested city file.......")
        with open(city_file) as csvfile:
            city_data = [{k:v for k, v in row.items() if v is not None} for row in csv.DictReader(csvfile,skipinitialspace=True)]
            return city_data

    # this condiion loads data for "month" filter
    elif time_period in month_list:
       print("\nOne moment please! Reading from requested city file.......")
       with open(city_file) as csvfile:

          for row in csv.DictReader(csvfile,skipinitialspace=True):
           # print(row)
            date_temp = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
            mon=date_temp.strftime('%B'.lower())

            if mon.lower()==time_period:
              city_data.append({k:v for k, v in row.items()})

       return city_data

    # this condition loads dta for the 'day' filter
    else:
       print("\nOne moment please! Reading from requested city file.......")
       with open(city_file) as csvfile:

          for row in csv.DictReader(csvfile,skipinitialspace=True):
           # print(row)
            date_temp = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
            day=date_temp.strftime('%A'.lower())
            #print(day)
            if day.lower()==time_period:
              city_data.append({k:v for k, v in row.items()})
       return city_data

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        The time filter based on user input
    '''
    # TODO: handle raw input and complete function
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    if time_period == "month":
        return get_month()
    elif time_period == "day":
        return get_day()
    elif time_period == "none":
        return "none"
    else:
        print("\nThat is not a valid filter\n")
        get_time_period()

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        The month value based on user input
    '''
    while True:

       month = input('\nWhich month? January, February, March, April, May, or June?\n')
       if month.lower() not in month_list:
          print("Please enter a valid choice from the list")
       else:
           break

    if month.lower() in ('jan','january'):
        return "jan"
    elif month.lower() in ('feb','february'):
        return "feb"
    elif month.lower() in ('mar','march'):
        return "mar"
    elif month.lower() in ('apr','april'):
        return "apr"
    elif month.lower() in ('may'):
        return "may"
    elif month.lower() in ('jun','june'):
        return "jun"
    '''else:
        print("\nThat is not a valid filter\n")
        get_month()'''

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        The day value based on user input
    '''
    # TODO: handle raw input and complete function
    while True:
       # month = input('\nFirst, lets select the month. January, February, March, April, May, or June?\n')
    #get_month()
         day = input('\nWhich day? Please type your response as "day" For eg. Monday,Tuesday, Wednesday..etc\n')
         if day.lower() not in day_list:
            print("Please enter valid choice")
         else:
            break

    if day.lower() in ('mon','monday'):
        return "mon"
    elif day.lower() in ('tue','tuesday'):
        return "tue"
    elif day.lower() in ('wed','wednesday'):
        return "wed"
    elif day.lower() in ('thu','thursday'):
        return "thu"
    elif day.lower() in ('fri','friday'):
        return "fri"
    elif day.lower() in ('sat','saturday'):
        return "sat"
    elif day.lower() in ('sun','sunday'):
        return "sun"


def popular_month(city_data, time_period):
    '''Calculates the count for the months and stores it in the pop_month dict.

    Args:
        city data and the time filter
    Returns:
        The month with the highest count
    '''

    # TODO: complete function

    pop_month={'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'September':0,'October':0,'November':0,'December':0}
    for row in city_data:
        date_temp = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        mon=date_temp.strftime('%B'.lower())
        #print(mon)
        if mon == 'Jan':
            pop_month['January']+= 1
        elif mon == 'Feb':
            pop_month['February']+= 1
        elif mon == 'Mar':
            pop_month['March']+= 1
        elif mon == 'Apr':
            pop_month['April']+= 1
        elif mon == 'May':
            pop_month['May']+= 1
        elif mon == 'Jun':
            pop_month['June']+= 1
        elif mon == 'Jul':
            pop_month['July']+= 1
        elif mon == 'Aug':
            pop_month['August']+= 1
        elif mon == 'Sep':
            pop_month['September']+= 1
        elif mon == 'Oct':
            pop_month['October']+= 1
        elif mon == 'Nov':
            pop_month['November']+= 1
        elif mon == 'Dec':
            pop_month['December']+= 1
        else:
            break
    print('\nThe most popular month for the selected city is ' +(max(pop_month, key=pop_month.get)),'. The Count is :',max(pop_month.values()))

def popular_day(city_data, time_period):
    '''Calculates the count for the days of the week and stores it in the pop_day dict.

    Args:
        city data and the time filter
    Returns:
        The day of the week with the highest count
    '''

    pop_day={'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0,'Sunday':0,}
    for row in city_data:
        date_temp = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        week_day=date_temp.strftime('%A'.lower())
        #print(mon)
        if week_day == 'Mon':
            pop_day['Monday']+= 1
        elif week_day == 'Tue':
            pop_day['Tuesday']+= 1
        elif week_day == 'Wed':
            pop_day['Wednesday']+= 1
        elif week_day == 'Thu':
            pop_day['Thursday']+= 1
        elif week_day == 'Fri':
            pop_day['Friday']+= 1
        elif week_day == 'Sat':
            pop_day['Saturday']+= 1
        elif week_day == 'Sun':
            pop_day['Sunday']+= 1
        else:
            break
    print('\nThe most popular day for the selected city is ' +(max(pop_day, key=pop_day.get)),'. The Count is :',max(pop_day.values()))

def popular_hour(city_data, time_period):
    '''Calculates the count for the hours in a day(24-hour format) and stores it in the pop_hour dict.

    Args:
        city data and the time filter
    Returns:
        The hour with the highest count
    '''
    # TODO: complete function
    pop_hour={'Midnight':0,'1 AM':0,'2 AM':0,'3 AM':0,'4 AM':0,'5 AM':0,'6 AM':0,
                '7 AM':0,'8 AM':0,'9 AM':0,'10 AM':0,'11 AM':0,'Noon':0,
                '1 PM':0,'2 PM':0,'3 PM':0,'4 PM':0,'5 PM':0,'6 PM':0,
                '7 PM':0,'8 PM':0,'9 PM':0,'10 PM':0,'11 PM':0,}
    for row in city_data:
        date_temp = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        day_hour=date_temp.strftime('%H')
        #print(day_hour)
        #print(mon
        if day_hour == '00':
            pop_hour['Midnight']+= 1
        elif day_hour == '01':
            pop_hour['1 AM']+= 1
        elif day_hour == '02':
            pop_hour['2 AM']+= 1
        elif day_hour == '03':
            pop_hour['3 AM']+= 1
        elif day_hour == '04':
            pop_hour['4 AM']+= 1
        elif day_hour == '05':
            pop_hour['5 AM']+= 1
        elif day_hour == '06':
            pop_hour['6 AM']+= 1
        elif day_hour == '07':
            pop_hour['7 AM']+= 1
        elif day_hour == '08':
            pop_hour['8 AM']+= 1
        elif day_hour == '09':
            pop_hour['9 AM']+= 1
        elif day_hour == '10':
            pop_hour['10 AM']+= 1
        elif day_hour == '11':
            pop_hour['11 AM']+= 1
        elif day_hour == '12':
            pop_hour['Noon']+= 1
        elif day_hour == '13':
            pop_hour['1 PM']+= 1
        elif day_hour == '14':
            pop_hour['2 PM']+= 1
        elif day_hour == '15':
            pop_hour['3 PM']+= 1
        elif day_hour == '16':
            pop_hour['4 PM']+= 1
        elif day_hour == '17':
            pop_hour['5 PM']+= 1
        elif day_hour == '18':
            pop_hour['6 PM']+= 1
        elif day_hour == '19':
            pop_hour['7 PM']+= 1
        elif day_hour == '20':
            pop_hour['8 PM']+= 1
        elif day_hour == '21':
            pop_hour['9 PM']+= 1
        elif day_hour == '22':
            pop_hour['10 PM']+= 1
        elif day_hour == '23':
            pop_hour['11 PM']+= 1

        else:
            break
    #print(max(pop_hour.values()))
    print('\nThe most popular hour for the selected city is ' +(max(pop_hour, key=pop_hour.get)),'. The Count is :',max(pop_hour.values()))


def convert_time(seconds):
    '''Used for trip_duration(city_data), converts seconds into (days hours minutes seconds)
    Args:
        seconds -- amount of seconds
    Returns:
        (str) Converts the amount of time to days-hours-minutes-seconds
    '''
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return '%d Days %02d Hours %02d Minutes' % (d,h,m) # only days and hours
    #'%d Days %02d Hours %02d Minutes and %02d seconds' % (d,h, m,s) <-- Days-hours-minutes-seconds


def trip_duration(city_data, time_period):
    '''Calculates the total trip duration and the average trip duration (based on the time filter)

    Args:
        city data and the time filter
    Returns:
        using the convert_time function return the total time in days hours minutes seconds format
    '''
    # TODO: complete function
    duration_count=0
    total_rows=0
    mean_duration=0
    total_duration=0
    for row in city_data:

        total_rows+=1
        duration_count+= float(row['Trip Duration'].strip())

    total= convert_time(duration_count)
    mean= convert_time(duration_count/total_rows)
    print("\nTotal duration of Trips for the city selected is {} and the average trip duration is {}.".format(total,mean))


def popular_stations(city_data, time_period):
    '''Calculates the count for the start and end stations and stores them in their respective dicts.

    Args:
        city data and the time filter
    Returns:
        The start and end station's highest count
    '''
    # TODO: complete function
    count_start_stations= {}
    count_end_stations= {}
    #user_count={'Customer':0,'Subscriber':0,}
    for row in city_data:
        start_station_info = row['Start Station'].strip()
        end_station_info = row['End Station'].strip()

        if start_station_info in count_start_stations:
           count_start_stations[start_station_info]+=1

        elif end_station_info in count_end_stations:
            count_end_stations[end_station_info]+=1

        elif (end_station_info =='' or start_station_info ==''):
            continue
        else:
           count_start_stations[start_station_info]=1
           count_end_stations[end_station_info]=1

    pop_start= max(count_start_stations, key=count_start_stations.get)
    pop_start_value= max(count_start_stations.values())
    pop_end= max(count_end_stations, key=count_end_stations.get)
    pop_end_value= max(count_end_stations.values())
    print('\nThe most popular start station is {}.The most popular end station is {}. The {} and {} are each counts respectively'.format(pop_start,pop_end,pop_start_value,pop_end_value))


def popular_trip(city_data, time_period):
    '''Calculates the count for the "pair" of start/end station and stores it in pair_count dict.

    Args:
        city data and the time filter
    Returns:
        The "pair" count with the highest count
    '''
    '''
    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?
    '''

    pair_count= {}
    for row in city_data:
        start_station_info = row['Start Station'].strip()
        end_station_info = row['End Station'].strip()

        pair_dict= (start_station_info + ' to '+ end_station_info)

        if pair_dict not in pair_count:
            pair_count[pair_dict]=1

        elif pair_dict == '':
            continue

        else:
            pair_count[pair_dict]+=1

    print('\nThe most popular trip for the selected city is between ' +(max(pair_count, key=pair_count.get)),'. The count for this Trip pair is :',max(pair_count.values()))


def users(city_data, time_period):
    '''Calculates the count for the 'subscriber' and 'customers' and stores them in the user_count dict.

    Args:
        city data and the time filter
    Returns:
        The count of Customers and Subscribers
    '''
    # TODO: complete function
    count=0
    user_count={'Customer':0,'Subscriber':0,}
    for row in city_data:
        user_info = row['User Type'].strip()
        #print(User_info)
        if user_info == 'Customer':
            user_count['Customer']+= 1
        elif user_info == 'Subscriber':
            user_count['Subscriber']+= 1
        elif user_info =='':
            continue
        else:
            count+=1
            break
    print('\nThere are {} Customers and {} Subscribers in your selected city '.format(user_count['Customer'],user_count['Subscriber']))
    #print(user_count)


def gender(city_data, time_period):
    '''Calculates the count for the 'male' and 'female' and stores them in the gender_count dict.

    Args:
        city data and the time filter
    Returns:
        The count of Males and Females
    '''
    count=0
    gender_count={'Female':0,'Male':0,}

    if any('Gender' in d for d in city_data) is False:
        print("\nThe selected city does not have gender data")
    else:
        for row in city_data:
            gender_info = row['Gender'].strip()
            if gender_info == 'Female':
                gender_count['Female']+= 1
            elif gender_info == 'Male':
                gender_count['Male']+= 1
            elif gender_info =='':
                continue
            else:
                count+=1
                break
        print('\nThere are {} Females and {} Males in your selected city '.format(gender_count['Female'],gender_count['Male']))


def birth_years(city_data, time_period):
    '''Calculates the count for each of the birth years and stores them in the counts dict.

    Args:
        city data and the time filter
    Returns:
        The oldest,youngest and the most common birth year
    '''

    '''
    Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    '''
    counts={}
    if any('Birth Year' in d for d in city_data) is False:
        print("\nThe selected city does not have birth year data")
    else:
        for row in city_data:
            birth_info=(row['Birth Year']).strip()
            if birth_info =='':
                continue
            elif birth_info in counts:
                counts[birth_info]+=1
            else:
                counts[birth_info]=1
        most_common = max(counts, key=lambda x: counts[x])
        temp=list(counts.keys())
        oldest_year=min(temp)
        latest_year=max(temp)
        print('\nThe most recent birth year is {}, the earliest is {} and the most popular is {}'.format(latest_year,oldest_year,most_common))


def display_data(city_data):
    '''Displays five lines of data if the user specifies that they would like to see individual data from the selected city_data.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        city data
    Returns:
        5 rows of raw data for each time user confirms
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    #city_data = collections.OrderedDict()
    #print(city_data)
    # TODO: handle raw input and complete function
    x=0
    y=5
    if display in ('Yes','yes','Ya','ya'):
      while True:
       #while(x<y):
        for row in city_data[x:y]:

            for k,v in row.items():
                print (k,': ',v,'\n')

        display = input('\nWould you like to view more individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
        if display in ('Yes','yes','Ya','ya'):
                x=y
                y=x+5
        else:
             break


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print("\nThe file for the selected city is {}".format(city))

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    # Open the CSV file and get the data into a list comprehension. i.e list of dictionary
    city_data = load_city_data(city,time_period)

    print("\nThe filter selected is {}".format(time_period))
    print('\nCalculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':

        #TODO: call popular_month function and print the results
        start_time = time.time()
        popular_month(city_data, time_period)
        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

        # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        #start_time = time.time()

    '''This section below is going to be printed only for "month" time_period filter'''
    if (time_period == 'none' or time_period in month_list):

        # TODO: call popular_day function and print the results
        start_time = time.time()
        popular_day(city_data,time_period)
        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")


    '''This section below is going to be printed only for "day" time_period filter'''
    if (time_period == 'none' or time_period in month_list or time_period in day_list):

        # What is the most popular hour of day for start time?
        # TODO: call popular_hour function and print the results
        start_time = time.time()
        popular_hour(city_data,time_period)
        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    '''This section below and the rest is going to be printed regardless of the time_period filter'''
    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    start_time = time.time()
    trip_duration(city_data,time_period)
    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    start_time = time.time()
    popular_stations(city_data,time_period)
    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")


    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    start_time = time.time()
    popular_trip(city_data,time_period)
    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")


    # What are the counts of each user type?
    # TODO: call users function and print the results
    start_time = time.time()
    users(city_data,time_period)
    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")


    # What are the counts of gender?
    # TODO: call gender function and print the results
    start_time = time.time()
    gender(city_data,time_period)
    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")


    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    start_time = time.time()
    birth_years(city_data,time_period)
    print("\nThat took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_data)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
