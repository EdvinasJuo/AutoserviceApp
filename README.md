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
- <b>Log in</b>
Shows log in form and if there is a bad log in then an error is displayed

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/f3c87847-977f-4793-9d1a-60f6ff2f4ed5)

### Superuser screenshots

Home page:
![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/d84f596f-9297-4e3a-9aef-1809c069e3d5)

Order Lines page:

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/e0d3311c-2147-4fe2-8523-261077e99a25)

New Order form:

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/50d72579-4a5d-49de-9055-91b38fb11b17)


Order Details view:

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/939f0729-d9ee-4704-ae4b-8a05473af468)

Services page:

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/9c703989-1ace-4059-b471-35df87219a8f)


Profile page:

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/f7a42efc-e823-4e5c-98aa-6693bf8ab33e)

### User screenshots

Main page: 

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/2384ec24-fccc-4d35-be54-89181406118c)

My services page:

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/e79f5c27-a58f-473e-971e-95d4658fc455)


My order details:

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/cf67ff93-59c6-4d9c-9eed-4d49e3c17e34)

Services page with prices:

![image](https://github.com/EdvinasJuo/AutoserviceApp/assets/97233138/9d777772-efba-4146-96df-674502abe34a)


## Contact
For any questions or feedback, feel free to contact me: edvinasjuodeika@gmail.com
