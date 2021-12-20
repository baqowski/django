from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return {self.id, self.name}


class Product(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.FloatField(default=0)

    # docelowo typ to PIZZA, DINNER itp

    def __str__(self):
        return {self.id, self.name, self.type}


class MenuCart(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, related_name='products')
    restaurant = models.ForeignKey(Restaurant, related_name='menuCarts', null=True, blank=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __add__(self, product):
        self.products.add(product)
        return None


class Order(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return self.name


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return {self.product, self.order}
