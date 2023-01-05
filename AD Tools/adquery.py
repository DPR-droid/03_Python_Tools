# Pythonic interface to Active Directory
# https://pypi.org/project/pyad/


from pyad import *
from pyad.pyadutils import *
import datetime
user = pyad.aduser.ADUser.from_cn('MEEE')
expirationdate=pyad.pyadutils.convert_datetime(user.get_attribute('accountExpires', False))
print(expirationdate)