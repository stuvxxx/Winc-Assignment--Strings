# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality
    }
    return passport


def add_stamp(passport, country):
    if country in passport["nationality"]:
        return passport
    else: 
        if "stamps" in passport:
            if country in passport["stamps"]:
                return passport
            else: 
                passport["stamps"].append(country)
                return passport
        else:
            passport["stamps"] = [country]
            return passport

def add_biometric_data(passport, bioname, values, date):
    d = {
        bioname: {
            "date": date,
            "value": values
        }
    }
    if "biometric" in passport:
        if bioname in passport["biometric"]:
            passport["biometric"][bioname]["date"] = date
            passport["biometric"][bioname]["value"] = values
            return passport
        else:
            passport["biometric"][bioname] = {
                "date": date,
                "value": values
            }
            return passport
    else: 
        passport["biometric"] = d
        return passport




