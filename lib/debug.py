from customer import Customer
from coffee import Coffee


def demo():
    alice = Customer("Alice")
    bob = Customer("Bob")

    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    alice.create_order(latte, 3.5)
    alice.create_order(latte, 4.0)
    bob.create_order(latte, 5.0)
    bob.create_order(espresso, 2.5)

    print("All customers:", Customer.all())
    print("All coffees:", Coffee.all())
    print("Latte orders:", latte.orders())
    print("Latte customers:", latte.customers())
    print("Latte num_orders:", latte.num_orders())
    print("Latte avg price:", latte.average_price())
    print("Alice coffees:", alice.coffees())
    print("Most aficionado for Latte:", Customer.most_aficionado(latte))


if __name__ == "__main__":
    demo()
