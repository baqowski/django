from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Restaurant
from ..serializer import RestaurantSerializer
from ..service import restaurant
from ..service.exception import RestaurantNotFoundException, RestaurantException


class RestaurantView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                return Response(RestaurantSerializer(restaurant.get_by_id(id)).data)
            except RestaurantNotFoundException as exc:
                return Response(exc.__str__(), status=status.HTTP_404_NOT_FOUND)
        return Response(RestaurantSerializer(Restaurant.objects.all(), many=True).data)

    def post(self, request):
        return restaurant.create(request)

    # toDo Put method

    def delete(self, request, id):
        try:
            restaurant.get_by_id(id).delete()
            return Response(status=status.HTTP_200_OK)
        except RestaurantNotFoundException as exc:
            return Response(exc.__str__(), status=status.HTTP_404_NOT_FOUND)
