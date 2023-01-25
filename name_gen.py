
import random
female_names = ['Ama','Efia','Adjoa']
male_names = ['Kojo','Yaw','Kofi']

def get_gender():
    return random.choice(["m","f"])

def get_name(gender= None):
    print(gender)
    if(gender == "m"):
        return male_names[random.randrange(len(male_names))]
    elif(gender == "f"):
        return female_names[random.randrange(len(female_names))]
    else:
        return "No gender entered"

def main():
    # gender = get_gender()
    # # print(gender)
    # name = get_name(gender)
    # print(name)

    print(" . ".split(" "))

main()