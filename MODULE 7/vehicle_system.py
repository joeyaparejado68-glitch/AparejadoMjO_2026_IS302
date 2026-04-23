class Transport:
    def __init__(self, motor_brand, motor_model):
        self.motor_brand = motor_brand
        self.motor_model = motor_model


class Auto(Transport):
    def __init__(self, motor_brand, motor_model, model_year):
        super().__init__(motor_brand, motor_model)
        self.model_year = model_year

    def display_car(self):
        print(self.motor_brand, self.motor_model, self.model_year)


# Create object
vehicle_obj = Auto("Suzuki", "Smash fi", 2025)

# Display info
vehicle_obj.display_car()