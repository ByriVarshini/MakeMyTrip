import re

class User:
    user_database = {}  # Class-level dictionary to store user data

    def __init__(self, name, email, password, mobile_number):
        self.name = name
        self.email = email
        self.password = password
        self.mobile_number = mobile_number

    def display_user_info(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nMobile Number: {self.mobile_number}")

    @staticmethod
    def validate_email(email):
        # Email validation using regex
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)

    @staticmethod
    def validate_password(password):
        # Password must be at least 8 characters long, include a mix of uppercase, lowercase, digits, and special characters
        if (len(password) >= 8 and
                any(char.isupper() for char in password) and
                any(char.islower() for char in password) and
                any(char.isdigit() for char in password) and
                any(char in "!@#$%^&*()-_+=<>?/|{}~" for char in password)):
            return True
        return False

    @staticmethod
    def validate_mobile_number(mobile_number):
        # Mobile number should contain exactly 10 digits
        return mobile_number.isdigit() and len(mobile_number) == 10

    @classmethod
    def user_login(cls):
        print("Welcome! Let's get started.")
        name = input("Enter your name: ")

        # Loop until a valid email is entered
        while True:
            email = input("Enter your email: ").strip()
            if cls.validate_email(email):
                break
            print("Error: Invalid email format. Please try again.")

        if email in cls.user_database:
            print(f"Welcome back, {cls.user_database[email].name}!")
            user = cls.user_database[email]

            # Loop until the correct password is entered or user exits
            while True:
                password = input("Enter your password (or type 'exit' to quit): ").strip()
                if password.lower() == 'exit':
                    print("Exiting login process.")
                    return None
                if user.password == password:
                    print("Login successful!")
                    return user
                else:
                    print("Error: Incorrect password. Please try again.")
        else:
            print(f"No account found with the email '{email}'. Let's register.")

            # Loop until a valid mobile number is entered
            while True:
                mobile_number = input("Enter your mobile number: ").strip()
                if cls.validate_mobile_number(mobile_number):
                    break
                print("Error: Invalid mobile number. It must contain exactly 10 digits. Please try again.")

            # Loop until a strong password is entered
            while True:
                password = input("Create a strong password: ").strip()
                if cls.validate_password(password):
                    break
                print("Error: Password must be at least 8 characters long and include uppercase, lowercase, digits, and special characters. Please try again.")

            # Register the user
            user = User(name, email, password, mobile_number)
            cls.user_database[email] = user
            print(f"User '{name}' registered successfully!")
            return user


# Example usage
if __name__ == "__main__":
    # Access the system (login or register)
    user = User.user_login()

    # Display user info if successfully logged in or registered
    if user:
        user.display_user_info()
