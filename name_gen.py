
import random
female_names = ['Ama','Efia','Adjoa']
male_names = ['Kojo','Yaw','Kofi']
last_names = ['Osei', "Poku", "Oware", "Mensah"]

first_names = female_names + male_names

email_providers = ["@gmail.com","@outlook.com", "@hotmail.com", "@yahoo.com"]
email_formats = [
            "{f}{last}",
            "{first}{last}",
            "{first}.{l}",
            "{first}_{l}",
            "{first}.{last}",
            "{first}_{last}",
            "{last}_{first}",
            "{last}.{first}",
    ]

def get_gender():
    return random.choice(["m","f"])

def get_name(gender= None):
    if(gender == "m"):
        fname = male_names[random.randrange(len(male_names))]
        lname = last_names[random.randrange(len(last_names))]
        name = "{f} {l}".format(f= fname, l = lname)
        return name
    elif(gender == "f"):
        fname = female_names[random.randrange(len(female_names))]
        lname = last_names[random.randrange(len(last_names))]
        name = "{f} {l}".format(f= fname, l = lname)
        return name
    else:
        fname = first_names[random.randrange(len(first_names))]
        lname = last_names[random.randrange(len(last_names))]
        name = "{f} {l}".format(f= fname, l = lname)
        return name

def get_email(name):
    names = name.split()
    fname = names[0]
    lname = names[-1]
    first_initial = fname[0]
    last_initial = lname[-1][0]

    mail_format = random.choice(email_formats)
    mail_provider = random.choice(email_providers)

    name_combination = mail_format.format(first = fname, last = lname, f = first_initial, l= last_initial)
    return (name_combination+ mail_provider).lower()



def main():
    gender = get_gender()
    # print(gender)
    name = get_name(gender)
    email = get_email(name)
    print(name)
    print(gender)
    print(email)



main()