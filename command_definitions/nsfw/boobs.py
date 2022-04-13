import discord
import requests


async def boobs_member(self, ctx):
    response = requests.get(
        'https://anime-api.hisoka17.repl.co/img/nsfw/boobs')
    json_ = response.json()
    url = json_['url']
    em = discord.Embed(title="Mommy milkers!", color=0xffd1dc)
    em.set_image(url=url)
    await ctx.send(embed=em)
