"""
Encapsulation
-------------
Encapsulation is an object-oriented programming principle that combines data
and the methods that operate on that data inside a class. It also controls
access to the object's internal state, preventing direct and unintended
changes from outside the class.

In Python, encapsulation is commonly represented by naming conventions:

* Public members can be accessed from anywhere.
* A single leading underscore (for example, ``_balance``) indicates that a
	member is intended for internal use.
* A double leading underscore (for example, ``__pin``) triggers name
	mangling, making accidental direct access more difficult.

Encapsulation improves data security, maintains consistency, and makes code
easier to maintain. Access to private data is usually provided through
methods or properties that can validate values before changing the state.
"""

class BankAccount:
	def __init__(self, balance):
		self.__balance = balance  # Private attribute

	def __show_balance(self):  # Private method
		return self.__balance

	def get_balance(self):  # Public method for controlled access
		return self.__show_balance()


account = BankAccount(1000)
print(account.get_balance())  # Allowed: access through a public method

# print(account.__balance)       # Not allowed directly: AttributeError
# account.__show_balance()       # Not allowed directly: AttributeError
# Python name-mangles private members, so this technically works, but is not
# recommended: print(account._BankAccount__balance)