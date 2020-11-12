# Author: Bianca Gedorio
# Project

import random

employee_id_list = [65324, 53218, 76438, 19367, 31434]
first_name_list = ['Billy', 'Brian', 'Kathlyn', 'Eoghan', 'Zach']
surname_list = ['Bob Joe', 'Bunbun', 'Beckham', 'Bateman', 'Kelly']
employee_email_list = ['billybobjoe@mycit.ie', 'brianbunbun@mycit.ie',
                       'kathlynbeckham@mycit.ie', 'eoghanbateman@mycit.ie', 'zachkelly@mycit.ie']
employee_salary_list = [25000.00, 98700.00, 40000.00, 65443.02, 23431.31]


# Displaying the Menu
def show_menu():
    print("\n\tWelcome to the Main Menu")
    menu = "\n\t1: Show all Employees" \
           "\n\t2: Find Employee " \
           "\n\t3: Change an Employee's Salary" \
           "\n\t4: Add Employee" \
           "\n\t5: Remove Employee" \
           "\n\t6: Save Bonus Information" \
           "\n\t7: Generate Report" \
           "\n\t8: Quit" \
           "\n==> "

    # The menu loop
    while True:
        try:
            number = int(input(menu))
            if 1 <= number <= 8:
                break
            else:
                print("Error. Try Again.")
        except ValueError:
            print("Only values 1, 2, 3, 4, 5, 6, 7, or 8 please...")
    return number


# User's choice
def get_choice(choice):
    try:
        if choice == int(1):
            read_file_in_a_list()
        elif choice == int(2):
            show_employee()
            find_employee()
        elif choice == int(3):
            change_salary()
        elif choice == int(4):
            add_employee()
        elif choice == int(5):
            remove_employee()
        elif choice == int(6):
            generate_bonus_info()
        elif choice == int(7):
            generate_reports()
        return choice
    except ValueError:
        print("Numeric digits only.")


# Loading the data from the employees text file
def load_data():
    employee_details_list = "Load File" + "\n" + "ID: " + str(employee_id_list) + "\n" + "First Name: " + \
                            str(first_name_list) + "\n" + "Surname" + str(surname_list) + \
                            "\n" + "Email: " + str(employee_email_list) + "\n" + \
                            "Employee's Salary: " + str(employee_salary_list)
    return employee_details_list


# First option: Separating the data into lists from a file.
def show_all_employee(name_of_file):
    employee_connection = open(name_of_file)
    # Five empty lists to store data from the file
    employee_id_list = []
    first_name_list = []
    surname_list = []
    employee_email_list = []
    employee_salary_list = []

    while True:
        # Append first line
        line = employee_connection.readline().rstrip()
        employee_id_list.append(str(line))
        # Append second line
        line = employee_connection.readline().rstrip()
        if line == "":
            break
        first_name_list.append(line)
        # Append third line
        line = employee_connection.readline().rstrip()
        if line == "":
            break
        surname_list.append(line)
        # Append fourth line
        line = employee_connection.readline().rstrip()
        if line == "":
            break
        employee_email_list.append(line)
        # Append fifth line
        line = employee_connection.readline().rstrip()
        employee_salary_list.append("€" + str(line))
    # Returning five parameters
    return employee_id_list, first_name_list, surname_list, employee_email_list, employee_salary_list


# Displaying the lists
def read_file_in_a_list():
    f_name = "text.txt"
    employee_id_list, first_name_list, surname_list, employee_email_list, employee_salary_list = \
        show_all_employee(f_name)
    list1 = "ID: " + str(employee_id_list) + "\n" + "First Name: " + str(first_name_list) + \
            "\n" + "Surname: " + str(surname_list) + "\n" + "Email: " + str(employee_email_list) + \
            "\n" + "Salary: " + str(employee_salary_list)
    print(list1)


