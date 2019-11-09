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

```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
-- Reloaded objects --
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
-- Create a new User --
[User] (83e494ae-8e2f-439e-a586-2e68e84671dc) {'last_name': 'Holberton', 'first_name': 'Betty', 'password': 'root', 'email': 'airbnb@holbertonshool.com', 'id': '83e494ae-8e2f-439e-a586-2e68e84671dc', 'created_at': datetime.datetime(2019, 11, 9, 3, 36, 23, 762584), 'updated_at': datetime.datetime(2019, 11, 9, 3, 36, 23, 762602)}
-- Create a new User 2 --
[User] (9fd30a8b-ab1d-40df-b83b-7e5419c606d2) {'first_name': 'John', 'password': 'root', 'email': 'airbnb2@holbertonshool.com', 'id': '9fd30a8b-ab1d-40df-b83b-7e5419c606d2', 'created_at': datetime.datetime(2019, 11, 9, 3, 36, 23, 764619), 'updated_at': datetime.datetime(2019, 11, 9, 3, 36, 23, 764641)}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4'}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba'}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4'}
[User] (9fd30a8b-ab1d-40df-b83b-7e5419c606d2) {'id': '9fd30a8b-ab1d-40df-b83b-7e5419c606d2', 'created_at': datetime.datetime(2019, 11, 9, 3, 36, 23, 764619), 'updated_at': datetime.datetime(2019, 11, 9, 3, 36, 23, 764641), 'email': 'airbnb2@holbertonshool.com', 'password': 'root', 'first_name': 'John'}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f'}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce'}
[User] (83e494ae-8e2f-439e-a586-2e68e84671dc) {'id': '83e494ae-8e2f-439e-a586-2e68e84671dc', 'created_at': datetime.datetime(2019, 11, 9, 3, 36, 23, 762584), 'updated_at': datetime.datetime(2019, 11, 9, 3, 36, 23, 762602), 'last_name': 'Holberton', 'email': 'airbnb@holbertonshool.com', 'password': 'root', 'first_name': 'Betty'}
-- Create a new User --
[User] (40b4407d-2945-404e-ba72-1e625abd8965) {'id': '40b4407d-2945-404e-ba72-1e625abd8965', 'created_at': datetime.datetime(2019, 11, 9, 3, 36, 44, 168207), 'updated_at': datetime.datetime(2019, 11, 9, 3, 36, 44, 168227), 'last_name': 'Holberton', 'email': 'airbnb@holbertonshool.com', 'password': 'root', 'first_name': 'Betty'}
-- Create a new User 2 --
[User] (8d5f2bf6-e59a-417f-b4ed-2a2384b99060) {'id': '8d5f2bf6-e59a-417f-b4ed-2a2384b99060', 'created_at': datetime.datetime(2019, 11, 9, 3, 36, 44, 170341), 'updated_at': datetime.datetime(2019, 11, 9, 3, 36, 44, 170362), 'email': 'airbnb2@holbertonshool.com', 'password': 'root', 'first_name': 'John'}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ cat file.json ; echo ""
{"User.40b4407d-2945-404e-ba72-1e625abd8965": {"id": "40b4407d-2945-404e-ba72-1e625abd8965", "created_at": "2019-11-09T03:36:44.168207", "email": "airbnb@holbertonshool.com", "updated_at": "2019-11-09T03:36:44.168227", "last_name": "Holberton", "first_name": "Betty", "password": "root", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "User.8d5f2bf6-e59a-417f-b4ed-2a2384b99060": {"id": "8d5f2bf6-e59a-417f-b4ed-2a2384b99060", "created_at": "2019-11-09T03:36:44.170341", "updated_at": "2019-11-09T03:36:44.170362", "email": "airbnb2@holbertonshool.com", "first_name": "John", "password": "root", "__class__": "User"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "User.9fd30a8b-ab1d-40df-b83b-7e5419c606d2": {"id": "9fd30a8b-ab1d-40df-b83b-7e5419c606d2", "created_at": "2019-11-09T03:36:23.764619", "updated_at": "2019-11-09T03:36:23.764641", "email": "airbnb2@holbertonshool.com", "first_name": "John", "password": "root", "__class__": "User"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.83e494ae-8e2f-439e-a586-2e68e84671dc": {"id": "83e494ae-8e2f-439e-a586-2e68e84671dc", "created_at": "2019-11-09T03:36:23.762584", "email": "airbnb@holbertonshool.com", "updated_at": "2019-11-09T03:36:23.762602", "last_name": "Holberton", "first_name": "Betty", "password": "root", "__class__": "User"}}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ cat file.json ; echo ""
{"User.40b4407d-2945-404e-ba72-1e625abd8965": {"id": "40b4407d-2945-404e-ba72-1e625abd8965", "created_at": "2019-11-09T03:36:44.168207", "email": "airbnb@holbertonshool.com", "updated_at": "2019-11-09T03:36:44.168227", "last_name": "Holberton", "first_name": "Betty", "password": "root", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "User.8d5f2bf6-e59a-417f-b4ed-2a2384b99060": {"id": "8d5f2bf6-e59a-417f-b4ed-2a2384b99060", "created_at": "2019-11-09T03:36:44.170341", "updated_at": "2019-11-09T03:36:44.170362", "email": "airbnb2@holbertonshool.com", "first_name": "John", "password": "root", "__class__": "User"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "User.9fd30a8b-ab1d-40df-b83b-7e5419c606d2": {"id": "9fd30a8b-ab1d-40df-b83b-7e5419c606d2", "created_at": "2019-11-09T03:36:23.764619", "updated_at": "2019-11-09T03:36:23.764641", "email": "airbnb2@holbertonshool.com", "first_name": "John", "password": "root", "__class__": "User"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.83e494ae-8e2f-439e-a586-2e68e84671dc": {"id": "83e494ae-8e2f-439e-a586-2e68e84671dc", "created_at": "2019-11-09T03:36:23.762584", "email": "airbnb@holbertonshool.com", "updated_at": "2019-11-09T03:36:23.762602", "last_name": "Holberton", "first_name": "Betty", "password": "root", "__class__": "User"}}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ cat file.json ; echo ""
{"User.40b4407d-2945-404e-ba72-1e625abd8965": {"id": "40b4407d-2945-404e-ba72-1e625abd8965", "created_at": "2019-11-09T03:36:44.168207", "email": "airbnb@holbertonshool.com", "updated_at": "2019-11-09T03:36:44.168227", "last_name": "Holberton", "first_name": "Betty", "password": "root", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "User.8d5f2bf6-e59a-417f-b4ed-2a2384b99060": {"id": "8d5f2bf6-e59a-417f-b4ed-2a2384b99060", "created_at": "2019-11-09T03:36:44.170341", "updated_at": "2019-11-09T03:36:44.170362", "email": "airbnb2@holbertonshool.com", "first_name": "John", "password": "root", "__class__": "User"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "User.9fd30a8b-ab1d-40df-b83b-7e5419c606d2": {"id": "9fd30a8b-ab1d-40df-b83b-7e5419c606d2", "created_at": "2019-11-09T03:36:23.764619", "updated_at": "2019-11-09T03:36:23.764641", "email": "airbnb2@holbertonshool.com", "first_name": "John", "password": "root", "__class__": "User"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.83e494ae-8e2f-439e-a586-2e68e84671dc": {"id": "83e494ae-8e2f-439e-a586-2e68e84671dc", "created_at": "2019-11-09T03:36:23.762584", "email": "airbnb@holbertonshool.com", "updated_at": "2019-11-09T03:36:23.762602", "last_name": "Holberton", "first_name": "Betty", "password": "root", "__class__": "User"}}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```

