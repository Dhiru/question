# Django API with Django Rest Framework

This is on build API with GET, POST, PUT call using Django Rest Framework.
Django REST framework is a powerful and flexible toolkit for building Web APIs.

# Setup

This is requried Django and Djangorestframework of python package

## Installation command

1. pip install Django==9.1
2. pip install djangorestframework


# Run the Server

python manage.py runserver


# URLS to hit on browser:

1. http://127.0.0.1:8000/book
2. http://127.0.0.1:8000/modify/<reservation_id>

# Project

This support API for create and modify reservation booking with API urls.
The models.py has class ReservationList- with attribute (name, check_in, check_out, status, count)
In views.py ListCreateAPIView, RetrieveUpdateDestroyAPIView inherited class from rest_frame, 
the following class helps to create and modify entry with linked to models.
 
