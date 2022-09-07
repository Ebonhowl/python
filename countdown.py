from datetime import date
d0 = date.today()
d1 = date(2022,10,20)
delta = d1 - d0
print("There are", delta.days, "days until your holiday!")