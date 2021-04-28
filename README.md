# EDA - LevelUp

Este repositorio contiene el proyecto que se desarollara para la clase de Estructuras de Datos de la Universidad Nacional de Colombia Semestre 2021-1

# Getting Started

Before working on this project, ensure your dependencies are up to date (preferably in a virtual environment).

`pip install -r requirements.txt`

## Hosting requirements
It is important to be able to start up a localhost on your computer.
Ideally use a WAMP or LAMP stack for this project.
However, separate hosting is also possible.

## When running Django
Remember to navigate to the Django where you will see the file **manage.py**:
`cd LevelUp`

## MongoDb Setup
Remember to startup your **mongodb** database 'EDA-Project' locally before running.
Remember to make migrations and migrate as well:
`python manage.py makemigrations`
`python manage.py migrate`

## C++ Volume protocol requirements
To use the volume protocol it is important to compile the C++ libraries into a shared link library in C in order to succesfully import into the python interpeter.
Through terminal navigate to the project's working directory.
Once there navigate to **structures_cpp**:
`cd LevelUp/structures_cpp`

**_This is not necessary to run the general program. It is only necesary to run the volume protocol at localhost:8000/volume_**

### On Linux
Using the internal **g++** compiler create the **libmain.so** shared library with the following commands:
`g++ -c -fPIC main.cpp -o main.o`
`g++ -shared -Wl,-soname,libmain.so -o libmain.so main.o`

This will generate the required shared library file libmain.so for use in python runVolumeProtocol

### On Windows
Depending on your windows distribution and available g++ compiler the compilation commands to generate the **libmain.dll** shared link library may vary.
Please verify the necessary commands for your distribution.
Once generating the .dll file you must change the file in _line 4_ in the file *generate\_volume\_cpp.py* to:
`run = cdll.LoadLibrary("structures_cpp/libmain.dll")`
