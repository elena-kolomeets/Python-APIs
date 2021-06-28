from datetime import datetime

from flask import make_response, abort

def get_time_stamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# data to serve with the API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_time_stamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_time_stamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_time_stamp()
    }
}


def read_all(): 
    """
    This function responds to a request for 
    /api/people with the complete lists of people.
    
    :return:        json string of list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    if lname in PEOPLE:
       return PEOPLE[lname]
    else:
        abort(
            404,
            f"Person with last name {lname} is not in the list."
        )


def add_one(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "fname": fname, 
            "lname": fname,
            "timestamp": get_time_stamp()
        }
        return make_response(
            f"{lname} successfully added to the list.", 
            201
        )
    else:
        # person's data is already in the list, so abort operation
        abort(
            406,
            f"Person with the last name {lname} is already in the list."
        )


def update_one(lname, person):
    """
    This function updates an existing person in the people structure
    :param lname:   last name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person["fname"]
        PEOPLE[lname]["timestamp"] = get_time_stamp
        return make_response(
            f"Successfully updated {lname}'s data in the people list",
            200
        )
    else:
        abort(
            404,
            f"Person with the last name {lname} is not in the list."
        )


def delete_one(lname):
    """
    This function deletes a person from the people structure
    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"Successfully deleted {lname}'s data in the people list",
            200
        )
    else:
        abort(
            404,
            f"Person with the last name {lname} is not in the list."
        )
