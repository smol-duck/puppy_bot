import discord


async def toggle(self, ctx, command):
    command = self.bot.get_command(command)
    try:
        command_name = str(command.qualified_name)
    except:
        pass

    banned_list = ['Shutdown', 'Setup', 'Test', 'Toggle', 'help', 'Bot']

    if command is None:
        em = discord.Embed(
            title="ERROR",
            description="I can't find a command with that name!",
            color=0xffd1dc)
        return await ctx.send(embed=em)

    elif ctx.command == command:
        em = discord.Embed(title="ERROR",
                           description="You cannot disable this command.",
                           color=0xffd1dc)
        return await ctx.send(embed=em)

    elif command_name in banned_list:
        em = discord.Embed(title="ERROR",
                           description="You cannot disable this command.",
                           color=0xffd1dc)
        return await ctx.send(embed=em)

    else:
        command.enabled = not command.enabled
        ternary = "enabled" if command.enabled else "disabled"
        em = discord.Embed(
            title="Toggle",
            description=f"I have {ternary} {command.qualified_name} for you!",
            color=0xffd1dc)

        command_file = open('utilities/disabled_commands.txt', 'r')
        command_lines = command_file.read()
        command_list = command_lines.split('\n')

        if ternary == "disabled":
            if command_name in command_list:
                pass
            else:
                command_list.append(command_name)

        elif ternary == "enabled":
            if command_name in command_list:
                command_list.remove(command_name)
            else:
                pass

        with open('utilities/disabled_commands.txt', 'w') as f:
            command_lines = "\n".join(command_list)
            f.write(command_lines)

        await ctx.send(embed=em)
