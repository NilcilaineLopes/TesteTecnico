def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "phone": user["phone"],
        "profession": user["profession"],
        "cit": user["cit"],
        "district": user["district"],
        "Street": user["Street"],
        "numberHouse": user["numberHouse"],
        "zipcode": user["zipcode"],
    }

def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]