from flask import make_response, abort
from config import db
from models import Person, PersonSchema


def read_all(): 
    """
    This function responds to a request for 
    /api/people with the complete lists of people.
    
    :return:        json string of list of people
    """
    # get the list of people
    people = Person.query.order_by(Person.lname).all()
    # serialize data for json response(incl. converting timestamp to string)
    person_schema = PersonSchema(many=True)
    return person_schema.dump(people).data


def read_one(person_id):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people

    :param person_id: ID of person to find
    :return:          person matching ID
    """
    # search for person in the db
    person = Person.query.filter(Person.person_id == person_id).one_or_none()
    if person is not None:
        # serialize person's data
        person_schema = PersonSchema()
        return person_schema.dump(person).data
    else:
        abort(
            404,
            f"Person with ID {person_id} is not in the database."
        )


def add_one(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 409 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    # check if the person already exists in db
    person = Person.query.filter(Person.lname == lname).filter(Person.fname == fname).one_or_none()
    if person is not None:
        # deserialize json data into db object
        person_schema = PersonSchema()
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)  # add new person to session
        db.session.commit()  # commit session changes to db
        # serialize and return the new person
        return person_schema.dump(new_person).data, 201
    else:
        abort(
            409,
            f"Person with the name {lname} {fname} already exists in the db."
        )


def update_one(person_id, person):
    """
    This function updates an existing person in the people structure
    :param person_id:   ID of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    # search person with person_id in db
    person = Person.query.filter(Person.person_id == person_id).one_or_none()
    if person is None:
        abort(
            404,
            f"Person with the ID {person_id} is not in the db."
        )
    else:
        # check if person with new name already exists in db
        update_person = Person.query.filter(Person.lname == lname).filter(Person.fname == fname).one_or_none()
        if update_person is not None and update_person.person_id != person_id:
            abort(
                404,
                f"Person with the name {lname} {fname} already exists in the db."
            )
        else:  # person's record can be updated
            # deserialize data from the request into db object
            person_schema = PersonSchema()
            # create a new person record
            new_person = person_schema.load(person, session=db.session).data
            # set ID of the new record
            new_person.person_id = person_id
            # to update a person, run merge: it will merge the state of
            # new (new_person) and old (person) objects with same ID
            db.session.merge(new_person)
            db.session.commit()
            # return the updated person's record
            return person_schema.dump(new_person).data, 200


def delete_one(person_id):
    """
    This function deletes a person from the people structure
    :param person_id:   ID of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # search for the requested person
    person = Person.query.filter(Person.person_id == person_id).one_or_none()
    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return make_response(
            f"Person {person_id} deleted", 200
        )
    else:
        abort(
            404,
            f"Person with the ID {person_id} is not in the db."
        )
