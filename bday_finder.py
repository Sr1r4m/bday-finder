#!/usr/bin/env python
import argparse
import csv
import time
import sys
from builtins import input

LightGreen   = "\033[92m"

parser = argparse.ArgumentParser()
parser.add_argument('-s', help='save to csv_file', dest='save', action='store_true')
parser.add_argument('-f', help='find from csv_file', dest='find', action='store_true')
args = parser.parse_args()

save_func = args.save
find_func = args.find

time_struct = time.localtime()                          #getting localtime in a struct
current_date = time.strftime("%d", time_struct)         #getting only date from the strct
current_month = time.strftime("%m", time_struct)

def banner():
    print('''   \033[1m %s                               _     _  _ _  __    _  _   _    _          __  _   _
                                  |_| | |_|  |  |  |  /_\  \ /    |_  | |\ | |  | _| |_|
                                  |_| | | \  |  |__| /   \  |     |   | | \| |__| _| | \______ @@ \033[0m\n ''' % LightGreen)

def find():
    result = []
    with open('test.csv') as f:
        main_dict = dict(filter(None, csv.reader(f)))   #reading from csv file into dictionary using dict call
    for key,value in main_dict.items():                 #iterating k,v into dict if dd/mm matches with current dd/mm appending into a list
        try:
            time_csv  = time.strptime(value,"%d.%m.%Y")
            month_csv = time.strftime("%m", time_csv)
            date_csv  = time.strftime("%d", time_csv)
        except ValueError:
            print("Data is wrong plz check CSV file. Throws ValueError \n")
            sys.exit(1)
        if month_csv == current_month:
            if date_csv == current_date:
                result.append(key)

    if result:
        return result
    else:
        return result

def save():
    add_new = dict()
    while True:
        key = input("Enter the Name: ")
        if not key.isalpha():
            print("Name should be in Alphabets..If u want to exit tap ctrl-c")
            continue
        value = input("Enter the DOB: ")
        try:
            value = time.strptime(value, "%d.%m.%Y")
        except ValueError:
            print("Please give D.O.B in dd/mm/yyyy format! :)")
            continue
        add_new[key] = value
        act = input("Still need to update csv ? y/n \n")
        if act == "y":
            print("Add another")
        elif act == "n":
            print("Added to csv")
            break
        else:
            print("Please enter the correct option")
    print("Added Names: \n", add_new)
    with open('test.csv','a') as csv_file:
        writer = csv.writer(csv_file)
        for key,value in add_new.items():
            writer.writerow([key,value])                #writing into csv files Note: It writes only two rows as dict's key & val 
                                                        #which is Name & DOB here

def print_found_names():
    name = []
    name = find()
    if name:
        for i in name:
            print("Today is " + i + "'s Birthday")
        input("Press a key to exit")
    else:
        print("None of them having Bday today!")

if __name__== "__main__":
    try:
        banner()
        if find_func:
            print_found_names()
        elif save_func:
            save()
        else:
            print_found_names()
    except KeyboardInterrupt:
        print("\n Sorry for Disliking the App \n Bye! \n :(")
        sys.exit(0)
