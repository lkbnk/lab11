class restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("Название ресторана: ",self.restaurant_name,"\nТип кухни:  ", self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт \n")

r_1 = restaurant("Mama Roma","Итальянская")
r_2 = restaurant("Маяк","Русская")
r_3 = restaurant("Тан-Жен","Русская")

r_1.describe_restaurant()
r_1.open_restaurant()
r_2.describe_restaurant()
r_2.open_restaurant()
r_3.describe_restaurant()
r_3.open_restaurant()