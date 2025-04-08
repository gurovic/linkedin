"""
Usage:

$ python3 manage.py shell 
Python 3.13.2 (main, Feb  5 2025, 08:05:21) [GCC 14.2.1 20250128]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.32.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from scripts.load_from_json import transfer

In [2]: transfer()
THIS SCRIPT WILL DELETE ALL UNIVERSITIES, MAJORS AND STUDENTS.
Type "Yes, do as I say!" and press Enter in order to continue.
> Yes, do as I say!
"""

transliteration = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "iy",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "sch",
    "ъ": "y",
    "ы": "y",
    "ь": "y",
    "э": "e",
    "ю": "yu",
    "я": "ya"
}

def transliterate(s: str):
    return "".join(list(map(lambda x: transliteration[x] if x in transliteration.keys() else "x", list(s.lower()))))

import json
import logging
import secrets
import os.path
from django.contrib.auth.models import User

from app.models.university import University
from app.models.universitystudent import UniversityStudent
from app.models.school import School, MajorSubject
from app.models.student_schools import StudentSchool

from .country_from_coords import get_country_from_coordinates

universities, alumnis = {}, {}

try:
    f_universities = open("universities.json")
    universities = json.load(f_universities)
    f_universities.close()
except FileNotFoundError:
    logging.error("universities.json not found! please save the file to /web/universities.json")
try:
    f_alumnis = open("alumnus.json")
    alumnis = json.load(f_alumnis)
    f_alumnis.close()
except FileNotFoundError:
    logging.error("alumnus.json not found! please save the file to /web/alumnus.json")

def transfer():
    print("THIS SCRIPT WILL DELETE ALL MAJORS, SCHOOLS AND STUDENTS.")
    print("Additionally, the old password list will be replaced.")
    print("Type \"Yes, do as I say!\" and press Enter in order to continue.")
    if input("> ") != "Yes, do as I say!":
        return 2

    MajorSubject.objects.all().delete()
    UniversityStudent.objects.all().delete()
    # University.objects.all().delete()
    School.objects.all().delete()

    # Creating majors
    majors = [MajorSubject.objects.create(subject=subject) for subject, _description in MajorSubject.MAJOR_CHOICES]

    # Creating the school
    letovo_school = School.objects.create(
        country="RU",
        name="Школа Летово",
        desc="Школа-пансион в Москве", # TODO: just a placeholder for now
        lat=55.55735129685743,
        lon=37.42254263170253
    )
    letovo_school.majors.set(majors)

    # Creating uiniversities
    for university in universities:
        print(f"start creating uni {university["name"]}...", end="", flush=True)
        if University.objects.filter(name=university["name"]).exists():
            print("already exists")
            continue
        # lat, lon can be ""
        University.objects.create(
            name=university["name"],
            description=university["description"],
            country=university["country"] or "Неизвестно",
            lat=university["lat"] or 0,
            lon=university["lon"] or 0
        )
        print("done")
    
    # Creating users and linking them to universities and schools TODO
    passwords = {}
    for alumni in alumnis:
        print(f"start creating user {alumni["name"]} {alumni["surname"]}...", end="", flush=True)
        password = secrets.token_urlsafe(32)
        username = f"{alumni["year"]}_{transliterate(alumni["name"])}_{transliterate(alumni["surname"])}"
        old_user = User.objects.filter(username=username)
        if old_user.exists():
            # print("removed old,", end="", flush=True)
            # old_user.get().delete()
            print("already exists")
            continue
        user = User.objects.create_user(username=username, password=password, first_name=alumni["name"], last_name=alumni["surname"])
        passwords[username] = password

        UniversityStudent.objects.create(
            student=user,
            university=University.objects.filter(name=alumni["univ"]).get(),
            start_year=alumni["year"]
        )
        StudentSchool.objects.create(
            student=user,
            school=letovo_school,
            start_year=alumni["year"] - 5,
            finish_year=alumni["year"],
            why_left="GR"
        )
        print("done")
    
    users_file = open("users.json", "w")
    json.dump(passwords, users_file)
    users_file.close()