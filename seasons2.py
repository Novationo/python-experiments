month = str(input())
day = int(input())
days = 0

# List of valid months
valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if month in valid_months:
    if day > 0 and day <= 31:
        # 31 days
        if month in ["January", "March", "May", "July", "August", "October", "December"]:
            if month == "January":
                days = 0 + day
            elif month == "March":
                days = 59 + day
            elif month == "May":
                days = 120 + day
            elif month == "July":
                days = 181 + day
            elif month == "August":
                days = 212 + day
            elif month == "October":
                days = 273 + day
            elif month == "December":
                days = 334 + day
        
        # 30 days
        elif month in ["April", "June", "September", "November"]:
            if day > 0 and day <= 30:
                if month == "April":
                    days = 90 + day
                elif month == "June":
                    days = 151 + day
                elif month == "September":
                    days = 243 + day
                elif month == "November":
                    days = 304 + day
            
        
        # february
        elif month == "February":
            if day > 0 and day <= 28:
                days = 31 + day
            else:
                print("Invalid")
        
        # season
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