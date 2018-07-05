import os
import discord
from discord.ext import commands


@commands.command()
async def info(ctx):
    embed = discord.Embed(title="FoxBot", description="Nicest fox there is, ever.", color=0xeee657)
    embed.add_field(name="Author", value="Fox")
    embed.add_field(name="Invite",
                    value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=420315380079263744&permissions=0&scope=bot)")

    await ctx.send(embed=embed)


@commands.command()
async def help(ctx):
    embed = discord.Embed(title="FoxBot", description="A very nice fox. List of commands are:", color=0xeee657)

    embed.add_field(name="!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!overwatch", value="Fetches a gif from /r/Overwatch", inline=False)
    embed.add_field(name="!roll", value="Rolls XdY dice.", inline=False)
    embed.add_field(name="!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


@commands.command()
async def greet(ctx):
    await ctx.send("Bark bork!")


def get_secret_key():
    foxbot_dir = os.path.expanduser('~/.foxbot')
    if not os.path.exists(foxbot_dir):
        os.makedirs(foxbot_dir)

    secret_key_file_name = '.env'
    full_path = '/'.join((foxbot_dir, secret_key_file_name))
    with open(full_path) as f:
        secret_key = f.readline()

    return secret_key.strip()
