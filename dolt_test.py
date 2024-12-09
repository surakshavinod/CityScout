import requests
import json
import csv
import urllib.parse

# # DoltHub API endpoint
# # Replace {org} and {repo} with your organization name and repository name
# api_url = "https://www.dolthub.com/api/v1alpha1/Liquidata/fbi-nibrs/branches/main/sql"

# Conversion from string method:
def query(base_url, sql_query):
    """
    Converts a SQL query string into a URL-encoded API URL for DoltHub.
    
    Args:
        base_url (str): The base API URL, e.g., "https://www.dolthub.com/api/v1alpha1/dolthub/fbi-nibrs/main?q="
        sql_query (str): The SQL query string to convert.
    
    Returns:
        str: The complete API URL with the SQL query encoded.
    """
    # URL encode the SQL query
    encoded_query = urllib.parse.quote(sql_query)

    # Construct the full API URL by appending the encoded query to the base URL
    api_url = f"{base_url}{encoded_query}"
    
    return api_url

# DON'T CHANGE BASE_URL
base_url = "https://www.dolthub.com/api/v1alpha1/dolthub/fbi-nibrs/main?q=" # Don't change
# Don't change above url

for offense_type_id in range(1, 5): # Eventually we'll want this loop to go through all the offense_type_id values
    # Format SQL query with the current OFFENSE_TYPE_ID
    sql_query = f"""SELECT nibrs_victim_offense.VICTIM_ID, nibrs_offense.OFFENSE_ID, nibrs_offense_type.OFFENSE_TYPE_ID, 
                    `OFFENSE_NAME`, `age_num`, nibrs_victim.incident_id, nibrs_incident.agency_id, 
                    cde_agencies.city_name, cde_agencies.state_abbr, cde_agencies.state_id
                FROM `nibrs_victim_offense` JOIN `nibrs_offense` JOIN `nibrs_offense_type` JOIN `nibrs_victim` JOIN 
                `nibrs_incident` JOIN `cde_agencies`
                WHERE nibrs_offense_type.OFFENSE_TYPE_ID = {offense_type_id}
                LIMIT 3000""" # Currently it seems it can only take 1000 rows, otherwise it outputs row limit in the header of the json file

    # Use query() method to create the API URL
    new_api_url = query(base_url, sql_query)

    # Print the API URL for verification
    # print("NEW API URL:", new_api_url)

    # Make the API request
    new_response = requests.get(new_api_url)
    if new_response.status_code == 200:
        # Parse and write the JSON response to a file
        data = new_response.json()
        # print(json.dumps(data, indent=4))
        json_filename = f"crime_{offense_type_id}.json"
        with open(json_filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data for OFFENSE_TYPE_ID {offense_type_id} written to {json_filename}")
    else:
        # Print error if the request fails
        print(f"Error: {new_response.status_code}, {new_response.text}")






# OLD Queries

# states_query = """SELECT *
#                 FROM `cde_agencies`
#                 WHERE state_id + 0 = 20
#                 LIMIT 100;
#                 """

# old_sql_query = "SELECT * FROM `agency_participation` WHERE `STATE_ID` = 40 ORDER BY `DATA_YEAR` ASC, `AGENCY_PARTICIPATION_ID` DESC LIMIT 10;"


# old_sql_query = """SELECT nibrs_victim_offense.VICTIM_ID, 
#        nibrs_offense.OFFENSE_ID, 
#        filtered_offense_type.OFFENSE_TYPE_ID, 
#        filtered_offense_type.OFFENSE_NAME, 
#        age_num, 
#        nibrs_victim.incident_id, 
#        nibrs_incident.agency_id, 
#        cde_agencies.city_name, 
#        cde_agencies.state_abbr, 
#        cde_agencies.state_id
# FROM `nibrs_victim_offense`
# JOIN `nibrs_offense` ON nibrs_offense.OFFENSE_ID = nibrs_victim_offense.OFFENSE_ID
# JOIN (
#     SELECT OFFENSE_TYPE_ID, OFFENSE_NAME
#     FROM `nibrs_offense_type`
#     WHERE OFFENSE_TYPE_ID = 1
# ) AS filtered_offense_type ON filtered_offense_type.OFFENSE_TYPE_ID = nibrs_offense.OFFENSE_TYPE_ID
# JOIN `nibrs_victim` ON nibrs_victim.VICTIM_ID = nibrs_victim_offense.VICTIM_ID
# JOIN `nibrs_incident` ON nibrs_incident.incident_id = nibrs_victim.incident_id
# JOIN `cde_agencies` ON cde_agencies.agency_id = nibrs_incident.agency_id
# LIMIT 100;"""

# sql_query = """SELECT nibrs_victim_offense.VICTIM_ID, nibrs_offense.OFFENSE_ID, nibrs_offense_type.OFFENSE_TYPE_ID, `OFFENSE_NAME`, `age_num`, nibrs_victim.incident_id, nibrs_incident.agency_id, cde_agencies.city_name, cde_agencies.state_abbr, cde_agencies.state_id
#                 FROM `nibrs_victim_offense` JOIN `nibrs_offense` JOIN `nibrs_offense_type` JOIN `nibrs_victim` JOIN   `nibrs_incident` JOIN `cde_agencies`
#                 WHERE nibrs_offense_type.OFFENSE_TYPE_ID = 12
#                 LIMIT 100"""

# # Convert the SQL query to a URL
# new_api_url = query(base_url, sql_query) 

# # Output the API
# print("NEW API URL:", new_api_url)

# new_response = response = requests.get(new_api_url)
# if new_response.status_code == 200:
#     # Parse the JSON response
#     data = new_response.json() 

#     # Output the data
#     print(json.dumps(data, indent=4)) # Output prints to console
# else:
#     # If there was an error, print the error code and message
#     print(f"Error: {new_response.status_code}, {new_response.text}")

