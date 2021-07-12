class Ingredient:
  """Models an Ingredient."""
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount

  def expire(self):
    """Expires the ingredient item."""
    print(f"whoops, these {self.name} went bad...")
    self.name = "expired " + self.name

  def __str__(self):
    return f"You have {self.amount} {self.name}."

p = Ingredient('peas', 12)
print(p)