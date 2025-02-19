#program with function to fetch data from NIHR Open Data Soft website for awards dataset
#load dependencies
import pandas as pd
import requests

# define function to make API call:
def fetch_json_from_api(url):
    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            return json_data
        else:
            print(f"Error: Unable to fetch data, Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Exception occurred: {e}")
        return None

# Example usage - check 
# if __name__ == "__main__":
#     api_url = "https://nihr.opendatasoft.com/api/explore/v2.1/catalog/datasets/nihr-infrastructure-supported-projects/exports/json"  # Replace with your API endpoint
#     data = fetch_json_from_api(api_url)
    
#     if data:
#         print("Fetched JSON data:")
#         #print(data)
#     else:
#         print("Failed to fetch JSON data.")

api_url = "https://nihr.opendatasoft.com/api/explore/v2.1/catalog/datasets/nihr-infrastructure-supported-projects/exports/json"  # Replace with your API endpoint
data = fetch_json_from_api(api_url)
df = pd.json_normalize(data)