# 0x00. AirBnB clone - The console

![hbnb](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191112T165345Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b87bd036fc4bf7a693ab5b10075df7865084aba20cd9bc98c28b6d13ae6dd01d)

## Description

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---

### [0. README, AUTHORS](./README.md)
* Write a README.md:

description of the project
description of the command interpreter:


### [1. Be PEP8 compliant!](./tests/)
* Write beautiful code that passes the PEP8 checks.


### [2. Unittests](./models/base_model.py)
* All your files, classes, functions must be tested with unit tests


### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes:

```
[BaseModel] (0da511bb-b7cb-4843-9ebc-2f43c99aecdc) {'created_at': datetime.datetime(2019, 11, 8, 9, 38, 27, 11686), 'name': 'Holberton', 'my_number': 89, 'updated_at': datetime.datetime(2019, 11, 8, 9, 38, 27, 11686), 'id': '0da511bb-b7cb-4843-9ebc-2f43c99aecdc'}
[BaseModel] (0da511bb-b7cb-4843-9ebc-2f43c99aecdc) {'created_at': datetime.datetime(2019, 11, 8, 9, 38, 27, 11686), 'name': 'Holberton', 'my_number': 89, 'updated_at': datetime.datetime(2019, 11, 8, 9, 38, 27, 12214), 'id': '0da511bb-b7cb-4843-9ebc-2f43c99aecdc'}
{'created_at': '2019-11-08T09:38:27.011686', 'name': 'Holberton', 'my_number': 89, 'updated_at': '2019-11-08T09:38:27.012214', 'id': '0da511bb-b7cb-4843-9ebc-2f43c99aecdc', '__class__': 'BaseModel'}
JSON of my_model:
	created_at: (<class 'str'>) - 2019-11-08T09:38:27.011686
	name: (<class 'str'>) - Holberton
	my_number: (<class 'int'>) - 89
	updated_at: (<class 'str'>) - 2019-11-08T09:38:27.012214
	id: (<class 'str'>) - 0da511bb-b7cb-4843-9ebc-2f43c99aecdc
	__class__: (<class 'str'>) - BaseModel
```

### [4. Create BaseModel from dictionary](./models/engine/file_storage.py)
* Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

```
686dd4d3-0e29-4b94-b0ea-d75ed0e7e468
[BaseModel] (686dd4d3-0e29-4b94-b0ea-d75ed0e7e468) {'my_number': 89, 'created_at': datetime.datetime(2019, 11, 8, 9, 40, 45, 483083), 'id': '686dd4d3-0e29-4b94-b0ea-d75ed0e7e468', 'name': 'Holberton', 'updated_at': datetime.datetime(2019, 11, 8, 9, 40, 45, 483083)}
<class 'datetime.datetime'>
--
{'my_number': 89, 'created_at': '2019-11-08T09:40:45.483083', 'id': '686dd4d3-0e29-4b94-b0ea-d75ed0e7e468', 'name': 'Holberton', '__class__': 'BaseModel', 'updated_at': '2019-11-08T09:40:45.483083'}
JSON of my_model:
	my_number: (<class 'int'>) - 89
	created_at: (<class 'str'>) - 2019-11-08T09:40:45.483083
	id: (<class 'str'>) - 686dd4d3-0e29-4b94-b0ea-d75ed0e7e468
	name: (<class 'str'>) - Holberton
	__class__: (<class 'str'>) - BaseModel
	updated_at: (<class 'str'>) - 2019-11-08T09:40:45.483083
--
686dd4d3-0e29-4b94-b0ea-d75ed0e7e468
[BaseModel] (686dd4d3-0e29-4b94-b0ea-d75ed0e7e468) {'my_number': 89, 'created_at': datetime.datetime(2019, 11, 8, 9, 40, 45, 483083), 'id': '686dd4d3-0e29-4b94-b0ea-d75ed0e7e468', 'name': 'Holberton', 'updated_at': datetime.datetime(2019, 11, 8, 9, 40, 45, 483083)}
<class 'datetime.datetime'>
--
False
```

