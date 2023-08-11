'''
Judy Wang
Fall 2022 CS5001
Final Project Milstone 1 
Function file
'''

import requests
from requests.exceptions import HTTPError
from requests.exceptions import MissingSchema
import pandas
from Class_school import School
from Class_housing import Housing
from data_dashboard_constance_wip import *
from data_dashboard_input_wip import *

def download_file(file_url):
    '''
    function download_file reads a url from terminal and save that into variable
    parameter: None
    return a string variable
    raise: HTTPError is page not found
    '''
    try: 
        
        resp_file = requests.get(file_url)
        resp_file.raise_for_status()
        file_content = resp_file.text

        return file_content

    except requests.exceptions.HTTPError as http_err:
        print(f'{http_err}')
        return

    except MissingSchema as schema_err:
        print(f'{schema_err}')
        return

    except ConnectionError as Connction_err:
        print(f'Connection error occurred')
        return
    
    except Exception:
        print(f'Other error occurred')
        return

def clean_school_file(file_school):
    '''
    function clean_school_file cleans the file
    parameter: string that returns from download_school_file()
    return 3 lists 
    raise: TypeError if the original row file passed file_school is not string 
    UnboundlocalError if clean_row is not iterable
    '''
            
    school_info = []
    school_category = []
    school_name = []
    school_area = []
    
    try:
        clean_row = file_school[FILE_SCHOOL_STARTING_CHARA:FILE_SCHOOL_ENDING_CHARA].split(FILE_SCHOOL_ROW_SPLITER) #slice header  
    except TypeError:
        print (f'can not clean data as variable "school_content" is not associated with a value')
        return

    try:
        for each_school in clean_row:
            if each_school is None:
                pass
            else:
                each_school = each_school.split(EACH_SCHOOL_ATTIBUTE_SPLITER)  #stripping "\n" for each_school attribute
                each_school[SCHOOL_AREA_INDEX] = each_school[SCHOOL_AREA_INDEX].strip(SCHOOL_AREA_STRIP_DELIMITER) #stripping "\r" for locations[index -1]
                school_info.append(each_school)
    except UnboundLocalError:
        print (f"cannot access local variable 'clean_row' is not associated with a value")
        return

    for every_school in school_info:

        category = every_school[SCHOOL_CATEGORY_INDEX]   #category is the index 1 of every school info
        school_category.append(category)
        name = every_school[SCHOOL_NAME_INDEX]  #name is the index 2 of every school info
        school_name.append(name)
        area = every_school[SCHOOL_AREA_INDEX]  #area is the index -1 of every school info
        school_area.append(area)

    return school_name,school_category,school_area
    
def clean_nonmarket_housing(file_nonmarket_housing):
    '''
    function clean_nonmarket_housing_file cleans the file
    parameter: string that returns from download_nonmarket_housing_file()
    return 3 lists 
    raise: TypeError if the original row file passed file_nonmarket_housing is not string 
    UnboundlocalError if clean_row is not iterable
    '''

    non_market_housing_info = []
    non_market_housing_name = []
    non_market_housing_status = []
    non_market_housing_area = []
    
    try:
        clean_row = file_nonmarket_housing[FILE_NONPUBLIC_HOUSING_STARTING_CHARA:FILE_NONPUBLIC_HOUSING_ENDING_CHARA].split('\n')
    except TypeError:
        print (f'can not clean data as variable "nonmarket_housing_content" is not associated with a value')
        return

    try:
        for each_housing in clean_row:
            if each_housing is None:  #pass empty rows 
                pass
            else:
                each_housing = each_housing.split(FILE_NONPUBLIC_HOUSING_ROW_SPLITER)
                for every in each_housing:
                    every = every.split(FILE_NONPUBLIC_HOUSING_ATTIBUTE_SPLITER)  #split each housing info by \n
                    name = every[PUBLIC_HOUSING_NAME_INDEX]  #name is the index 1 of every housing info
                    non_market_housing_name.append(name)
                    status = every[PUBLIC_HOUSING_STATUS_INDEX]  #status is the index 3 of every housing info
                    non_market_housing_status.append(status)
                    area = every[PUBLIC_HOUSING_AREA_INDEX]  #area is the index -3 of every housing info
                    non_market_housing_area.append(area)
            
        return non_market_housing_name,non_market_housing_status,non_market_housing_area

    except UnboundLocalError:
        print (f"cannot access local variable 'clean_row' is not associated with a value")
        return

