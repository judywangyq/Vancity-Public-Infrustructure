'''
Judy Wang
Fall 2022 CS5001
Final Project Milstone 1 Class Housing
'''

class Housing:
    '''
    create a class Housing, take 3 attributes, house_name,house_status,and house_area
    all three attributes should be str, otherwise raise ValueError
    '''

    def __init__(self,house_name,house_status,house_area):
        '''
        create a class for non-marketing Housing, takes 3 parameters house_name,house_status,house_area
        all should be string, and house_status should be within "Completed","Approved","Proposed" or "Under Construction", otherwise raise ValueError
        '''

        self.name = "Non-Market Housing"

        if type(house_name) != str and type(house_status) != str and type(house_area) != str:
            raise ValueError ('Non-Market Housing input should be string')

        if house_status != "Completed" and house_status != "Approved" and house_status != "Proposed" and house_status != "Under Construction" :
            raise ValueError ('School type is not valid')

        self.housing_name = house_name
        self.housing_status = house_status
        self.housing_area = house_area

    def __str__(self):
        '''
        Returns a description of non-market housing name, area and status in string
        '''
        output = self.name + "in area" + str(self.housing_area) + "and it's " + str(self.housing_status)
        return output

    def __eq__(self, other): 
        '''
        Compares a housing object to another, if they have same name, and in the same area, they're equal
        Returns True, return False otherwise
        '''
        if self.name != other.name:
            raise AttributeError ('the comparasion should between Housing and Housing!')
        
        return (self.housing_area == other.housing_area and self.housing_area == other.housing_area)
