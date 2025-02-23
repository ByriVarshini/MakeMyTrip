from pckg.User import User
from pckg.Admin import Admin
from pckg.Trips import TripPlanner

def main():
    is_logged_in = False  # Flag to track login status
    current_user = None   # Store the currently logged-in user
    planner=TripPlanner()
    while True:
        print("\n--- User and Admin Management ---")
        print("1. Login as User/Admin")
        print("2. Plan a Trip")
        print("3. View My Trip")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ch = input("Enter User or Admin (U/A): ").upper()
            if ch == "U":
                current_user = User.user_login()
                if current_user:
                    is_logged_in = True
                    print("User login successful!")
            elif ch == "A":
                print("\n--- Admin Panel ---")
                A_name = input("Enter your name: ")
                A_pass = input("Enter your password: ")
                if A_name == Admin.Admin_name and A_pass == Admin.Admin_pass:
                    is_logged_in = True
                    print("Welcome Admin!")
                    while True:
                        print("\n--- Admin Panel ---")
                        print("1. View All Users")
                        print("2. Edit User")
                        print("3. Delete User")
                        print("4. Logout")
                        admin_choice = input("Enter your choice: ")

                        if admin_choice == "1":
                            Admin.view_all_users()
                        elif admin_choice == "2":
                            email_to_edit = input("Enter the email of the user to edit: ")
                            Admin.edit_user(email_to_edit)
                        elif admin_choice == "3":
                            email_to_delete = input("Enter the email of the user to delete: ")
                            Admin.delete_user(email_to_delete)
                        elif admin_choice == "4":
                            print("Admin logged out.")
                            is_logged_in = False
                            break
                        else:
                            print("Invalid admin choice.")
                else:
                    print("Invalid admin credentials.")
            else:
                print("Invalid input. Please choose U for User or A for Admin.")

        elif choice in ["2", "3"]:
            if not is_logged_in:
                print("Error: Please login or register first.")
            else:
                if choice == "2":
                    print("Planning a trip...")
                    planner.plan_trip(current_user)
                elif choice == "3":
                    print("Viewing your trip...")
                    planner.view_my_trip(current_user)

        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()