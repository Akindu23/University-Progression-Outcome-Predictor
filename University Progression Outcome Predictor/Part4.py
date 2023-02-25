# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.
# https://www.w3schools.com/python/python_functions.asp
# https://www.linkedin.com/learning/python-essential-training-2018/the-string-type?autoplay=true&resume=false&u=76664938

# IIT Student ID: 20211364
# UoW ID: w1898951 / 18989511
# Date: 07/04/2022

# Declaring variables
pass_credits = 0
defer_credits = 0
fail_credits = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
total = 0
progression_outcome = ''
outcome_list = []


# Part 1
# Function for the text displayed for user with range and data type validation in Student Version
def input_student(credit_level_student):
    while True:
        try:
            credit_student = int(input("Please enter your credits at " + credit_level_student + ": "))
            if credit_student not in range(0, 121, 20):
                print("Out of range\n")
                continue

        except ValueError:
            print("Integer required\n")
            continue

        break

    return credit_student


# Function for the text displayed for user with range and data type validation in Staff Version
def input_staff(credit_level_staff):
    while True:
        try:
            credit_staff = int(input("Enter your total " + credit_level_staff + " credits: "))
            if credit_staff not in range(0, 121, 20):
                print("Out of range\n")
                continue

        except ValueError:
            print("Integer required\n")
            continue

        break

    return credit_staff


# Function for progress outcome with validation for total credits for Student Version
def student_validation():
    while True:
        pass_credits = input_student('pass')
        defer_credits = input_student('defer')
        fail_credits = input_student('fail')

        if pass_credits + defer_credits + fail_credits != 120:
            print("Total incorrect\n")
            continue
        break

    if pass_credits == 120:
        progression_outcome = 'Progress'

    elif pass_credits == 100:
        progression_outcome = 'Progress (module trailer)'

    elif fail_credits == 80 or fail_credits == 100 or fail_credits == 120:
        progression_outcome = 'Exclude'

    else:
        progression_outcome = 'Do not Progress - module retriever'

    print(progression_outcome)


# Function for progress outcome with validation for total credits for Staff Version
def staff_validation():
    global progress, trailer, retriever, exclude

    while True:
        pass_credits = input_staff('PASS')
        defer_credits = input_staff('DEFER')
        fail_credits = input_staff('FAIL')

        if pass_credits + defer_credits + fail_credits != 120:
            print("Total incorrect\n")
            continue
        break

    if pass_credits == 120:
        progression_outcome = 'Progress'
        progress += 1

    elif pass_credits == 100:
        progression_outcome = 'Progress (module trailer)'
        trailer += 1

    elif fail_credits == 80 or fail_credits == 100 or fail_credits == 120:
        progression_outcome = 'Exclude'
        exclude += 1

    else:
        progression_outcome = 'Module retriever'
        retriever += 1

    # Part3
    # Appending list data with progression outcomes and credit values

    outcome_list.append([progression_outcome, pass_credits, defer_credits, fail_credits])

    # Part4
    # Appending text file with formatting for progression outcomes and credit values

    outcome_file = open("outcomefile.txt", "a")
    outcome_file.write(f"{progression_outcome} - {pass_credits},{defer_credits},{fail_credits}\n")
    outcome_file.close

    print(progression_outcome)


# Function to Print Horizontal Histogram
def horizontal_histogram(outcome, outcome_count):
    print(f"{outcome:<9} {outcome_count}:", "*" * outcome_count)


# Part 2
# Function to print Vertical Histogram
def vertical_histogram():
    global progress, trailer, retriever, exclude

    total = progress + trailer + retriever + exclude

    print("Vertical Histogram\n")
    print(f"{'Progress'} {progress} |", f"{'Trailer'} {trailer} |", f"{'Retriever'} {retriever} |",
          f"{'Excluded'} {exclude}")

    while progress != 0 or trailer != 0 or retriever != 0 or exclude != 0:
        if progress > 0:
            print(f"{' ':>4}", f"{'*':<9}", end="")
            progress -= 1
        else:
            print(f"{' ':>4}", f"{' ':<9}", end="")

        if trailer > 0:
            print(f"{' ':>2}", f"{'*':<9}", end="")
            trailer -= 1
        else:
            print(f"{' ':>2}", f"{' ':<9}", end="")

        if retriever > 0:
            print(f"{' ':>2}", f"{'*':<9}", end="")
            retriever -= 1
        else:
            print(f"{' ':>2}", f"{' ':<9}", end="")

        if exclude > 0:
            print(f"{' ':>4}", f"{'*':<9}", end="\n")
            exclude -= 1
        else:
            print(f"{' ':>4}", f"{' ':<9}", end="\n")

    print()
    print(total, "outcomes in total.")
    print("-" * 75)


# Function for Staff Version to get 'y' or 'q' input from user
def staff_program():
    option = input('''
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')

    if option == 'y':
        print()
        while True:  # Looping Staff Version
            staff_validation()
            staff_program()
            break

    elif option == 'q':
        print()
        print("-" * 75)
        print("Horizontal Histogram\n")
        horizontal_histogram('Progress', progress)  # Calling Horizontal Histogram Function
        horizontal_histogram('Trailer', trailer)
        horizontal_histogram('Retriever', retriever)
        horizontal_histogram('Excluded', exclude)
        print()
        print(f"{progress + trailer + retriever + exclude}"" outcomes in total.")
        print("-" * 75)

        vertical_histogram()  # Part 2. Calling Vertical Histogram Function to print.

        print(
            "Progression Outcomes List\n")  # Part3 contd. Displaying progress outcomes and credit values stored in list
        for item in outcome_list:
            print(f"{item[0]} - {item[1]},{item[2]},{item[3]}")
        print("-" * 75)

        print("Reading from File\n")  # Part 4 contd. Reading from file and displaying content in the file.
        outcome_file = open("outcomefile.txt", "r")
        print(outcome_file.read())
        print("-" * 75)

    else:
        print("Invalid Input! Please try again!")
        staff_program()


# Menu option where user is asked an input to select the version or quit the program
while True:
    user = input('''
Enter '1' to Open Student Version
Enter '2' to Open Staff Version
Enter '3' to Quit Program

Enter your option here: ''')

    if user == '1':
        print('-' * 75)
        print('Student Version \n')
        student_validation()

    elif user == '2':
        outcome_file = open("outcomefile.txt", "w")  # Part 4 contd. Writing the file when staff version is selected.
        outcome_file.close()

        print('-' * 75)
        print('Staff Version with Histogram\n')
        staff_validation()
        staff_program()

    elif user == '3':
        break

    else:
        print("Invalid input")
