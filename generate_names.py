import random
import math


female_names = ['Ama','Efia','Adjoa']
male_names = ['Kojo','Yaw','Kofi']
countries = {
    "Ghana" : ["Accra", "Kumasi", "Koforidua","Cape Coast"],
    "Nigeria": ["Abuja", "Lagos", "Ibadan", ""]
}

get_gender = input("What gender should this name be?, f or m: ")
get_age = int(input("Please enter their age: "))

if(get_gender == "m"):
    get_name = male_names[random.randrange(len(male_names))]
else:
    get_name = female_names[random.randrange(len(female_names))]

def nearest_ten_up(get_age):
    return math.ceil(get_age/10)*10

def nearest_ten_down(get_age):
    return math.floor(get_age/10)*10

# age_range = nearest_ten_up(get_age) + " - " + nearest_ten_down(get_age)
def get_address(country_name):
    return ""

print("Name: ", get_name )
print("Age range: ", nearest_ten_down(get_age) , " - " , nearest_ten_up(get_age))
print("Address: ")