# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type

from csv import DictReader
import requests

PEOPLE_CSV_FILE = "people.csv"
API_URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={}"


def read_csv(filename: str) -> list[dict]:
    """Function to read a csv with the given filename to a list of dicts."""
    with open(filename, 'r', encoding='utf-8') as file:
        return list(DictReader(file))


def get_nearest_courts_from_API(postcode: str) -> list[dict]:
    """
    Returns list of dicts of nearest courts to a given postcode from courts and tribunals finder
    API; if error in getting data from API, an empty list is returned.
    """
    response = requests.get(API_URL.format(postcode))
    if response.status_code != 200:
        return []
    return response.json()


def format_court_data(type: str, courts: list[dict]):
    """
    Removes any courts which do not have the desired type, and leaves only the fields name,
    dx_number and distance for each court dictionary.
    """
    courts_to_remove = []
    for i, court in enumerate(courts):
        if (type not in court.get("types", [])) or (court.get("distance", None) is None):
            courts_to_remove.append(court)
        else:
            courts[i] = {
                "name": court.get("name", ""),
                "dx_number": court.get("dx_number", ""),
                "distance": court['distance']
            }
    for court in courts_to_remove:
        courts.remove(court)



if __name__ == "__main__":
    people = read_csv(PEOPLE_CSV_FILE)
    for person in people:
        nearest_courts = get_nearest_courts_from_API(person['home_postcode'])
        format_court_data(person['looking_for_court_type'], nearest_courts)
        person['nearest_court'] = nearest_courts[0]
    
    for person in people:
        print(person)