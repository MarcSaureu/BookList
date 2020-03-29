# BookList
Web Project - Main Project

## Collaborators
* Ahmed Azzamouri
* Pau Agusti
* Daniel Farre
* Guillem Felis
* Marc Saureu

## Tecnologias
### Back-End
Para desarrollar la logica de negocio de BookList utilizamos las siguientes tecnologias:
- [X] Utilizamos el ***Framework* Django** en su ultima versión, la 3.1.
- [X] Utilizamos la libreria: **Google Books APIs**

### Front-End
Para desarrollar la interfaz web de BookList utilizamos las siguientes tecnologias:
- [X] Utilización de **HTML 5**
- [X] Utilización de **CSS 3**
- [X] Utilización de la versión 4 del famoso Framework **Bootstrap**


## How to RUN
### Requisites
- [X] This project uses [**python 3.7.6**][1] and pip.
- [X] With the first step done, you will need to install with pip all the prerequisites in *requirements.txt*.

[1]: https://www.python.org/downloads/release/python-376/ "Download Python 3.7.6"
  
### Running Project
First of all you **need to clone the repository** before the requeriments part:  
```console
$ source venv/bin/activate
$ pip install whitenoise
$ python manage.py runserver
```

### Users

  - **Admin** User
    * Username : **admin**
    * Password : **admin**

  - **Normal** User
    * Username : **provauser**
    * Password : **user1234**

## Design Decisions
Models
:  The model we are using is defined in the file *ClassDiagram.png*

## License

Copyright (c) **BookList**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
