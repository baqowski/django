from django.urls import path
from .view import restaurant
from .views import MenuCartView, ProductView

urlpatterns = [
    path('restaurants', restaurant.RestaurantView.as_view()),
    path('restaurants/<int:id>', restaurant.RestaurantView.as_view()),
    path('menu-carts', MenuCartView.as_view()),
    path('menu-carts/<int:id>', MenuCartView.as_view()),
    path('products', ProductView.as_view()),

]
