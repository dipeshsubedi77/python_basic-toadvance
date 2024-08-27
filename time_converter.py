total_seconds =int(input("enter a number of seconds:"))
hours = total_seconds /3600
minutes = (total_seconds //60) % 60
seconds = total_seconds % 60
print("here is the time:",hours,minutes,seconds)
