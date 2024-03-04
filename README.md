# swcms
School Website Content Management System
Author -Vijay Kumar

Create a Folder swcms

create Virtual Enviornment

    python -m venv venv

Activate virtual Enviornment
    
    source venv/Scripts/activate

Install Django

    pip install django
    

Create Django Project in Present Working Directory

    django-admin startproject school .
    

Test Server

    python manage.py runserver 


Apply Admin Migrations

    python manage.py migrate

Create Admin Login

    python manage.py createsuperuser

