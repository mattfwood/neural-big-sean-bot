import os
import json
import random
from dotenv import load_dotenv
from twython import Twython

# env_path = '.env'
# load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

json_data = open('./output_big_sean.json').read()
data = json.loads(json_data)

random_line = random.choice(data)
print(random_line)

twitter_client = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_client.update_status(status=random_line)
