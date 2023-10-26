#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.total = 0
    self._discount = discount
    self.items = []
    self.last_item = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    self._discount = value

  def add_item(self, title, price, quantity=1):
    self.last_item = [title, price * quantity]
    self.total += (price * quantity)
    # if title not in self.items:
    #   self.items.append(title)
    i = 0
    while i < quantity:
      self.items.append(title)
      i += 1

  def apply_discount(self):
    if self._discount:
      self.total -= round(self.total * float(self.discount / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_item[1]
    self.items.remove(self.last_item[0])  



cash_register = CashRegister()
cash_register.add_item("apple", 0.99)
cash_register.add_item("tomato", 1.76)
cash_register.void_last_transaction()