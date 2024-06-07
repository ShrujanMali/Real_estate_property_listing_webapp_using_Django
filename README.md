# Real Estate web application using Django

## Overview

This project is a real estate listing web application developed using Django. Initially conceptualized as a blog application, it has been adapted to allow users to sell, rent, or lease properties such as apartments, flats, and bungalows. The application includes user authentication, CRUD operations for property listings, a contact form for inquiries, and an integrated map to display property locations using TomTom geocoder and map services. And also implemented the serach functionality for seamles peroperty search.


## Features
  
  1. User Authentication: Users can sign up, log in, and change their passwords.
  2. Property Listings: Users can create, view, update, and delete property listings with details such as title, description, address, price, and type (sell, rent, lease).
  3. Contact Us Form: Users can fill out a form with their name, email, subject, and message to send inquiries or feedback. These inquiries are sent to the admin via Mailtrap.
  4. Property Map: The application converts property addresses into latitude and longitude using TomTom geocoder and displays all properties on a map using TomTom map services.
  5. Search functionality: User can serach the property by City, Amenities, Property type

## Technology Stack

   1. Django: Web framework used to build the application.
   2. SQLite: Database used to store user and property data.
   3. WTForms: Library used for form handling.
   4. Geocoder: Used to convert property addresses into latitude and longitude.
   5. TomTom Maps: Used to display property locations on an interactive map.
   6. Mailtrap: Email service used to handle inquiry submissions.
   7. HTML/CSS: Front-end design and styling.
