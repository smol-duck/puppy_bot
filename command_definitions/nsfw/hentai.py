import discord
import requests


async def hentai_member(self, ctx):
    response = requests.get(
        'https://anime-api.hisoka17.repl.co/img/nsfw/hentai')
    json_ = response.json()
    url = json_['url']
    em = discord.Embed(title="Weeb...", color=0xffd1dc)
    em.set_image(url=url)
    await ctx.send(embed=em)
