import discord
import datetime
import contextlib

from discord.ext import commands
from utilities.utilities import Utilities


class HelpEmbed(
        discord.Embed
):  # Our embed with some preset attributes to avoid setting it multiple times
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timestamp = datetime.datetime.now(Utilities.timezone())
        text = "Use help [command] or help [section] for more information | <> is required | [] is optional"
        self.set_footer(text=text)
        self.color = 0xffd1dc


class HelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__(
            command_attrs={
                'help': 'Shows help about the bot, a command, or a section',
                'cooldown': commands.Cooldown(1, 3.0,
                                              commands.BucketType.member)
            })

    async def send(self, **kwargs):
        """Shortcut for get_destination"""
        await self.get_destination().send(**kwargs)

    async def send_help_embed(
            self, title, description,
            commands):  # a helper function to add commands to an embed
        embed = HelpEmbed(title=title,
                          description=description or "No help found...")

        if filtered_commands := await self.filter_commands(commands):
            for command in filtered_commands:
                embed.add_field(name=self.get_command_signature(command),
                                value=command.help or "No help found...",
                                inline=False)

        await self.send(embed=embed)

    async def send_bot_help(self, mapping):
        """Called when {prefix}help with no arguement is called"""
        ctx = self.context
        embed = HelpEmbed(title="Help")
        embed.set_thumbnail(url=ctx.me.avatar_url)
        usable = 0

        for cog, commands in mapping.items(
        ):  #iterating through our mapping of cog: commands
            if filtered_commands := await self.filter_commands(commands):
                # if no commands are usable in this category, we don't want to display it
                amount_commands = len(filtered_commands)
                usable += amount_commands
                if cog:  # getting attributes dependent on if a cog exists or not
                    name = cog.qualified_name
                    description = cog.description or "No description"

                    embed.add_field(
                        name=f"{name} Section",
                        value=description,
                        inline=False)

        embed.description = f"{len(ctx.bot.commands)} commands | {usable} usable"

        await self.send(embed=embed)

    async def send_cog_help(self, cog):
        title = cog.qualified_name or "No"
        await self.send_help_embed(f'{title}', cog.description,
                                   cog.get_commands())

    async def send_group_help(self, group):
        title = self.get_command_signature(group)
        await self.send_help_embed(title, group.help, group.commands)

    async def send_command_help(self, command):
        signature = self.get_command_signature(
            command
        )  # get_command_signature gets the signature of a command in <required> [optional]
        embed = HelpEmbed(title=signature,
                          description=command.help or "No help found...")

        if cog := command.cog:
            embed.add_field(name="Section", value=cog.qualified_name)

        can_run = "No"
        # command.can_run to test if the cog is usable
        with contextlib.suppress(commands.CommandError):
            if await command.can_run(self.context):
                can_run = "Yes"

        embed.add_field(name="Usable", value=can_run)

        if command._buckets and (
                cooldown := command._buckets._cooldown
        ):  # use of internals to get the cooldown of the command
            embed.add_field(
                name="Cooldown",
                value=f"{cooldown.rate} per {cooldown.per:.0f} seconds")

        await self.send(embed=embed)
