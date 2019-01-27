# Victory Hockey League Discord Bot
# Developer: DilIsPickle

# libraries
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import os
import requests


# main
version = 1.0
client = Bot(
	command_prefix = '.',
	case_insensitive=True

	)
client.remove_command('help')
# events
@client.event
async def on_ready():
	print(f"""
+--------------------+
VHL Bot is now online.
Bot Version: {version}
Developer: DilIsPickle
+--------------------+
		""")
	return await client.change_presence(game=discord.Game(name='https://vhlportal.com/'))

# commands
@client.command()
async def help():
	embed = discord.Embed(
		title = "Victory Hockey League",
		url = "https://vhlportal.com/",
		description = """
		**Commands**
		-------------
		.help *shows this helpful message*
		.info *sends information about the bot*
		.portal *sends the VHL Portal link*
		.forums *sends the VHL Forum link*
		.index *sends the VHL Index link*
		.tpe *sends list of links where you can earn TPE*
		""",
		colour = discord.Colour.dark_red()
		)
	embed.set_footer(text='VHL Bot 2019')

	await client.say(embed=embed)
@client.command()
async def info():
	embed = discord.Embed(
		title = "VHL Bot | Information",
		colour = discord.Colour.dark_red()
		)
	embed.set_footer(text='VHL Bot 2019')
	embed.set_thumbnail(url="https://media.discordapp.net/attachments/346058650781089802/523687540843085835/image.png?width=559&height=559")
	embed.add_field(name='Name', value="VHL Bot", inline=False)
	embed.add_field(name='Command Prefix', value=" **.** ", inline=False)
	embed.add_field(name='Support Contact', value="DilIsPickle#3545 or support@pingpro.tk", inline=False)
	embed.add_field(name='Version', value=version, inline=False)

	await client.say(embed=embed)

@client.command()
async def portal():
	await client.say("Victory Hockey League Portal: https://vhlportal.com/")

@client.command()
async def forums():
	await client.say("Victory Hockey League Forums: https://vhlforum.com/")

@client.command()
async def index():
	await client.say("""
Victory Hockey League Minors Index: https://vhlportal.com/VHLM/64/
Victory Hockey League Index: https://vhlportal.com/VHL/64/"""
	)

@client.command()
async def tpe():
	embed = discord.Embed(
		title = "Victory Hockey League | TPE",
		description = """
		**TPE Links**
		**--------------**
		**Welfare & Pension:** http://bit.ly/WelfarePension *4+ Tpe*

		**Practice Facility:** http://bit.ly/PracticeFacility *1+ Tpe*

		**Media Spots:** http://bit.ly/MediaSpots *6 Tpe*

		**Graphics/Videos:** http://bit.ly/GraphicsVideos *6 Tpe*

		**Podcasts:** http://bit.ly/vhlpodcasts *6 Tpe*

		**Press Conferences:** http://bit.ly/PressConferences *2 Tpe*

		**Rookie Profile:** http://bit.ly/RookieProfile *8 Tpe*

		**Biography:** http://bit.ly/vhlbiography *10 Tpe*

		**First-Gen Bonus:** http://bit.ly/firstgenbonuns *10 Tpe*
		""",
		colour = discord.Colour.dark_red()
		)
	embed.set_footer(text='VHL Bot 2019')
	
	await client.say(embed=embed)


client.run(str(os.environ.get('BOT_TOKEN')))
