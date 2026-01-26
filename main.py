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

# After this please create your own discord bot and own discord server to test!
# This part should be simple and the video will help you create your own bot.
# You'll need to create a file ".env"
# Inside .env you'll need to put DISCORD-TOKEN=
# comment out the hosting token and uncomment the two localhost token variables

###
# When you are done and ready to submit for review, Please comment out the local host and uncomment the hosting
###

#Localhost Token: loads and sets environment discord token for localhosting
#load_dotenv()
#token = os.getenv("DISCORD-TOKEN")

#Hosting Token: loads and sets environment discord token for render hosting
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
