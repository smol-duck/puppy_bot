from utilities.utilities import Utilities


async def display_prefix(self, ctx):
    pfx = Utilities.prefix()
    if ctx.guild != None:
        await ctx.send(f"My prefix in this server is: {pfx}")
    else:
        await ctx.send(f"My default prefix is {pfx}")
