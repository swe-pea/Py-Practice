#Override Explicitly , implicit inheritence, and super()
class Parent(object):

    def override(self):
        print("PARENT override")

    def implicit(self):
        print("PARENT implicit")

    def altered(self):
        print("PARENT altered")

class Child(Parent):

    #EXPLICITLY overrides the override function from the parent class
    def override(self):
        print("CHILD override")

    #overrides the altered function from the parent class
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        #This calls the super class of class Child, passing in Itself as an objecet, and then
        #calls the altered method
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

#Example of using both Super and __init__
class ChildvTwo(Parent):

    # Overrides the __init__ I think? setting it's stuff variable/attr to the stuff object passed in to the constructor
    # And then continues to calling the init function of the Childs super class .
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

#Composition
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class smolHooman(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("SMOLHOOMAN override()")

    def altered(self):
        print("smolHooman, before other altered()")
        self.other.altered()
        print("smolHooman, after other altered()")



smolDude = smolHooman()
smolDude.implicit()
smolDude.override()
smolDude.altered()
