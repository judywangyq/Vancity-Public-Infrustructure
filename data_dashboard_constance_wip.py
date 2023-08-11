'''
Judy Wang
Fall 2022 CS5001
Final Project Milstone 2
Constance file
'''
#Valid links
SCHOOL_CSV_URL = 'https://opendata.vancouver.ca/explore/dataset/schools/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B'
NON_MARKET_HOUSING_CSV_URL = 'https://opendata.vancouver.ca/explore/dataset/non-market-housing/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B'

#Invalid links
#SCHOOL_CSV_URL = 'https://opendata.vanc.ca/explore/dataset/schools/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B'
#NON_MARKET_HOUSING_CSV_URL = 'https://opendata.vancouver.caet/non-market-housing/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B'


SCHOOL_CATEGORY_INDEX = 1
SCHOOL_NAME_INDEX = 2
SCHOOL_AREA_INDEX = -1
FILE_SCHOOL_STARTING_CHARA = 57
FILE_SCHOOL_ENDING_CHARA = -1
FILE_SCHOOL_ROW_SPLITER = '\n'
EACH_SCHOOL_ATTIBUTE_SPLITER = ';'
SCHOOL_AREA_STRIP_DELIMITER = '\r'

PUBLIC_HOUSING_NAME_INDEX = 1
PUBLIC_HOUSING_STATUS_INDEX = 3
PUBLIC_HOUSING_AREA_INDEX = -3
FILE_NONPUBLIC_HOUSING_STARTING_CHARA = 520
FILE_NONPUBLIC_HOUSING_ENDING_CHARA = -1
FILE_NONPUBLIC_HOUSING_ROW_SPLITER = '\n'
FILE_NONPUBLIC_HOUSING_ATTIBUTE_SPLITER = ';'

CHOOSE_SCHOOL_CATEGORY_PUBLIC = "Public School"
CHOOSE_SCHOOL_CATEGORY_PRIVATE = "Independent School" #next step to prompt user input
CHOOSE_SCHOOL_CATEGORY_STRONGBC = "StrongStart BC"
CHOOSE_ALL_SCHOOLS = "Public School"

DATA_FRAME_HEADERS_AREA = 'Area'
DATA_FRAME_HEADERS_RATIO = 'Rate of School / Public Housing'
DATA_FRAME_HEADERS_NUM_OF_SCHOOL = '# of Public Schools'
DATA_FRAME_HEADERS_NUM_OF_HOUSING = '# of Public Housing'
DATA_FRAME_HEADERS = (DATA_FRAME_HEADERS_AREA,DATA_FRAME_HEADERS_RATIO,DATA_FRAME_HEADERS_NUM_OF_SCHOOL,DATA_FRAME_HEADERS_NUM_OF_HOUSING)

ROUND_DIGITS = 2

DATA_FRAME_HEADERS_SCHOOL_FACTS = (DATA_FRAME_HEADERS_AREA,DATA_FRAME_HEADERS_NUM_OF_SCHOOL)



