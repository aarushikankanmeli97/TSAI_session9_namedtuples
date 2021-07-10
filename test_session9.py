import pytest
from session9 import *

# First five test cases

def test_calculateAge():
    calculated_age = calculateAge(date(1997, 2, 3))
    assert calculated_age == 24 , 'Age calculator is not working!!!!'

def test_get_fake_profile_1():
    prof_list = get_fake_profile(num_profiles = 10)
    assert len(prof_list) == 10 , "profiles missing!!!"

def test_get_fake_profile_2():
    prof_list = get_fake_profile(num_profiles = 10)
    assert len(prof_list[0]) == 4 , "profile details missing!!!"

def test_get_fake_profile_3():
    prof_list =  get_fake_profile(num_profiles = 10)
    assert type(prof_list[0].current_location) == tuple , "wrong data!!!"

def test_get_fake_profile_4():
    prof_list =  get_fake_profile(num_profiles = 10)
    assert prof_list[0].blood_type in ["A-","AB+","O+","B-","A+-","AB-","A+","B-"] , "Invalid blood group!!"

# Second five test cases

def test_get_dict_list_1():
    dict_list = get_dict_list(population=10)
    assert len(dict_list) == 10 , "profiles missing!!!"

def test_get_dict_list_2():
    dict_list = get_dict_list(population=10)
    assert type(dict_list[0]["current_location"]) == tuple , "wrong data!!!"

def test_get_dict_list_3():
    dict_list = get_dict_list(population=10)
    assert dict_list[0]["blood_type"] in ["A+","AB+","O+","B+","A-","AB-","O-","B-"] , "Invalid blood group!!"

def test_cal_named_tuple():
    result_1,nt_time_consumption,nt = cal_named_tuple(10)
    age_list  = []
    for i in nt :
        age =  calculateAge(birthDate = i.DOB)
        age_list.append(age)
    np.mean(age) == result_1[-1] , "Age calculate wrong!!"

def test_nt_vs_dict_2():
    nt_time_list = []
    dict_time_list = []
    for i in range(5):
        result_1,nt_time_consumption = cal_named_tuple(100) 
        result_2,dict_time_consumption = cal_dict(100)
        nt_time_list.append(nt_time_consumption)
        dict_time_list.append(dict_time_consumption)
    # assert result_1 == result_2
    assert np.mean(nt_time_list) < np.mean(dict_time_list) , 'nt_time_consumption is high!!!!!!'

# Last 10 test cases
def test_create_companies_list_1(): #1
    companies_list,market_capital_list = create_companies_list(10)
    assert len(companies_list) == 10 , "Profiles missing!!"

def test_create_companies_list_2(): #2
    companies_list,market_capital_list = create_companies_list(10)
    assert len(companies_list[0]) == 7 , "data missing!!"

def test_weights():#3
    companies_list,weight_list = create_companies_list(10)
    market_sum  = get_market_sum(weight_list)
    weights_list = get_weights_list(weight_list ,market_sum)
    assert round(sum(weights_list)) == 100 , "Wrong weights calculation"

def test_create_companies_list_3():#4
    companies_list,market_capital_list = create_companies_list(10)
    assert companies_list[1].open_value <= companies_list[1].high_value , "open value higher than the high value !!!"

def test_create_companies_list_4(): #5
    companies_list,market_capital_list = create_companies_list(10)
    assert companies_list[1].high_value >= companies_list[1].close_value , "close value higher than the high value!!!"

def test_create_companies_list_5(): #6
    companies_list,market_capital_list = create_companies_list(10)
    market_sum  = get_market_sum(market_capital_list)
    weights_list = get_weights_list(market_capital_list ,market_sum)

    if companies_list[0].market_capital > companies_list[1].market_capital :
        assert weights_list[0] > weights_list[1] , "Wrong weights calculation"
    else:
        assert weights_list[0] < weights_list[1] , "Wrong weights calculation"

def test_get_stockmarket_points_1():
    companies_list,market_capital_list = create_companies_list(10)
    market_sum  = get_market_sum(market_capital_list)
    weight_list = get_weights_list(market_capital_list ,market_sum)
    open_value, high_value , close_value = get_stockmarket_points(companies_list,weight_list)
    assert open_value <= high_value , "wrong entries!!!"  

def test_get_stockmarket_points_2():
    companies_list,market_capital_list = create_companies_list(10)
    market_sum  = get_market_sum(market_capital_list)
    weight_list = get_weights_list(market_capital_list ,market_sum)
    open_value, high_value , close_value = get_stockmarket_points(companies_list,weight_list)
    assert close_value <= high_value , "wrong entries!!!"  

def test_symbol():
    companies_list,market_capital_list = create_companies_list(10)
    sym = []
    for c in companies_list:
        sym.append(c.symbol)
    assert len(np.unique(sym)) == 10 , "symbols are not unique!!!"

def test_get_stockmarket_points_3():
    companies_list,market_capital_list = create_companies_list(10)
    market_sum  = get_market_sum(market_capital_list)
    weight_list = get_weights_list(market_capital_list ,market_sum)
    open_value, high_value , close_value = get_stockmarket_points(companies_list,weight_list)
    difference =( abs(open_value - close_value)/open_value )*100 
    assert difference < 50 , "Stock market point are highly random!!"

# def 
# def test

# def test_get_stockmarket_points():
#     get_stockmarket_points()