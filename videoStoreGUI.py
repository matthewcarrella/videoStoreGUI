"""

Program: GUI_template.py
Author: Matthew 7/10/2023

A GUI-based application that calculates the total bill for customers at a fake video rental store

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly,


"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header
class VideoStore(EasyFrame):
	# Definition of our class constructor
	def __init__(self):
		EasyFrame.__init__(self, title="Five Star Video", width=700, height=300, resizable=False, background="lightyellow")
		self.normalFont = Font(family="Tahoma", size=24)
		self.addLabel(text="Five Star Video", row=0, column=0, columnspan=2, sticky="NSEW", background="darkred", foreground="lightyellow", font=Font(family="Arial", size=25))
		self.addLabel(text="New Rentals: $3.00\n Old Rentals: $2.00", row=1, column=0, columnspan=2, sticky="NSEW", background="lightyellow", font=self.normalFont)
		self.addLabel(text="# of New Rentals: ", row=2, column=0, sticky="NE", background="lightyellow", font=self.normalFont)
		self.newRentals = self.addIntegerField(value=0, row=2, column=1, sticky="NW")
		self.addLabel(text="# of Old Rentals: ", row=3, column=0, sticky="NE", background="lightyellow", font=self.normalFont)
		self.oldRentals = self.addIntegerField(value=0, row=3, column=1, sticky="NW")
		self.button = self.addButton(text="Calculate Total", row=4, column=0, columnspan=2, command=self.calculateTotal)
		self.addLabel("The total for the order is: ", row=5, column=0, background="darkred", foreground="white", font=self.normalFont)
		self.total = self.addFloatField(value=0.0, row=5, column=1, sticky="NW")
		
	def calculateTotal(self):
		total = self.newRentals.getNumber() * 3 + self.oldRentals.getNumber() * 2
		self.total.setValue(total)

# Global definition of the main() method
def main():
	VideoStore().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()