def car_serializer(car)->dict:
    return {
        "id": str(car["_id"]),
        "marca": car["marca"],
        "modelo": car["modelo"],
        "año": car["año"],
        "precio": car["precio"],
        "kilometraje": car["kilometraje"],
        "color": car["color"],
        "imagen_principal": car["imagen_principal"],
        "descripcion": car["descripcion"],
        "urlShop": car["urlShop"],
    }

def cars_serializer(cars) -> list:
    return [car_serializer(car) for car in cars]