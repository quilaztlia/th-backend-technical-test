# backend-technical-test

Technical test for backend developer candidates at LPI

## 1. Create a repository from the template

Go on https://github.com/CyberCRI/backend-technical-test and select *Use this template*.

Create a new repository to avoid modifying the template, make it private and share it with the person who will evaluate your test when you are done.

## 2. Run locally

### Requirements

- Docker
- Docker Compose V2

### Run the stack

    make local

### Migrate the database

The stack need to be running in another terminal.

    make bash
    python manage.py migrate

## 3. Exercise

The structure of the project is already created and the dependencies to django, django rest framework and postgres are already listed in the `requirements.txt` file.

You will find the main project package in `/technicaltest`, and the django applications in the `/apps` directory.

You must at least complete the required tasks, if you want you can also work on the optional tasks, are you can just look at them to discuss how you would have done them with your interviewer. 

### Required tasks

#### 1. Create models

Create the following models in the relevant apps : 

**Meeting**

The following fields are required : 

- title (name of the meeting)
- description (free text field)
- date (date and time of the meeting)
- duration (in minutes)
- contacts (you can have a meeting with several contacts)
- status (completed, to do, canceled, etc.)

**Contact**

The following fields are required :

- first name
- last name
- email
- phone number

#### 2. Create the views

Using django rest framework, create the views and serializers needed to create, read, update and delete instances of these models and create urls for these views.

### Optional tasks

You don't have to complete these tasks, and you can complete them in any order you want.

#### 1. Add filters to the routes

#### 2. Implement tests

#### 3. Create a user model and authentication system 
 
#### 4. Make the routes accessible by authenticated users (needs #3)