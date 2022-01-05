from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Connected")
    await client.get_channel(770480715279761414).send("Congrats baby")

client.load_extension('commandCogs.HelpCommands')