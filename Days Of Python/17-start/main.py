class User:

    # Constructor
    def __init__(self, user_id, username):
        # Name of Parameter often same as Attribute
        self.id = user_id
        self.username = username
        self.followers = 0  # Default Value, no need Input Parameter
        self.following = 0
        # print("new user being created...")

    def follow(self, user):
        user.followers += 1  # Do to selected user
        self.following += 1  # Do to itself


# Using Constructor
user_1 = User("001", "angela")
user_2 = User("002", "darren")

user_1.follow(user_2)


# NOT Using Constructor
# user_2 = User()
# user_2.id = "002"
# user_2.username = "darren"


print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


