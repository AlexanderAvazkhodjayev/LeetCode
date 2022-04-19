
def timeConversion(s):
    militaryHour = ""

    hour = s.split(":",1)
    print(hour)
    print(s[-2:])
    if int(hour[0]) == 12:
        militaryHour = "00"
        print(militaryHour)
    else:    
        militaryHour = str(int(hour[0]) + 12)
    militaryHour += ":" + hour[1]
    print(militaryHour)
    newString = militaryHour[:-2]
    print(newString)
    
timeConversion("04:59:59AM")