Welcome to Romy's Coffee!

Final Project CS50

INTRODUCTION

ROMY'S COFFEE is a small web-application that is using Python and JavaScript with the aim of selling and presenting varieties of coffee.

My web application is utilizing Django (has more than one model) on the back-end and JavaScript on the front-end.
Romy's Coffee is build in that way that is mobile-responsive.

LET'S GO THROUGH THE FILES!

Inside tha main folder 'CAPSTONE', we have two other folders: 'capstone' and 'RoMoCcino'.

capstone folder:

This folder is created by Django when initializing a new project. In urls.py I've include the paths for my application 'Romy's Coffee', so I can edit my paths directly in the urls.py within my application's folder.

RoMoCcino folder:

Here in this other folder is mostly everything. I'll try to explain the most relevant.

RoMoCcino/models.py: This is where I defined my models for my web application, where each model represents some type of data I want to store in my database. I’ve started you with a User model that represents each user of the application. Because it inherits from AbstractUser, it will already have fields for a username, email, password, etc. Each time I changed anything in RoMoCcino/models.py, I had to run python manage.py makemigrations and then python manage.py migrate to migrate those changes to the database. This applies also when you make a new model(new class).

RoMoCcino/urls.py: the place where the URL configuration for this app is defined.

RoMoCcino/views.py: This is where we see the views that are associated with each of the routes that we defined in RoMoCcino/urls.py. The basics like 'home' page, to 'register' a user, to 'login' or 'logout'. I also have implemented the collections of the products where a user can see all of the products specific to that category. I also have a view for the cart itslef, add to cart, and products.

Templates folder:

All the HTML code for the templates.

'index.html' is one of interest. Here you can see the main page with all the functionality of the app. Here we find all the popular products where we have the option to select just one product and see details about it and if we wish we can go ahead and add to cart or continie shopping and navigatinf through the website options. From here also we can easlity navigate to other templates like 'collections.html' by clicking on the "Caffeinate my day!", or "My Order" to se the status of want we added to the cart.

Static folder:

This project has been making use of a local copy of Bootstrap stylesheets plus an customized CSS stylesheet.

Also we have static/js where we are using Java Script for the functionality of the cart.

For the app to run we need to type in the terminal: python manage.py runserver

I believe my project satisfies the distinctiveness and complexity requirements, mentioned by the CS50 course becasue is made from scratch with no guidance and I implemented all the functionality of the app by using all that we have learned during this intense course, like Python, Java Script, Django, Bootstrap and also I added Glide.js in my project(for this you will need to install glide by running ("npm install @glidejs/glide").

I hope you ennjoyed visiting Romi's Coffee.
