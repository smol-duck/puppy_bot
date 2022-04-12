import requests
import discord


async def cuddle_member(self, ctx, member):
    response = requests.get('https://anime-api.hisoka17.repl.co/img/cuddle')
    json_ = response.json()
    url = json_['url']
    if member != None:
        em = discord.Embed(
            title=f"{ctx.author.display_name} cuddled {member.display_name}!",
            color=0xffd1dc)
    elif member == None:
        em = discord.Embed(title="Cuddle time?", color=0xffd1dc)
    em.set_image(url=url)
    await ctx.send(embed=em)
