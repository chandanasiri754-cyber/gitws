import getpass
d={"Siri": "2006", "Tarini": "2009", "Hema": "1982", "Gautham": "1975"}
username = input("Enter your username: ")
if username in d:
    password = getpass.getpass("Enter your password: ")