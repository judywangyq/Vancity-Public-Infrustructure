'''
Judy Wang
Fall 2022 CS5001
Final Project Milstone 1 Class School
'''

class School:
    '''
    create a class School, take 3 attributes, school_name,school_category,school_area
    all three attributes should be str, otherwise raise ValueError
    '''

    def __init__(self,school_name,school_category,school_area):
        '''
        create a class School, takes 3 parameters school_name,school_category,school_area
        all should be string, and school_category should be either "Public School","Independent School" or "StrongStart BC", otherwise raise ValueError
        '''

        self.name = "School"

        if type(school_name) != str and type(school_category) != str and type(school_name) != str:
            raise ValueError ('School input should be string')

        if school_category != "Public School" and school_category != "Independent School" and school_category != "StrongStart BC" :
            raise ValueError ('School type is not valid')
        
        self.school_name = school_name
        self.school_category = school_category
        self.school_area = school_area

    def __str__(self):
        '''
        Returns a description of school name, area and caregory in string
        '''
        output = self.name +' ' + str(self.school_area) +' ' + str(self.school_category)
        return output

    def __eq__(self, other): 
        '''
        Compares a school object to another, if they have same name, and in the same area, they're equal
        Returns True, return False otherwise
        '''
        if self.name != other.name:
            raise AttributeError ('the comparasion should between School and School!')
        
        return (self.school_area == other.school_area and self.school_name == other.school_name)
