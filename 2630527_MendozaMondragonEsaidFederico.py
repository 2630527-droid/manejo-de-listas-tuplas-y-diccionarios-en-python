# Name: Esaid Federico Mendoza Mondragon 
# Student ID: 2630527
# Group: IM 1-2
# File: 2630527_Men.py

# EXECUTIVE SUMMARY
# A list is an ordered collection that can be changed after it is created.
# A tuple is an ordered collection that cannot be changed after it is created.
# A dictionary stores information as key-value pairs.
# Lists are mutable, so items can be added or removed.
# Tuples are immutable, so they are useful for fixed data such as coordinates.
# Dictionaries let us find information by using a key.
# This file contains six beginner exercises using lists, tuples, and dictionaries.
# Each problem includes inputs, outputs, validations, and three test cases.
# The exercises cover shopping items, points, products, grades, word counts, and contacts.

# PRINCIPLES AND GOOD PRACTICES
# Use lists when items may need to be added or removed.
# Use tuples for data that should not change, such as coordinates.
# Use dictionaries to find information by a key, such as a name or code.
# Avoid changing a list while looping through it with for.
# Use descriptive dictionary keys, such as "name", "age", and "price".
# Write readable code and clear messages for the user.


# PROBLEM 1: SHOPPING LIST BASICS
# Description:
# Create a list of products, add one product, show the number of
# products, and check whether a product is in the list.
#
# Inputs:
# - initial_items_text: product names separated by commas.
# - new_item: product to add.
# - search_item: product to search for.
#
# Outputs:
# - Items list, total items, and whether the product was found.
#
# Validations:
# - The initial text, new item, and search item cannot be empty.
# - Spaces around product names are removed.
#
# Test cases:
# 1) Normal: "apple, banana", add "orange", search "banana".
# 2) Border: "apple", add "pear", search "pear".
# 3) Error: empty initial text; an error message is shown.

initial_items_text = input("Enter products separated by commas: ")

if initial_items_text.strip() == "":
    print("Error: initial items cannot be empty")
else:
    items_list = initial_items_text.split(",")
    clean_items_list = []

    for item in items_list:
        if item.strip() != "":
            clean_items_list.append(item.strip())

    if len(clean_items_list) == 0:
        print("Error: no valid products were entered")
    else:
        new_item = input("Enter a new product: ").strip()
        search_item = input("Enter a product to search for: ").strip()

        if new_item == "" or search_item == "":
            print("Error: product names cannot be empty")
        else:
            clean_items_list.append(new_item)
            is_in_list = search_item in clean_items_list

            print("Items list:", clean_items_list)
            print("Total items:", len(clean_items_list))
            print("Found item:", is_in_list)


# PROBLEM 2: POINTS AND DISTANCES WITH TUPLES
# Description:
# Store two 2D points in tuples, calculate the distance between
# them, and create a tuple with the midpoint.
#
# Inputs:
# - x1, y1, x2, y2: numeric coordinates.
#
# Outputs:
# - Point A, Point B, distance, and midpoint.
#
# Validations:
# - The user must enter numeric values for all coordinates.
# - To keep the code at beginner level, enter numbers as instructed.
#
# Test cases:
# 1) Normal: A=(0, 0), B=(3, 4); distance is 5.
# 2) Border: A=(2, 2), B=(2, 2); distance is 0.
# 3) Error: entering text instead of a number cannot be processed by float().


print("Enter numbers for the coordinates.")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

point_a = (x1, y1)
point_b = (x2, y2)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", round(distance, 2))
print("Midpoint:", midpoint)



# PROBLEM 3: PRODUCT CATALOG WITH DICTIONARY
# Description:
# Use a dictionary of product prices and calculate the total
# cost for a product and quantity.
#
# Inputs:
# - product_name: product name.
# - quantity: number of units.
#
# Outputs:
# - Unit price, quantity, and total, or an error message.
#
# Validations:
# - The product name cannot be empty.
# - Quantity must be greater than zero.
# - The product must exist in the dictionary.
# - Enter a whole number for quantity.
#
# Test cases:
# 1) Normal: product "apple", quantity 2.
# 2) Border: product "bread", quantity 1.
# 3) Error: unknown product or quantity equal to 0.

product_prices = {"apple": 10.0, "bread": 25.0, "milk": 30.0}

product_name = input("Enter a product name: ").strip().lower()

if product_name == "":
    print("Error: product name cannot be empty")
else:
    quantity = int(input("Enter quantity as a whole number: "))

    if quantity <= 0:
        print("Error: quantity must be greater than zero")
    elif product_name not in product_prices:
        print("Error: product not found")
    else:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity

        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", round(total_price, 2))


