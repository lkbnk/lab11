class restaurant:
    def __init__(self,name, type, rating):
        self.restaurant_name = name
        self.cuisine_type = type
        self.rating = rating
    def new_rating(self, new_rating):
        self.rating = new_rating
        print("Новый рейтинг ресторана: ", self.restaurant_name, "-", self.rating)

r = restaurant("Маяк", "Русская", 1)
print("Изначальный рейтинг ресторана:", r.restaurant_name, "-",  r.rating)
r.new_rating(5)