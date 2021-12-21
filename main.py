import randomstuff
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
with randomstuff.Client(api_key=API_KEY) as client:
  response = client.get_ai_response(input())
  print(response.message)