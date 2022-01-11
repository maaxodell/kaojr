# Module imports
from discord.ext import commands
import discord
from datetime import datetime
import pytz

# Personal imports
from resources import devChannelID

# Create bot object and its listening status 
activity = discord.Activity(type=discord.ActivityType.listening, name="!helpme")
client = commands.Bot(command_prefix="!", activity=activity, help_command=None)

# Send 'connected' message to development channel 
@client.event
async def on_ready():
    # Get current local time of connection
    tz = pytz.timezone('Australia/Queensland')
    time = datetime.now(tz).strftime("%I:%M:%S %p")

    await client.get_channel(devChannelID).send("`Connected at {}`".format(time))

# Load bot command cogs
client.load_extension('commandCogs.HelpCommands')
client.load_extension('commandCogs.StatsCommands')
client.load_extension('music.MusicCommands')