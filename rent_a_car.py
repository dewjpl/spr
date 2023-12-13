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

    def utilization(self, start_hour, end_hour, plate_number=None):
        if plate_number:
            car = self.find_car_by_plate(plate_number)
            if car:
                utilization = self.calculate_utilization(start_hour, end_hour, car)
                print(f"Utilization for car {plate_number}: {utilization:.1f}%")
            else:
                print(f"Car with plate number {plate_number} does not exist")
        else:
            total_utilization = self.calculate_total_utilization(start_hour, end_hour)
            print(f"Total utilization for all cars: {total_utilization:.1f}%")

    def find_car_by_plate(self, plate_number):
        for car in self.cars:
            if car["plate_number"] == plate_number:
                return car
        return None

    def calculate_utilization(self, start_hour, end_hour, car):
        total_hours = end_hour - start_hour
        used_hours = 0

        for booking in car["booked"]:
            if not (end_hour <= booking["start_hour"] or start_hour >= booking["end_hour"]):
                used_hours += min(end_hour, booking["end_hour"]) - max(start_hour, booking["start_hour"])

        utilization = (used_hours / total_hours) * 100 if total_hours > 0 else 0
        return utilization

    def calculate_total_utilization(self, start_hour, end_hour):
        total_cars = len(self.cars)
        total_used_hours = 0
        total_hours = total_cars * (end_hour - start_hour)

        for car in self.cars:
            for booking in car["booked"]:
                if not (end_hour <= booking["start_hour"] or start_hour >= booking["end_hour"]):
                    total_used_hours += min(end_hour, booking["end_hour"]) - max(start_hour, booking["start_hour"])

        total_utilization = (total_used_hours / total_hours) * 100 if total_hours > 0 else 0
        return total_utilization

def main():
    rent_a_car = RentAcar()

    while True:
        command = input("> ")

        if command.startswith("add_car"):
            _, plate_number = command.split(" ")
            rent_a_car.add_car(plate_number)
        elif command.startswith("book_car"):
            _, start_hour, end_hour, customer_name = command.split(" ")
            rent_a_car.book_car(int(start_hour), int(end_hour), customer_name)
        elif command.startswith("utilization"):
            _, start_hour, end_hour, *plate_number = command.split(" ")
            plate_number = plate_number[0] if plate_number else None
            rent_a_car.utilization(int(start_hour), int(end_hour), plate_number)
        elif command == "quit":
            break

if __name__ == "__main__":
    main()
