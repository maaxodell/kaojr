from asyncio import queues
import discord, youtube_dl, json
from discord.ext import commands
from resources import musicChannelID
from datetime import timedelta
from youtube_search import YoutubeSearch

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    songMessage = None
    pauseReaction = "\u23F8"

    queue = {}

    def checkQueue(self, ctx, id):
        if self.queue[id] !={}:
            voice = ctx.guild.voice_client
            source = self.queue[id].pop(0)
            voice.play(source, after=lambda x=0: self.checkQueue(ctx, ctx.message.guild.id))

    @commands.command(help="")
    async def play(self, ctx, *, songName=None):
        with ctx.channel.typing():
            if not await self.checkMessage(ctx):
                return
            
            # Check for different voice channel
            if ctx.voice_client is None or not ctx.author.voice.channel == ctx.voice_client.channel:
                await ctx.reply("Looks like we're not in the same voice channel - use `{}join`.".format(self.bot.command_prefix))
                return

            # Check for missing song name
            if songName is None:
                await ctx.reply("Missing song name!")
                return

            # Delete original command message
            await ctx.message.delete()

            # Find song on youtube
            yt = YoutubeSearch(songName, max_results = 1).to_json()
            ytid = str(json.loads(yt)['videos'][0]['id'])
            url = "https://www.youtube.com/watch?v={}".format(ytid)

            # Set options for external libraries
            FFMOPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format': 'bestaudio'}
            vc = ctx.voice_client

            # Download and play audio
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                title = info.get('title', None)
                duration = str(timedelta(seconds=info.get('duration', None))) 
                source = await discord.FFmpegOpusAudio.from_probe(url2,
                **FFMOPTIONS)
                
            if vc.is_playing():
                guild_id = ctx.message.guild.id
                if guild_id in self.queue:
                    self.queue[guild_id].append(source)
                else:
                    self.queue[guild_id] = [source]
            else:
                vc.play(source, after=lambda x=0: self.checkQueue(ctx, ctx.message.guild.id))
        
        # Send message about song
        self.songMessage = await ctx.send(":loud_sound: `{} [{}]` - {}".format(title, duration, ctx.author.name))

    @commands.command(help="")
    async def pause(self, ctx):
        if not await self.checkMessage(ctx):
            return

        ctx.voice_client.pause()
        await self.songMessage.add_reaction(self.pauseReaction)

    @commands.command(help="")
    async def resume(self, ctx):
        if not await self.checkMessage(ctx):
            return
            
        ctx.voice_client.resume()
        await self.songMessage.clear_reaction(self.pauseReaction)

    async def checkMessage(self, ctx):
        # Check if user in a voice channel to join
        if ctx.author.voice is None:
            await ctx.reply("It doesn't look like you're in a voice channel!")
            return False

        # Check for music channel
        # if not ctx.channel.id == musicChannelID:
        #     await ctx.reply("Please use {} for music commands.".format(self.bot.get_channel(musicChannelID).mention))
        #     return False

        return True

    @commands.command(help="")
    async def join(self, ctx):
        if not await self.checkMessage(ctx):
            return

        vc = ctx.author.voice.channel
        if ctx.voice_client is None:
            await vc.connect()
        else:
            await ctx.voice_client.move_to(vc)

    @commands.command(aliases=['dc', 'leave'], help="")
    async def disconnect(self, ctx):
        if not await self.checkMessage(ctx):
            return

        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(MusicCommands(bot))