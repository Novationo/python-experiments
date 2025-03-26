month = str(input())
day = int(input())
# if month == "January":
#     month = 1
# if month == "February":
#     month = 2

if month == "January" or "February" or "March" or "April" or "May" or "June" or "July" or "August" or "September" or "October" or "November" or "December":
    if day > 0 and day < 31:
        if month == "January":
            days = 31 - day
        elif month == "February":
            days = 59 - day
        elif month == "March":
            days = 90 - day
        elif month == "April":
            days = 120 - day
        elif month == "May":
            days = 151 - day
        elif month == "June":
            days = 181 - day
        elif month == "July":
            days = 212 - day
        elif month == "August":
            days = 243 - day
        elif month == "September":
            days = 273 - day

    else:
        print("Invalid")
else:
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



if days >= 70 and days <= 161:
    season = "spring"
if days >= 162 and days <= 252:
    season = "summer"
if days >= 253 and days <= 345:
    season = "autumn"
if days > 0 and days <= 69 and days >= 346 and days <= 365:
    season = "winter"

print(days, season)