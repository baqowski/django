from rest_framework import status
from rest_framework.response import Response

from .exception import RestaurantNotFoundException
from ..models import Restaurant
from ..serializer import RestaurantSerializer


def create(request):
    restaurant = RestaurantSerializer(data=request.data)
    if restaurant.is_valid():
        restaurant.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "error", "data": restaurant.errors}, status=status.HTTP_400_BAD_REQUEST)


def get_one_or_all(id):
    if id:
        try:
            restaurant = Restaurant.objects.get(id=id)
            serializer = RestaurantSerializer(data=restaurant)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(data={'Not found restaurant with id ': id}, status=status.HTTP_404_NOT_FOUND)
    else:
        restaurants = Restaurant.objects.all()
        print(restaurants)
        serializer = RestaurantSerializer(data=restaurants, many=True)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        print('not valid')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def remove(id):
    return get_by_id(id).delete()

# toDo Put method


def get_by_id(id):
    try:
        return Restaurant.objects.get(id=id)
    except Exception:
        raise RestaurantNotFoundException('Not found restaurant with id', id)
