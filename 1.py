class restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("Название ресторана: ",self.restaurant_name,"\nТип кухни:  ", self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт")

newRestaurant = restaurant("Теремок", "Руская")

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()