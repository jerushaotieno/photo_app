### Author
Jerusha Otieno

### Description
This is a clone of the website for the popular photo app Instagram. 

### User Story
A user of the application is able to:

* Sign in to the application to start using the application.
*  Upload pictures to the application.
* See their profile with all their pictures.
* Follow other users and see their pictures on the user's timeline.
* Like a picture and leave a comment on it.

### Prerequisites
Install all project requirements using the package manager pip.

(virtual) $ pip install -r requirements.txt

### Installation
* Use the .env.example file to create a .env file with appropriate values to get a development env running.
* Create a postgres db and add the credentials to .env file
* Apply all migrations
    (virtual) $ python manage.py migrate 

* Create admin account
    (virtual) $ python manage.py createsuperuser

* Make migrations to your database
    (virtual) $ python manage.py makemigrations (app name)
    (virtual) $ python manage.py migrate

* Start development server
    (virtual) $ python3 manage.py runserver

### Running Tests
To run automated tests for the system:

(virtual) $ python3 manage.py test (app name)

### Deployment
With all environment variables changed to suit your local copy of this repository, deploy the application to Heroku to see it live or simply run it locally

(virtual) $ python3 manage.py runserver

### Technology Used
* Django 3.0.8 - The web framework used 
* Heroku - Deployment platform 
* Python3 - Backend logic 
* Postresql - Database system

### Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

### Contact Information
If you have any question or contributions, please email: jerushaotienocoding@gmail.com

### License
MIT License

### Copyright
Copyright (c) 2022 Jerusha Otieno