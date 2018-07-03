import os
import discord
import random
from discord.ext import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

bot = commands.Bot(command_prefix='!', description='Foxhole Foxbot Butler')


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.event
async def on_message(message: discord.Message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    if "beeindruck" in message.content:
        await message.channel.send("Bark bork! Sehr beeindruckend!")

    if "recht" in message.content and "rechts" not in message.content:
        await message.channel.send("Bark bork! Recht hat er!")

    if "alive" in message.content:
        await message.channel.send("Bark bork! I'm alive!")

    command_list = ['$help', '$info']

    if isinstance(message.channel, discord.DMChannel) and message.content not in command_list:
        await message.author.send("Bark bork! Du erfährst mehr über mich mit $help und $info!")


@bot.command()
async def greet(ctx):
    await ctx.send("Bark bork!")


@bot.command()
async def roll(ctx, query: str, additionals=''):
    if len(query) > 8:
        await ctx.send('Bark bork! Zu gross!')
        return

    result = 0
    addition = 0
    subtraction = 0
    if '+' in additionals:
        addition = int(additionals[1:])
    if '-' in additionals:
        subtraction = int(additionals[1:])

    try:
        result = process_query(query) + addition - subtraction
    except:
        await ctx.send('Bark bork! Falsches Format! Versuch mal XdY!')
        return

    await ctx.send(result)


def process_query(query):
    addition = 0
    subtraction = 0
    if '+' in query:
        dice_info, addition = query.split('+')
    elif '-' in query:
        dice_info, subtraction = query.split('-')
    else:
        dice_info = query

    result = 0
    dice_amount, dice_upper_limit = dice_info.split('d')
    for i in range(int(dice_amount)):
        result += random.randint(1, int(dice_upper_limit))

    result = result + int(addition) - int(subtraction)
    return result


@bot.command()
async def overwatch(ctx):
    url = "https://www.reddit.com/r/Overwatch/"

    try:
        page = urlopen(url)
    except HTTPError:
        await ctx.send("Bark bork! Reddit is busy!")

    soup = BeautifulSoup(page, 'lxml')

    site_table = soup.find('div', {'id': 'siteTable'})
    divs = site_table.findChildren(['div'])

    gif = None
    for div in divs:
        try:
            val = div.attrs['data-url']
            if "gfycat.com" in val:
                gif = val
                break
        except KeyError:
            pass

    if gif:
        await ctx.send(gif)
    else:
        await ctx.send("Bark bork! No gif found!")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="FoxBot", description="Nicest fox there is, ever.", color=0xeee657)
    embed.add_field(name="Author", value="Fox")
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite",
                    value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=420315380079263744&permissions=0&scope=bot)")

    await ctx.send(embed=embed)


bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="FoxBot", description="A very nice fox. List of commands are:", color=0xeee657)

    embed.add_field(name="!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!overwatch", value="Fetches a gif from /r/Overwatch", inline=False)
    embed.add_field(name="!roll", value="Rolls XdY dice.", inline=False)
    embed.add_field(name="!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


def get_secret_key():
    path = os.path.expanduser('~/.foxbot.env')
    with open(path) as f:
        secret_key = f.readline()

    return secret_key


if __name__ == '__main__':
    bot.run(get_secret_key())
