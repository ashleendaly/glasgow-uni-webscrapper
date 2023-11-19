
import requests 
import json
import os
from dotenv import load_dotenv
load_dotenv()
      
url = 'https://api.aiseo.ai/v2/rewrite'
headers = {
    'Authorization': 'Bearer ' + os.getenv('AISEO_API_KEY'),
    'Content-Type': 'application/json'
}

with open('out.txt', 'r') as f:
    text = f.read()

data = { 
    'text': text, 
    'audience': 'general',
    'formality': 'neutral',
    'intent': 'inform' 
}
response = requests.post(url, headers=headers, data=json.dumps(data))
    
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.text)