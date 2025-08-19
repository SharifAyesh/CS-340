# CS-340
Client Server Development 


Project Two

Grazioso Salvare- Austin Animal Outcomes


Overview

This project implements an interactive data dashboard for Grazioso Salvare, designed to help the organization efficiently track, filter, and visualize animal outcome data from the Austin Animal Center. The application connects to a MongoDB database containing detailed animal intake and outcome records, including breed, age, sex, outcome type, and geolocation data.

Through the dashboard, users can filter results by rescue type (Water Rescue, Mountain/Wilderness Rescue, Disaster/Individual Tracking) and preferred breed, with the option to reset filters instantly. Data is displayed in an interactive, searchable table, while dynamic visualizations, including a pie chart for outcome types and a geolocation map for animal locations, update automatically based on the user’s selections.

The dashboard is built using Plotly Dash, providing a responsive and user-friendly interface that integrates seamlessly with the MongoDB backend. This tool enhances Grazioso Salvare’s ability to identify animals suitable for specific rescue missions, monitor adoption trends, and analyze outcome patterns in real time, ultimately supporting data-driven decision-making for their rescue operations.

Required Functionality
The dashboard meets the following functionality requirements:
1.	Filter Options
•	Radio buttons to filter animals by rescue type:
1.	Water Rescue
2.	Mountain/Wilderness Rescue
3.	Disaster/Individual Tracking
4.	Reset (show all data)
•	Dropdown menu to filter by preferred breed within a selected rescue type.
2.	Dynamic DataTable
•	Displays filtered animal data including animal_id, name, breed, age_upon_outcome, sex_upon_outcome, outcome_type, and more.
•	Supports scrolling, sorting, and searching within columns.
3.	Interactive Visualizations
•	Pie chart showing distribution of Outcome Types for the current filter.
•	Geolocation map plotting the latitude and longitude of animals in the filtered dataset.
4.	Branding
•	Displays the Grazioso Salvare logo at the top of the page.

Screenshots 
 
    










Tools Used and Rationale

MongoDB
•	Role: Stores the Austin Animal Center dataset and serves as the model component in the project.
•	Reason for Use: MongoDB’s flexible schema is ideal for handling JSON-like documents, allowing the dataset to include additional fields like location_lat, location_long, and age_upon_outcome_in_weeks without structural issues. It integrates seamlessly with Python via the PyMongo library, enabling direct CRUD operations.

Python
•	Role: Backend logic for querying and processing MongoDB data.
•	Reason for Use: Python offers robust data handling, strong library support for dashboards, and easy integration with MongoDB.

Dash by Plotly
•	Role: Provides the framework for building the interactive web application.
•	Reason for Use: Dash simplifies creating data-driven web apps entirely in Python, without needing separate front-end languages. It supports responsive layouts, interactive components, and dynamic visual updates.

Leaflet (via Dash Leaflet)
•	Role: Renders the geolocation map.
•	Reason for Use: Dash Leaflet integrates mapping features directly into the Dash app, allowing real-time updates to plotted coordinates.

Steps to Complete the Project
1.	Upload the dataset to MongoDB
•	Use the provided Austin Animal Center CSV file.
•	Import it into your MongoDB database (AAC) and collection (animals).
•	Ensure the file contains location_lat, location_long, and age_upon_outcome_in_weeks fields.
2.	Create the CRUD Python module
•	Develop animal_shelter.py to perform Create, Read, Update, and Delete operations.
•	Connect to the MongoDB instance using credentials and connection details provided in the course environment.
3.	Develop the dashboard layout
•	Create interactive components (radio buttons, dropdowns, DataTable, pie chart, and map).
•	Configure callbacks to update the DataTable, pie chart, and map based on user selections.
4.	Add branding
•	Create an assets folder.
•	Place the provided grazioso_logo.png file inside this folder.
5.	Test functionality
•	Verify that each filter updates all dashboard components as expected.
•	Take required screenshots for submission.

Challenges and Solutions

During development, several challenges were encountered. The first issue involved incorrect constructor parameters for the AnimalShelter class, which caused initialization errors. This was resolved by updating both the class and the dashboard instantiation so that parameter names matched exactly between the Python module and the notebook. The second challenge arose from data type conflicts in function parameters, specifically when mixing str type annotations with NoneType defaults. This was addressed by adjusting the function signatures to set proper default values without creating type mismatches. Lastly, the map component initially failed to display points due to issues with the latitude and longitude fields. This problem was solved by ensuring that the field names were correct and that they matched the dataset values before plotting.

Contact Information:

Sharif Ayesh
Sharif.ayesh@snhu.edu
