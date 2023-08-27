import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, I am role-bot, thanks for adding")

    
    # Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(1144693904176844812)
        await channel.send("Welcome to the Server")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(1144693904176844812)
        await channel.send("Goodbye")

def setup(client):
    client.add_cog(Greetings(client))
