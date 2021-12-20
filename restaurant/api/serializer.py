from rest_framework import serializers

from .models import Restaurant, MenuCart, Product


class RestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=True)
    menuCarts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
        # fields = ['name', 'menuCarts']


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=50)
    price = serializers.FloatField()

    class Meta:
        model = Product
        fields = '__all__'


class MenuCartSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=False)
    restaurant = RestaurantSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCart
        fields = '__all__'
