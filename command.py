import discord

def handler(command):
    commandContent = command.content[1:]
    response = ""

    if commandContent.startswith("test"):
        response = "tested"
    else:
        response = "Not yet supported."
    
    return response