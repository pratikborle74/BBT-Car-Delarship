import numpy as np
import pandas as pd
from datetime import date

# Function to display the car management menu
def carmenu():
    print("_" * 60)
    print("               Car Details MENU")
    print(" " * 14, "." * 16)
    print('=' * 60)
    print("         1 - Add a new car")
    print("         2 - Delete a car")
    print("         3 - Update a car")
    print("         4 - Show List of cars")
    print("         5 - Back")
    
    y = int(input("Choose your option from 1-5: "))
    
    if y == 1:
        add_cars()
    elif y == 2:
        delete_cars()
    elif y == 3:
        update_cars()
    elif y == 4:
        car_list()
    else:
        print("Back to the main menu")
    menu()

# Function to add a new car
def add_cars():
    try:
        x = pd.read_csv("car.csv", index_col=0)
    except FileNotFoundError:
        print("car.csv not found. Creating a new file.")
        x = pd.DataFrame(columns=["car_Code", "car_type", "car_Name", "Brand_Name", "Color", "Fuel_type", "Engine", "Horsepower", "transmission_type", "Price"])

    a = "Y"
    
    while a.lower() == "y":
        new_index = x.index.max() + 1 if not x.empty else 1
        b = input("Enter car_type: ")
        c = input("Enter car Name: ")
        r = input("Enter Brand Name: ")
        d = input("Enter Color: ")
        g = input("Enter Fuel_type: ")
        f = input("Enter Engine: ")
        h = input("Enter Horsepower: ")
        i = input("Enter transmission type: ")
        e = input("Enter Price: ")
        
        # Validate price input
        try:
            float(e)  # Check if price is a valid float
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue
        
        new_record = [new_index, b, c, r, d, g, f, h, i, e]
        if len(new_record) == len(x.columns):
            x.loc[new_index, :] = new_record
            x.to_csv("car.csv")

            print("_" * 60)
            print(x)
            print("Record added successfully")
            print("=" * 60)
            a = input("Do you want to add more records (Y or N): ")
        else:
            print(f"Error: The length of the record provided ({len(new_record)}) doesn't match the number of columns ({len(x.columns)}) in the DataFrame.")
    carmenu()

# Function to delete a car
def delete_cars():
    ans = "Y"
    
    while ans.lower() == "y":
        try:
            d = pd.read_csv("car.csv", index_col='car_Code')
            print(d)
            index = int(input('Enter car_Code: '))

            if index in d.index:
                d = d.drop([index], axis=0)
                d.to_csv("car.csv")
                print("Record Deleted successfully")
                print(d)
                ans = input("Do you want to delete more records, Y or N: ")
            else:
                print("Wrong car_Code")
                print("Try Again")
                break
        except FileNotFoundError:
            print("car.csv not found.")
            break
    carmenu()

# Function to update a car
def update_cars():
    s = "Y"
    
    while s.lower() == "y":
        try:
            f = pd.read_csv("car.csv", index_col='car_Code')
            print(f)
            i = int(input("Enter car Code to be updated: "))

            if i in f.index:
                print("Select Column to be updated")
                print(f.columns)
                c = input("Enter column name to update: ")
                v = input("Enter new value: ")
                f.loc[i, c] = v
                f.to_csv("car.csv")
                print(f)
                print("Record updated successfully")
                s = input("Do you want to Update more records, Y or N: ")
            else:
                print("Wrong car Code")
                print("Try Again")
        except FileNotFoundError:
            print("car.csv not found.")
            break
    carmenu()

# Function to list all cars
def car_list():
    try:
        f = pd.read_csv("car.csv")
        print(f)
    except FileNotFoundError:
        print("car.csv not found.")
    carmenu()

# Function to display the buyer management menu
def custmenu():
    print("_" * 60)
    print("               Buyer details Menu")
    print(" " * 14, "•" * 18)
    print('=' * 60)
    print("          1 - Add Buyers_Details")
    print("          2 - Delete Buyers_Details")
    print("          3 - Update Buyers_Details")
    print("          4 - Show Buyers_Details")
    print("          5 - Back")
    
    x = int(input("Enter your choice (1-5): "))
    
    if x == 1:
        add_customer()
    elif x == 2:
        delete_customer()
    elif x == 3:
        update_customer()
    elif x == 4:
        cust_list()
    else:
        print("Back to Main Menu")
    menu()

