from __future__ import annotations
from typing import List, Optional
from order import Order
from coffee import Coffee


class Customer:
    _all_customers: List["Customer"] = []

    def __init__(self, name: str):
        self._name = None
        self.name = name
        Customer._all_customers.append(self)

    def __repr__(self):
        return f"Customer(name={self.name!r})"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        value = value.strip()
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters")
        self._name = value

    @classmethod
    def all(cls) -> List["Customer"]:
        return list(cls._all_customers)

    def orders(self) -> List[Order]:
        return [o for o in Order.all() if o.customer is self]

    def coffees(self) -> List[Coffee]:
        seen = []
        for o in self.orders():
            if o.coffee not in seen:
                seen.append(o.coffee)
        return seen

    def create_order(self, coffee: Coffee, price: float) -> Order:
        if not isinstance(coffee, Coffee):
            raise TypeError("create_order expects a Coffee instance")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee: Coffee) -> Optional["Customer"]:
        if not isinstance(coffee, Coffee):
            raise TypeError("most_aficionado expects a Coffee instance")

        totals = {}
        for o in coffee.orders():
            totals[o.customer] = totals.get(o.customer, 0.0) + o.price

        if not totals:
            return None

        return max(totals.items(), key=lambda kv: kv[1])[0]
