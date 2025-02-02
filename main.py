import time
import requests

def add_memory(content: str) -> dict:
    """
    Add a memory to the system.
    
    Args:
        content (str): The content to add as a memory
        
    Returns:
        dict: The response from the API parsed as JSON
    """
    url = "http://localhost:3000/api/v1/memories/add"
    
    payload = {"content": content}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer (Your 'token' cookie)"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

user_info = [
    "User's name is John Smith",
]

for info in user_info:
    print(add_memory(info))
    time.sleep(0.4)
