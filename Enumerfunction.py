days = "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
for enum_days in enumerate(days,1):
    print(enum_days)
for count,enum_days in enumerate(days,1):
    print(count,enum_days)

names = "Riya","Prachi","Anjali","Neha","Preeti","Garima","Priyanshi"
for index, girls in enumerate(names):
    if index%2 == 0:
        print(girls)


