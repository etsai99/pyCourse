class Car:
    # class attribute
	# material = "Mental"
    
	def __init__(self, model, color, price):
		# Constructor
		self.model = model
		self.color = color
		self.price = price

	def drive(self, drive_mode):
		print(f"Set {self.model} into drive {drive_mode} mode")
		# Get class attribute (through method)
		#print(f"Get class attribute from innne method- {self.__class__.material}")
	def brake(self, brake_mode):
		print(f"Set {self.model} into brake {brake_mode} mode")
	def power(self, power_mode):
		print(f"Set {self.model} into power {power_mode} mode")
	#def get_class_attribute(self):
	#	Get class attribute (through method)
	#	print(f"Get class attribute from self-defined method - {self.__class__.material}")
  
  

# Create object Tesla  
Tesla = Car("Model Y", "White", 2000000)
print(f"Object Type: {type(Tesla)}")


print(Tesla.drive("Auto"))
print(Tesla.brake("Auto"))
print(Tesla.power("Recharge"))

# Get class attribute (through object or class)
# print(f"Get class attribute from object.attribute - {Tesla.material}")
# print(f"Get class attribute from class.attribute - {Car.material}")
# print(f"Get class attribute from self-defined method - {Tesla.get_class_attribute()}")
        