import json


def save_user_profile(profile):
    with open("user_profile.json", "w") as out:
        json.dump(profile["name"], out)


def load_profile(data):
    return json.loads(data)


if __name__ == "__main__":
    profile = {"name": "Alice", "age": 30}
    save_user_profile(profile)
    print(load_profile(profile))
