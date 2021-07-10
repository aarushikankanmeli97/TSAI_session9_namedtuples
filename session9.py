from faker import Faker
import statistics
from collections import namedtuple
import datetime
from datetime import date, time
import numpy as np
import random

fake = Faker()

def get_fake_profile(num_profiles):
    '''
    This function helps generate random profiles using faker library based on the 
    num input given.
    '''
    
    prof_list = []
    Profile = namedtuple('Profile',['blood_type', 'current_location', 'DOB'])
    for i in range(num_profiles):
        profiles = fake.profile()
        prof = Profile(profiles['blood_group'], profiles['current_location'], profiles['birthdate'])
        prof_list.append(prof)
        
    return prof_list

def calculateAge(birthDate): 
    '''
    This function helps calculate the age of a person with Date of Birth as input 
    parameter.
    '''
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 

def calculate_mean_current_location(name_tuple_list):
    '''
    This function returns the mean of current location (x and y coordintes).
    '''
    lan = []
    lon = []
    for name in name_tuple_list:
        lan.append(name.current_location)
        lon.append(name.current_location)
    return np.mean(lan),np.mean(lon)

def cal_named_tuple(population):
    '''
    This function calculates and returns the largest blood type, mean current location,
    oldest person age, average age and time taken for calculation using namedtuple.
    '''
    t0 = datetime.datetime.now()
    named_tuple_list = get_fake_profile(population)
    lan = []
    lon = []
    age = []
    blood_group = []
    for name in named_tuple_list:
        lan.append(name.current_location[0])
        lon.append(name.current_location[1])
        age.append(calculateAge(name.DOB))
        blood_group.append(name.blood_type)
    try:
        largest_blood_type = statistics.mode(blood_group)
    except:
        largest_blood_type = statistics.multimode(blood_group)
    mean_location = (np.mean(lan),np.mean(lon))
    maximum_age = np.max(age)
    average_age = np.mean(age)
    result = largest_blood_type,mean_location,maximum_age,average_age
    t1 = datetime.datetime.now()
    time_elapsed = (t1-t0).total_seconds()
    return result , time_elapsed

def get_dict_list(population) :
    ''' 
    This function gives random profiles using using Faker library for to create 
    dictionary.
    '''
    dict_list = []
    for i in range(population):
        profile =  fake.profile()
        d = {'name':profile['name'],"blood_type":profile['blood_group'],"current_location":profile['current_location'],
            "DOB": profile['birthdate']}
        dict_list.append(d)
    return dict_list

def cal_dict(population):
    '''
    This function calculates and returns the
    largest blood type, mean-current_location,
    oldest_person_age ,average age and time taken for calculation using Dictionary.
    '''
    t2 = datetime.datetime.now()
    dict_list = get_dict_list(population)
    lan = [] 
    lon = []
    age = []
    blood_group = []
    for name in dict_list:
        lan.append(name['current_location'][0])
        lon.append(name['current_location'][1])
        age.append(calculateAge(name['DOB']))
        blood_group.append(name['blood_type'])
    try:
        largest_blood_type = statistics.mode(blood_group)
    except:
        largest_blood_type = statistics.multimode(blood_group)
    mean_location = (np.mean(lan),np.mean(lon))
    maximum_age = np.max(age)
    average_age = np.mean(age)
    result = largest_blood_type,mean_location,maximum_age,average_age
#     result = statistics.mode(blood_group), (np.mean(lan),np.mean(lon)),np.max(age),np.mean(age)
    t3 = datetime.datetime.now()
    # print(f'Time taken for claculation{t3-t2}')
    time_elapsed = (t3-t2).total_seconds()
    return result,time_elapsed

def get_comp_symbol(com_name,i):
    '''
    This function returns the symbol for given company name.
    '''
    symbol = str(i)
    for c in com_name:
        symbol += '_' + c[0]
    return symbol

def get_random_weights():
    '''
    This function returns random weights of given 100 companies.
    '''
    return random.uniform(0,100) 

def get_weight(market_capital,total_capital):
    """
    This function return weights calculated based on the market capital
    """
    weight = (market_capital/total_capital)*100
    return weight

def get_weights_list(market_capital_list ,market_sum):
    weight_list = []
    for li in market_capital_list:
        weight = get_weight(market_capital = li,total_capital = market_sum)
        weight_list.append(weight)
    return weight_list

def get_random_market_capital():
    """
    This function return random market_capital in range of 500,10000.
    """
    return random.uniform(500,10000) 

def get_market_sum(market_capital_list):
    """
    This function calculate the Total market capital
    """
    total = sum(market_capital_list)
    return total

def update_weight(comp_list , weight_list):
    """
    This function update the weight in the named tuple with the calculated weights
    """
    for c,w in zip(comp_list , weight_list):
        c._replace(weight = w)
    return  comp_list

def get_random_open_value():
    '''
    This function return the opening value of a stock.
    '''
    return round((random.uniform(300,1000)),2)

def get_high_value(open_value):
    '''
    This function calculates the high value of a stock.
    '''
    return round(open_value*(random.uniform(1,3.0)),3)

def get_close_value(high_value):
    '''
    This is function calculates the closing vlue of a stock.
    '''
    return round(high_value*(random.uniform(0.2,1.2)),3)

def create_companies_list(no_of_companies):
    '''
    This function creates a  list of fake companies with following values,
    company name, stock symbol for particular company, opening value, high value, closing value and weight.
    '''
    company = namedtuple('company',['com_name', "symbol", 'open_value', 'high_value', 'close_value','weight','market_capital'])
    companies_list = []
    weight_list = []
    for i in range(no_of_companies):
        com_name = fake.company()
        symbol = get_comp_symbol(com_name,i)
        weight = get_random_weights()
        market_capital = get_random_market_capital()
        open_value = get_random_open_value()
        high_value = get_high_value(open_value)
        close_value = get_close_value(high_value)
        companies_list.append(company(com_name,symbol, open_value, high_value, close_value ,weight,market_capital))
        weight_list.append(weight)
    return companies_list,weight_list

def get_stockmarket_points(companies_list,weight_list):
    '''
    This function calculates the stock markets opening point , highest point , closing point.
    The points are calculated by multiplying the values with the normalized weights and summing up all the values.
    '''
    open_points = []
    high_points = []
    close_points = []
    sum_weight = sum(weight_list)
    for com in companies_list:
        open_point = com.open_value * com.weight
        high_point = com.high_value * com.weight
        close_point = com.close_value * com.weight
        open_points.append(open_point)
        high_points.append(high_point)
        close_points.append(close_point)
    return round(sum(open_points),2),round(sum(high_points),2),round(sum(close_points),2)

