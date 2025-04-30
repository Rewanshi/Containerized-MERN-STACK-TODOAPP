# # import requests
# # import time


# # api_url = "http://localhost:5000/tasks"  
# # headers = {
    
# #     "text":"gifts"
# # }

# # # Function to make a single API call
# # def make_api_call():
# #     try:
# #         response = requests.get(api_url, headers=headers)
# #         response.raise_for_status()  
# #         return response.json()  
# #     except requests.exceptions.RequestException as e:
# #         print(f"An error occurred: {e}")
# #         return None

# # # Loop to make 10,000 API calls
# # for i in range(10000):
# #     result = make_api_call()
# #     if result:
# #         print(f"Call {i+1}: Success")
# #     else:
# #         print(f"Call {i+1}: Failed")

    
# #     time.sleep(1)

# # print("Completed 10,000 API calls.")

# import requests
# import time

# # Define the API endpoint
# api_url = "http://localhost:5000/tasks"  # Ensure this is the correct endpoint

# # JSON payload to send with the POST request
# payload = {
#     "text": "gifts"  # Replace with the actual data your API expects
# }

# # Function to make a single API call
# def make_api_call():
#     try:
#         # Send a POST request with JSON payload
#         response = requests.post(api_url, json=payload)
#         response.raise_for_status()  # Raise an error for bad responses
#         return response.json()  # Expect JSON response
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         return None

# # Loop to make 10,000 API calls
# for i in range(10000):
#     result = make_api_call()
#     if result:
#         print(f"Call {i+1}: Success - {result}")
#     else:
#         print(f"Call {i+1}: Failed")

#     # Optional: Sleep to avoid overwhelming the server (e.g., 1 second)
#     #time.sleep(1)

# print("Completed 10,000 API calls.")

import requests
import random
import string
import time

# Define the API endpoint
api_url = "http://localhost:5000/tasks"  # Ensure this is the correct endpoint

# Function to generate a random string of fixed length
def generate_random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Function to make a single API call with a random entry in the payload
def make_api_call(entry):
    try:
        # JSON payload to send with the POST request
        payload = {"text": entry}

        # Send a POST request with JSON payload
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Expect JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Loop to make 10,000 API calls with random entries
for i in range(10000):
    random_entry = generate_random_string()  # Generate a random string entry
    result = make_api_call(random_entry)  # Make the API call with the random entry

    if result:
        print(f"Call {i+1}: Success - {result}")
    else:
        print(f"Call {i+1}: Failed")

    # Optional: Sleep to avoid overwhelming the server (e.g., 0.1 second)
    # time.sleep(0.1)

print("Completed 10,000 API calls.")

