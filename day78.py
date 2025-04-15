# Single inheritance
class animal:
 def __init__(self, name, species):
   self.name = name
   self.species = species

   def make_sound(self):
     print("sound made by animal")

     class dog(animal):
       def __init__(self, name, bread):
         animal.__init__(self, name, species="dog")
         self.bread = bread
         def make_sound(self):
           print("bark!")
           a=animal("dog", "dog")
           a.make_sound()

         d=dog("dog", "doggerman")
         d.make_sound()
         