# Function to add a new customer
def add_customer():
    ans = "Y"
    while ans.lower() == "y":
        try:
            x = pd.read_csv("Buyers_Details.csv")
        except FileNotFoundError:
            print("Buyers_Details.csv not found. Creating a new file.")
            x = pd.DataFrame(columns=["Cust_ID", "Cust_Name", "Contact_No", "Address", "Email_ID"])
        
        a = x["Cust_ID"].max() + 1 if not x.empty else 1
        b = input("Enter Purchaser's Name: ")
        c = input("Enter Contact No: ")
        d = input("Enter Address: ")
        e = input("Enter Email_ID: ")
        x.loc[len(x), :] = [a, b, c, d, e]
        x.to_csv("Buyers_Details.csv", index=False)
        print(x)
        print("Record Added Successfully")

        ans = input("Do you want to add more records (Y or N): ")
    custmenu()

# Function to delete a customer
def delete_customer():
    try:
        x = pd.read_csv("Buyers_Details.csv", index_col='Cust_ID')
    except FileNotFoundError:
        print("Buyers_Details.csv not found.")
        return

    v = "Y"
    while v.lower() == "y":
        print(x)
        i = int(input("Enter Cust_ID to be deleted: "))
        if i in x.index:
            x = x.drop([i], axis=0)
            x.to_csv("Buyers_Details.csv")
            print(x)
            print("Record deleted successfully")
            v = input("Do you want to delete more records (Y or N): ")
        else:
            print("Wrong Cust_ID")
            print("Try Again")
            break
    custmenu()

# Function to update a customer
def update_customer():
    try:
        cust = pd.read_csv("Buyers_Details.csv", index_col='Cust_ID')
    except FileNotFoundError:
        print("Buyers_Details.csv not found.")
        return

    l = "Y"
    while l.lower() == "y":
        print(cust)
        Cid = int(input("Enter Cust_ID to be updated: "))
        if Cid in cust.index:
            print("Select Column To Be Updated")
            print(cust.columns)
            Ccl = input("Enter Column Name to be updated: ")
            val = input("Enter new value: ")
            cust.loc[Cid, Ccl] = val
            cust.to_csv("Buyers_Details.csv")
            print(cust)
            print("Record Updated Successfully")
            l = input("Do you want to update more records, Y or N: ")
        else:
            print("Wrong Cust_Id")
            print("Try Again")
            break
    custmenu()

# Function to list all customers
def cust_list():
    try:
        f = pd.read_csv("Buyers_Details.csv")
        pd.set_option("display.max_rows", None)
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_colwidth", None)
        pd.set_option('display.expand_frame_repr', True)
        print(f)
    except FileNotFoundError:
        print("Buyers_Details.csv not found.")
    custmenu()

# Function to display the vehicle registration menu
def regmenu():
    print("_" * 60)
    print("              Vehicle Registration Menu")
    print(" " * 13, "." * 25)
    print('=' * 60)
    print("          1 - Car Registration")
    print("          2 - Delete Car Registration")
    print("          3 - Show Registration Record")
    print("          4 - Back")
    
    i = int(input("Enter your choice (1-4): "))
    
    if i == 1:
        car_registration()
    elif i == 2:
        delete_car_registration()
    elif i == 3:
        show_registration_records()
    else:
        print("Back to Main Menu")
    menu()

