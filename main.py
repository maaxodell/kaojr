# Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load token
load_dotenv()
token = os.getenv("TOKEN")

# Initialise bot client
client = discord.Client()

client.run(token)

test = 'test'