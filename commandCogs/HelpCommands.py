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
        
    @commands.command(help="get started with my functionality")
    async def helpme(self, ctx):
        await ctx.send("For a full list of my commands, {}, type `!commands`.".format(ctx.author.name))

    @commands.command()
    async def commands(self, ctx):
        commandList = ""
        for command in self.bot.commands:
            if (command.name != "commands"): commandList += "`{}{}` - {}\n".format(self.bot.command_prefix, command, command.help)
        await ctx.send("{}\n*more to come  :eyes:*".format(commandList))


def setup(bot):
    bot.add_cog(HelpCommands(bot))