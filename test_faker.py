import pandas as pd
import random
from datetime import datetime
from faker import Faker

faker = Faker()

print(f'name: {faker.name()}')
print(f'address: {faker.address()}')
print(f' random text: {faker.text()}')

# def get_first_name():
#     first_name = faker.unique.first_name()
#     return first_name

# def get_name(gender):
#     if(gender == "Male"):
#         return faker.name_male()
#     else:
#         return faker.name_female()

#     # faker.name_male()
#     # first_name = faker.unique.first_name()
#     # return first_name

# def get_last_name():
#     last_name = faker.unique.last_name()
#     return last_name


# def get_gender(self):
#     gender = faker.gender()


# def get_date_of_birth(self):


# def get_email(self):


# def get_race(self):


# def get_country(self):


# def get_location(self):


