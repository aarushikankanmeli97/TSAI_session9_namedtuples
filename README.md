# TSAI_EPAi3.0

# Project Description:

    This repository contains Assignment for session 9 on namedtuples.

# Tuples :
    A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.

# Namedtuple : 
    Python supports a type of container like dictionaries called “namedtuple()” present in module, “collections“. Like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.

# Faker Module :
    Faker is a Python package that generates fake data. Faker has the ability to print/get a lot of different fake data, for instance, it can print fake name, address, email, text, etc.

# Detailed break-down of the functions used : 
    - We begin with importing necessary modules, namedtuples being the major library present in the collections module.
    
    - The function 'get_fake_profile' is used to generate 10000 random profiles using the Faker library. Here the variable 'Profile' contains the namedtuple which gives  blood group, current location and Date of Birth in order to calculate largest blood type, mean current location, oldest person age and average age.

    - The function 'calculateAge' gives the curent age using the date of birth as input.

    - The function 'cal_mean_current_location' calculates the mean of the x and y coordinates. The attribute 'current_location' in the faker library gives the decimal of longitude and lattitude. 

    - The function 'named_tuple_cal' calculates the largest blood group, mean current location, oldest person age and average age. Here, we get the list of 10000 random profiles and extract the information on longitude, lattitude, age and blood group from the acquired list. Along with this, the function calculates the time taken for this operation to execute using namedtuple.

    - The function 'get_dict_list' performs the same operation of generating 10000 random profiles using Faker library and is saved in a dictionary in order to calculate the same parameters as previous functions.

    - The function 'dict_cal' calculates the largest blood group, mean current location, oldest person age and average age. Here along with these prameters, the function also gives the time take to execute all the above mentioned operations using a dictionary (the same way we calculated fo namedtuple in above functions).

    - The function 'get_symbol' retuns the NSE/BSE symbol of a company.

    - The function 'get_random_weights' returns the random weights of 100 companies.

    - The function 'get_random_open' returns the opening price of a stock.

    - The function 'get_high' gives the highest price of the day of a stock.

    - The function 'get_close' gives the closing price of a stock.

    - The function 'create_fake_companies_list' creates a list of 100 companies (based on user preference) having information like company name, company symbol, opening value, highest price of the day, lowest price of a day and weight of a company. 

    - The function 'get_stockmarket_points' calculates the opening value, highest prce and closng value of stock market.The points are calculated by multiplying the values with the normalized weights and summing up all the values.

    - The 'Population data' block gives the overall data like largets blood type, mean curent location, oldest person age and average age using namedtuples and dictionary. Also the results show that namedtuples take less time when compared to dictionary in order to execute the functions.

    - The 'Stocks data' block gives the information about Opening value, highest price and closing value of a stock.

# Table of contents :

- session_9_namedtuples_assignment
    - .github
		- classroom
			- autograding.json
		- workflow
			- ci.yml
    - .gitignore
	- requirements.txt
	- Session9_namedtuples_assignment.ipynb
	- test_session9.py
