import random
import math


female_names = ['Ama','Efia','Adjoa']
male_names = ['Kojo','Yaw','Kofi']
countries = {
    "Ghana" : ["Accra", "Kumasi", "Koforidua","Cape Coast"],
    "Nigeria": ["Abuja", "Lagos", "Ibadan", ""]
}


def get_name(gender):
    if(gender == "m"):
        return male_names[random.randrange(len(male_names))]
    else:
        return female_names[random.randrange(len(female_names))]

def nearest_ten_up(get_age):
    return math.ceil(get_age/10)*10

def nearest_ten_down(get_age):
    return math.floor(get_age/10)*10

# age_range = nearest_ten_up(get_age) + " - " + nearest_ten_down(get_age)
def get_address(country):
    gen_city = countries[country][random.randrange(len(countries[country]))]
    street_num = random.randint(1,200)
    # address= random.randrange[200], " ", countries[country][random.randrange(len(country))], " Street"
#    address = '',street_num ,'', gen_city
    return gen_city






gender = input("What gender should this name be?, f or m: ")
age = int(input("Please enter their age: "))
country = input("Please enter a country: ")

# gender, age, country = input("Please what the gender, age and country of user: ").split()

print("Name: ", get_name(gender) )
print("Age range: ", nearest_ten_down(age) , " - " , nearest_ten_up(age))
print("Address: ", random.randint(1,200), " ", get_address(country), " Street")