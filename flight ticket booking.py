print("<<<<<<>>>>>>Welcome to TATA Airline<<<<<<>>>>>>")

class Flight:
    def __init__(self, flight_number, seats, business_class_rate, economy_class_rate):
        self.flight_number = flight_number
        self.seats = seats
        self.business_class_rate = business_class_rate
        self.economy_class_rate = economy_class_rate

    def book_ticket(self):
        #print("\n")
        print("==========================================")
        print("Please enter your details to book the ticket")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        contact_number = input("Enter your contact number: ")
        #print("\n")

        meals = input("Do you want meals? (yes or no): ")
        seat_type = input("Which class do you want to book? (business or economy): ")
        seat_number = None

        if seat_type == "business":
            seat_number = self._get_seat_number("business")
            print("Enjoy your business class!")
            ticket_price = self.business_class_rate
        elif seat_type == "economy":
            seat_number = self._get_seat_number("economy")
            print("Enjoy your economy class!")
            ticket_price = self.economy_class_rate
        else:
            print("Invalid input. Please enter either business or economy.")
            return

        if meals == "yes":
            print("Enjoy your meals!")
            ticket_price += 500

        print(f"Thank you for booking with TATA Airline, {name}!")
        print(f"Your seat number is {seat_number}.")
        print(f"Your ticket price is {ticket_price}.")
        print("==========================================")
        print("\n")

    def _get_seat_number(self, class_type):
        if class_type == "business":
            for i in range(1, 7):
                if self.seats[i] == 0:
                    self.seats[i] = 1
                    return i
        elif class_type == "economy":
            for i in range(7, 16):
                if self.seats[i] == 0:
                    self.seats[i] = 1
                    return i

        print(f"Sorry, {class_type} class is full.")
        return None

flight_101 = Flight("101", [0]*16, 4000, 2000)
flight_102 = Flight("102", [0]*16, 3500, 1500)

while True:
    print("Which flight do you want to book?")
    flight_number = input("Enter 101 for Flight 101 or 102 for Flight 102: ")
    if flight_number == "101":
        flight_101.book_ticket()
    elif flight_number == "102":
        flight_102.book_ticket()
    else:
        print("Invalid input. Please enter either 101 or 102.")
