class RestaurantException(Exception):

    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class RestaurantNotFoundException(RestaurantException):

    def __init__(self, message, value) -> None:
        self.message = message
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} {self.value}'
