import discord
from discord.ext import commands


class FoxBot(commands.Bot):
    command_list = []

    def __init__(self):
        super(FoxBot, self).__init__(command_prefix='!', description='Foxhole Foxbot Butler')

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_message(self, message: discord.Message):
        await self.process_commands(message)

        if message.author == self.user:
            return

        if "beeindruck" in message.content:
            await message.channel.send("Bark bork! Sehr beeindruckend!")

        recht = [" recht", "recht ", " recht "]
        if any(r in message.content.lower() for r in recht) and "rechts" not in message.content:
            await message.channel.send("Bark bork! Recht hat er!")

        if "alive" in message.content:
            await message.channel.send("Bark bork! I'm alive!")

        if isinstance(message.channel, discord.DMChannel) and message.content.split()[0][1:] not in self.command_list:
            await message.author.send("Bark bork! Du erfährst mehr über mich mit !help und !info!")

    def add_command(self, command):
        super(FoxBot, self).add_command(command)
        self.command_list.append(command.name)
