#PRINTS A TREE/LIST OF SUBCLASSES OF A GIVEN CLASS
def printSubclassTree(thisclass,nest=0):
	if nest > 1:
		print("  |" * (nest - 1), end="")
	if nest > 0:
		print("  +--", end="")
	print(thisclass.__name__)
	
	for subclass in thisclass.__subclasses__():
		printSubclassTree(subclass,nest + 1)
		
printSubclassTree(BaseException)
