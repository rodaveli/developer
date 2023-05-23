# Revised Political Campaign CRM Program Specification

## Overview
The purpose of this CRM system is to efficiently manage and track voters, their intentions, referrals, and requests for a political campaign. The back end of this system will be implemented in Python using the SQLite3 database, while the front end will use the Tailwind CSS framework. The system will include an authentication system and will be designed for cloud deployment.

## Functional Requirements

### Voters

1. **Add/Remove/Update Voters:** The system should allow CRUD (Create, Read, Update, Delete) operations on voter records. Each voter record will include the following fields:
    - Voter ID (auto-generated)
    - Full Name
    - Date of Birth
    - Phone Number
    - Email
    - Instagram
    - Facebook
    - Key Issues (one or more from list: Healthcare, Public Safety, Transportation, Education, Corruption, Jobs, Economy)
    - Data Consent (Yes/No)
    - Address
    - Location (geographic coordinates for map view)
    - Referral (the person who referred this voter, if any)
    - Vote Intent (Yes, No, Maybe)

2. **Track Referrals:** The system should allow tracking who referred which voters. This can be done by linking the referrer to the referred voter(s) in the database.

3. **Voter List View:** The system should provide a list view where users can see all voters and their details. This list should support sorting and filtering options.

### Voter Requests

4. **Add/Remove/Update Voter Requests:** The system should allow CRUD operations on voter requests. Each voter request will include the following fields:
    - Request ID (auto-generated)
    - Name
    - Description
    - Associated Voter (linked via Voter ID)
    - Date Submitted
    - Location
    - Status (Not Started, In Progress, Completed_Success, Completed_Failure)

5. **Request List and Kanban View:** Users should be able to see voter requests in a list view as well as in a kanban or pipeline view, sorted by status.

### Map View

6. **Map View of Voters:** The system should provide a map view where users can see all voters as points on the map. Users should be able to input a location and a radius and view all voters within that radius. This view should support filtering based on voter attributes.

Map View should utilize the Google Maps API, with the following credentials:

Google Geocode API key: AIzaSyDM5zZdZCOfguxHyDESvEhzxVJIOeqmGto
Google Map API Key: AIzaSyDM5zZdZCOfguxHyDESvEhzxVJIOeqmGto
<!---
### Authentication System

7. **User Login and Authentication:** The system should have a secure login and authentication system for users.
-->
## Non-Functional Requirements

1. **Performance:** The system should be able to handle a large number of voters and requests, with quick response times for database queries.

2. **Usability:** The interface should be user-friendly, making it easy for users to navigate through different views and perform actions.

3. **Scalability:** The system should be scalable to support the addition of new voters and requests.

4. **Cloud Deployment:**  The system should be designed for cloud deployment, allowing it to be easily set up and run on a cloud platform. Preferrably Digital Ocean.

## Technology Stack

- Back-end: Python, SQLite3
- Front-end: HTML, CSS (Tailwind), JavaScript (for interactive elements)

## Debugging

The file main.py is missing several imports. Go over the imported modules and functions and check that they have been created and written. 

Also, for each of the following files:

1. `main.py`:
- Check if all the necessary modules are imported correctly.
- Check if the function calls are correct and the arguments are passed in the correct order.
- Check if there are any syntax errors or logical errors in the code.

2. `utils.py`:
- Check if the function definitions are correct and the arguments are named correctly.
- Check if there are any syntax errors or logical errors in the code.

3. `data.txt`:
- Check if the data is formatted correctly and there are no missing or extra values.
- Check if the data is being read correctly in the `main.py` file.

4. `output.txt`:
- Check if the file is being created and written to correctly in the `main.py` file.
- Check if the output is formatted correctly and there are no missing or extra values.