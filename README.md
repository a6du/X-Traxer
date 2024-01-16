# X-Traxer - Daily Life Expense Tracker

X-Traxer is a simple and efficient expense tracker application built using Python Flask and several other technologies. It allows users to easily manage their daily life expenses, providing a convenient way to track and analyze spending patterns. Also, the app will be connected to a Large language Model(LLM) and this can help for a hassle free expense analysis on your data using the latest NLP technology.    

## Technologies Used

- **Python Flask**: A micro web framework for building web applications in Python.
- **Flask Smorest**: Extension for Flask that simplifies the creation of RESTful APIs.
- **Marshmallow**: A library for object serialization/deserialization.
- **Flask-JWT-extended**: Flask extension for JSON Web Token (JWT) authentication.
- **Flask-SQLAlchemy**: Flask extension for SQL databases, using SQLAlchemy as the ORM.
- **Postgres Database**: A powerful, open-source relational database.
- **Docker**: Containerization platform for packaging, distributing, and running applications.
- **Docker-compose**: A tool for defining and running multi-container Docker applications.

## Getting Started

Follow these steps to set up and run X-Traxer on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/x-traxer.git
cd x-traxer

2. Build and Run Docker Containers
bash
Copy code
docker-compose up --build
This command will build and start the Flask app, Postgres database, and pg-admin for database management.

3. API Documentation
Visit http://localhost:5000/swagger-ui to access the Swagger documentation for the API. This documentation provides details about the available endpoints and how to interact with them.

4. Authentication
X-Traxer uses JWT for authentication. To access protected endpoints, obtain a JWT token by making a request to the /login endpoint with valid credentials.
5. pg-admin
    You can viere

## Database Models
The application utilizes the following database models:

1. User: Represents a registered user.
2. Expense: Stores information about daily expenses.
3. Category: Categorizes expenses for better organization.
4. Tag: Allows users to add tags to expenses for further classification.
5. PaymentMethod: Records different methods of payment used for expenses.

## Relationships
One-to-Many: User has many expenses, category has many expenses.
Many-to-Many: Expense can have multiple tags.

##Contributing
Contributions are welcome! If you find any issues or have suggestions, please open an issue or create a pull request.

#License
This project is licensed under the MIT License - see the LICENSE file for details.

#Acknowledgments
Special thanks to the Flask, Docker, and SQLAlchemy communities for providing excellent tools and documentation.

Happy Expense Tracking with X-Traxer! 📊💸


# Steps taken:
1. Create an ER diagram for an already existing expense tracker app data.
2. Create the required DB models and the api endpoints.
3. Add tables that have one to many and many to many relationships with expenses table.
4. Dockerise the flask app, postgres DB and pg-admin.
5. Add authentication features using JWT.
6. 

# ToDo:
1. Unit testing in backend.
2. LLM model integration for analytics, data extraction and fast data retrievals. Also a motivator agent to reduce expense and increase investment.
3. Api integration of live stock market prices for tracking personal investment.
4. Front end creation for better user experience.
5. Unit testing for front-end.