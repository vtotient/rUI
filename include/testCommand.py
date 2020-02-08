def do_add(self, inp):
	"Add a test to the queue"
	# Todo:
	#	* Add dictionaries to queue instead of text.
	#	* Read from YAML file.
	
	args = inp.split()

	if args[0] == "-f": # Handle from file
		try:
			with open(args[1],"r") as f:
				for line in f.readlines():
					testObject = line.strip() # create test object
					self.testQueue.append(testObject)
					print("Added", testObject, "to queue.")
		except FileNotFoundError:
			print("File not found. Try again.")
	else:
		testObject = inp # create test object
		self.testQueue.append(testObject)
		print("Added", testObject, "to queue.")

def do_list(self, inp):
	"List the currently queued tests."

	if not self.testQueue:
		print("The test queue is empty")
		return
	for i, testObject in enumerate(self.testQueue):
		print("["+str(i)+"] "+testObject)

def do_remove(self, inp):
	"""Remove a test
	Args:
		testNumber: test number from `listTests` to remove
		`-f`: Force remove/skip confirmation
	Example:  
		rUI> test remove -f 2
		Removed test2 from the queue."""
	inp = inp.split()
	if len(inp) < 1:
		print("Please input a test number")
		return
	try:
		if inp[0] != '-f':
			toRemoveIndex = int(inp[0])
			ans = input("Are you sure you would like to remove "+str(self.testQueue[toRemoveIndex])+" from the testQueue (Y/n)? ")
			if not (ans.lower() == "y" or ans.lower() == "yes" or ans.lower() == ""):
				print("Canceling...")
				return
		else:
			toRemoveIndex = int(inp[1])
		print("Removed", self.testQueue.pop(toRemoveIndex),"from queue.")
	except ValueError:
		print("Please input a valid test number")

def do_run(self, inp):
	"""Runs a test. Excecute test plan outlined by queue if no\n      test number specified.
	Args:
		testNumber (optional): test number from `listTests` to remove

	Todo:
		* CREATE TEST OBJECT HERE and run it
	"""

	if inp:
		try:
			print("Running test",self.testQueue.pop(int(inp)))
		except IndexError:
			print("Please enter a valid queue index.")
			return
	else:
		print("Excecuting test plan:")
		while len(self.testQueue) > 0:
			print("Running test",self.testQueue.pop(0))


