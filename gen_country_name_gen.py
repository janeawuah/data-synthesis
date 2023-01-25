import csv, math,random,six
import pandas as pd


# female_names = ['Ama','Efia','Adjoa']
# male_names = ['Kojo','Yaw','Kofi']

female_names = { 
    "Ghana" : ['Ama','Efia','Adjoa','Abena', 'Emefa'],
    "Nigeria": ["Amaka", "Ebube", "Ebire", "Lola", "Tiwa"],
    "International": ["Edna","Ava", "Svet","Lily", "Polly"]
    }
    
male_names = { 
    "Ghana" : ['Kojo','Yaw','Kofi','Kobby','Kwame'],
    "Nigeria": ["Emeka", "Yemi", "Femi", "Dozie", "Chima"],
    "International": ["Billy","Suarez", "Tom","Harry", "Tony"]
    }



last_names = {"Ghana" : ['Ampfo','Safo', 'Osei', 'Mensah', 'Ofei'],
"Nigeria" : ['Ibrahim', 'Musa','Azeez', 'Chukwuma', 'Adisa'],
"International": ['Peters', 'Graham', 'Wang', 'Kim', 'Twist']
}

countries = {
    "Ghana" : ["Accra", "Kumasi", "Koforidua","Cape Coast"],
    "Nigeria": ["Abuja", "Lagos", "Ibadan"],
    "International": ['Abidjan','Paris',"Washington DC","London", "Dublin"]
}


def get_name(gender, country):
    if(gender == "m"):
        # return male_names[random.randrange(len(male_names))]
        return male_names[country][random.randrange(len(male_names[country]))]
    else:
        # return female_names[random.randrange(len(female_names))]
        return female_names[country][random.randrange(len(female_names[country]))]


def get_lastname(country):
    # return last_names[random.randrange(len(last_names))]
    return last_names[country][random.randrange(len(last_names[country]))]

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





# # For individual inputs
# # # ----------------------------------------------------------------------------------------------------
# gender = input("What gender should this name be?, f or m: ")
# age = int(input("Please enter their age: "))
# country = input("Please enter a country: ")

# # gender, age, country = input("Please what the gender, age and country of user: ").split()


# name = get_name(gender,country)
# lname = get_lastname(country)
# email = name.lower()+'.' + lname.lower()+ '@gmail.com'

# print(name, end =' ')
# print(lname, end='  ')
# print(email, end='   ')
# print(gender, end='   ')
# print(nearest_ten_down(age) , " - " , nearest_ten_up(age) , end =' ')
# print(get_address(country), end =' ')
# print(country)

# ----------------------------------------------------------------------------------------------------

# For file inputs
# ----------------------------------------------------------------------------------------------------

# fields = ['gender', 'date_of_birth', 'country']
fields = ['gender', 'country']
select_column = pd.read_csv('user_data.csv', skipinitialspace=True, usecols=fields)
# print(select_column.gender)

# for date in select_column.date_of_birth:
#     print(date[-4:])


for gender,country in select_column.itertuples(index=False):
    if country in countries:
        name = get_name(gender,country)
        lname = get_lastname(country)
    else:
        name = get_name(gender,'International')
        lname = get_lastname("International")
    # lname = get_lastname()
    email = name.lower()+'.' + lname.lower()+ '@gmail.com'


    print(name, end =' ')
    print(lname, end='  ')
    print(email, end='   ')
    print(gender, end='   ')
    # print(nearest_ten_down(age) , " - " , nearest_ten_up(age) , end =' ')
    # print(get_address(country), end =' ')
    print(country)


# for gender,country in select_column.itertuples(index=False):
#        print( gender, country)


