# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# # READ MODE "r"
# with open("my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

# # WRITE MODE "w"
# with open("new_file.txt", mode="w") as file:  # Can create new file if "w" mode and file DNE
#     file.write("New text.")
#
# # APPEND MODE "a"
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")


# # READ MODE "r" FROM Desktop
# with open("/Users/Darren Ting/Desktop/new_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

# READ MODE "r" RELATIVE from Desktop
with open("../../Desktop/new_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