def construct_school_info(school_name,category,area):
    '''
    function construct_school_info parse data lists into objects from class School
    parameter: 3 lists returned in clean_school_file(file_school)
    return a list of School objects
    raise: TypeError if the index iterate over each list isn't an integer
    '''

    school_list = []

    try:
        for i in range(len(school_name)):
            school_instance = School(school_name[i],category[i],area[i])  #loop every index and pass attributes to class to generate objects           
            school_list.append(school_instance)
        return school_list

    except TypeError:
        print ('Index in range must be integers')
        return

def school_area_category_dictionary(school_list,user_input):
    '''
    function school_area_dictionary construct a dictionary where key is school area, and value is #of schools in that area
    parameter: school list that integrates all objects generated from class School
    return dictionary 
    raise: TypeError if school list constructed from class School was not successful 
    '''
    
    area_category_school_dictionary = {}
    school_available_area = []
    user_choose_school_category = ''

    if user_input == "1":
        user_choose_school_category = CHOOSE_SCHOOL_CATEGORY_PUBLIC

    if user_input == "2":
        user_choose_school_category = CHOOSE_SCHOOL_CATEGORY_PRIVATE

    if user_input == "3":
        user_choose_school_category = CHOOSE_SCHOOL_CATEGORY_STRONGBC

    if user_input == "4":
        area_category_school_dictionary = {}
        school_available_area = []
        user_choose_school_category = "Any Type of School"

        for school_object in school_list:

#            if school_object.school_area not in school_available_area:
#                school_available_area.append(school_object.school_area)

            if school_object.school_category == CHOOSE_SCHOOL_CATEGORY_PUBLIC or school_object.school_category == CHOOSE_SCHOOL_CATEGORY_PRIVATE or school_object.school_category == CHOOSE_SCHOOL_CATEGORY_STRONGBC:  ##set school category to "public school", next step to prompt user input               
                if school_object.school_area not in area_category_school_dictionary:
                    area_category_school_dictionary[school_object.school_area] = 1
                    
                else:
                    area_category_school_dictionary[school_object.school_area] += 1 
                
        return user_choose_school_category, dict(sorted(area_category_school_dictionary.items()))
                

    try:
        for school_object in school_list:
            if school_object.school_area not in school_available_area:
                school_available_area.append(school_object.school_area)

            if school_object.school_category == user_choose_school_category:  ##set school category to "public school", next step to prompt user input
                if school_object.school_area not in area_category_school_dictionary:
                    area_category_school_dictionary[school_object.school_area] = 1
                    
                else:
                    area_category_school_dictionary[school_object.school_area] += 1 
            else:
                pass   #it school category is not public school, pass for now

        for given_type_shool_area in school_available_area:   #some areas don't have certain type of school, such as shannesy doesn't have public school, we still add the area into dictionary, and set vaule to 0
            if given_type_shool_area not in area_category_school_dictionary.keys():
                area_category_school_dictionary[given_type_shool_area] = 0
                
                
        return user_choose_school_category,dict(sorted(area_category_school_dictionary.items()))

    except TypeError:
        print ('School object was not generated successfully, it is not iterable')
        return

def construct_housing_info(housing_name,status,area):
    '''
    function construct_housing_info parse data lists into objects from class Housing
    parameter: 3 lists returned in clean_nonmarkg_fileet_housin(file_nonmarket_housing):
    return a list of Housing objects
    raise: TypeError if the index s over each list isn't an integer
    '''
    
    housing_list = []

    try:
        for i in range(len(housing_name)):
            instance = Housing(housing_name[i],status[i],area[i])
#            instance = Housing(housing_name['asdfa'],status[i],area[i])  #error testing row
            housing_list.append(instance)

        return housing_list

    except TypeError:
        print ('Index in range must be integers')
        return

def housing_area_dictionary(housing_list):
    '''
    function housing_area_dictionary construct a dictionary where key is non-market housing area, 
    and value is # of non-market housing in that area
    parameter: non-market housing list that integrates all objects generated from class Housing
    return dictionary 
    raise: TypeError if housing list constructed from class Housing was not successful 
    '''
    
    area_dictionary_housing = {}

    try:
        for house_object in housing_list:
            if house_object.housing_area == '':
                pass
            
            elif house_object.housing_area not in area_dictionary_housing:
                area_dictionary_housing[house_object.housing_area] = 1
            
            else:
                area_dictionary_housing[house_object.housing_area] = area_dictionary_housing[house_object.housing_area] +1
        else:
            pass
        return area_dictionary_housing

    except TypeError:
        print ('Housing object was not generated successfully, it is not iterable')
        return

