import time
if time.strftime("%H") == "00":
    print("6:30")
if time.strftime("%H") == "02":
    print("8:30")
if time.strftime("%H") == "04":
    print("10:30")
if time.strftime("%H") == "08":
    print("12:30")
if time.strftime("%H") == "10":
    print("2:30")
if time.strftime("%H") == "12":
    print("4:30")
if time.strftime("%H") == "14":
    print("6:30")
if time.strftime("%H") == "16":
    print("8:30")


time_check = True
while time_check:
    if time.strftime("%H%M") == "1316":
        time_check = False
print("loop has been exited")
