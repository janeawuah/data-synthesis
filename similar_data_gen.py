# importing the csv file
import csv, math,random
import pandas as pd

female_names = ['Ama','Efia','Adjoa']
male_names = ['Kojo','Yaw','Kofi']
last_names = ['Ampfo','Safo', 'Osei', 'Mensah', 'Ofei']

def get_name(gender):
    if(gender == "Male"):
        return male_names[random.randrange(len(male_names))]
    else:
        return female_names[random.randrange(len(female_names))]


def get_lastname():
    return last_names[random.randrange(len(last_names))]
# get the csv file
# with open("./user_data.csv", 'r') as file:
#     input_data = csv.reader(file, delimiter=',')

#     # List to store column names
#     data_labels = []

#     # adding rows to list
#     for record in input_data:
#         data_labels.append(record)

#     # print column names
#     print("List of column names : ", data_labels[0])


fields = ['gender', 'date_of_birth', 'country']
select_column = pd.read_csv('user_data.csv', skipinitialspace=True, usecols=fields)
# print(select_column.gender)

# for date in select_column.date_of_birth:
#     print(date[-4:])


for gender in select_column.gender:
    name = get_name(gender)
    lname = get_lastname()
    email = name.lower()+'.' + lname.lower()+ '@gmail.com'
    print(name, end =' ')
    print(lname, end='  ')
    print(email, end='   ')
    print(gender)



