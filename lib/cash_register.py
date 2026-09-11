#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        print(
            f"After the discount, the total comes to ${self.total:g}."
        )

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()

        self.total -= transaction["price"] * transaction["quantity"]

        for _ in range(transaction["quantity"]):
            self.items.pop()