# PROBLEM 4: STUDENT GRADES WITH DICTIONARY AND LIST
# Description:
# Store student grades in lists inside a dictionary.
# Calculate the average and check whether the student passed.
#
# Inputs:
# - student_name: student's name.
#
# Outputs:
# - Grades, average, and passed status, or an error message.
#
# Validations:
# - The student's name cannot be empty.
# - The student must exist in the dictionary.
# - The grade list must not be empty before calculating an average.
#
# Test cases:
# 1) Normal: "Alice" has grades [90, 85, 80].
# 2) Border: "Bob" has one grade [70].
# 3) Error: enter a name that is not in the dictionary.


grades = {
    "Alice": [90.0, 85.0, 80.0],
    "Bob": [70.0],
    "Charlie": [60.0, 65.0, 68.0]
}

student_name = input("Enter a student name: ").strip()

if student_name == "":
    print("Error: student name cannot be empty")
elif student_name not in grades:
    print("Error: student not found")
else:
    student_grades = grades[student_name]

    if len(student_grades) == 0:
        print("Error: grade list is empty")
    else:
        average = sum(student_grades) / len(student_grades)
        is_passed = average >= 70.0

        print("Grades:", student_grades)
        print("Average:", round(average, 2))
        print("Passed:", is_passed)


# PROBLEM 5: WORD FREQUENCY COUNTER
# Description:
# Convert a sentence to lowercase, split it into words, count
# each word with a dictionary, and find the most common word.
#
# Inputs:
# - sentence: a sentence entered by the user.
#
# Outputs:
# - Words list, frequency dictionary, and most common word.
#
# Validations:
# - The sentence cannot be empty.
# - Simple punctuation marks are removed.
# - The word list must not be empty.
#
# Test cases:
# 1) Normal: "cat dog cat"; cat appears twice.
# 2) Border: "hello"; hello appears once.
# 3) Error: an empty sentence.

sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: sentence cannot be empty")
else:
    sentence = sentence.lower()
    sentence = sentence.replace(".", "")
    sentence = sentence.replace(",", "")
    sentence = sentence.replace("!", "")
    sentence = sentence.replace("?", "")
    words_list = sentence.split()

    if len(words_list) == 0:
        print("Error: no words were found")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] = freq_dict[word] + 1
            else:
                freq_dict[word] = 1

        most_common_word = words_list[0]

        for word in freq_dict:
            if freq_dict[word] > freq_dict[most_common_word]:
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# PROBLEM 6: SIMPLE CONTACT BOOK
# Description:
# Use a dictionary to add, search, or delete a contact.
# Contact names are keys and phone numbers are values.
#
# Inputs:
# - action_text: ADD, SEARCH, or DELETE.
# - name: contact name.
# - phone: phone number, only for ADD.
#
# Outputs:
# - A message describing the result of the operation.
#
# Validations:
# - The action must be ADD, SEARCH, or DELETE.
# - The contact name cannot be empty.
# - For ADD, the phone number cannot be empty.
#
# Test cases:
# 1) Normal: ADD "Dana" with phone "1234567890".
# 2) Border: SEARCH for an existing contact.
# 3) Error: use an unsupported action or search for a missing contact.

contacts = {"Alice": "1112223333", "Bob": "4445556666"}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    name = input("Enter contact name: ").strip()

    if name == "":
        print("Error: contact name cannot be empty")
    elif action_text == "ADD":
        phone = input("Enter phone number: ").strip()

        if phone == "":
            print("Error: phone number cannot be empty")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")


# CONCLUSIONS
# Lists are useful when a collection needs to change over time.
# They allow items to be added or removed with simple operations.
# Tuples are useful for fixed data that should not be changed.
# Dictionaries connect keys with values and make searches easier.
# A dictionary can contain lists, such as a student's grades.
# These exercises show that each collection is useful for a different purpose.
# Checking inputs helps prevent common errors during processing.
# Clear variable names and messages make programs easier to understand.


# REFERENCES
# 1) Python Software Foundation. Built-in Types:
#    https://docs.python.org/3/library/stdtypes.html
# 2) Python Software Foundation. Data Structures:
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Python Software Foundation. Input and Output:
#    https://docs.python.org/3/tutorial/inputoutput.html
# 4) Python Software Foundation. Errors and Exceptions:
#    https://docs.python.org/3/tutorial/errors.html
# 5) Python Software Foundation. Control Flow Tools:
#    https://docs.python.org/3/tutorial/controlflow.html
