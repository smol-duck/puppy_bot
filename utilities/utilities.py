import json

from pytz import timezone


class Utilities:
    def channel(channel):
        with open('utilities/settings.json', 'r') as f:
            settings = json.load(f)
        channel_id = settings[channel]
        return channel_id

    def prefix():
        with open('utilities/settings.json', 'r') as f:
            settings = json.load(f)
        pfx = settings['prefix']
        return pfx

    def roles(member):
        role_list = [
            role.mention for role in member.roles
            if role != member.guild.default_role
        ]
        roles = ",\n".join(reversed(role_list))
        if len(role_list) == 0:
            roles = "No roles :("
        return roles

    def timezone():
        with open('utilities/settings.json', 'r') as f:
            settings = json.load(f)
        tz = settings['timezone']
        return timezone(tz)

    def disabled_commands():
        command_file = open('utilities/disabled_commands.txt', 'r')
        command_lines = command_file.read()
        command_list = command_lines.split('\n')
        return list(command_list)

    async def permission_check(ctx, member, action):
        owner_id = ctx.guild.owner_id
        author = ctx.author

        if author.id == owner_id:
            if author == member:
                return await ctx.send(f"You cannot {action} yourself")
            else:
                return True

        else:
            if author == member:
                return await ctx.send(f"You cannot {action} yourself")
            elif author.bot:
                return await ctx.send(f"Bots cannot perform {action} actions")
            elif author.top_role == member.top_role:
                return await ctx.send(
                    f"You cannot {action} someone who has the same top role as you"
                )
            elif author.top_role < member.top_role:
                return await ctx.send(
                    f"You cannot {action} someone who has a higher role than you"
                )
            elif author.top_role > member.top_role:
                return True

    def permissions(member):
        x = member.guild_permissions
        pl = []
        if x.administrator:
            pl.append('`administrator`')
        if x.ban_members:
            pl.append('`ban members`')
        if x.kick_members:
            pl.append('`kick members`')
        if x.manage_guild:
            pl.append('`manage server`')
        if x.view_audit_log:
            pl.append('`view audit log`')
        if x.mention_everyone:
            pl.append('`mention everyone`')
        if x.manage_channels:
            pl.append('`manage channels`')
        if x.manage_nicknames:
            pl.append('`manage nicknames`')
        if x.manage_roles:
            pl.append('`manage roles`')
        if x.send_tts_messages:
            pl.append('`send TTS messages`')
        if x.manage_messages:
            pl.append('`manage messages`')
        if x.embed_links:
            pl.append('`embed links`')
        if x.send_messages:
            pl.append('`send messages`')
        if x.read_message_history:
            pl.append('`read message history`')
        if x.mute_members:
            pl.append('`mute members`')
        if x.deafen_members:
            pl.append('`deafen members`')
        if x.move_members:
            pl.append('`move members`')
        if x.stream:
            pl.append('`stream`')
        if x.priority_speaker:
            pl.append('`priority speaker`')

        permissions = ", ".join(pl)

        if len(pl) == 0:
            permissions = "You have basic permissions"

        return permissions
