import psycopg2
from configparser import ConfigParser

conf = ConfigParser()
conf.read('cfg/appsettings.development.ini')

dbname = conf.get('login', 'dbname')
user = conf.get('login', 'user')
password = conf.get('login', 'password')

conn = psycopg2.connect(database=dbname, user=user, password=password)
cursor = conn.cursor()

with open('queries.txt') as file:
    for line in file:
        line = line.strip()
        if not line or line == "" or line[0] == '#':
            continue
        try:
            cursor.execute(line)
            conn.commit()
        except psycopg2.ProgrammingError:
            print("query already executed before, skipping")

print("OK")