from discord.ext import commands
from messageLogger import log

devChannelID = "770480715279761414"

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if (ctx.author.id != self.bot.user.id) & (str(ctx.channel.id) == devChannelID):
            log(ctx.author.name, ctx.content)
        
    @commands.command()
    async def helpme(self, ctx):
        await ctx.send("Help is on it's way, " + ctx.author.name)

def setup(bot):
    bot.add_cog(HelpCommands(bot))