from . import UserProfileQueries as queries
import uuid
import psycopg2
from configparser import ConfigParser

conf = ConfigParser()
conf.read('database/cfg/appsettings.development.ini')

dbname = conf.get('login', 'dbname')
user = conf.get('login', 'user')
password = conf.get('login', 'password')

class UserProfileHandler:

    def __init__(self):
        self.conn = psycopg2.connect(database=dbname, user=user, password=password)
        self.cursor = self.conn.cursor()

    def get(self, id):
        query = queries.get
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()

        return result

    def insert(self, profile):
        # generate new guid
        new_guid = str(uuid.uuid4())

        query = queries.insert
        data = (new_guid, profile.UserTypeCode, profile.Name, profile.School, profile.Major, profile.Street1, profile.Street2, profile.City, profile.StateCode, profile.ZipCode, profile.CountryCode, profile.Phone, profile.Email, profile.BirthDate, profile.ProfileImageUrl)

        self.cursor.execute(query, data)
        self.conn.commit()

    def update(self, profile):
        query = queries.update
        data = (profile.UserTypeCode, profile.Name, profile.School, profile.Major, profile.Street1, profile.Street2, profile.City, profile.StateCode, profile.ZipCode, profile.CountryCode, profile.Phone, profile.Email, profile.BirthDate, profile.ProfileImageUrl, profile.UserProfileId)

        self.cursor.execute(query, data)
        self.conn.commit()

    def delete(self, id):
        query = queries.delete

        self.cursor.execute(query, (id,))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()