# Adding a new employee in the list and entering their details
def add_employee():
    print("\nPlease enter your details: ")
    read_fullname()
    generate_unique_id()
    generate_unique_email_address()
    give_salary()
    # Validating the input
    updated_list = "Updated" + "\n" + "ID: " + str(employee_id_list) + "\n" + "First Name: " + str(first_name_list) +\
                   "\n" + "Surname: " + str(surname_list) + "\n" + "Email: " + str(employee_email_list) + \
                   "\n" + "Salary: " + str(employee_salary_list)
    print(updated_list)


def read_nonempty_alphabetical_string(prompt):
    while True:
        s = input(prompt)
        s_with_no_spaces = s.replace(' ', '')
        if len(s_with_no_spaces) > 0 and s_with_no_spaces.isalpha():
            break
        else:
            print("Please type letters only")
    return s


# Input name
def read_fullname():
    first_name_list.append(read_nonempty_alphabetical_string("First Name >>> "))
    surname_list.append(read_nonempty_alphabetical_string("Surname >>> "))
    return first_name_list, surname_list


# Create a random, five digit ID number
def generate_unique_id():
    try:
        num = random.randint(10000, 99999)
        while True:
            if num == employee_id_list:
                print("That ID already exits.")
                break
            else:
                employee_id_list.append(num)
            return employee_id_list
    except ValueError:
        print("Invalid")


# Creating an email address
def generate_unique_email_address():
    domain = "mycit.ie"
    email_name = input("Enter your name: ")
    employee_email_list.append(email_name + "@" + domain)
    return email_name, employee_email_list


# Giving the employee a salary
def give_salary():
    employee_salary_list.append(int(input("Enter Salary: €")))
    return employee_salary_list


# Finding an employee using ID and showing their personal details
def show_employee():
    while True:
        try:
            employ_id = int(input("Enter employee's ID: "))
            if employ_id == 65324:
                billy = ("First name: " + first_name_list[0],
                         "Surname: " + surname_list[0],
                         "Email: " + employee_email_list[0],
                         "Salary: €" + str(employee_salary_list[0]))
                print(billy)
                break
            elif employ_id == 53218:
                brian = ("First name: " + first_name_list[1],
                         "Surname: " + surname_list[1],
                         "Email: " + employee_email_list[1],
                         "Salary: €" + str(employee_salary_list[1]))
                print(brian)
                break
            elif employ_id == 76438:
                kathlyn = ("First name: " + first_name_list[2],
                           "Surname: " + surname_list[2],
                           "Email: " + employee_email_list[2],
                           "Salary: €" + str(employee_salary_list[2]))
                print(kathlyn)
                break
            elif employ_id == 19367:
                eoghan = ("First name: " + first_name_list[3],
                          "Surname: " + surname_list[3],
                          "Email: " + employee_email_list[3],
                          "Salary: €" + str(employee_salary_list[3]))
                print(eoghan)
                break
            elif employ_id == 31434:
                zach = ("First name: " + first_name_list[4],
                        "Surname: " + surname_list[4],
                        "Email: " + employee_email_list[4],
                        "Salary: €" + str(employee_salary_list[4]))
                print(zach)
                break
            elif employ_id > 10000 or employ_id <= 99999:
                unknown = ("First name: " + first_name_list[5],
                           "Surname: " + surname_list[5],
                           "Email: " + employee_email_list[5],
                           "Salary: €" + str(employee_salary_list[5]))
                print(unknown)
                break
            else:
                print("The ID you entered doesn't exist.")
            return employ_id
        except ValueError:
            print("Must enter in five digits only.")


# Finding the position of an employee using ID
def find_employee():
    while True:
        try:
            em_id = int(input("Enter employee's ID: "))
            if em_id == 65324:
                position = employee_id_list.index(65324)
                print("Position: " + str(position))
                break
            elif em_id == 53218:
                position = employee_id_list.index(53218)
                print("Position: " + str(position))
                break
            elif em_id == 76438:
                position = employee_id_list.index(76438)
                print("Position: " + str(position))
                break
            elif em_id == 19367:
                position = employee_id_list.index(19367)
                print("Position: " + str(position))
                break
            elif em_id == 31434:
                position = employee_id_list.index(31434)
                print("Position: " + str(position))
                break
            elif em_id > 10000 or em_id <= 99999:
                position = employee_id_list.index(em_id)
                print("Position: " + str(position))
                break
            else:
                print("Invalid")
        except ValueError:
            print("The ID you entered doesn't exist.")
    return em_id, employee_id_list


