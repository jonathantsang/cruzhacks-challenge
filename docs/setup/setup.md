# Setting up your environment to use this project

## Last updated March 5th, 2019 at 10:17 PM

### Setup

- Install PostgreSQL ( <https://www.postgresql.org/download> ) 
- Install python and pip ( <https://www.python.org/downloads> )
  - NOTE: This project was built using Python 3.7.0. Future or older versions may have side effects.
- Install requirements from requirements.txt
  - ```pip install --no-cache-dir -r requirements.txt```
- Create a database, title it whatever you want. 
  - I called mine "cruzhacks".
  - The name doesn't matter, just put it into appsettings.development.ini in the "dbname" section.
- Update appsettings.development.ini with your machine-specific details, using appsettings.template.ini as a guide in database/cfg/
- set cwd to /database/ and run setup.py (this will create the proper tables in your database).
- If at some point you want to add new scripts, add them to the end of the /database/queries.txt in one line.