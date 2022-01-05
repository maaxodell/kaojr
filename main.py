# Imports
from dotenv import load_dotenv
import os, sys
test = 2

from bot import client

sys.dont_write_bytecode = True

# Load token
load_dotenv()
token = os.getenv("TOKEN")

# Connect to server
client.run(token)