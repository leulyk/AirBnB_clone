# [AirBnB clone - The Console](https://github.com/leulyk/AirBnB_clone/blob/main/README.md)

<p float="left">
<img src="https://lh3.googleusercontent.com/oVJxT1yn7vwaEM8t9A5MGL6emG0j-_uqHa5H8ikWLvl6Ka-nVmUJZblqWDqPiY-S6itPLnZNgcc8rviK8AVT65l_a3zHiyctwy8=s0" width="245" height="150"/>
<img src="https://github.com/leulyk/AirBnB_clone/blob/main/AirBnB.png" width = "355" height = "150" />
</p>
<p>
<img src="https://github.com/leulyk/AirBnB_clone/blob/main/framework.png" width="600" height = "320" />
</p>

> This is the first step towards building a full web application: the **AirBnB clone**. This project builds an interpreter to manage the AirBnB objects.

The interpreter manages the objects of the project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### Execution

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

## Commands

| Command | Usage | Description |
| ------- | ----- | ----------- |
| **all** | *all \<class\_name>* **/** *all* / *\<class\_name>.all()* | Prints all instances created or all instances of a certain class |
| **count** | |
| **create** | |
| **destroy** | |
| **help** | |
| **quit** | |
| **show** | |
| **update** | |
