# -*- coding: utf-8 -*-


#A break down (Total analysis) of the functions responsible for the 
#conversion of weight of certain qty(Quantity) from one to other forms of  
#fundamental units.
 

def kilo_to_pounds():
    """ Converts weights from kilograms to pounds  """
    
    print('''\nCONVERSION FROM KILOGRAMS TO POUNDS IN (L)bs ''')
    try:
        weight  = float(input("enter weight: "))
        conversion = weight * 0.00224    
        print('\n\tCONVERSION:',conversion,"lbs")
    except ValueError:
        print("invalid literal:  for int() with base 10")
        

def pounds_to_kilo():
    """ Converts weights from pounds to kilograms  """
    
    print("""\nCONVERSION FROM POUNDS TO KILOGRAMS IN [K]g """)
    try:
        weight  = int(input("enter weight: "))
        conversion = weight / 0.00224    
        print('\tCONVERSION:',conversion,"kg")
    except ValueError:
        print("invalid literal:  for int() with base 10")
        
    
def gram_to_kilo(): 
    """ Converts weights from grams to kilograms  """
    
    print('''\nCONVERSION FROM GRAMS TO KILOGRAMS IN [K]g ''')
    try:        
        weight  = int(input("enter weight: "))
        conversion = weight / 1000  
        print('\tCONVERSION:', conversion,"kg")
    except ValueError:
        print("invalid literal:  for int() with base 10")
        

def kilo_to_gram():
    """ Converts weights from kilograms to grams  """
    
    print('''\nCONVERSION FROM KILOGRAMS TO GRAMS [g] ''')
    try:
        weight  = float(input("enter weight: "))
        conversion = weight * 1000  
        print("\n\tCONVERSION:", round(conversion),'g')
    except ValueError:
        print("invalid literal:  for int() with base 10")
    
    
def pounds_to_gram():
    """ Converts weights from pounds to grams  """
    
    print('''\nCONVERSION FROM POUNDS TO GRAMS [g] ''')
    try:
        weight  = float(input("enter weight: "))
        conversion = weight * 2.24
        print('\n\tCONVERSION:', round(conversion),"g")
        
    except ValueError:
        print("invalid literal:  for int() with base 10")
    

def grams_to_pounds():
    """ Converts weights from grams to pounds  """
    
    print('''\nCONVERSION FROM GRAMS TO POUNDS [L]bs ''')
    try:
        
        weight  = int(input("enter weight: ")) 
        conversion = weight / 2.24 
        print('\n\tCONVERSION: ',conversion,"lbs")
    except ValueError:
        print("invalid literal:  for int() with base 10")