# Preventing negative values
def no_negative_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Invalid. Positive numbers only")
                break
            return number
        except ValueError:
            print("Must be numeric")


# Changing the salary of an employee
def change_salary():
    try:
        while True:
            employ_id = int(input("Enter employee's ID: "))
            salary = input("Do you want to edit their salary? ")
            if salary == "Y" or salary == "y" and employ_id == 65324:
                employee_salary_list.remove(25000.00)
                employee_salary_list.insert(0, int(no_negative_number("Enter new Salary: €")))
                print("Updated Salary: " + str(employee_salary_list))
                break
            elif salary == "Y" or salary == "y" and employ_id == 53218:
                employee_salary_list.remove(98700.00)
                employee_salary_list.insert(1, int(no_negative_number("Enter new Salary: €")))
                print("Updated Salary: " + str(employee_salary_list))
                break
            elif salary == "Y" or salary == "y" and employ_id == 76438:
                employee_salary_list.remove(40000.00)
                employee_salary_list.insert(2, int(no_negative_number("Enter new Salary: €")))
                print("Updated Salary: " + str(employee_salary_list))
                break
            elif salary == "Y" or salary == "y" and employ_id == 19367:
                employee_salary_list.remove(65443.02)
                employee_salary_list.insert(3, int(no_negative_number("Enter new Salary: €")))
                print("Updated Salary: " + str(employee_salary_list))
                break
            elif salary == "Y" or salary == "y" and employ_id == 31434:
                employee_salary_list.remove(23431.31)
                employee_salary_list.insert(4, int(no_negative_number("Enter new Salary: €")))
                print("Updated Salary: " + str(employee_salary_list))
                break
            elif salary == "Y" or salary == "y" and employ_id == employ_id:
                del employee_salary_list[-1]
                employee_salary_list.insert(5, int(no_negative_number("Enter new Salary: €")))
                print("Updated Salary: " + str(employee_salary_list))
                break
            elif salary == "N" or salary == "n":
                break
            else:
                print("Please choose y or n.")
        return salary, employee_salary_list
    except ValueError:
        print("The ID you entered doesn't exist.")


# Removing/Deleting the last employee from the list
def remove_employee():
    try:
        position = input("Delete last employee? ")
        if position == 'Y' or position == 'y':
            del employee_id_list[-1]
            del first_name_list[-1]
            del surname_list[-1]
            del employee_email_list[-1]
            del employee_salary_list[-1]
            # Validating the input
            update_list = "Updated" + "\n" + "ID: " + str(employee_id_list) + "\n" + "First Name: " + \
                          str(first_name_list) + "\n" + "Surname" + str(surname_list) + "\n" + "Email: " + \
                          str(employee_email_list) + "\n" + "Salary: " + str(employee_salary_list)
            print(update_list)
        elif position == 'N' or position == 'n':
            print("Okay")
        else:
            print("Error")
        return employee_id_list, first_name_list, surname_list, employee_email_list, employee_salary_list
    except ValueError:
        print("Invalid. Please choose Y or N")


