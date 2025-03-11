import os
import requests
import json


def categorize_event(title, description):
    print ("In categorize_event code")
    prompt = f"Categorize the following event: Title: {title}, Description: {description}"
    
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "mistral",
        "prompt": prompt
    }

    response = requests.post(url, json=data)
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")


    # Read the full response content
    full_response = ""
    for chunk in response.iter_lines():
        if chunk:
            print ("Chunk : ", chunk)
            chunk_data = json.loads(chunk.decode("utf-8"))  # Convert JSON string to dict
            full_response += chunk_data.get("response", "")
         
    print("Full Response: ",full_response.strip()) 

    if response.status_code == 200:
        return full_response.strip() if full_response else 'Uncategorized'
    else:
        return 'Uncategorized'