import random
from faker import Faker


faker = Faker()

def gen_pii():
    name = faker.name()
    # race =  faker.race()
    country = faker.country
    address = faker.address()
    occupation = faker.job()
    dob = faker.date()
    gender = random.choice(['m', 'f'])
    phone_number = faker.phone_number()

    entry = ''+ name+' '+ gender + ' '+ dob+ ' '+ country + ' '+ address + ' '+ occupation + ' '+ phone_number
    return entry






def gen_create_num_piis(num):
    for i in num:
        print(gen_pii())



def get_first_name():
    first_name = faker.unique.first_name()
    return first_name

def get_name(gender):
    if(gender == "m"):
        return faker.name_male()
    else:
        return faker.name_female()


def get_last_name():
    last_name = faker.unique.last_name()
    return last_name


def get_gender():
    # gender = faker.gender()
    return random.choice(['m', 'f'])


def get_date_of_birth():
    return faker.date()


def get_email(fname, lname):
    email =fname,'.',lname,'@gmail.com'
    return email


def get_address():
    return faker.address()


# def get_race(self):

def get_job():
    return faker.job()

def get_country():
    return faker.country()

def get_phone_number():
    return faker.phone_number()




# print(faker.name())
# print(faker.date())
# print(faker.job())
# print(faker.address())
# print(random.choice(['m', 'f']))
# print(faker.country())
# print(faker.phone_number())


def main():

    num = int(input("Please enter the number of records you would like: "))
    # gen_create_num_piis(num)

    for i in range(num):
        gender = get_gender()
        name = get_name(gender)
        
        country = get_country()
        address = get_address()
        occupation = get_job()
        dob = get_date_of_birth()
        phone_number = get_phone_number()

        print(i+1, ' ',name+' '+ gender + ' '+ dob+ ' '+ country + ' '+ address + ' '+ occupation + ' '+ phone_number)


main()
