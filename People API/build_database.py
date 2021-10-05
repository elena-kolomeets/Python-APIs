import os
from config import db
from models import Person


# initial data
PEOPLE = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny', 'lname': 'Easter'}
]
# remove db if it exists already
if os.path.exists('people.db'):
    os.remove('people.db')
# create db
db.create_all()
# populate db (session object)
for p in PEOPLE:
    person = Person(lname=p['lname'], fname=p['fname'])
    db.session.add(person)
# save changes from the session
db.session.commit()