### [5. Store first object](./console.py)
* Now we can recreate a BaseModel from another one by using a dictionary representation:

```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ cat file.json
cat: file.json: No such file or directory
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (d64ac0c4-cc5b-462e-8332-35f3f6e62d7e) {'created_at': datetime.datetime(2019, 11, 8, 9, 43, 0, 558089), 'name': 'Holberton', 'my_number': 89, 'id': 'd64ac0c4-cc5b-462e-8332-35f3f6e62d7e', 'updated_at': datetime.datetime(2019, 11, 8, 9, 43, 0, 558106)}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ cat file.json ; echo ""
{"BaseModel.d64ac0c4-cc5b-462e-8332-35f3f6e62d7e": {"created_at": "2019-11-08T09:43:00.558089", "name": "Holberton", "__class__": "BaseModel", "my_number": 89, "id": "d64ac0c4-cc5b-462e-8332-35f3f6e62d7e", "updated_at": "2019-11-08T09:43:00.558106"}}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (d64ac0c4-cc5b-462e-8332-35f3f6e62d7e) {'name': 'Holberton', 'updated_at': datetime.datetime(2019, 11, 8, 9, 43, 0, 558106), 'id': 'd64ac0c4-cc5b-462e-8332-35f3f6e62d7e', 'my_number': 89, 'created_at': datetime.datetime(2019, 11, 8, 9, 43, 0, 558089)}
-- Create a new object --
[BaseModel] (5b7d1866-d7bc-45c7-9958-98042c3a0343) {'name': 'Holberton', 'updated_at': datetime.datetime(2019, 11, 8, 9, 43, 15, 973202), 'id': '5b7d1866-d7bc-45c7-9958-98042c3a0343', 'my_number': 89, 'created_at': datetime.datetime(2019, 11, 8, 9, 43, 15, 973188)}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (5b7d1866-d7bc-45c7-9958-98042c3a0343) {'name': 'Holberton', 'my_number': 89, 'created_at': datetime.datetime(2019, 11, 8, 9, 43, 15, 973188), 'id': '5b7d1866-d7bc-45c7-9958-98042c3a0343', 'updated_at': datetime.datetime(2019, 11, 8, 9, 43, 15, 973202)}
[BaseModel] (d64ac0c4-cc5b-462e-8332-35f3f6e62d7e) {'name': 'Holberton', 'my_number': 89, 'created_at': datetime.datetime(2019, 11, 8, 9, 43, 0, 558089), 'id': 'd64ac0c4-cc5b-462e-8332-35f3f6e62d7e', 'updated_at': datetime.datetime(2019, 11, 8, 9, 43, 0, 558106)}
-- Create a new object --
[BaseModel] (c2294559-6f6c-4a76-abae-d14cb8babd02) {'name': 'Holberton', 'my_number': 89, 'created_at': datetime.datetime(2019, 11, 8, 9, 44, 20, 205907), 'id': 'c2294559-6f6c-4a76-abae-d14cb8babd02', 'updated_at': datetime.datetime(2019, 11, 8, 9, 44, 20, 205924)}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ cat file.json ; echo ""
{"BaseModel.c2294559-6f6c-4a76-abae-d14cb8babd02": {"name": "Holberton", "my_number": 89, "__class__": "BaseModel", "created_at": "2019-11-08T09:44:20.205907", "id": "c2294559-6f6c-4a76-abae-d14cb8babd02", "updated_at": "2019-11-08T09:44:20.205924"}, "BaseModel.5b7d1866-d7bc-45c7-9958-98042c3a0343": {"name": "Holberton", "my_number": 89, "__class__": "BaseModel", "created_at": "2019-11-08T09:43:15.973188", "id": "5b7d1866-d7bc-45c7-9958-98042c3a0343", "updated_at": "2019-11-08T09:43:15.973202"}, "BaseModel.d64ac0c4-cc5b-462e-8332-35f3f6e62d7e": {"name": "Holberton", "my_number": 89, "__class__": "BaseModel", "created_at": "2019-11-08T09:43:00.558089", "id": "d64ac0c4-cc5b-462e-8332-35f3f6e62d7e", "updated_at": "2019-11-08T09:43:00.558106"}}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```

