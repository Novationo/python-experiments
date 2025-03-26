month = str(input())
day = int(input())

if month == "January" or "February" or "March" or "April" or "May" or "June" or "July" or "August" or "September" or "October" or "November" or "December":
    if day > 0 and day <= 31:
        if month == "January":
            days = 0 + day
        elif month == "February":
            days = 32 + day
        elif month == "March":
            days = 60 + day
        elif month == "April":
            days = 91 + day
        elif month == "May":
            days = 121 + day
        elif month == "June":
            days = 152 + day
        elif month == "July":
            days = 182 + day
        elif month == "August":
            days = 213 + day
        elif month == "September":
            days = 244 + day
        elif month == "October":
            days = 274 + day
        elif month == "November":
            days = 305 + day
        elif month == "December":
            days = 335 + day
        if 79 <= days <= 171:
            season = "Spring"
        elif 172 <= days <= 264: 
            season = "Summer"
        elif 265 <= days <= 354:
            season = "Autumn"
        elif (355 <= days <= 365) or (1 <= days <= 78):  
            season = "Winter"
        else:
            season = "Invalid"

        print(season)
    else:
        print("Invalid")
else:
    print("Invalid")

try:
    print(season)
except:
    print("Invalid")

'''
months in total days:
january = 0 - 31
february = 32 - 59
march = 60 - 90
april = 91 - 120
may = 121 - 151
june = 152 - 181
july = 182 - 212
august = 213 - 243
september = 244 - 273
october = 274 - 304
november = 305 - 334
december = 335 - 365

day range of seasons:
spring = 70 - 161 
summer = 162 - 252
autumn = 253 - 345
winter = 346 - 69
'''