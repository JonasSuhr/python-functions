def create_user_profile(name, email, **kwargs):
    profile = {
        "Name": name,
        "Email": email 
    }

    for key, value in kwargs.items():
        profile[key] = value

    return profile


alice = create_user_profile(name="Alice", email="alice@example.com", Age="33", City="New York")
Bob = create_user_profile(name="Bob", last_name="Smith", email="bob@example.com", Age="22", Phone_number="1234567890")

print(alice)
print(Bob)