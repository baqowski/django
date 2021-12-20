from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant, MenuCart, Product
from .serializer import RestaurantSerializer, MenuCartSerializer, ProductSerializer
from .service import restaurant


# class RestaurantView(APIView):
#     def get(self, request, id=None):
#         if (id):
#             serializer = RestaurantSerializer(Restaurant.objects.get(id=id))
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         restaurants = Restaurant.objects.all()
#         serializer = RestaurantSerializer(restaurants, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         return restaurant.create(request)


class MenuCartView(APIView):
    def post(self, request):
        serializer = MenuCartSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        menuCart = MenuCart.objects.get(id=id)
        ids = request.data.get('products')
        for i in ids:
            print(i.get('id'))
            product = Product.objects.get(id=i.get('id'))
            menuCart.products.add(product)

        serializer = MenuCartSerializer(menuCart, request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            menuCart = MenuCartSerializer(MenuCart.objects.get(id=id))
            return Response({"status": "success", "data": menuCart.data}, status=status.HTTP_200_OK)

        menuCarts = MenuCart.objects.all()
        serializer = MenuCartSerializer(menuCarts, many=True)
        return Response(serializer.data)


class ProductView(APIView):
    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": product.errors}, status=status.HTTP_400_BAD_REQUEST)

# class OrderView(APIView):
#     def post(self, request):
