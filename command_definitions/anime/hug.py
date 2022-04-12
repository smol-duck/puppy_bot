import discord
import requests


async def hug_member(self, ctx, member):
    response = requests.get('https://anime-api.hisoka17.repl.co/img/hug')
    json_ = response.json()
    url = json_['url']
    if member != None:
        em = discord.Embed(
            title=
            f"{ctx.author.display_name} hugged {member.display_name}! UwU",
            color=0xffd1dc)
    else:
        em = discord.Embed(title=f"Need a hug?", color=0xffd1dc)
    em.set_image(url=url)
    await ctx.send(embed=em)
