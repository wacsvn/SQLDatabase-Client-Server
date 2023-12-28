# Climate Data Retrieval and Storage

## Overview
This Python program is designed for retrieving, storing, and querying climate-related data, focusing on CO2 levels and sea level information. The data retrieval process involves web scraping using BeautifulSoup, extracting CO2 data from an HTML file, and processing sea level data from a CSV file. The collected data is then stored in SQLite databases, facilitating efficient querying. The program utilizes a client-server architecture with socket connections to enable users to query and retrieve climate data seamlessly.

## Prerequisites
Before starting, ensure that the `climate_data4-3.db` file is present in the project directory. This database file is crucial for storing and retrieving climate-related information.

## Instructions

1. **Data Retrieval:**
   - CO2 data is extracted from an HTML file (`Co2.html`) using web scraping techniques.
   - Sea level data is processed from a CSV file (`SeaLevel.csv`).

2. **Database Setup:**
   - The program employs SQLite databases (`climate_data.db`) to store CO2 and sea level data separately.

3. **Client-Server Interaction:**
   - The system utilizes a client-server architecture with socket connections.
   - Users can query the databases using SQL statements through the client-side script.

4. **Running the Program:**
   - Ensure the presence of `climate_data4-3.db` in the project directory.
   - Run the server script to establish a server instance.
   - Execute the client script to interact with the server and retrieve climate data.

**Note:** Make sure to review and comply with the program's dependencies and file requirements.

## Files
- **Query.py:** Contains the main logic for data retrieval, database operations, and the query builder.
- **Client.py:** Implements the client-side script for interacting with the server through socket connections.
- **Server.py:** Implements the server-side script, handling client connections and database queries.
- **Co2.html:** HTML file containing CO2 data for web scraping.
- **SeaLevel.csv:** CSV file containing sea level data for processing.
- **climate_data.db:** SQLite database storing CO2 and sea level data.

## Dependencies
- Python 3.x
- BeautifulSoup
- SQLite

## Usage
1. Run the server script (`Server.py`).
2. Execute the client script (`Client.py`) to query and retrieve climate data.
