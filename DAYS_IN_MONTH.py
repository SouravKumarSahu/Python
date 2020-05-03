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


testYears = [1900, 2000, 2016, 1987, 2020]
testMonths = [2, 2, 1, 11, 13]
testResults = [28, 29, 31, 30, None]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
