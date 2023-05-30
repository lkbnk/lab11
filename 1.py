class restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def d_restaurant(self):
        print(" Название ресторана: ",self.restaurant_name,"\n Тип кухни:  ", self.cuisine_type)
    def o_restaurant(self):
        print(" Ресторан открыт")

newRestaurant = restaurant("Теремок", " Руская ")

newRestaurant.d_restaurant()
newRestaurant.o_restaurant()