# Displaying employee's bonus information
def generate_bonus_info():
    try:
        print("End-of-Year Bonus\n")
        percentage = float(input("Enter bonus: "))
        display_percentage = percentage / 100
        add = display_percentage * employee_salary_list[0]
        add2 = display_percentage * employee_salary_list[1]
        add3 = display_percentage * employee_salary_list[2]
        add4 = display_percentage * employee_salary_list[3]
        add5 = display_percentage * employee_salary_list[4]
        print("Bonus: {}%" .format(percentage))
        total1 = add + employee_salary_list[0]
        total2 = add2 + employee_salary_list[1]
        total3 = add3 + employee_salary_list[2]
        total4 = add4 + employee_salary_list[3]
        total5 = add5 + employee_salary_list[4]
        # Validating the input
        print("Name: " + first_name_list[0] + " " + surname_list[0] + "\n" +
              "Salary: €" + str(employee_salary_list[0]) + "\n" +
              "Bonus: €" + str(add) + "\n" +
              "Total: €" + str(total1))
        print("\n\nName: " + first_name_list[1] + " " + surname_list[1] + "\n" +
              "Salary: €" + str(employee_salary_list[1]) + "\n" +
              "Bonus: €" + str(add2) + "\n" +
              "Total: €" + str(total2))
        print("\n\nName: " + first_name_list[2] + " " + surname_list[2] + "\n" +
              "Salary: €" + str(employee_salary_list[2]) + "\n" +
              "Bonus: €" + str(add3) + "\n" +
              "Total: €" + str(total3))
        print("\n\nName: " + first_name_list[3] + " " + surname_list[3] + "\n" +
              "Salary: €" + str(employee_salary_list[3]) + "\n" +
              "Bonus: €" + str(add4) + "\n" +
              "Total: €" + str(total4))
        print("\n\nName: " + first_name_list[4] + " " + surname_list[4] + "\n" +
              "Salary: €" + str(employee_salary_list[4]) + "\n" +
              "Bonus: €" + str(add5) + "\n" +
              "Total: €" + str(total5))

        # Write bonus information in a file
        bonus_file = open("Bonus.txt", 'w')
        bonus_file.write("End-of-Year Bonus\n")
        bonus_file.write("Name: " + first_name_list[0] + " " + surname_list[0] + "\n" +
                         "Salary: €" + str(employee_salary_list[0]) + "\n" +
                         "Bonus: €" + str(add) + "\n" +
                         "Total: €" + str(total1))
        bonus_file.write("\n\nName: " + first_name_list[1] + " " + surname_list[1] + "\n" +
                         "Salary: €" + str(employee_salary_list[1]) + "\n" +
                         "Bonus: €" + str(add2) + "\n" +
                         "Total: €" + str(total2))
        bonus_file.write("\n\nName: " + first_name_list[2] + " " + surname_list[2] + "\n" +
                         "Salary: €" + str(employee_salary_list[2]) + "\n" +
                         "Bonus: €" + str(add3) + "\n" +
                         "Total: €" + str(total3))
        bonus_file.write("\n\nName: " + first_name_list[3] + " " + surname_list[3] + "\n" +
                         "Salary: €" + str(employee_salary_list[3]) + "\n" +
                         "Bonus: €" + str(add4) + "\n" +
                         "Total: €" + str(total4))
        bonus_file.write("\n\nName: " + first_name_list[4] + " " + surname_list[4] + "\n" +
                         "Salary: €" + str(employee_salary_list[4]) + "\n" +
                         "Bonus: €" + str(add5) + "\n" +
                         "Total: €" + str(total5))
        bonus_file.close()
    except ValueError:
        print("Invalid")


# Writing a report showing the salary average, largest salary and the employee's name
def generate_reports():
    print("Report\n")
    # Calculating the employee's average salary
    average = sum(employee_salary_list) / len(employee_salary_list)
    print(" Total Sum: €", sum(employee_salary_list), "\n",
          "Total Employees: ", len(employee_salary_list), "\n",
          "Average Salary: €", round(average, 2))

    # Finding the largest salary and the employee who earned it
    largest = len(employee_salary_list)
    employee_salary_list.sort()
    print(" Largest Salary is: €", employee_salary_list[largest - 1])
    name = (" Name: " + first_name_list[1] + " " + surname_list[1])
    print(name)


# Saving the file
def save_data(filename):
    destination = open(filename, 'w')
    destination.write("Saved File" + "\n" + "Employee's ID: " + str(employee_id_list) + "\n" +
                      "Employee's First Name: " + str(first_name_list) + "\n" + "Employee's Surname" +
                      str(surname_list) + "\n" + "Employee's Email: " + str(employee_email_list) + "\n" +
                      "Employee's Salary: " + str(employee_salary_list))
    return destination.close()


def main():
    load_data()
    while True:
        users_choice = show_menu()
        get_choice(users_choice)
        if users_choice == 8:
            break
    save_data("employees.txt")


main()
