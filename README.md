# Smart Delivery Time Prediction System

## Overview

The Smart Delivery Time Prediction System is a Machine Learning-powered web application that predicts the estimated delivery time of orders based on multiple real-world factors. The system helps logistics and delivery services improve operational efficiency, optimize delivery planning, and enhance customer satisfaction.

## Features

* Predict delivery time using a trained Machine Learning model
* Interactive analytics dashboard with visual insights
* Prediction history stored in MySQL database
* Vehicle type and weather-based analysis
* Weather condition filtering and analytics
* Real-time KPI metrics and performance visualization
* Database integration for persistent storage
* Modern Streamlit user interface with custom styling

## Input Features

The prediction model uses the following features:

* Distance (km)
* Order Preparation Time (minutes)
* Traffic Index
* Number of Items
* Weekend Indicator
* Order Hour
* Weather Condition
* Vehicle Type

## Output

* Predicted Delivery Time (minutes)

## Technology Stack

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python
* Pandas
* NumPy
* PyMySQL

### Machine Learning

* Scikit-learn
* XGBoost

### Database

* MySQL

### Visualization

* Plotly Express

## Application Modules

### Home

Provides an overview of the application and navigation to all modules.

### Prediction

Allows users to enter delivery-related information and generate delivery time predictions using the trained machine learning model.

### Analytics

Displays interactive charts, KPI cards, traffic analysis, weather analysis, vehicle performance insights, and delivery trends from stored prediction data.

### History

Maintains a record of all previous predictions stored in the MySQL database for future reference and analysis.

### About

Contains project information, technologies used, and system architecture details.

## System Workflow

User Input → Data Preprocessing → Machine Learning Prediction → Store Results in MySQL → Analytics & History Dashboard

## Key Benefits

* Improves delivery planning and resource allocation
* Provides data-driven insights for logistics operations
* Reduces uncertainty in delivery estimation
* Supports business decision-making through analytics
* Enhances customer experience with accurate delivery predictions

## Future Enhancements

* FastAPI backend integration
* Real-time traffic and weather API integration
* User authentication system
* Deployment on cloud platforms
* Advanced forecasting and reporting features

