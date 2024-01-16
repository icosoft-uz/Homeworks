import json


class BankomatApp:
    def __init__(self, cards, translations):
        self.cards = cards
        self.current_card = None
        self.current_language = "en"
        self.translations = translations
        self.max_pin_attempts = 3
        self.pin_attempts = 0

    def display_message(self, key, **kwargs):
        message = self.translations[self.current_language][key]
        print(message.format(**kwargs))

    def validate_card_number(self, card_number):
        # Check if input is a valid numeric string
        if not card_number.isdigit():
            self.display_message("invalid_card_number")
            return False

        if not (16 <= len(card_number) <= 19):
            self.display_message("invalid_card_number_length")
            return False

        card_found = any(card["card_number"] == card_number for card in self.cards)
        if not card_found:
            self.display_message("invalid_card_number")
            return False

        return True

    def login(self, card_number, pin):
        if not self.validate_card_number(card_number):
            return False

        for card in self.cards:
            if card["card_number"] == card_number and card["pin_code"] == pin:
                self.current_card = card
                return True

        self.pin_attempts += 1
        if self.pin_attempts >= self.max_pin_attempts:
            self.display_message("card_frozen")
            self.current_card = None  # Freeze the card
        else:
            self.display_message("invalid_card_pin")

        return False

    def cancel_action(self):
        # Ask for confirmation to cancel
        user_input = input(self.translations[self.current_language]["cancel_confirmation"])
        if user_input.lower() == "yes":
            self.current_card = None
            return True
        else:
            return False

    def check_balance(self):
        return self.current_card["balance"]

    def withdraw(self, amount):
        if self.current_card["balance"] >= amount > 0:
            self.current_card["balance"] -= amount
            return True
        return False

    def deposit(self, amount):
        if amount > 0:
            self.current_card["balance"] += amount
            return True
        return False

    def change_pin(self, new_pin):
        if new_pin == input(self.translations[self.current_language]["repeat_new_pin"]):
            self.current_card["pin_code"] = new_pin
            self.display_message("pin_changed")
        else:
            self.display_message("invalid_new_pin")

    def change_connected_number(self, new_number):
        self.current_card["connected_number"] = new_number
        self.display_message("connected_number_changed")


if __name__ == "__main__":
    with open("cards.json", "r") as file:
        cards_data = json.load(file)["cards"]

    with open("translations.json", "r", encoding="utf-8") as file:
        translations_data = json.load(file)

    bankomat = BankomatApp(cards_data, translations_data)

    while True:
        print("\n===== Welcome to the ATM App =====")
        print(bankomat.translations[bankomat.current_language]["select_language"])
        selected_language = input().lower()

        if selected_language in bankomat.translations:
            bankomat.current_language = selected_language
        else:
            print(bankomat.translations[bankomat.current_language]["invalid_language"])
            continue

        while True:
            card_number = input(bankomat.translations[bankomat.current_language]["enter_card_number"])

            if card_number.lower() == "q":
                break

            pin = input(bankomat.translations[bankomat.current_language]["enter_pin_code"])

            if bankomat.login(card_number, pin):
                print("\n===== Login Successful! Welcome, {} =====".format(bankomat.current_card["name"]))
                while True:
                    print("\n1. {}".format(bankomat.translations[bankomat.current_language]["check_balance"]))
                    print("2. {}".format(bankomat.translations[bankomat.current_language]["withdraw"]))
                    print("3. {}".format(bankomat.translations[bankomat.current_language]["change_pin_code"]))
                    print("4. {}".format(bankomat.translations[bankomat.current_language]["change_connected_number"]))
                    print("q. Logout")

                    action = input(bankomat.translations[bankomat.current_language]["choose_option"])

                    if action == "1":
                        print("Balance: $", bankomat.check_balance())
                    elif action == "2":
                        amount = float(input(bankomat.translations[bankomat.current_language]["enter_amount"]))
                        if bankomat.withdraw(amount):
                            print(bankomat.translations[bankomat.current_language]["withdrawing"].format(amount))
                            print(bankomat.translations[bankomat.current_language]["printing_check"])
                            check_option = input(
                                bankomat.translations[bankomat.current_language]["print_check"]).lower()
                            if check_option == "yes":
                                print(bankomat.translations[bankomat.current_language]["printing_check"])
                            print("Withdrawal successful. New balance: $", bankomat.check_balance())
                        else:
                            print("Invalid withdrawal amount.")
                    elif action == "3":
                        if bankomat.cancel_action():
                            break
                        old_pin = input(bankomat.translations[bankomat.current_language]["enter_old_pin"])
                        if old_pin == pin:
                            new_pin = input(bankomat.translations[bankomat.current_language]["enter_new_pin"])
                            bankomat.change_pin(new_pin)
                        else:
                            print(bankomat.translations[bankomat.current_language]["invalid_card_pin"])
                    elif action == "4":
                        if bankomat.cancel_action():
                            break
                        new_number = input(bankomat.translations[bankomat.current_language]["enter_new_number"])
                        bankomat.change_connected_number(new_number)
                    elif action.lower() == "q":
                        break
                    else:
                        print(bankomat.translations[bankomat.current_language]["invalid_option"])

                    # Ask if the user wants to continue
                    continue_option = input(
                        bankomat.translations[bankomat.current_language]["continue_action"]).lower()
                    if continue_option not in ["yes", "ha", "да"]:
                        break

            else:
                print(bankomat.translations[bankomat.current_language]["invalid_card_pin"])
