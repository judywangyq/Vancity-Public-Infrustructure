'''
Judy Wang
Fall 2022 CS5001
Final Project Milstone 1 
Driver file
'''

from data_dashboard_functions_wip import *
from data_dashboard_constance_wip import *
from data_dashboard_view_wip import *
from data_dashboard_input_wip import *
import numpy as np
import pandas 

    
def main():

    try:
        school_file_download = download_file(SCHOOL_CSV_URL)
        school_name,school_category,school_area = clean_school_file(school_file_download)

        housing_file_download = download_file(NON_MARKET_HOUSING_CSV_URL)
        non_market_housing_name,non_market_housing_status,non_market_housing_area = clean_nonmarket_housing(housing_file_download)
        
        school_list = construct_school_info(school_name,school_category,school_area)

        housing_list = construct_housing_info(non_market_housing_name,non_market_housing_status,non_market_housing_area)
        housing_dictionary = housing_area_dictionary(housing_list)

        starting_question = 0
        starting_with = False

        while starting_with == False:
            
            starting_question = str(input("Are you looking for facts or analysis?, type 'f' for facts or 'a' for analysis" '\n'))
            if starting_question == "f" or starting_question == "a":
                starting_with = True
            else:
                print ("Oops we don;t have that analysis, please choose again:"'\n')
 
                
        user_choice = loop_input()

        starting_choice = ''

        while starting_choice !="b":
            
            if starting_question  == 'f':

                user_choose_school_type,user_choose_school_dictionary = school_area_category_dictionary(school_list,user_choice)
                area_list,ratio_list,num_school_list,num_housing_list,area_has_public_shool_no_housing,area_has_public_housing_no_public_school = ratio_housing_school(user_choose_school_dictionary,housing_dictionary)

                print ('\n','-----'*3,f'User choosed {user_choose_school_type}','-----'*3,'\n')
                print ('\n','-----'*3,f'{user_choose_school_type} Dictionary showing as','-----'*3,'\n', f'{user_choose_school_dictionary}')

        #        make_bar_graph_from_dictionary(user_choose_school_dictionary, f'Graph of {user_choose_school_type}')
                #1 at the end will be used as input
                make_pie_graph_from_dictionary(user_choose_school_dictionary,f'Graph of {user_choose_school_type}')
                user_choice = loop_input()    
                
            if starting_question  == 'a':
                
                user_choose_school_type,user_choose_school_dictionary = school_area_category_dictionary(school_list,user_choice)
                area_list,ratio_list,num_school_list,num_housing_list,area_has_public_shool_no_housing,area_has_public_housing_no_public_school = ratio_housing_school(user_choose_school_dictionary,housing_dictionary)

        #        print (area_list,'\n',ratio_list,'\n',num_school_list,'\n',num_housing_list,'\n',area_has_public_shool_no_housing,'\n',area_has_public_housing_no_public_school)
        #        print (len(area_list),'\n',len(ratio_list),'\n',len(num_school_list),'\n',len(num_housing_list),'\n',len(area_has_public_shool_no_housing),'\n',len(area_has_public_housing_no_public_school))
                dataframe_headers,ratio_dataframe = dispay_ratio_dataframe(user_choose_school_type,area_list,ratio_list,num_school_list,num_housing_list)

                min_ratio,min_ratio_area,max_ratio,max_ratio_area, average_ratio = data_analysis(dataframe_headers,ratio_dataframe)
                print_results(user_choose_school_type,ratio_dataframe,min_ratio,min_ratio_area,max_ratio,max_ratio_area, average_ratio,area_has_public_shool_no_housing,area_has_public_housing_no_public_school)

                make_bar_graph_from_data_frame(ratio_dataframe,area_list, f'Graph of {user_choose_school_type} and Public Housing in Each Area')
                user_choice = loop_input()

            else:
                print ("Oops we don;t have that analysis, please choose again:"'\n')
                user_choice = loop_input()
                
    except ValueError:
        return

    except TypeError:
        return

    except KeyError:
        return

    except NameError:
        return

    except Exception:
        return

    
if __name__ == "__main__":
    main()














