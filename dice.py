import random
from discord.ext import commands


@commands.command()
async def roll(ctx, query: str, additionals=''):
    addition = 0
    subtraction = 0
    if '+' in additionals:
        addition = int(additionals[1:])
    if '-' in additionals:
        subtraction = int(additionals[1:])

    try:
        result = process_query(query)
        if isinstance(result, int):
            result = result + addition - subtraction
    except:
        await ctx.send('Bark bork! Falsches Format! Versuch mal XdY!')
        return

    await ctx.send(result)


def process_query(query):
    addition = 0
    subtraction = 0
    if '+' in query:
        dice_info, addition = query.split('+')
    elif '-' in query:
        dice_info, subtraction = query.split('-')
    else:
        dice_info = query

    result = 0
    dice_amount, dice_upper_limit = dice_info.split('d')

    if len(dice_amount) > 3 and len(dice_upper_limit) > 3:
        return 'Bark bork! Soweit kann ich nicht zählen!'

    for i in range(int(dice_amount)):
        result += random.randint(1, int(dice_upper_limit))

    result = result + int(addition) - int(subtraction)
    return result
