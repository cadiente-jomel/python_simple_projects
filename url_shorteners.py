import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = str(os.getenv('API_KEY'))

url = input()

api_url = f"https://cutt.ly/api/api.php?key={API_KEY}&short={url}"

data = requests.get(api_url).json()['url']

if data['status'] == 7:
    shortened_linked = data['shortLink']
    print(f'Shorted Link: {shortened_linked}')
else:
    print('[!] Error Occured unabled to shortend link')
