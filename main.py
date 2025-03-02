from device import Smartphone, Laptop, Tablet
from cart import Cart

devices = [
    Smartphone("iPhone 13", 799, 10, 24, 6.1, 20),
    Laptop("MacBook Pro", 1299, 5, 36, 16, 3.2),
    Tablet("iPad Pro", 999, 8, 24, "2048x1536", 500)
]

cart = Cart()
while True:
    print("\n1. Show Devices\n2. Show Cart\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        for i, device in enumerate(devices):
            print(f"{i + 1}. {device}")
        index = int(input("Enter device number to add to cart: ")) - 1
        quantity = int(input("Enter quantity: "))
        if 0 <= index < len(devices):
            cart.add_device(devices[index], quantity)

    elif choice == "2":
        cart.print_items()
        print(f"Total: ${cart.get_total_price()}")

    elif choice == "3":
        print("Exiting...")
        break