### [9. More classes!](./console.py)
* Write all those classes that inherit from BaseModel:
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) all
["[Place] (82b45132-04bb-4153-bc22-0a2ed44c12c0) {'updated_at': datetime.datetime(2019, 11, 9, 3, 39, 16, 767687), 'id': '82b45132-04bb-4153-bc22-0a2ed44c12c0', 'created_at': datetime.datetime(2019, 11, 9, 3, 39, 16, 767687)}", "[Amenity] (cda4a63a-9ef2-4c66-9b11-ccd474bf4aa5) {'updated_at': datetime.datetime(2019, 11, 9, 3, 39, 11, 407578), 'id': 'cda4a63a-9ef2-4c66-9b11-ccd474bf4aa5', 'created_at': datetime.datetime(2019, 11, 9, 3, 39, 11, 407578)}", "[State] (7d5e1594-5242-498e-bc24-1c7baceb4fee) {'updated_at': datetime.datetime(2019, 11, 9, 3, 39, 2, 393367), 'id': '7d5e1594-5242-498e-bc24-1c7baceb4fee', 'created_at': datetime.datetime(2019, 11, 9, 3, 39, 2, 393367)}", "[City] (62c496a6-7a6b-4185-bb53-e92870c04d3c) {'updated_at': datetime.datetime(2019, 11, 9, 3, 39, 6, 1272), 'id': '62c496a6-7a6b-4185-bb53-e92870c04d3c', 'created_at': datetime.datetime(2019, 11, 9, 3, 39, 6, 1272)}", "[Review] (dc4a95ae-a130-4791-880c-91e288e1cace) {'updated_at': datetime.datetime(2019, 11, 9, 3, 39, 22, 509737), 'id': 'dc4a95ae-a130-4791-880c-91e288e1cace', 'created_at': datetime.datetime(2019, 11, 9, 3, 39, 22, 509737)}"]
(hbnb)
{"Amenity.cda4a63a-9ef2-4c66-9b11-ccd474bf4aa5": {"updated_at": "2019-11-09T03:39:11.407578", "__class__": "Amenity", "created_at": "2019-11-09T03:39:11.407578", "id": "cda4a63a-9ef2-4c66-9b11-ccd474bf4aa5"}, "State.7d5e1594-5242-498e-bc24-1c7baceb4fee": {"updated_at": "2019-11-09T03:39:02.393367", "__class__": "State", "created_at": "2019-11-09T03:39:02.393367", "id": "7d5e1594-5242-498e-bc24-1c7baceb4fee"}, "City.62c496a6-7a6b-4185-bb53-e92870c04d3c": {"updated_at": "2019-11-09T03:39:06.001272", "__class__": "City", "created_at": "2019-11-09T03:39:06.001272", "id": "62c496a6-7a6b-4185-bb53-e92870c04d3c"}, "Place.82b45132-04bb-4153-bc22-0a2ed44c12c0": {"updated_at": "2019-11-09T03:39:16.767687", "__class__": "Place", "created_at": "2019-11-09T03:39:16.767687", "id": "82b45132-04bb-4153-bc22-0a2ed44c12c0"}, "Review.dc4a95ae-a130-4791-880c-91e288e1cace": {"updated_at": "2019-11-09T03:39:22.509737", "__class__": "Review", "created_at": "2019-11-09T03:39:22.509737", "id": "dc4a95ae-a130-4791-880c-91e288e1cace"}}
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```

### [10. Console 1.0](./console.py)
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review


### [11. All instances by class name](./console.py)
* Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) User.all()
["[User] (700534fd-2e57-4c5f-86da-4908b9ec483c) {'created_at': datetime.datetime(2019, 11, 9, 3, 43, 28, 44380), 'updated_at': datetime.datetime(2019, 11, 9, 3, 43, 28, 44380), 'id': '700534fd-2e57-4c5f-86da-4908b9ec483c'}", "[User] (f46abdec-26e1-432e-910a-a9fe097870b4) {'created_at': datetime.datetime(2019, 11, 9, 3, 43, 10, 36878), 'updated_at': datetime.datetime(2019, 11, 9, 3, 43, 10, 36878), 'id': 'f46abdec-26e1-432e-910a-a9fe097870b4'}"]
(hbnb)
```

