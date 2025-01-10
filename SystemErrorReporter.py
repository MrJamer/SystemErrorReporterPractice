import json
from LoggerFormatter import Logger
from ErrorHandler import ErrorHandler
from TestModule import TestModule

# Відображення меню користувача
class UserInterface:
    def __init__(self, logger, test_module):
        self.logger = logger
        self.test_module = test_module

    def display_menu(self):
        print("\n=== System Error Reporter ===")
        print("1. Run tests")
        print("2. Enter user data")
        print("3. View logs")
        print("4. Exit the program")

# Запит на введення даних
    def get_user_input(self, prompt):
        return input(prompt)

# Основний цикл інтерфейсу користувача
    def run_interface(self):
        while True:
            self.display_menu()
            choice = self.get_user_input("Select an option (1-4): ")

            if choice == "1":
                self.logger.log_info("Run tests")
                self.test_module.run_tests()
            elif choice == "2":
                name = self.get_user_input("Enter your name: ")
                self.logger.log_info(f"User entered name: {name}")
            elif choice == "3":
                self.view_logs()
            elif choice == "4":
                self.logger.log_info("Exiting the programm")
                print("Programm ended.")
                break
            else:
                print("Wrong choice. Please try again.")
                self.logger.log_warning("The user entered an incorrect selection in the menu")

# Відображення логів
    def view_logs(self):
        try:
            with open(self.logger.logger.handlers[0].baseFilename, "r") as file:
                logs = file.readlines()
                print("\n--- Logs ---")
                for log in logs: 
                    print(log.strip())
        except FileNotFoundError:
            print("The log file has not been created yet.")
            self.logger.log_warning("Trying to view logs before they are created")

# Завантаження конфігурації з JSON
def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)

# Основна функція програми
def main():
    
    # Завантаження конфігурації
    config = load_config()
    email_settings = config["email_settings"]
    logging_settings = config["logging_settings"]

    # Ініціалізація компонентів
    logger = Logger(logging_settings["log_file"], logging_settings["log_level"])
    error_handler = ErrorHandler(logger, email_settings)
    test_module = TestModule(error_handler)
    user_interface = UserInterface(logger, test_module)

    # Логування старту програми
    logger.log_info("Application started")

    # Запуск інтерфейсу користувача
    user_interface.run_interface()

    # Завершення програми
    logger.log_info("Application finished successfully")

if __name__ == "__main__":
    main()
    