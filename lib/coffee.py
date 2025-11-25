from __future__ import annotations
from typing import List
from order import Order


class Coffee:
    _all_coffees: List["Coffee"] = []

    def __init__(self, name: str):
        self._name = None
        self.name = name
        Coffee._all_coffees.append(self)

    def __repr__(self):
        return f"Coffee(name={self.name!r})"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters")
        self._name = value

    @classmethod
    def all(cls) -> List["Coffee"]:
        return list(cls._all_coffees)

    def orders(self) -> List[Order]:
        return [o for o in Order.all() if o.coffee is self]

    def customers(self):
        seen = []
        for o in self.orders():
            if o.customer not in seen:
                seen.append(o.customer)
        return seen

    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> float:
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(o.price for o in orders) / len(orders)
