from dotenv import load_dotenv
import os


load_dotenv('.env')

API_KEY = os.environ['API_KEY']
TIMEOUT = int(os.environ.get('TIMEOUT', 1))



