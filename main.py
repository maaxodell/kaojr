# Module imports
from dotenv import load_dotenv
import os, sys

# Personal imports
from bot import client

# Development variable
sys.dont_write_bytecode = True

# Load application token
load_dotenv()
token = os.getenv("TOKEN")

# Connect to server
client.run(token)