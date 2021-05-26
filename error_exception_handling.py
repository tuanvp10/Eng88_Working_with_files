# `try`, `except` and `finally` block of codes

# They as if and else block

# Create a function called greetings
# def greetings():
#       pass

# name = 'devops'
# year = 2021
# print(name + year)
# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     # raise
# # Creating aliases
#     print("order.txt not found" + str(errmsg))
#
# finally:
#     print("Thank you for visiting, hope to see you again!")


# Second Iteration
# def open_using_with_and_print(file):
#
#     try:
#         with open("order.txt", "r") as file:
#             for line in file.readlines():
#                 print(line.rstrip('\n'))
#     # try code block ends
#     except FileNotFoundError as errmsg:
#         print("Sorry file not found :( ")
#         # raise
#         #print("order.txt not found" + str(errmsg))
#
#     finally:
#         return "Thank you for visiting, hope to see you again!"
#
# print(open_using_with_and_print("order.txt"))

# Create a function to called open_with_to_write_to_file write/add/append
# Display the data with the added items - item names = Pizza, Velvet Cake, Avacado, Biriyani, Pasta

def open_with_to_write_to_file(file, new_items):
    try:
        with open("order.txt", "a") as file: # a = open file in append mode to add new items to the list
            for item in new_items:
                file.write('\n' + item)
        with open("order.txt", "r") as file: # r = opens document for reading
            for line in file.readlines():
                print(line.rstrip('\n'))
    # try code block ends
    except FileNotFoundError as errmsg:
        print("Sorry file not found :( ")
        # raise
        #print("order.txt not found" + str(errmsg))
    finally:
        return "Thank you for visiting, hope to see you again!"

new_items = ["Pizza", "Velvet Cake", "Avocado", "Biriyani", "Pasta"]

print(open_with_to_write_to_file("order.txt", new_items))