import io
import json
import os
from datetime import datetime

# import pyautogui

# Global Variables
MONTHS = ["Jan", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"]
CURRENT_MONTH = datetime.now().month - 1
TAX_RATE = 0.17  # or 0.155671, 0.159, 0.124, 0.106, 0.114, 0.169 (0.169 max found)
TITHING = 0.1
FUN_PERCENT_CUT = 0.025
TUITION_TOTAL = 1576
PAYMENT_RATE = 22
AVERAGE_OF_CLASSES_MISSED = 0.1  # 10% classes are missed


#
def organizeData(info):
    """
    Organizes the given information dictionary to include the account name and each month if present.

    :param info: The original information dictionary.
    :return: The organized information dictionary.
    """

    return {key: info[key] for key in ["name"] + MONTHS if key in info}


#
def getContents(file_name):
    """
    Retrieves the contents of a JSON file, or creates the file if it does not exist.

    :param file_name: The name of the file to retrieve or create.
    :return: The contents of the file, if it exists and is not empty.
    """

    file_path = f"./{file_name}.json"

    # Checks if the file exists and is readable
    if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
        # Checks if the file size is more than 2 bytes
        if os.path.getsize(file_path) > 2:
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            print(f"{file_name}.json is empty")
            exit(1)
    else:  # If the file is missing or not readable, create the file
        with open(file_path, 'w') as db_file:
            json.dump({}, db_file)
        print("The file did not exist so an empty one was created")


#
# def clearScreen():
#     pyautogui.click(x=730, y=920)  # Generally click on output terminal
#     pyautogui.hotkey('ctrl', 'l')  # Shortcut to clear the screen


#
def calcMaxSize(info):
    """
    Calculates maximum sizes for printing tables.

    :param info: The information to be printed, in dictionary format.
    :return: A tuple containing the maximum type size and maximum value size.
    """

    # The maximum type size is at least the length of the account name
    max_type_size = len(info.get("name", ""))

    # The maximum value size is initially set to the length of each month name
    max_value_size = {month: max(3, len(str(info.get(month, "")))) for month in MONTHS}

    # Determine maximum lengths for each type and value
    for month, data in info.items():
        if isinstance(data, dict):
            max_type_size = max(max_type_size, max((len(category) for category in data.keys()), default=0))
            max_value_size[month] = max(max_value_size.get(month, 0),
                                        max((len(str(value)) for value in data.values()), default=0))

    return max_type_size, max_value_size


# Pad output with spaces
def pad(_item, _maxSize):
    """
    Returns a string padded with spaces to a specified size.

    :param _item: The item to convert to a string and pad.
    :param _maxSize: The size to pad the string to.
    :return: A string representation of _item, padded with spaces to _maxSize.
    """
    return str(_item).ljust(_maxSize)


# Write a print function to print out the tables of each section
def printTables(_info):
    """
    Prints tables from the provided information.

    :param _info: The information to print, in a dictionary format.
    """

    maxTypeSize, maxValueSize = calcMaxSize(_info)

    # Print the top row with name and month names
    for key in ['name'] + MONTHS:
        if key in _info:
            print(pad(key, maxValueSize.get(key, 0)), end="\t")
    print()

    # Get data for the first month available in _info
    month_data = next((_info[month] for month in MONTHS if month in _info), {})

    # Print each category per month
    for category in month_data.keys():  # "Jan" is just general in order to loop through the types
        # Print resized key/name
        print(pad(category, maxTypeSize), end="\t")

        # Print padded data
        for month in MONTHS:
            if month in _info and category in _info[month]:
                print(pad(_info[month][category], maxValueSize[month]), end="\t")
        print()


# Sort dictionary/table
def sortInfo(_info, _category=None, _month=None):
    """
    This function sorts a given dictionary based on specified categories and/or months.

    :param _info: original dictionary to be sorted.
    :param _category: list of categories to include in the sorted dictionary. If None, all categories are included.
    :param _month: list of months to include in the sorted dictionary. If None, all months are included.
    :return: sorted dictionary.
    """

    # Initialize the sorted dictionary with the account name
    sortedDict = {"name": _info.get("name", "")}

    # Loop over the months defined in the MONTHS list
    for _monthName in MONTHS:

        # Check if the month exists in the input dictionary
        if _monthName in _info:

            # Check if a specific category is given or if the given category exists in the month's info
            if _category is None or any(_originalCategory in _category for _originalCategory in _info[_monthName]):
                # If a specific category is provided, include only those categories.
                # If no specific category is provided, include all categories.
                # Do this only if the month is in the given month list, or if no specific month is given.
                sortedDict[_monthName] = {
                    _originalCategory: _info[_monthName][_originalCategory]
                    for _originalCategory in _info[_monthName]
                    if _category is None or _originalCategory in _category
                }

    return sortedDict


# Input to clear
def Input(prompt):
    val = input(prompt)
    # clearScreen()
    return val


# Compare the two (also possible print these out using the function?)
# Then work on a way to get the inputs easily from the user
# Add option to enter amount spent on food
# Add option to enter estimated bimonthly hours and actual bimonthly hours
# Implement option to look for and remove the letter 'c' from numeric input to add comment
# Compare values and find differences
# Add option to use current month by default unless specified to the contrary
# Possibly combine the projected and the savings files together

def updateValue(info, selection):
    # Update a value in the selected account
    print(f"Selected: Update Value in {selection}")
    print("Enter a Value, Month, and Category")

    # Input and validate value
    value = input("Value: ")
    comment = ""
    if "c" in value:
        value, comment = value.split("c")

    # Ensure value is an integer
    try:
        value = int(value)
    except ValueError:
        print("Invalid input. Please input a valid integer value.")
        return info

    # Input and validate month
    month = input("Month (leave blank for current month): ")
    if month == "":
        month = datetime.now().strftime('%B')
    while month not in MONTHS:
        month = input("Please enter a valid Month: ")

    # Input and validate category
    category = input("Category: ")
    while category not in info[month]:
        category = input("Please input a valid Category: ")

    # Update the value for the given month and category
    info[month][category] = {"value": value, "comment": comment}

    return info


def terminalFinance():
    """
    A terminal-based financial management program. Allows for managing multiple accounts and performing various operations on them.
    """
    option = ""
    selection = ""

    while option != "quit":
        # Load accounts
        accounts = getContents("Accounts")

        # Display and select budget type
        for key, value in accounts.items():
            print(f"{key}. {value['name']}")
        option = input("Select Budget Type: ")
        while option not in accounts:
            option = input(f"Select a valid option (1-{len(accounts)}): ")

        # Update accounts and remove "name" field
        accounts = accounts[option]
        selection = accounts['name']
        print(f"Selected: {selection}")
        del accounts["name"]

        # Display and select account option
        for key, value in accounts.items():
            print(f"{key}. {value}")
        option = input("Select Account Option: ")
        while option not in accounts:
            option = input(f"Select a valid option (1-{len(accounts)}): ")

        selection = f"{selection} {accounts[option]}"

        # Load and organize the selected account's data
        info = organizeData(getContents(selection))
        print(f"Selected: {selection}")

        # Display main menu options
        print(f"""Options:
    1. Update value
    2. Print
    3. Graph
    4. Edit Fields""")
        repeat = True
        while repeat:
            repeat = False
            option = input("Select a value 1-4: ")
            if option == "1":
                info = updateValue(info, selection)

            elif option == "2":
                # Print the selected account's data
                print(f"Selected: Print {selection}")
                option = input("Enter 1 to sort or anything else to continue: ")
                if option == "1":
                    print("Nothing here yet... Sorry for the inconvenience")  # Sort and get inputs
                else:
                    printTables(info)

            elif option == "3":
                # Graph the selected account's data
                print(f"Selected: Graph {selection}")
                print("Again, nothing here yet...")

            elif option == "4":
                # Edit the selected account's fields
                print(f"Selected: Edit Fields in {selection}")
                print("""Options:
                         1. Add Field
                         2. Remove Field
                         3. Rename Field""")
                option = input("Select a value 1-3: ")
                print("Again, nothing here yet...")

            else:
                # Reprint the main menu options if the input was invalid
                print(f"""Options:
    1. Update value
    2. Print
    3. Graph
    4. Edit Fields""")
                option = input(f"Select a valid option (1-4): ")
                repeat = True

        # Save the updated account data back to the file
        with open(f"./{selection}.json", 'w') as file:
            json.dump(info, file, indent=2)


def manualAdjustment():
    """
    Loads information from a file, performs some operations, and writes the updated information back to the file.
    """

    # Name of the file to read from and write to (without the .json extension)
    fileName = "Projected Savings"

    # Load and organize the information from the file
    info = organizeData(getContents(fileName))

    # Uncomment the block below if you want to set all of a specific category to a value
    """
    category = "6-Month"
    for month in info:
        if isinstance(info[month], dict):
            if category not in info[month]:
                print("Not found")
                exit(1)
            info[month][category] = 25
    """

    # Sort the information by specific categories and print the sorted tables
    sortedInfo = sortInfo(info, _category=["Total", "Tuition"])
    printTables(sortedInfo)

    # Write the updated information back to the file
    with open(f"./{fileName}.json", 'w') as file:
        json.dump(info, file, indent=2)


manualAdjustment()

"""
# Sort dictionary/table
def sort(_info, _category=None, _month=None):
    # Add account name
    sortedDict = {"name": _info["name"]}

    # Add months in order
    for month in MONTHS:
        # If _category is specified verify month is in new dictionary and add only specified types
        if _category is not None:
            for originalCategory in _info[month]:
                if originalCategory in _category and (_month is None or month in _month):
                    if month not in sortedDict:
                        sortedDict[month] = {}
                    sortedDict[month][originalCategory] = _info[month][originalCategory]
        # If there is no _category specifier copy everything into the month
        elif _month is not None:
            if month in _month:
                sortedDict[month] = _info[month]
        else:
            sortedDict[month] = _info[month]

    return sortedDict


def sort(_info, _category=None, _month=None):
    # Add account name
    sortedDict = {"name": _info.get("name", "")}

    # Add months in order
    for _monthName in MONTHS:
        # If _category is specified verify month is in new dictionary and add only specified types
        if _monthName in _info:
            if _category is None or any(_originalCategory in _category for _originalCategory in _info[_monthName]):
                sortedDict[_monthName] = {_originalCategory: _info[_monthName][_originalCategory] for _originalCategory
                                          in _info[_monthName]
                                          if _category is None or _originalCategory in _category} if _category else _info[_monthName]

    return sortedDict

def sort_info(_info, _category=None, _month=None):
    \"""
    This function sorts a given dictionary based on specified categories and/or months.

    :param _info: original dictionary to be sorted.
    :param _category: list of categories to include in the sorted dictionary. If None, all categories are included.
    :param _month: list of months to include in the sorted dictionary. If None, all months are included.
    :return: sorted dictionary.
    \"""

    # Initialize the sorted dictionary with the account name
    sortedDict = {"name": _info.get("name", "")}

    # Loop over the months defined in the MONTHS list
    for _monthName in MONTHS:

        # Check if the month exists in the input dictionary
        if _monthName in _info:

            # Check if a specific category is given or if the given category exists in the month's info
            if _category is None or any(_originalCategory in _category for _originalCategory in _info[_monthName]):

                # If a specific category is provided, include only those categories.
                # If no specific category is provided, include all categories.
                # Do this only if the month is in the given month list, or if no specific month is given.
                sortedDict[_monthName] = { 
                    _originalCategory: _info[_monthName][_originalCategory] 
                    for _originalCategory in _info[_monthName] 
                    if _category is None or _originalCategory in _category 
                } 

    return sortedDict
"""
