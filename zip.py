# zip(*itterables) aggregates 2 or more itterables into a single zip object
# zip object stores every group as a tuple
# it can be cast to dict or list

usernames = ["Dude", "Bro", "Mister"]
passwords = ["Password", "ABC123", "guest"]
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = list(zip(usernames, passwords, login_date))
for i in users:
    print(i)


