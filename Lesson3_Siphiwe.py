def total_height(user_list):
    return user_list[0]["height"] + user_list[1]["height"]

users = []

print("User 1")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

user1 = {
    "name": name,
    "age": age,
    "height": height
}
users.append(user1)

print("\nUser 2")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

user2 = {
    "name": name,
    "age": age,
    "height": height
}

users.append(user2)

print("User Information")

for user in users:
    print(user["name"], "is", user["age"], "years old and",
          user["height"], "cm tall.")

combined_height = total_height(users)

print("Their total combined height is", combined_height, "cm")