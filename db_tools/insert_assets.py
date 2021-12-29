import requests
import json
import psycopg2
import time

asset_dict = {
    #NOTE: 31514 is the index of the first non entirely numerical stock
    'stocks':           '/stocks',          #87013  symbol, name, curency, exchange, country, type USE NAME 
    'forex_pairs':      '/forex_pairs',     #1998   symbol, currency_group, curreny_base, currency_quote
    'cryptocurrencies': '/cryptocurrencies',#3555   symbol, available_exchanges, currency_base, currency_quote
    'etf':              '/etf',             #2984   symbol, name, currency, exchange STANDS FOR EXCHANGE TRADED FUND
    'indices':          '/indices',         #1652   symbol, name, country, currency
    }
#                                           #97202 entries total

def get_asset_list(asset_list, csv):
      
    base_url = 'https://api.twelvedata.com'
    complete_url = base_url + asset_list

    if csv == True:
        complete_url += '?format=CSV'
    
    response = requests.get(complete_url)
    return response

def add_to_db(asset_list):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="password",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="ichi2")
        cursor = connection.cursor()

        for i, asset in enumerate(asset_list):
            print(asset)
            postgres_insert_query = '''INSERT INTO main_Assets (asset_symbol, asset_name, asset_type) 
            Values(%s, %s, %s)'''
            record_to_insert = (asset['symbol'], asset['name'], '/stocks')
            cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_assets(chosen, number):
    asset_list = get_asset_list(asset_dict[chosen], False).json()
    asset_string_list = [asset['symbol'] for asset in asset_list['data']]
    print(asset_string_list[-1])

    return asset_list['data'][-number:]
'''
if __name__ == '__main__':
    chosen = 'stocks'
    asset_list = get_asset_list(asset_dict[chosen], False).json()
    length = len(asset_list['data'])
    print(chosen, length)
    asset_string_list = [asset['symbol'] for asset in asset_list['data']]
    #print(asset_string_list[-99:])
    add_to_db(asset_list['data'][-99:])
'''
