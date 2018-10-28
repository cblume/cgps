import random
import re
from cgps_misc import CGPS_TOKEN
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ('?', '!')
TOKEN = CGPS_TOKEN

client = Bot(command_prefix=BOT_PREFIX)


@client.command(
    name='hello',
    pass_context=True)
async def hello(context):
    message = 'Hello, {}.'.format(context.message.author.mention)
    await client.say(message)


@client.command(
    name='roll',
    description='Rolls a single or multiple specified dice.',
    brief='May you roll well.',
    pass_context=True)
async def roll(context, dice):
    matches = re.match(r"([1-9]\d*)d([1-9]\d*)[ ]?([-+]?[1-9]\d*)?(!)?", dice)
    if matches:
        number_of_dice = matches.group(1)
        type_of_dice = matches.group(2)
        modifier = matches.group(3)
        apply_modifier_to_all = matches.group(4) == '!'

        print('number_of_dice:', number_of_dice)
        print('type_of_dice:', type_of_dice)
        print('modifier:', modifier)
        print('apply_modifier_to_all:' , apply_modifier_to_all)
    else:
        print("I'm sorry, I didn't get that.")

    rolls = roll_dice(number_of_dice, type_of_dice)

    result = 0;
    message = "```\nIndividual rolls: "
    message += '(' if modifier and not apply_modifier_to_all else ''
    for roll in rolls:
        message += '<{}>{} '.format(roll, modifier if modifier and apply_modifier_to_all else '')
        result += roll + (int(modifier) if modifier and apply_modifier_to_all else 0)
    
    if modifier and not apply_modifier_to_all:
        message = message[:-1]
        message += '){}'.format(modifier)

    message += "\nResult: {}\n```".format(result)
    print(message)
    await client.say("{},\n{}".format(context.message.author.mention, message))


def roll_dice(number, type):
    rolls = []
    print('Rolling dice...')
    for _ in range(int(number)):
        roll = random.randint(1, int(type))
        print('Rolled: {}'.format(roll))
        rolls.append(roll)

    return rolls


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')

client.run(TOKEN)