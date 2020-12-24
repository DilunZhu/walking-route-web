import geo
import pandas as pd


def direction_walking(key, start_address, end_address):
    """    """
    start = geo.geocode(key, start_address)['geocodes'][0]['location']
    end = geo.geocode(key, end_address)['geocodes'][0]['location']
    results = geo.walking(key, start, end)
    df = pd.json_normalize(results['route']['paths'][0]['steps'])
    return df


def total_walk(df):
    """    """
    distance = df['distance'].to_list()
    sum_num = 0
    for i in distance:
        sum_num += int(i)
    return sum_num


def total_walk_time(df):
    """    """
    duration = df['duration'].to_list()
    sum_num = 0
    for i in duration:
        sum_num += int(i)
    return sum_num // 60
