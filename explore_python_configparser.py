import configparser

config = configparser.ConfigParser()

config.read('credentials.ini')

credentials = config['admin']

print(credentials['user'])
print(credentials['password'])