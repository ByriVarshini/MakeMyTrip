from pckg.User import User  
class Admin:
    Admin_name="varshini"
    Admin_pass="varshu123"
    @staticmethod
    def view_all_users():
        if not User.user_database:
            print("No users are registered yet.")
        else:
            print("\n--- Registered Users ---")
            for email, user in User.user_database.items():
                print(f"Name: {user.name}, Email: {email}")

    @staticmethod
    def edit_user(email):
        if email in User.user_database:
            user = User.user_database[email]
            print(f"\nEditing user: {user.name} ({email})")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_password = input("Enter new password (leave blank to keep current): ")
            if new_name:
                user.name = new_name
            if new_password:
                user.password = new_password
            print("User details updated successfully.")
        else:
            print(f"Error: No user found with the email '{email}'.")

    @staticmethod
    def delete_user(email):
        if email in User.user_database:
            del User.user_database[email]
            print(f"User with email '{email}' has been deleted.")
        else:
            print(f"Error: No user found with the email '{email}'.")
