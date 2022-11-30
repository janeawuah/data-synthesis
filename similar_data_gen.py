# importing the csv file
import csv

# get the csv file
with open("./user_data.csv", 'r') as file:
    input_data = csv.reader(file, delimiter=',')

    # List to store column names
    data_labels = []

    # adding rows to list
    for record in input_data:
        data_labels.append(record)

    # print column names
    print("List of column names : ", data_labels[0])

    