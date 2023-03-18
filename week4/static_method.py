class Car:
	def __init__(self, model, color, price):
		# Constructor
		self.model = model
		self.color = color
		self.price = price

	def drive(self, drive_mode):
		print(f"Set {self.model} into drive {drive_mode} mode")
	def brake(self, brake_mode):
		print(f"Set {self.model} into brake {brake_mode} mode")
	def power(self, power_mode):
		print(f"Set {self.model} into power {power_mode} mode")

	@staticmethod
	def get_wheels():
		print("4")
  
# Create object Tesla  
Tesla = Car("Model Y", "White", 2000000)
print(f"Object Type: {type(Tesla)}")


print(Tesla.drive("Auto"))
print(Tesla.brake("Auto"))
print(Tesla.power("Recharge"))

print(f"Get Wheels number through class  {Car.get_wheels()} ")
print(f"Get Wheels number through object {Tesla.__class__.get_wheels()} ")

        