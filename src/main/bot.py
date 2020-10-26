# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# Prints out the result when the Client (representation of the connection to Discord) has connected to Discord.
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
