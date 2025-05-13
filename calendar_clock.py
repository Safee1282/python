# from datetime import date , time , datetime

# today=date.today()
# now=datetime.now()
# print("Today's date is ",today)
# print("\nCurrent Date and time is ",now)
# print("\nDate components",today.year , today.month , today.day)


# import random 
# import time
# def getrandomdate(startdate , endate):
#     print("printing random date bw ",startdate, "and",endate )
#     randomGenerator=random.random()
#     dateformat= '%d/%m/%y'

#     starttime=time.mktime(time.strptime(startdate , dateformat))
#     endtime=time.mktime(time.strptime(endate , dateformat))
    
    
    
#     randomtime = starttime + randomGenerator * (endtime - starttime)
#     randomdate = time.strftime( dateformat , time.localtime(randomtime)) 
#     return randomdate

# print("Random Date = " , getrandomdate("1/1/2010","12/12/2015"))

import calendar
yy=2013
mm=2
print(calendar.month)