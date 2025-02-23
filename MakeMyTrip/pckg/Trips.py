class TripPlanner:
    def __init__(self):
        self.trips = {
            "national": {
                "beach": [
                    {"destination": "Goa Beach", "price_per_person": 1000},
                    {"destination": "Kochi Beach", "price_per_person": 1200},
                ],
                "city": [
                    {"destination": "Jaipur City Tour", "price_per_person": 1500},
                    {"destination": "Delhi City Tour", "price_per_person": 1800},
                ],
                "temple": [
                    {"destination": "Tirupati Temple", "price_per_person": 1200},
                    {"destination": "Varanasi Pilgrimage", "price_per_person": 1300},
                ],
                "destination_wedding": [
                    {"destination": "Udaipur Royal Wedding", "price_per_person": 4500},
                    {"destination": "Goa Beach Wedding", "price_per_person": 4700},
                ],
            },
            "international": {
                "beach": [
                    {"destination": "Maldives Beach", "price_per_person": 5000},
                    {"destination": "Bora Bora Beach", "price_per_person": 6000},
                ],
                "city": [
                    {"destination": "Paris City Tour", "price_per_person": 10000},
                    {"destination": "New York City Tour", "price_per_person": 12000},
                ],
                "temple": [
                    {"destination": "Angkor Wat Temple", "price_per_person": 8000},
                    {"destination": "Golden Temple Amritsar", "price_per_person": 7000},
                ],
                "destination_wedding": [
                    {"destination": "Paris Destination Wedding", "price_per_person": 15000},
                    {"destination": "Santorini Wedding", "price_per_person": 17000},
                ],
            },
        }
        self.trips_booked = {}  # To store booked trips per user

    def display_trip_types(self):
        print("\nChoose your trip type:")
        print("1. National Trip")
        print("2. International Trip")
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            print("\nYou chosed a National Trip.")
            return "national"
        elif choice == "2":
            print("\nYou chose an International Trip.")
            return "international"
        else:
            print("Invalid choice. Please choose either 1 or 2.")
            return self.display_trip_types()

    def display_categories(self, trip_type):
        print(f"\nChoose your trip category for {trip_type.capitalize()} trips:")
        categories = self.trips[trip_type]
        for idx, category in enumerate(categories.keys(), start=1):
            print(f"{idx}. {category.capitalize()}")
        choice = input("Enter your choice (1-4): ").strip()

        categories_list = list(categories.keys())
        if choice.isdigit() and 1 <= int(choice) <= len(categories_list):
            print(f"\nYou chose the {categories_list[int(choice) - 1].capitalize()} category.")
            return categories_list[int(choice) - 1]
        else:
            print("Invalid choice. Please choose a valid category.")
            return self.display_categories(trip_type)

    def process_payment(self, total_cost):
        print(f"\n--- Payment Portal ---")
        print(f"Total Amount to be Paid: ${total_cost:.2f}")
        print("Choose a payment method:")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. Net Banking")
        print("4.Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice in ["1", "2", "3"]:
            payment_details = input("Enter payment details (Card Number/UPI ID): ")
            print(f"Processing payment of ${total_cost:.2f}...")
            print("Payment successful! Your trip is confirmed.Thank you for booking with Make My Trip!")
            return True
        elif choice == "4":
            print("\nBooking process incomplete. Please revisit the payment portal.")
        else:
            print("Invalid payment choice. Payment failed.")
            return False

    def recommend_trip(self, trip_type, category, budget, num_people, user_name):
        print(f"\nPlanning a {trip_type.capitalize()} trip with a budget of ${budget} for {num_people} people...")

        available_trips = self.trips[trip_type][category]
        possible_trips = []

        for package in available_trips:
            total_cost = package["price_per_person"] * num_people
            if total_cost <= budget:
                possible_trips.append((package, total_cost))

        if not possible_trips:
            print("\nNo packages available within your budget and preference.")
        else:
            print("\nRecommended Packages within your budget:")
            for idx, (package, total_cost) in enumerate(possible_trips, start=1):
                print(f"{idx}. {package['destination']} - Total Cost: ${total_cost}")

            # Allow the user to book a trip
            choice = int(input("Enter the number of the package you want to book (or 0 to skip): "))
            if 1 <= choice <= len(possible_trips):
                selected_trip, total_cost = possible_trips[choice - 1]
                print(f"\nYou have selected: {selected_trip['destination']} - Total Cost: ${total_cost:.2f}")
                
                # Process Payment
                if self.process_payment(total_cost):
                    self.trips_booked[user_name] = {
                        "trip_type": trip_type,
                        "category": category,
                        "destination": selected_trip["destination"],
                        "total_cost": total_cost,
                        "num_people": num_people
                    }
                else:
                    print("Payment failed. Trip booking canceled.")

    def plan_trip(self, user_name):
        print("\n--- Step 1: Trip Type Selection ---")
        trip_type = self.display_trip_types()

        print("\n--- Step 2: Trip Category Selection ---")
        category = self.display_categories(trip_type)

        print("\n--- Step 3: Budget and Number of People ---")
        budget = float(input(f"\nEnter your budget for the {category} trip: $"))
        num_people = int(input("Enter the number of people: "))

        print("\n--- Step 4: Trip Recommendation ---")
        self.recommend_trip(trip_type, category, budget, num_people, user_name)

    def view_my_trip(self, user_name):
        if user_name in self.trips_booked:
            trip_details = self.trips_booked[user_name]
            print("\n--- Your Trip Details ---")
            print(f"Trip Type: {trip_details['trip_type'].capitalize()}")
            print(f"Category: {trip_details['category'].capitalize()}")
            print(f"Destination: {trip_details['destination']}")
            print(f"Number of People: {trip_details['num_people']}")
            print(f"Total Cost: ${trip_details['total_cost']}")
        else:
            print("\nYou have not booked any trips yet.")