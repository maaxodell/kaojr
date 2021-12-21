# Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from command import handler

# Load token
load_dotenv()
token = os.getenv("TOKEN")

class KaoJrClient(discord.Client):
    async def on_ready(self):
        print('Connected')

    async def on_message(self, message):
        if message.content.startswith("."):
            response = handler(message)
            await message.channel.send(response)
            return
        
# Initialise bot client
client = KaoJrClient()
client.run(token)