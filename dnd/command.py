from dnd import doodle_handler
from discord.ext import commands


msg_unknown = "Bark bork! Diesen Befehl kenne ich nicht!"


@commands.command()
async def dnd(ctx, *args):
    args = list(args)
    if len(args) > 0:
        request = args.pop(0)
    else:
        await ctx.send(msg_unknown)
        return

    module_list = [doodle_handler]

    msg = call_module_distribution_function(module_list, request, args)
    await ctx.send(msg)


def call_module_distribution_function(module_list, request, args):
    for module in module_list:
        module_contents = dir(module)
        if request in module_contents:
            method = getattr(module, request)
            return method(args)

    return msg_unknown
