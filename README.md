# Shopping Cart App

Simple Django shopping cart application.

## How to run:

1) Clone repository
2) Install dependencies 
3) Make migrations for DB `python3 manage.py migrate`
4) Create super user: `python3 manage.py createsuperuser`
5) Run the server: `python3 manage.py runserver`
6) Login to admin panel: `localhost:8000/admin`, add first/last to `Users` table for super user.
7) Add products to `Products` table.
8) Restart development server (step 5).
