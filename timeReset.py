import time

new_file = ""

with open("restricted.txt") as file:

    users = file.readlines()
    for i in users:
        final_string = ""
        i = i.rstrip()
        words = i.split(" ")

        if words[3] == time.strftime("%H%M"):
            words[3] = "1"

            for f in words:
                final_string += f + " "
            i = final_string.rstrip()

        new_file += i + "\n"

file = open("restricted.txt", "w")
file.write(new_file)
