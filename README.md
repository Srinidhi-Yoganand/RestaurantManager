# Restaurant Manager App

A simple **Restaurant Management System** built with **MERN stack** (MongoDB, Express.js, React, Node.js). This application allows users to manage a list of restaurants, with features for adding, updating, and deleting restaurants. It also includes a user authentication system with JWT tokens to protect sensitive operations.

## Features

- **User Registration & Login**: Secure user registration and login using JWT authentication.
- **Restaurant Management**: Add, update, delete, and view restaurant data.
- **Protected Routes**: Secure access to restaurant management features with JWT token-based authentication.
- **Responsive UI**: The front-end is built with React and styled with custom CSS, making it responsive on both desktop and mobile devices.

## Tech Stack

- **Frontend**: React.js
- **Backend**: Node.js with Express.js
- **Database**: MongoDB
- **Authentication**: JWT (JSON Web Token)
- **Password Hashing**: bcryptjs

### Prerequisites

1. **Node.js**: Ensure Node.js is installed on your machine. You can download it from [here](https://nodejs.org/).
2. **MongoDB**: Install MongoDB locally or use a cloud database like MongoDB Atlas.

## API Endpoints

- **POST /register**: Register a new user (expects `username` and `password` in the body).
- **POST /login**: Login an existing user (expects `username` and `password` in the body).
    - Returns a JWT token upon successful login.
- **GET /restaurants**: Get the list of restaurants (requires JWT token in the `Authorization` header).
- **POST /insertRestaurants**: Insert a new restaurant (requires JWT token in the `Authorization` header).
    - Expects restaurant data (`id`, `name`, `type`, `location`, `rating`, `top_food`).
- **PUT /updateRestaurant/:id**: Update a restaurant (requires JWT token in the `Authorization` header).
    - Expects updated restaurant data in the body.
- **DELETE /deleteRestaurant/:id**: Delete a restaurant by ID (requires JWT token in the `Authorization` header).

## Usage

- **Login / Register**: Users must first register an account and then log in to access protected routes.
- **Manage Restaurants**: Once logged in, users can add, update, or delete restaurants from the database. A list of restaurants will be displayed once logged in.

## Screenshots

### Login / Register

![Login](screenshots/login.png)
![Register](screenshots/register.png)

### Restaurant Management

![General UI](screenshots/restaurant_management1.png)
![General UI](screenshots/restaurant_management2.png)

![Adding Restaurant Info](screenshots/insert_restaurant1.png)
![Adding Restaurant Info](screenshots/insert_restaurant2.png)

![Updating Restaurant Info](screenshots/update_restaurant1.png)
![Updating Restaurant Info](screenshots/update_restaurant2.png)

![Deleting Restaurant Info](screenshots/delete_restaurant1.png)
![Deleting Restaurant Info](screenshots/delete_restaurant2.png)
