import requests
import json
import psycopg2
from datetime import datetime
from time import time

'''
month starts at 00:00:00 first day of the month
week starts at 00:00:00 first day of the week
day starts at 00:00:00

use each 12 hours at 00:00 and 12:00
4 hours from 01:00
hour from 00 mins
30 mins from 30 mins 00
15 mins from the hour

initial stamp must be from the hour


m2, m3, m4, m5, m15, m30, m60, m240(4 hr), m720(12 hr), day_end, week_end, month_end

1. get 2880 rows
2. insert each row into table with minute timestamps
3. if minute timestamp - now_timestamp % 2 == 0, mark as 2 minute
4. if minute timestamp - now_timestamp % 3 == 0, mark as 3 minute
5. if minute timestamp - now_timestamp % 4 == 0, mark as 4 minute
....5, 15, 30, 60, 240, 720
6. Count count all values with 60 minute markers and retrieve hour values from oldest timestamp till we have 52 markers
7. Same for 240 and 720
8. Get day end
9. Get week
10 get month

Need the 52 prior values for all periods

most recent 60 minute interval values less the 60 minute values retrieved already.
Need the 52 most recent 240 minute interval values less the 60 minute values retrieved already
And so on.
Not a problem to just get the most recent 60, 240, ... 52 values and then store just the ones we don't already have.
Worst case we have 7 (8?) queries returning a total of 2880 + (6*52) rows of data.
ropped

Initial Data Load:

Query-1 - 2880 one row each min (up to 52 30 min periods)
Query-3 - 52 hour-end 
Query-3 - 52 (240 min periods)
Query-4 - 52 (720 min periods)
Query-5 - 52 day ends
Query-6  - 52 week end
Query-7 - 52 month ends

each query added with timestamps # standardise timestamps...

yyyy-mm-dd hh:mm

for day, week, month, add hh:mm as 00:00

Algo...
get month ends and store
get week ends and store
get day ends and store
get hour ends and store

How do we know where to assign flags from?
Assign minute data stamp to asset and do maths from there?

so, we have a minute data stamp from the first request made. Do we need to compare everything else to that?

current - first ever and check against that



'''

def get_load(asset, time_frame, size):#this works
    '''
    query all active 
    '''
    params = [
    "apikey=b410a081bcbe42bc8807dc30e1407ede", #Essential
    f"symbol={asset}",
    #f"methods=price",
    f"interval={time_frame}",#1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 1day, 1week, 1mon, 
    f"outputsize={size}",
    #f"dp=4"#decimal places?
    ] 
    '''
    time_series forex, cryptocurrency, etf, indices, stocks 
    '''
    url_root = 'https://api.twelvedata.com/time_series?'
    url_with_params = url_root + "&".join(params)
    print(url_with_params)
    response = requests.get(url_with_params)
    print(response)
    return response

def to_unix_timestamp_mins(date, epoch=datetime(1970,1,1)):

    if len(date) < 12:
        date += ' 00:00:00'
    dt = datetime.strptime(date,"%Y-%m-%d %H:%M:%S")#create datetime object
    
    td = dt - epoch#subtract made object from start of unix epoch
    # return td.total_seconds()
    return round((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6) / 60, date

def process_individual_value(value_dict, initial_stamp_mins):
    '''
    value_dict = {'datetime':'YYYY-mm-dd HH:MM:SS', 'close':'0.0666'}
    '''
    #1. convert datetime to stamp_mins
    stamp_mins, date = to_unix_timestamp_mins(value_dict['datetime'])
    #2. value
    asset_value = float(value_dict['close'])
    #3. Populating flags
    mins_difference = initial_stamp_mins - stamp_mins
    time_intervals = {
        'm2':{'index':(-5, -3), 'value':2},
        'm3':{'index':(-5, -3), 'value':3}, 
        'm4':{'index':(-5, -3), 'value':4},
        'm5':{'index':(-5, -3), 'value':5},
        'm15':{'index':(-5, -3), 'value':15},
        'm30':{'index':(-5, -3), 'value':30},
        'h1':{'index':(-5, -3), 'value':60},
        'h4':{'index':(-8, -6), 'value':4},
        'h12':{'index':(-8, -6), 'value':12},
        'day':{'index':(-8, -6), 'value':24},
        #'week1':{'index':(), 'value':0},#How can I check that it's Monday???
        'month':{'index':(8, 10), 'value':30},
    }

    flags = {}
    'YYYY-mm-dd HH:MM:SS'
    '0123456789 87654321'
    for key, value in time_intervals.items():
        start=value['index'][0]#first index value
        stop=value['index'][1]#second index value
        if int(date[start:stop]) % value['value'] == 0:#indexing the date string and int-ing it
            flags[key] = True
        else:
            flags[key] = False

        if key == 'h4':
            if (int(date[start:stop])-1) % value['value'] == 0:#indexing the date string and int-ing it
                flags[key] = True
            else:
                flags[key] = False
        if key == 'month':
            if int(date[start:stop]) == 1:
                flags[key] = True
            else:
                flags[key] = False

    return stamp_mins, asset_value, flags

def make_response_useful(asset_id, response, initial_stamp_mins):
    print(response['status'])
    values_list = response['values']
    useful = []
    for item in values_list:
        print(item)
        timestamp_mins, value, flags = process_individual_value(item, initial_stamp_mins)
        dict_one = {'asset_id':asset_id, 'timestamp_mins':timestamp_mins, 'value':value}
        to_append = {**dict_one, **flags}
        useful.append(to_append)
    return useful #a list of list[asset_id, stamp_mins, value, m2,3,4,5,15,30,60,240,720,day,week,month all flags....]

def get_prepped_data(asset_id, symbol, interval, count):
    initial_stamp_mins = round(time()/60)
    response = get_load(symbol, interval, count).json()
    useful_data = make_response_useful(asset_id, response, initial_stamp_mins)
    print(response['values'][0])
    print(response['values'][-1])
    return useful_data


def get_all_prepped_data(asset_id, symbol):
    initial_stamp_mins = round(time()/60)

    response = get_load(symbol, '1min', 2880).json()
    useful_data = make_response_useful(asset_id, response, initial_stamp_mins)
    
    print('Got first load')

    intervals = ['1h', '1day', '1week', '1month']
    for interval in intervals:
        response = get_load(symbol, interval, 52).json()
        useful_data += make_response_useful(asset_id, response, initial_stamp_mins)
        print(useful_data[-1])
        print(f'Got {interval} load')

    return useful_data

