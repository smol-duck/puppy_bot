import discord

from utilities.utilities import Utilities

from utilities.config.announcement_config import announcement_setup
from utilities.config.leavers_config import leavers_setup
from utilities.config.logs_config import logs_setup
from utilities.config.prefix_config import prefix_setup
from utilities.config.timezone_config import timezone_setup
from utilities.config.welcome_config import welcome_setup


async def bot_setup(ctx, bot):
    check = await prefix_setup(ctx, bot)
    pfx = Utilities.prefix()
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'{pfx}help for help | Made by Duckling#0007'))
    if check == False:
        return
    check = await timezone_setup(ctx, bot)
    if check == False:
        return
    check = await logs_setup(ctx, bot)
    if check == False:
        return
    check = await welcome_setup(ctx, bot)
    if check == False:
        return
    check = await leavers_setup(ctx, bot)
    if check == False:
        return
    check = await announcement_setup(ctx, bot)
    if check == False:
        return
    await ctx.send("Setup complete", delete_after=20)
