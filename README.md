# [AirBnB clone - The console & Web static](https://github.com/leulyk/AirBnB_clone/blob/main/README.md)

<p float="left">
<img src="https://lh3.googleusercontent.com/oVJxT1yn7vwaEM8t9A5MGL6emG0j-_uqHa5H8ikWLvl6Ka-nVmUJZblqWDqPiY-S6itPLnZNgcc8rviK8AVT65l_a3zHiyctwy8=s0" width="245" height="150"/>
<img src="https://github.com/leulyk/AirBnB_clone/blob/main/images/AirBnB.png" width = "355" height = "150" />
</p>
<p>
<img src="https://github.com/leulyk/AirBnB_clone/blob/main/images/hbnb_step1.png" width="600" height = "320" />
</p>

> This is the first step towards building a full web application: the **AirBnB clone**. This project builds an interpreter to manage the AirBnB objects and initiates the front-end development by building the static web page with HTML and CSS.

## [The interpreter](https://github.com/leulyk/AirBnB_clone/blob/main/console.py)

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
| **all** | *- all <class_name>* <br/> *- all* <br/> *- <class_name>.all()* | Prints all instances created or all instances of a certain class |
| **count** | *- count <class_name>* <br/> *- <class_name>.count()* | Counts number of instances of a class | 
| **create** | *- create <class_name>* | Creates an object of any available class |
| **destroy** | *- destroy <class_name> <instance_id>* <br/> *- <class_name>.destroy(<instance_id>)* | Deletes an instance based on class name and id |
| **help** | *- help* | List available commands with "help" or detailed help with "help cmd". |
| **quit** | *- quit* | Quit command to exit the program |
| **show** | *- show <class_name> <instance_id>* <br/> *- <class_name>.show(<instance_id>)* | Shows string representation of an object instance |
| **update** | *- update <class_name> <instance_id> <attribute_name> "- <attribute_value>"* <br/> *- <class_name>.update(<instance_id>, <attribute_name>, <attribute_value>)* <br/> *- <class_name>.update(<instance_id>, <dictionary_representation>)* | Updates an instance based on class name and id by adding or updating attribute, or by using dictionary |

## Examples

<p>
<img src="https://github.com/leulyk/AirBnB_clone/blob/main/images/example_1.png" />
</p>
<p>
<img src="https://github.com/leulyk/AirBnB_clone/blob/main/images/example_2.png" />
</p>
<p>
<img src="https://github.com/leulyk/AirBnB_clone/blob/main/images/example_3.png" />
</p>
