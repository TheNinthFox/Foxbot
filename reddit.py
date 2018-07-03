from bs4 import BeautifulSoup
from discord.ext import commands
from urllib.error import HTTPError
from urllib.request import urlopen


@commands.command()
async def reddit(ctx, command='fetch', subreddit='Overwatch'):
    if command == 'fetch':
        fetch_subreddit_gif(ctx, subreddit)


async def fetch_subreddit_gif(ctx, subreddit):
    url = "https://www.reddit.com/r/{}/".format(subreddit)

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
