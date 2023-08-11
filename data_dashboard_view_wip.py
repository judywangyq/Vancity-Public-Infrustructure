'''
Judy Wang
Fall 2022 CS5001
Final Project Milstone 2
View file
'''
import matplotlib.pyplot as plt
import pandas 
import numpy as np
from data_dashboard_functions_wip import *
from data_dashboard_constance_wip import *
from data_dashboard_input_wip import *

def make_bar_graph_from_dictionary(dictn1, title):

    plt.bar(range(len(dictn1)), list(dictn1.values()), align='center')
    plt.xticks(range(len(dictn1)), list(dictn1.keys()),rotation=45)
    plt.title(title)

    plt.show()


def make_pie_graph_from_dictionary(dictn2,title):

    dictionary_list = list(dictn2.values())

    y = np.array(dictionary_list)
    pie_labels = list(dictn2.keys())

    plt.pie(y,labels = pie_labels, startangle = 90)
    plt.title(title)

    plt.show()
        


def make_bar_graph_from_data_frame(df1, xticklabels, title):


    figure1, ax1 = plt.subplots()

    df1.plot(x = df1.columns[0], y = [df1.columns[2],df1.columns[3]], kind='bar', legend=True, ax=ax1,color=["green","yellow"])

    ax1.set_xticklabels(xticklabels)
    ax1.set_ylabel('Count', fontsize=14)

    ax2 = ax1.twinx()
    df1.plot(x = df1.columns[0], y = df1.columns[1], kind='line', legend=True, ax=ax2,color="red")
    ax2.set_ylabel('Rates', fontsize=14)

    ax1.set_title(title)
    figure1.autofmt_xdate()
    plt.show()


def dispay_ratio_dataframe(user_choose_school_type,area_list,ratio_list,num_school_list,num_housing_list):
    '''
    function dispay_dataframe construct a dataframe by using pandas
    parameters: 4 lists constructed by combining 2 dictionaries
    return:a sorted data frame
    raise ValueError if the number of columns is not euqal to the number of headers
    '''

    combined_ratio_data = (area_list,ratio_list,num_school_list,num_housing_list)
    dataframe_headers = (DATA_FRAME_HEADERS_AREA,f'Rate of {user_choose_school_type} / Public Housing',f'# of {user_choose_school_type}',DATA_FRAME_HEADERS_NUM_OF_HOUSING)

    if len(combined_ratio_data) != len(dataframe_headers):
        raise ValueError("The number of columns in dataframe must equal to the number of headers!")
    
    else:
        dataframe_dictionary = dict(zip(dataframe_headers,combined_ratio_data))

        try:
            ratio_data_frame = pandas.DataFrame(dataframe_dictionary)
        except ValueError:
            print ('All arrays must be of the same length to construct data frame! Check the length of the lists')
            return 
        
        sorted_display_dataframe = ratio_data_frame.sort_values(dataframe_headers[1])

        return dataframe_headers,sorted_display_dataframe


    