### [6. Console 0.0.1](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter:

```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) help quit

        Quits the command line - type 'quit' to exit command line

(hbnb) quit
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```

### [7. Console 0.1](./models/user.py)
* Update your command interpreter (console.py) to have these commands:

```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
294c15a7-1530-4c0c-af2f-0491f8794343
(hbnb) all BaseModel
["[BaseModel] (294c15a7-1530-4c0c-af2f-0491f8794343) {'id': '294c15a7-1530-4c0c-af2f-0491f8794343', 'created_at': datetime.datetime(2019, 11, 9, 2, 14, 39, 760216), 'updated_at': datetime.datetime(2019, 11, 9, 2, 14, 39, 760216)}"]
(hbnb) show BaseModel 294c15a7-1530-4c0c-af2f-0491f8794343
[BaseModel] (294c15a7-1530-4c0c-af2f-0491f8794343) {'id': '294c15a7-1530-4c0c-af2f-0491f8794343', 'created_at': datetime.datetime(2019, 11, 9, 2, 14, 39, 760216), 'updated_at': datetime.datetime(2019, 11, 9, 2, 14, 39, 760216)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 294c15a7-1530-4c0c-af2f-0491f8794343 first_name "Betty"
(hbnb) show BaseModel 294c15a7-1530-4c0c-af2f-0491f8794343
[BaseModel] (294c15a7-1530-4c0c-af2f-0491f8794343) {'id': '294c15a7-1530-4c0c-af2f-0491f8794343', 'first_name': 'Betty', 'created_at': datetime.datetime(2019, 11, 9, 2, 14, 39, 760216), 'updated_at': datetime.datetime(2019, 11, 9, 2, 15, 17, 941780)}
(hbnb) create BaseModel
273f40f9-002b-4dca-98c1-eb45d44797e1
(hbnb) all BaseModel
["[BaseModel] (273f40f9-002b-4dca-98c1-eb45d44797e1) {'created_at': datetime.datetime(2019, 11, 9, 2, 16, 24, 845049), 'id': '273f40f9-002b-4dca-98c1-eb45d44797e1', 'updated_at': datetime.datetime(2019, 11, 9, 2, 16, 24, 845049)}", "[BaseModel] (294c15a7-1530-4c0c-af2f-0491f8794343) {'created_at': datetime.datetime(2019, 11, 9, 2, 14, 39, 760216), 'id': '294c15a7-1530-4c0c-af2f-0491f8794343', 'first_name': 'Betty', 'updated_at': datetime.datetime(2019, 11, 9, 2, 15, 17, 941780)}"]
(hbnb) destroy BaseModel 273f40f9-002b-4dca-98c1-eb45d44797e1
(hbnb) show BaseModel 273f40f9-002b-4dca-98c1-eb45d44797e1
** no instance found **
(hbnb)
```

### [8. First User](./models/state.py)
* Write a class User that inherits from BaseModel:


### [9. More classes!](./console.py)
* Write all those classes that inherit from BaseModel:


### [10. Console 1.0](./console.py)
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review


### [11. All instances by class name](./console.py)
* Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().


### [12. Count instances](./console.py)
* Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().


### [13. Show](./console.py)
* Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).


### [14. Destroy](./console.py)
* Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).


### [15. Update](./console.py)
* Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).


### [16. Update from dictionary](./tests/test_console.py)
* Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).


---

## Author
* **Ryuichi Miyazaki** - [rmiyazaki6499](https://github.com/rmiyazaki6499)
