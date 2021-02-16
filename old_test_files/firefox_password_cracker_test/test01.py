

with open("logins.json", "r") as f:
    content = f.read()

x = content.split('hostname":"')
print(content)

# content = content.replace(',"guid":"{c', " ")
# content = content.replace("07a3aa7-ae'", " ")

website_list = []

for i in range(len(x)):
    list_item = x[i]
    cop_string = x[i].find('"')
    only_url = list_item[:cop_string]

    website_list.append(only_url)

    # print(x[i])
    # print(only_url)


website_list.remove("{")
print(website_list)

##### Usernames #####

u = content.split('encryptedUsername":"')
username_list = []


for i in range(len(u)):
    list_item = u[i]
    cop_string = u[i].find('"')
    only_user = list_item[:cop_string]

    username_list.append(only_user)

    # # print(x[i])
    # print(only_user)

username_list.remove("{")
print(username_list)

##### Passwords #####


p = content.split('encryptedPassword":"')
password_list = []


for i in range(len(p)):
    list_item = p[i]
    cop_string = u[i].find('"')
    only_pswd = list_item[:cop_string]

    password_list.append(only_pswd)

    # # print(p[i])
    print(only_pswd)

password_list.remove("{")
# password_list = password_list[0].replace(',"guid":"{c"', "")
#password_list.remove(password_list[3])
print(password_list)