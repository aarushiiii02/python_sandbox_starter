# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#core module
import datetime
from datetime import date
import email
import time
from time import time 
#pip module
#from camelcase import camelcase
#import custom module
import validator
from validator import validate_email
#today = datetime.date.today()
#today =  date.today()
#timestamp = time.time()
# timestamp = time()
# c =  camelcase()
# print(c.hump('hello there world'))
email = 'test@test.com'
if validate_email(email):
    print('emailis valid')
else:
    print ('email is bad')
# print(timestamp)


