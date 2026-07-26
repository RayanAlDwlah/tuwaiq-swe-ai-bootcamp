user = {"name": "Sara", "age": 28}

print(user["name"])
print(user.get("email", "no email"))

for key, value in user.items():
    print(key, "=", value)
