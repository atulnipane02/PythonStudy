

class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
        elif scoops > 3 or scoops < 1:
            print("Choose between 1-3 scoops")
        else:
            print("Order Created")
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.enqueue(order)

    def show_all_orders(self):
        print("\n")
        print("All pending Ice cream Orders:")
        for val in range(0, self.orders.size()):
            order = self.orders.items[val]
            orderTxt = "Customer: {customer} -- Flavor: {flavor} -- Scoops: {scoops}".format(
                customer=order["customer"], flavor=order["flavor"], scoops=order["scoops"])
            print(orderTxt)

    def next_order(self):
        print("\n")
        order = self.orders.dequeue()
        orderTxt = "Customer: {customer} -- Flavor: {flavor} -- Scoops: {scoops}".format(
            customer=order["customer"], flavor=order["flavor"], scoops=order["scoops"])
        print("Next Order Up!")
        print(orderTxt)


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