# Function to register a car
def car_registration():
    e = 'Y'
    while e.lower() == 'y':
        try:
            o = pd.read_csv("Vehicle_Registration.csv")
        except FileNotFoundError:
            print("Vehicle_Registration.csv not found. Creating a new file.")
            o = pd.DataFrame(columns=["Bill_No", "Bill_Date", "Name", "City", "car_Name", "color", "showroom_price", "discount", "tax", "grand_total", "transmission_type"])

        try:
            cus = pd.read_csv("Buyers_Details.csv", index_col=0)
            it = pd.read_csv("car.csv", index_col=0)
        except FileNotFoundError:
            print("Required CSV files not found.")
            return
        
        pd.set_option("display.max_rows", 10)
        pd.set_option("display.max_columns", 10)
        pd.set_option("display.max_colwidth", 10)
        pd.set_option('display.expand_frame_repr', True)
        
        a = o['Bill_No'].max() + 1 if not o.empty else 1
        b = date.today()
        
        print(cus)
        c = int(input("Enter Customer_Id: "))
        
        if c in cus.index:
            d = cus.at[c, 'Cust_Name']
            print("Customer_Name:", d)
            f = cus.at[c, 'Cust_Address']
            print("Customer_Address:", f)
        else:
            print("Wrong Customer_Id")
            print("Try Again")
            e = input("Do you want to add more registrations (Y or N): ")
            continue
        
        print(it)
        g = int(input("Enter car Code: "))
        
        if g in it.index:
            h = it.at[g, 'car_Name']
            print("Car_Name:", h)
            x = it.at[g, 'Color']  # Ensure this matches the CSV header
            print("Car color:", x)
            eng = it.at[g, 'Engine']  # Use the correct column name
            v = it.at[g, 'transmission_type']  # Ensure this matches the CSV header
        else:
            print("Wrong car_Code")
            print("Try Again")
            e = input("Do you want to add more registrations (Y or N): ")
            continue
        
        j = float(it.at[g, 'Price']) if g in it.index else 0  # Convert 'price' to float
        print("Item_Price:", j)

        try:
            p = float(input("Enter % of discount (float-type-only): "))
        except ValueError:
            print("Invalid input for discount percentage. Please enter a float.")
            e = input("Do you want to add more registrations (Y or N): ")
            continue

        q = (j * p) / 100
        t = j * 0.10
        l = j - q + t

        o.loc[len(o)] = [a, b, d, f, h, x, j, q, t, l, e, v]  # Fixed column order
        o.to_csv("Vehicle_Registration.csv", index=False)
        print("Record added successfully")
        print(o)

        e = input("Do you want to add more registrations (Y or N): ")

    regmenu()  # Call regmenu() at the end                

# Function to delete a car registration
def delete_car_registration():
    try:
        x = pd.read_csv("Vehicle_Registration.csv", index_col='Bill_No')
    except FileNotFoundError:
        print("Vehicle_Registration.csv not found.")
        return
    
    while True:
        print(x)
        i = int(input("Enter Bill_No to be deleted: "))
        if i in x.index:
            x = x.drop([i], axis=0)
            x.to_csv("Vehicle_Registration.csv")
            print("Record deleted successfully")
        else:
            print("Wrong Bill_No")
            print("Try Again")
            break
        v = input("Do you want to delete more records (Y or N): ")
        if v.lower() != "y":
            break
    regmenu()

# Function to show registration records
def show_registration_records():
    try:
        bill = pd.read_csv("Vehicle_Registration.csv", index_col=0)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_colwidth", None)
        print(bill)
    except FileNotFoundError:
        print("Vehicle_Registration.csv not found.")
        return

    y = int(input("Enter Bill_No to view: "))
    if y in bill.index:
        print("_" * 70)
        print("\t", "\t", "\t", "BBT CAR DEALERSHIP")
        print('_' * 70)
        print("=" * 70)
        print("Date:", bill.at[y, "Bill_Date"], "\t", "Bill_No:", y)
        print("Name:", bill.at[y, "Name"], "\t")
        print("City:", bill.at[y, "City"])
        print("Car_Name:", bill.at[y, "car_Name"], "\t")
        print("Color:", bill.at[y, "color"])
        print("Showroom_price:", "$", bill.at[y, "showroom_price"], "\t")
        print("Discount:", "$", bill.at[y, "discount"])
        print("Tax:", "$", bill.at[y, "tax"], "\t")
        print("=" * 70)
        print("Grand_total:", "$", bill.at[y, "grand_total"])
        print('_' * 70)
        print("\t", "\t", "\t", "Thank You Visit Again")
    else:
        print("Wrong Bill No:")
    regmenu()

# Main menu function
def menu():
    print("_" * 60)
    print("               Welcome To BBT CAR DEALERSHIP")
    print(" " * 14, "." * 29)
    print('=' * 60)
    print("                1 - Car Details")
    print("                2 - Buyer Details")
    print("                3 - Vehicle Registration")
    print("                4 - Exit")
    
    z = int(input("Enter your choice (1-4): "))
    
    if z == 1:
        carmenu()
    elif z == 2:
        custmenu()
    elif z == 3:
        regmenu()
    else:
        print("Thank you for visiting again")

# Start the program
menu()
