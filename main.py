import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix= ',',intents=intents)


@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")



initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        # Remove the '.py' extension and add to initial_extensions list
        initial_extensions.append("cogs." + filename[:-3])




if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

client.run('BOTTOKEN')
