class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount

    def remove_device(self, device, amount):
        for i, (d, qty) in enumerate(self.items):
            if d == device:
                self.total_price -= d.price * min(amount, qty)
                if qty <= amount:
                    del self.items[i]
                else:
                    self.items[i] = (d, qty - amount)
                break

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for device, amount in self.items:
            print(f"{device.name} x{amount} - ${device.price * amount}")

    def checkout(self):
        for device, amount in self.items:
            device.reduce_stock(amount)
        self.items.clear()
        self.total_price = 0
        print("Purchase complete!")