# importing the csv file
import csv, math,random
import pandas as pd

female_names = ['Ama','Efia','Adjoa']
male_names = ['Kojo','Yaw','Kofi']


def get_name(gender):
    if(gender == "Male"):
        return male_names[random.randrange(len(male_names))]
    else:
        return female_names[random.randrange(len(female_names))]

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


for gender in select_column.gender:
    name = get_name(gender)
    email = name.lower()+'@gmail.com'
    print(name, end =' ')
    print(email, end=' ')
    print(gender)



