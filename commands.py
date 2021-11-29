from discord.ext import commands
from discord.ext.commands import Cog, Bot, command, Context

class SomeCommands(Cog): 
    """A couple of simple commands.""" 
    
    def __init__(self, bot: Bot): 
        self.bot = bot
        
    @command(name="ping")
    async def ping(self, ctx: Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong!")
        
    @command(name="stats")
    async def stats(self, ctx: Context):
        await ctx.send("Here are the stats.")
        
def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))