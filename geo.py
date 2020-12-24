#!/usr/bin/env python
# coding: utf-8

import requests,json


# 地理编码
def geocode(key, formatted_address, city=None, batch="false", sig=None, output="json", callback=None):
    """将详细的结构化地址转换为高德经纬度坐标"""
    geocode_url = "https://restapi.amap.com/v3/geocode/geo?parameters"
    params = {
        "key": key,
        "address": formatted_address,
        "city": city,
        "batch": batch,
        "sig": sig,
        "output": output,
        "callback": callback
    }
    r = requests.get(geocode_url, params=params)
    return r.json()


# 步行路径规划
def walking(key, origin, destination, sig=None, output="json", callback=None):
    """可以规划100KM以内的步行通勤方案，并且返回通勤方案的数据"""
    walking_url = "https://restapi.amap.com/v3/direction/walking?parameters"
    params = {
        "key": key,
        "origin": origin,
        "destination": destination,
        "sig": sig,
        "output": output,
        "callback": callback
    }
    r = requests.get(walking_url, params=params)
    return r.json()


# 公交路径规划
def busing(key, origin, destination, city, cityd=None, extensions="base", strategy=0, nightflag=0, date=None, time=None,
           sig=None, output="json", callback=None):
    """规划综合各类公共（火车、公交、地铁）交通方式的通勤方案，并且返回通勤方案的数据"""
    busing_url = "https://restapi.amap.com/v3/direction/transit/integrated?parameters"
    params = {
        "key": key,
        "origin": origin,
        "destination": destination,
        "city": city,
        "cityd": cityd,
        "extensions": extensions,
        "strategy": strategy,
        "nightflag": nightflag,
        "date": date,
        "time": time,
        "sig": sig,
        "output": output,
        "callback": callback
    }
    r = requests.get(busing_url, params=params)
    return r.json()


# 驾车路径规划
def driving(key, origin, destination, originid=None, destinationid=None, origintype=None, destinationtype=None,
            strategy=0, waypoints=None, avoidpolygons=None, avoidroad=None, province=None, number=None, cartype=0,
            ferry=0, roadaggregation="false", nosteps=0, sig=None, output="json", callback=None, extensions="base"):
    """规划以小客车、轿车通勤出行的方案，并且返回通勤方案的数据"""
    driving_url = "https://restapi.amap.com/v3/direction/driving?parameters"
    params = {
        "key": key,
        "origin": origin,
        "destination": destination,
        "originid": originid,
        "destinationid": destinationid,
        "origintype": origintype,
        "destinationtype": destinationtype,
        "strategy": strategy,
        "waypoints": waypoints,
        "avoidpolygons": avoidpolygons,
        "avoidroad": avoidroad,
        "province": province,
        "number": number,
        "cartype": cartype,
        "ferry": ferry,
        "roadaggregation": roadaggregation,
        "nosteps": nosteps,
        "sig": sig,
        "output": output,
        "callback": callback,
        "extensions": extensions
    }
    r = requests.get(driving_url, params=params)
    return r.json()


# 骑行路径规划
def bicycling(key, origin, destination):
    """规划骑行通勤方案，规划时不会考虑路况；考虑天桥、单行线、封路等情况"""
    bicycling_url = "https://restapi.amap.com/v4/direction/bicycling?parameters"
    params = {
        "key": key,
        "origin": origin,
        "destination": destination,
    }
    r = requests.get(bicycling_url, params=params)
    return r.json()
