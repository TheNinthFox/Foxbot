import dice
import foxbot
import helper
import reddit
from dnd import command as dnd_command

if __name__ == '__main__':
    # Create our bot
    bot = foxbot.FoxBot()
    bot.remove_command('help')

    # Helper commands
    bot.add_command(helper.help)
    bot.add_command(helper.info)
    bot.add_command(helper.greet)

    # Dice commands
    bot.add_command(dice.roll)

    # Reddit commands
    bot.add_command(reddit.reddit)

    # DnD commands
    bot.add_command(dnd_command.dnd)

    # Run our bot
    bot.run(helper.get_secret_key())
