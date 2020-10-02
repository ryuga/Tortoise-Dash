import json


def read_data():
    with open("logindata.txt", "r") as myfile:
        return json.loads(myfile.read())


def valuate_credentials(username, password):
    data = read_data()
    if username in data:
        if data[username] == password:
            return True
    return False


def write_data(data):
    with open("logindata.txt", "w") as myfile:
        myfile.write(json.dumps(data, indent=4, sort_keys=True))


def add_data(username, password):
    data = read_data()
    data[username] = password
    write_data(data)
    return data
