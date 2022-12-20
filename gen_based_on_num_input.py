from faker import Faker

import random

faker = Faker()

def gen_pii():
    name = faker.name()
    race =  faker.race()
    country =
    address = faker.address()
    ocuupation = faker.job()
    dob =
    gender =






def gen_create_num_piis(num):
    for i in num:
        print(gen_pii())
