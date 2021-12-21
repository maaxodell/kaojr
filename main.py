# Imports
import discord
from dotenv import load_dotenv
import os

# Environment variables
load_dotenv()
token = os.getenv("TOKEN")

client = discord.Client()

client.run(token)