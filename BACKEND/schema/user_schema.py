def car_serializer(user)->dict:
    return {
        "username": user["username"],
        "password": user["password"],
        
    }

