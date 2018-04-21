import discord
from discord.ext.commands import bot
from discord.ext import commands
import doxdatabase
from os import environ

bot = commands.Bot(command_prefix=".")
print('Connecting')
bot.remove_command('help')

madeby = "Bot made by ICSharp#0546 and Ælix#5549"
colornigga = 0x00ffdd
debot = environ.get("BOT_TOKEN")

@bot.event
async def on_ready():
	print('ready ur ass')
	await bot.change_presence(game=discord.Game(name="100 Databases", url="https://www.twitch.tv/myname", type=1))

@bot.command(pass_context=True)
async def help(ctx):
	try:
		embed = discord.Embed(title="Dox bin commands  Prefix : `.`", description="Search : Searches a person in the database\n"
																				  "doxlist : Shows the list of doxed users", color=colornigga)
		embed.set_footer(text=madeby)
		await bot.say(embed=embed)
	except Exception as e:
		await bot.say(e)

@bot.command(aliases=['dox'], pass_context=True)
async def search(ctx, *, user: str = None):
	try:
		if user == None:
			embed = discord.Embed(title="Please provide a name for the person you're trying to search", color=colornigga)
			await bot.say(embed=embed)
		else:
			if user.upper() in doxdatabase.doxes:
				if user.upper().startswith('AMA'):
					embed = discord.Embed(title="Amateurz's dox results", color=colornigga)
					embed.add_field(name="Username", value="Ama, Amateurz")
					embed.add_field(name="Discord", value="ama#1337")
					embed.add_field(name="Visa Electron & Number", value="[Subcribe](https://discord.gg/BhZphCj)") #4716458381455325
					embed.add_field(name="Dad", value="Petri Kartunnen")
					embed.add_field(name="Mom", value="Hannele Kartunnen")
					embed.add_field(name="Name", value="Joni Kartunnen")
					embed.add_field(name="Address", value="Kellontie 17")
					embed.add_field(name="Birthday", value=" 11 / 9 / 2000")
					embed.set_footer(text="Doxed by Smecks")
					await bot.say(embed=embed)
				if user.upper().startswith('ALIX'):
					embed = discord.Embed(title="Who are you trying to search?", color=colornigga)
					embed.set_image(url="https://media.giphy.com/media/l2R0aIkYUXywiDMdO/giphy.gif")
					await bot.say(embed=embed)
				if user.upper().startswith('SHIELD'):
					embed = discord.Embed(title="Who are you trying to search?", color=colornigga)
					embed.set_image(url="https://media.giphy.com/media/DeBBINXN86r8Q/giphy.gif")
					await bot.say(embed=embed)
				if user.upper().startswith('ICSHARP'):
					embed = discord.Embed(title="ICSharp? Why are you trying to search for it", color=colornigga)
					embed.set_image(url="https://media.giphy.com/media/tJeGZumxDB01q/giphy.gif")
				if user.upper().startswith("SETH"):
					embed = discord.Embed(title="Seth's dox results", color=colornigga)
					embed.add_field(name="Names", value="@Seth, Seth, Seth A Robinson")
					embed.add_field(name="Address", value="6-17-5 Makuyama, Fukuyama Hiroshima 721-0913 JP ")
					embed.add_field(name="Phone", value="+81849482151")
					embed.add_field(name="GT Password", value="2B607D78393C4CF12B61DC2FE0FC84167") #2B607D78393C4CF12B61DC2FE0FC84167
					embed.add_field(name="Email", value="rtsoftjapan@gmail.com")
					embed.set_footer(text="Doxed by Alix")
					await bot.say(embed=embed)
				if user.upper().startswith("NADO"):
					embed = discord.Embed(title="Nadohack's dox results", color=colornigga)
					embed.add_field(name="Phone Number", value="+994 51 693 93 97")
					embed.add_field(name="IDD Code", value="+994")
					embed.add_field(name="Real Name", value="Isa Bozkurt")
					embed.add_field(name="IP", value="5.197.89.204")
					embed.add_field(name="Country", value="Azerbaijan")
					embed.add_field(name="Capital City", value="Bakue")
					embed.add_field(name="State", value="Baki")
					embed.add_field(name="GT Username", value="G0BLIN")
					embed.add_field(name="GT Email", value="wizard.hax55@gmail.com")
					embed.add_field(name="ISP", value="AG Telecom LTD.")
					embed.add_field(name="Time Zone", value="Asia")
					embed.add_field(name="Country Lat/Lon", value="40.5/47.5")
					embed.add_field(name="Continent Lat/Lon", value="29.8505/89.296")
					embed.add_field(name="Language", value="Azerbaijani")
					embed.add_field(name="City Lat/Lon", value="40.3953/49.8822")
					embed.add_field(name="Emails", value="savedata.stealer31@gmail.com\n"
														 "wizard.hax55@gmail.com")
					embed.add_field(name="Channel", value="Nadohack GT")
					embed.add_field(name="Skype", value="ghost.gamer69")
					embed.add_field(name="Facebooks", value="https://www.facebook.com/growtopia.pinjump.9\n"
															"https://www.facebook.com/profile.php?id=100013470661589")
					embed.set_footer(text="Doxed by Alix")
					await bot.say(embed=embed)

				if user.upper().startswith('HAXRIN'):
					embed = discord.Embed(title="Haxrin's dox results", color=colornigga)
					embed.add_field(name="Username", value="Haxrin, DarkNoobz, iHek")
					embed.add_field(name="Email", value="levhart289@gmail.com")
					embed.add_field(name="Discord", value="Haxrin#9299")
					embed.add_field(name="IP Address", value="84.42.161.126")
					embed.add_field(name="Discord ID", value="430596449365917708")
					embed.add_field(name="Channel", value="https://www.youtube.com/channel/UCiSC76ifuNxy0_1RGba_IcA")
					embed.add_field(name="Country", value="Czech Republic")
					embed.add_field(name="Continent", value="Europe(EU)")
					embed.add_field(name="Capital", value="Prague")
					embed.add_field(name="ISP", value="UPC Ceska Republica")
					embed.add_field(name="State", value="Hlavni mesto Praha")
					embed.add_field(name="Postal", value="130 00")
					embed.set_footer(text="Doxed by Alix and ICSharp")
					await bot.say(embed=embed)

				if user.upper().startswith('NOOBES'):
					embed = discord.Embed(title="Noobes GT's dox results", color=colornigga)
					embed.add_field(name="Facebook", value="https://www.facebook.com/people/Dani-Daniel/100006517634083\n"
						"https://www.facebook.com/Onlyvpn-421883254893691/?fref=pb&hc_location=profile_browser")
					embed.add_field(name="Real Name", value="Dani Daniel")
					embed.add_field(name="Home Town", value="Botosani")
					embed.add_field(name="Gender", value="Transgender")
					embed.add_field(name="School", value="Liceul cu Program Sportiv")
					embed.add_field(name="School Address", value="Strada Mihail Kogălniceanu str. M. Kogalniceanu nr. 29, Botoșani, Romania")
					embed.add_field(name="Channel", value="https://www.youtube.com/channel/UCfunMdsG4jgH6ZNJwhvuoSQ/videos")
					embed.add_field(name="Usernames", value="OnlyVPN, Noobes GT")
					embed.set_footer(text="Doxed by ICSharp")
					await bot.say(embed=embed)
				if user.upper().startswith('ONLY'):
					embed = discord.Embed(title="Noobes GT's dox results", color=colornigga)
					embed.add_field(name="Facebook", value="https://www.facebook.com/people/Dani-Daniel/100006517634083\n"
						"https://www.facebook.com/Onlyvpn-421883254893691/?fref=pb&hc_location=profile_browser")
					embed.add_field(name="Real Name", value="Dani Daniel")
					embed.add_field(name="Home Town", value="Botosani")
					embed.add_field(name="Gender", value="Transgender")
					embed.add_field(name="School", value="Liceul cu Program Sportiv")
					embed.add_field(name="School Address", value="Strada Mihail Kogălniceanu str. M. Kogalniceanu nr. 29, Botoșani, Romania")
					embed.add_field(name="Channel", value="https://www.youtube.com/channel/UCfunMdsG4jgH6ZNJwhvuoSQ/videos")
					embed.add_field(name="Usernames", value="OnlyVPN, Noobes GT")
					embed.set_footer(text="Doxed by ICSharp")
					await bot.say(embed=embed)
				if user.upper().startswith('ZTZ'):
					embed = discord.Embed(title="ZTzTopia's dox results (He wanted to be in the list)", color=colornigga)
					embed.add_field(name="Usernames", value="ZTzTopia")
					embed.add_field(name="IP", value="139.228.105.1")
					embed.add_field(name="Country", value="Indonesia")
					embed.add_field(name="Continent", value="Asia")
					embed.add_field(name="State", value="Jawa Barat")
					embed.add_field(name="City Location", value="Tangerang")
					embed.add_field(name="ISP", value="Fastnet")
					embed.add_field(name="Continent Lat/Lon", value="29.8405 / 89.296")
					embed.add_field(name="City Lat/Lon", value="(-6.1781) / (106.63)")
					embed.add_field(name="IDD Code", value="+62")
					embed.add_field(name="Discord", value="ZTzTopia®#2250")
					embed.add_field(name="Discord ID", value="436171327968116738")
					embed.add_field(name="Facebook", value="https://www.facebook.com/ZTzTopia")
					embed.add_field(name="Real Name", value="Muhamad Zibrisky")
					embed.add_field(name="School", value="SMA Negeri 4 Kendari")
					embed.add_field(name="Face", value="https://scontent.fmnl6-2.fna.fbcdn.net/v/t1.0-9/565058_1398551303707809_2082087174_n.jpg?_nc_cat=0&oh=8b94faa4861fd710c6b7226493552ece&oe=5B9CC448")
					embed.set_footer(text="Doxed by ICSharp")
					await bot.say(embed=embed)
			else:
				embed = discord.Embed(description="The user is not in the dox bin database", color=colornigga)
				await bot.say(embed=embed)
	except Exception as e:
		await bot.say(e)

@bot.command(pass_context=True)
async def doxlist(ctx):
	embed = discord.Embed(title="Available doxes, To get the results simply search them using the search command", description="Amateurz\n"
		"Haxrin\n"
		"Seth\n"
		"NadoHack\n"
		"OnlyVPN or Noobes GT\n"
		"ZTzTopia\n", color=colornigga)
	await bot.say(embed=embed)

bot.run(debot)
