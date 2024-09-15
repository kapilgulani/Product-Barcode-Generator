# Product Barcode Generator

Product Barcode Generator is a Django web application that allows users to generate barcodes for their products and store their details in a MySQL database. The application consists of four main pages: Home, About, Register, and Search.

## Features

1. **Home Page**: Provides an introduction to the application and its purpose.
2. **About Page**: Gives more information about the application and its features.
3. **Register Page**: Allows users to register product details such as name, address, buying price, and selling price. The application generates a random 12-digit barcode, stores the barcode number in the database, and generates a barcode image that is saved in the file system.
4. **Search Page**: Requires login credentials. Users can enter a barcode number to retrieve the details of the corresponding product from the database.

## Prerequisites

1. **XAMPP**: Install XAMPP to set up the MySQL database and Apache web server.
2. **Python and Django**: Install Python and Django to develop and run the web application.

## Setup Instructions

1. **Start XAMPP**: Open XAMPP and start the Apache and MySQL modules.
2. **Create a MySQL database**: Use phpMyAdmin or the MySQL command line interface to create a new database for the application.
3. **Configure the Django project**: Update the `settings.py` file in the Django project with the MySQL database connection details.
4. **Run the Django development server**: Open a command prompt, navigate to the Django project directory, and run the command `python manage.py runserver` to start the development server.
5. **Access the application**: Open a web browser and go to `http://localhost:8000` to access the Product Barcode Generator application.

## Technologies Used

- Python
- Django
- MySQL
- XAMPP
- HTML
- CSS
- JavaScript

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License.
