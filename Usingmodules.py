#Play localfile.mp3 using playsound module(External module used)
# from playsound import playsound
# playsound(r"C:\Users\Riya Tiwari\Music\MaBelle.mp3")
# print('playing sound using  playsound')

# Find out the day of your birthdate in current year(Built-in module used)
import datetime
print("Find out the day of your birthdate in current year.")
date_entry = input('Enter your current year birth date in DD-MM-YYYY format\n')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(day, month, year)
print(date1.strftime("%A"))






