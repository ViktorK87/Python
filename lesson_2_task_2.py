print("Введите год")
year = int(input())

def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
    

var = is_year_leap(2009)   
print("год ",  year , ":" , var)

