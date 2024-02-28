# Autoservice Application Project

## Description
This Django project is designed for managing a car service. It includes features for handling car models, services, customer information, and order tracking.

## Features
- <b>Dashboard:</b> Provides an overview of the service statistics, including the number of services, cars, orders, and customers. It also displays the number of orders in progress, pending orders, and completed orders.

- <b>Car Models:</b> Allows superusers to view a list of car models, search for specific models, and access detailed information about each model.

- <b>Customers:</b> Provides a list of customers with the ability to search for specific customers based on various criteria such as car model, owner name, license plate, VIN number, etc.

- <b>Services:</b> Displays a list of services offered by the car service. Users can search for specific services based on the service name or price.

- <b>Order Lines:</b> Allows superusers to view and manage order lines, including information about the ordered services, order date, car details, quantity, repair status, and car problems.

- <b>User Services:</b> Displays order history for the currently logged-in user, allowing them to track their previous services.

- <b>User Authentication:</b> Includes user registration, login, and profile update functionalities. Customers can create and manage their profiles. When superuser creates an order, an profile is automatically created for the customer with the username and default password: Test123.

- <b>Admin Panel:</b> Superusers have special access to certain features in the admin panel. They can perform CRUD operations on car models, services, and order lines.

## Installation
1. Clone the repository to your local machine:
```bash
https://github.com/EdvinasJuo/AutoserviceApp.git
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
python manage.py migrate
```

4. Create a superuser account to access the admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your superuser account.

5. Run the development server:
```bash
python manage.py runserver
```
Visit http://localhost:8000/admin to log in with your superuser credentials and start managing the car service data.

## Usage
1. Log in to the admin panel to manage car models, services, customers, and orders.

2. Navigate to the dashboard for a quick overview of service statistics.

3. Explore other sections like car models, customers, services, and order lines for more detailed information.

4. Use the search functionality to find specific data within each section.

5. Superusers have access to additional features and can perform CRUD operations on car models, services, and order lines.
   
7. Customers can create and manage their profiles, and when superuser places an order, an user profile is automatically created for them with the default password: Test123.

## Screenshots
