class Employee:
 def __init__(self, name):
  self.name = name
#  name = "Harry"
 def __len__(self):
  i = 0
  for c in self.name:
   i = i+1
  return i
#  def __str__(self):
#   return f"the name of thye employee is {self.name}str"
 
 def __repr__(self):
  return f"the name of employee is {self.name}repr" 
 def __repr__(self):
  return f"Employee('{self.name}')"
  