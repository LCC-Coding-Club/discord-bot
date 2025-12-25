import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import webserver

# documentation reference: https://discordpy.readthedocs.io/en/stable/
# Video used to set up bot: https://www.youtube.com/watch?v=YD_N6Ffoojw
# You might have to look up some things on your own. Google is a valuable resource.


### Your setup ###
# Install python: https://www.python.org/downloads/
# download the github repo https://github.com/LCC-Coding-Club/discord-bot
# run pip install -r .\requirements.txt
# your IDE might require additional setup to run the bot. Try to use google first. If you still cant figure it out, ask for help on discord.

# if you need to test something get the .env file from a club officer.
# Do NOT share the .env file with anyone outside of club officers.

# if you have the .env file, be careful when you run the bot.
# If the bot is running in the server DO NOT RUN ANOTHER INSTANCE. 
# Only one instance of the bot can run at a time.
# it is reccomended to test with your own separate test bot.


#loads and sets environment discord token for localhosting
#load_dotenv()
#token = os.getenv("DISCORD-TOKEN")

#loads and sets environment discord token for render hosting
token = os.environ['DISCORD-TOKEN']

#sets up logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

#sets up bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#creates bot instance
bot = commands.Bot(command_prefix='>', intents=intents)

#logs a message when bot starts up, we can possibly use this for other things later
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

#simple hello command
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

# for hosting the bot online 24/7
webserver.keep_alive()

#log_levels: NOTSET(0), DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)
#We cant use logging.debug for reasons
bot.run(token,log_handler=handler,log_level=10)