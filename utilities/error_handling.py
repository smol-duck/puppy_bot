import discord
import math
import sys
import traceback
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # if command has local error handler, return
        if hasattr(ctx.command, 'on_error'):
            return

        # get the original exception
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            command_name = (str(error)).split('"')
            em = discord.Embed(
                title="Uh oh! Command not found!",
                description=
                f'I cannot find a command named "{command_name[1]}". Please check your seplling or for more help use `>help`',
                colour=0xffd1dc)
            return await ctx.send(embed=em)

        if isinstance(error, commands.BotMissingPermissions):
            missing = [
                perm.replace('_', ' ').replace('guild', 'server').title()
                for perm in error.missing_perms
            ]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]),
                                          missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = 'I need the **{}** permission(s) to run this command.'.format(
                fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send('This command has been disabled.')
            return

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                "This command is on cooldown, please retry in {}s.".format(
                    math.ceil(error.retry_after)))
            return

        if isinstance(error, commands.MissingPermissions):
            missing = [
                perm.replace('_', ' ').replace('guild', 'server').title()
                for perm in error.missing_perms
            ]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]),
                                          missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = 'You need the **{}** permission(s) to use this command.'.format(
                fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"{error.param} is a required arguement in this command")
            await self.send_command_help(ctx.command)
            return

        if isinstance(error, commands.UserInputError):
            await ctx.send("Invalid input.")
            await self.send_command_help(ctx.command)
            return

        if isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(
                    'This command cannot be used in direct messages.')
            except discord.Forbidden:
                pass
            return

        if isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have permission to use this command.")
            return

        # ignore all other exception types, but print them to stderr
        print('Ignoring exception in command {}:'.format(ctx.command),
              file=sys.stderr)

        traceback.print_exception(type(error),
                                  error,
                                  error.__traceback__,
                                  file=sys.stderr)
