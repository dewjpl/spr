class RentAcar:
    def __init__(self):
        self.cars = []

    def add_car(self, plate_number):
        for car in self.cars:
            if car["plate_number"] == plate_number:
                print("ERROR")
                return
        self.cars.append({"plate_number": plate_number, "booked": []})
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
    
    def check_availability(self, start_hour, end_hour):
        for car in self.cars:
            is_available = True
            
            for booked in car["booked"]:
                if not (end_hour <= booked["start_hour"] or start_hour >= booked["end_hour"]):
                    is_available = False
                    break

            if is_available:
                return car
        
        return None

