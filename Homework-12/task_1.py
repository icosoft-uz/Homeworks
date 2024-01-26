from collections import deque
import keyboard


class Service:
    def __init__(self):
        self.queue = deque()
        self.order_id = 1

    def enqueue(self, fullname):
        order_id = self.order_id
        self.order_id += 1
        self.queue.append({'fullname': fullname, 'order_id': order_id})
        return order_id

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.popleft()


class Cards(Service):
    pass


class Credits(Service):
    pass


class Exchange(Service):
    pass


class Main:
    def __init__(self):
        self.cards_service = Cards()
        self.credits_service = Credits()
        self.exchange_service = Exchange()

    @staticmethod
    def show_menu():
        print("Choose a service:")
        print("[1] Cards")
        print("[2] Credits")
        print("[3] Exchange")
        print("[4] Exit")

    @staticmethod
    def handle_keyboard_input():
        while True:
            try:
                key_event = keyboard.read_event(suppress=True)
                if key_event.event_type == keyboard.KEY_DOWN:
                    key = key_event.name
                    if key == '1':
                        return '1'
                    elif key == '2':
                        return '2'
                    elif key == '3':
                        return '3'
                    elif key == '4':
                        print('Exiting...')
                        return '4'
            except KeyboardInterrupt:
                break

    def start(self):
        print("Welcome to the E-Orderer!")
        fullname = input("Enter your full name: ")

        while True:
            self.show_menu()
            choice = self.handle_keyboard_input()

            if choice == '1':
                order_id = self.cards_service.enqueue(fullname)
                self.print_order_details("Cards", order_id)
            elif choice == '2':
                order_id = self.credits_service.enqueue(fullname)
                self.print_order_details("Credits", order_id)
            elif choice == '3':
                order_id = self.exchange_service.enqueue(fullname)
                self.print_order_details("Exchange", order_id)
            elif choice == '4':
                print("Thank you for using E-Orderer. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def print_order_details(service_name, order_id):
        print(f"Service: {service_name}")
        print(f"Order ID: {order_id}")
        print("Order placed successfully!\n")


if __name__ == "__main__":
    main = Main()
    main.start()