def ratio_housing_school(area_school_dictionary,area_public_housing_dictionary):
    '''
    function ratio_housing_school function links school and housing dictionaries, and constructs:
    a list of areas that have either public schools or public housing, or both; And
    a list of how many # schools are in each area, and 
    a list of how many # public housing are in each area, and 
    a list calculates public schools/public housing ratios by area,
    and 2 dictionaries:
    the areas have public housing, but no public school,
    the areas have public schools, but no public housing

    parameter: 2 dictionaries (school & housing)
    return 4 lists and 2 dictionaries

    raise: AttributeError if either housing/school dictionary was not passed apropriately
    '''

    area_list = []
    ratio_list = []
    num_school_list = []
    num_housing_list = []

    area_has_public_shool_no_housing = {}
    area_has_public_housing_no_public_school = {}

    try:
        for area_school,value_school in area_school_dictionary.items():
            if area_school not in area_public_housing_dictionary.keys(): #construct area_has_public_shool_no_housing dictionary
    #           value_school = 0   ### check why Shaughnessy not in the list
                area_has_public_shool_no_housing[area_school] = value_school
                area_list.append(area_school)
                ratio_list.append(0)
                num_school_list.append(value_school)
                num_housing_list.append(0)
            

            else:
                for area_housing,value_housing in area_public_housing_dictionary.items():
                    if area_housing not in area_school_dictionary.keys():
    #                    value_housing = 0  ### check why Shaughnessy not in the list
                        area_has_public_housing_no_public_school[area_housing] = value_housing
                    elif area_school == area_housing:
    #                   ratio_dictionary[area_school] = [round((value_school/value_housing),2),value_school,value_housing]
                        area_list.append(area_school)
                        ratio_list.append(round((value_school/value_housing),2))
                        num_school_list.append(value_school)
                        num_housing_list.append(value_housing)

            #some area has public schools but no public housing : Shaughnessy
            #print(area_list,'\n',len(area_list),ratio_list,'\n',len(ratio_list),'\n',num_school_list,'\n',len(num_school_list),'\n',num_housing_list,len(num_housing_list))
                        if len(area_list) != len(ratio_list) != num_school_list != len(num_school_list)!= len(num_housing_list):
                            raise ValueError (f"Something is wrong with data list, can't construct ratio dictionary!")
        
        return area_list,ratio_list,num_school_list,num_housing_list,area_has_public_shool_no_housing,area_has_public_housing_no_public_school

    except AttributeError:
        print ('A dictionary was not successfully constructed!')
        return

def data_analysis(dataframe_headers,school_data_frame):
    '''
    function data_analysis analyzes the min and max % of #school/# of housing 
    parameters: sorted data frame
    return:integers,strings 
    raise TypeError if data frame is invalid or didn't constructed successfully
    raise KeyError is sorting criteria (column name) is not available 
    '''

    try:
        print (dataframe_headers[1])
        min_ratio = school_data_frame[dataframe_headers[1]].min()
        min_ratio_area = school_data_frame[DATA_FRAME_HEADERS_AREA].iloc[0]

        max_ratio = school_data_frame[dataframe_headers[1]].max()
        max_ratio_area = school_data_frame[DATA_FRAME_HEADERS_AREA].iloc[-1]

        average_ratio = round(school_data_frame[dataframe_headers[1]].mean(),ROUND_DIGITS)

    except TypeError:
        print ('Data frame can not be sorted because array was not constructed properly!')
        return 
    except KeyError:
        print ('Look up key is not found!')
        return 
    except NameError:
        print ('Parameter names is not defined!')
        return

    return min_ratio,min_ratio_area,max_ratio,max_ratio_area, average_ratio

def print_results(user_choose_school_type,sorted_display_dataframe,min_ratio,min_ratio_area,max_ratio,max_ratio_area, average_ratio,public_shool_no_housing_dictionary,public_housing_no_public_school_dictionary):
    '''
    function print_results displaying results
    parameters: dataframe, variable, string
    return:none
    '''
    try:

        print ("\n","-------"*5)
        print (f"The ratio of public housing to {user_choose_school_type} in Vancouver is shown below in ascending order:")
        print (sorted_display_dataframe)

        if user_choose_school_type == "Public School":

            for area,num in public_shool_no_housing_dictionary.items():
                print ("\n","-------"*5)
                print(area,"has",num,"public schools, but no public housing")

            for area,num in public_housing_no_public_school_dictionary.items():
                if area == '':
                    pass
                else:
                    print ("\n")
                    print(area,"has",num,"public housings, but no public school")

        print ("-------"*5)
        print (min_ratio_area,f"has the lowest ratio of {user_choose_school_type} to public housing at",min_ratio)
        print (max_ratio_area,f"has the highest ratio of  {user_choose_school_type} to public housing at", max_ratio,)
        print (f"The average ratio of {user_choose_school_type} to public housing is:", average_ratio)
        print ("-------"*5)

    except NameError:
        print ('Parameter names is not defined!')
        return







