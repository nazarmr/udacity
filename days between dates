daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonths2 =[ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isLeapYear(year): 
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    
    if ((year%400 ==0 ) or ((year%4 == 0)and (year%100 !=0))):
        return True
    else:
        return False
 


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    result1 = 0
    result2 = 0
    nb_of_days_in_m1 = 0
    nb_of_days_in_m2 = 0
    for c in range(y1) :
        if isLeapYear(c) == True:
            result1 = result1 + 366
        else :
            result1 = result1 + 365
    for d in range(y2):
        if isLeapYear(d) == True :
            result2 = result2 + 366
        else:
            result2 = result2 +365
    if isLeapYear(y1) == True:
        x = daysOfMonths2[:m1]
        nb_of_days_in_m1 = sum(x)
    else :
        x = daysOfMonths[:m1]
        nb_of_days_in_m1 = sum(x)
        
        
    if isLeapYear(y2) == True:
        y = daysOfMonths2[:m2]
        nb_of_days_in_m2 = sum(y)
    else: 
        y = daysOfMonths[:m2]
        nb_of_days_in_m2 = sum(y)
        pass
        
    total_of_first = result1 + nb_of_days_in_m1 + d1
    total_of_second = result2 + nb_of_days_in_m2 + d2
    days = total_of_second - total_of_first
    print  result1 
    print nb_of_days_in_m1
    print  result2 
    print nb_of_days_in_m2
    
    return days
