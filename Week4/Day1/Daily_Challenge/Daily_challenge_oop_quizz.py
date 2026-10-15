#part 1: quizz
# - What is a class?
# A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (behaviors) that objects created from it will have.
#
# - What is an instance?
# An instance is an individual object created from a class. Each instance has its own unique data based on the structure of the class.
#
# - What is encapsulation?
# Encapsulation is the principle of bundling data and the methods that operate on that data within a single unit (a class), restricting direct access from the outside to protect the internal state.
#
# - What is abstraction?
# Abstraction is the concept of hiding complex internal implementation details and exposing only the essential functionality to the user.
#
# - What is inheritance?
# Inheritance is a mechanism that allows a new class (child class) to inherit attributes and methods from an existing class (parent class), promoting code reuse.
#
# - What is multiple inheritance?
# Multiple inheritance is a feature that allows a class to inherit attributes and methods from more than one parent class simultaneously.
#
# - What is polymorphism?
# Polymorphism is the ability of different classes to implement methods with the same name but tailored behaviors, allowing them to be used interchangeably.
#
# - What is method resolution order or MRO?
# MRO is the hierarchical order Python uses to search for methods and attributes in a class structure, especially important when using multiple inheritance.


#part 2: create a deck of cards class

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        self.shuffle()

    def shuffle(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()