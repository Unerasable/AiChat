import randomstuff
import os
from dotenv import load_dotenv
os.system('pip install python-dotenv')
load_dotenv()

API_KEY = os.getenv('API_KEY')
while True:
  with randomstuff.Client(api_key=API_KEY) as client:
    response = client.get_ai_response(input())
    print(response.message)