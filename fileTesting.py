import os


class Users:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


with open("restricted.txt") as file:
    user_list = []
    inputs = file.readlines()
    count = 0
    for i in inputs:
        temp_list = i.split(" ")
        user = temp_list[0].strip()
        user_username = temp_list[1].strip()
        user_password = temp_list[2].strip()
        user_list.append(Users(user, user_password, user_username))

    for user in user_list:
        print(user.name)


