def isYearLeap(year):
    if year%4 == 0:
        if year % 100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInMonth(year, month):
    if 1 <= month <= 7:
        
        if month == 2:
            if isYearLeap(year):
                return 29
            else:
                return 28
        elif month % 2 == 0:
            return 30
        else:
            return 31
        
    elif 8 <= month <=12:
        
        if month % 2 == 0:
            return 31
        else:
            return 30
        
    else:
        return None
        
        
def dayOfYear(year, month, day):
    DOY = 0
    if day <= daysInMonth(year, month):
        DOY += day
    else:
        return None
        
    for m in range(1,month):
        DOY += daysInMonth(year, m)
    
    return DOY

print(dayOfYear(2000, 12, 31))
