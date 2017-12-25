"""Bank account project"""

class BankAccount(object):
  balance = 0.0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "This account belongs to %s. It has $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print "$%.2f" % self.balance
    
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print "User deposits $%.2f" % amount
      print "The new balance is",
      self.show_balance()
    else:
      print "You can't deposit the amount: %.2f" % amount
      return 0
  
  def withdraw(self, amount):
    if amount > self.balance:
      print "You don't have enough money to withdraw that ammount."
    else:
      print "You are withdrawing $%.2f" % amount
      self.balance -= amount
      print "Your new ballance is",
      self.show_balance()

my_account = BankAccount("Alex")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account