## SAVVYHR SIMPLE API AUTH ENDPOINT

[![CircleCI](https://circleci.com/gh/olacodes/savvyHr.svg?style=svg)](https://circleci.com/pipelines/github/olacodes/savvyHr)

This is a simple user authentication api built with flask

### Technolgies

* [Python 3.8](https://python.org) : Base development programming language
* [Flask Framework](https://flask.palletsprojects.com/en/1.1.x/) : Host development framework built on top of python
* [SQLite](https://www.sqlite.org/) : Application backing relational databases
* [Flask-Restful Framework](https://flask-restful.readthedocs.io/en/latest/) : Provides API development tools for easy API development
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) : An ORM (object Relational Mapper) that used for easy databases access
* [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/): For generating JWT tokens
* [CircleCI]() : Continous Integration and Deployment


### How To Run This App
Few things you need to setup to get started, set up a virtual environment majorly for isolating installs.

#### Clone the repository
$ git clone https://github.com/olacodes/savvyHr.git

#### Install the requirements
install all requirements in the `requirements.txt` files within the virtual environment with the command `pip install -r requirements.txt`.

#### Change directory into the cloned folder
$ cd application

#### Start the application
$ export FLASK_APP=app.py

$ flask run

## Available Endpoints

#### Application Index
`make a GET to this api endpoint request`

* http://127.0.0.1:5000

#### Application Api Index
`make a GET to this api endpoint request`

* http://127.0.0.1:5000/api

#### User Registration Api Endpoint
`Make a POST request with username, email and password to this endpoint to register as a user`

* http://127.0.0.1:5000/api/register

#### User Login Api Endpoint
`Make a POST request with username and password of a registered user to this endpoint to login as a user`

* http://127.0.0.1:5000/api/login
  
#### Users Api Endpoint
`Make a GET request to this enpoint to see all registered users`

* http://127.0.0.1:5000/api/users

#### Protected Api Endpoint
This is a protected api endpoint that only allows login in users

`Make a GET request to this endpoint with authentication header of Bearer Token and value of your access token generated when logged in`
* http://127.0.0.1:5000/api/protected


## Owner
<div>
    <img src="https://res.cloudinary.com/olacode/image/upload/v1583016760/personal/sodiq_1_xorws5.webp" width='400px' height='400px'>
    <br /><sub><b>Olatunde Sodiq</b></sub>
</div>