### [12. Count instances](./console.py)
* Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) User.count()
2
(hbnb)
```

### [13. Show](./console.py)
* Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) User.show(f46abdec-26e1-432e-910a-a9fe097870b4)
[User] (f46abdec-26e1-432e-910a-a9fe097870b4) {'updated_at': datetime.datetime(2019, 11, 9, 3, 43, 10, 36878), 'created_at': datetime.datetime(2019, 11, 9, 3, 43, 10, 36878), 'id': 'f46abdec-26e1-432e-910a-a9fe097870b4'}
(hbnb)
```

### [14. Destroy](./console.py)
* Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("f46abdec-26e1-432e-910a-a9fe097870b4")
(hbnb) User.count()
1
(hbnb) User.destroy("Holberton")
** no instance found **
(hbnb)
```

### [15. Update](./console.py)
* Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) City.show("62c496a6-7a6b-4185-bb53-e92870c04d3c")
[City] (62c496a6-7a6b-4185-bb53-e92870c04d3c) {'id': '62c496a6-7a6b-4185-bb53-e92870c04d3c', 'created_at': datetime.datetime(2019, 11, 9, 3, 39, 6, 1272), 'updated_at': datetime.datetime(2019, 11, 9, 3, 39, 6, 1272)}
(hbnb)
(hbnb) City.update("62c496a6-7a6b-4185-bb53-e92870c04d3c", "name", "Santa Barbara")
(hbnb) City.update("62c496a6-7a6b-4185-bb53-e92870c04d3c", "home_town", "True")
(hbnb)
[City] (62c496a6-7a6b-4185-bb53-e92870c04d3c) {'created_at': datetime.datetime(2019, 11, 9, 3, 39, 6, 1272), 'home_town': 'True', 'id': '62c496a6-7a6b-4185-bb53-e92870c04d3c', 'name': 'Santa Barbara', 'updated_at': datetime.datetime(2019, 11, 9, 3, 49, 5, 85672)}
(hbnb)
```

### [16. Update from dictionary](./tests/test_console.py)
* Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).


---

## Author
* **Jessica Bathel** - [jbathel](https://github.com/jbathel)
* **Ryuichi Miyazaki** - [rmiyazaki6499](https://github.com/rmiyazaki6499)
