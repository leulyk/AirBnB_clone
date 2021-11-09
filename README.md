# [AirBnB clone]()

<p float="left">
<img src="https://lh3.googleusercontent.com/oVJxT1yn7vwaEM8t9A5MGL6emG0j-_uqHa5H8ikWLvl6Ka-nVmUJZblqWDqPiY-S6itPLnZNgcc8rviK8AVT65l_a3zHiyctwy8=s0" width="245" height="150"/>
<img src="https://blog.holbertonschool.com/wp-content/uploads/2019/04/instagram_feed180.jpg" width = "150" height="150"/>
<img src="https://github.com/leulyk/AirBnB_clone/blob/main/AirBnB.png" width = "150" height = "355" />
</p>

## The Interpreter

The interpreter manages the objects of the project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

- ### Execution

The shell should work like this in interactive mode:

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================

	EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$

But also in non-interactive mode:

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================	

	EOF  help  quit
	(hbnb)
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================	

	EOF  help  quit
	(hbnb)
	$
