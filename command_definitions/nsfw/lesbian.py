import requests
import discord


async def lesbian_member(self, ctx):
    response = requests.get(
        'https://anime-api.hisoka17.repl.co/img/nsfw/lesbian')
    json_ = response.json()
    url = json_['url']

    em = discord.Embed(title="UwU", color=0xffd1dc)
    em.set_image(url=url)

    await ctx.send(embed=em)
