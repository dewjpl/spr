class RentAcar:
    def __innit__(self):
        self.cars = []

    def add_car(self, plate_number):
        for car in self.cars:
            if car["plate_number"]  == plate_number:
                print("ERROR")
                return
            self.cars.append(plate_number)
            print("OK")

    def book_car(self, start_hour, end_hour, customer_name):
        availability = self.check_availability(start_hour, end_hour)

        if availability:
            availability["booked"].append({
                "start_hour": start_hour,
                "end_hour": end_hour,
                "customer_name": customer_name
            })
            print("OK")
        else:
            print("ERROR")
    
    def check_availability(self, start_hour, end_hour)


book car start_hour end_hour customer_name	Rezerwuje samochód w czasie pomiędzy start_hour a end_hour dla klienta o customer_name	Nie ma dostępnych samochodów w okresie pomiędzy start_hour a end_hour