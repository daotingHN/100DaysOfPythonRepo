#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)


########################## ERROR CATCH PATTER ##########################
# try:
#     # TRY reading file
#     file = open("a_file.txt", "r")
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["key"]
#
# except FileNotFoundError:
#     # EXCEPT when File Not Found, create file and write something
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message:
#     # EXCEPT when Key Error, get hold of error message and print DNE
#     print(f"The key {error_message} does not exist.")
#
# else:
#     # If TRY succeeds, read and print file content
#     content = file.read()
#     print(content)
#
# finally:
#     # FINALLY, close the file
#     file.close()
#     print("File was closed.")
#
#     # Voluntarily RAISE errors when FINALLY is met
#     raise KeyError("This is a bullshit error.")



########################## ERROR CATCH PATTER ##########################

height = float(input("Height (m): "))
weight = int(input("Weight (kg): "))

if height > 3:
    # ValueError: Valid code, bad input
    raise ValueError("The tallest man was only 2.72 meters tall.")

bmi = weight / height ** 2
print(bmi)