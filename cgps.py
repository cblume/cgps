import discord

TOKEN = 'NTA2MDQ3Nzk5OTc3MDUwMTEy.Drcd1A.CxpVv_OqdPnDq_K5mD4FI-2lhHw'

client = discord.Client()

@client.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')

client.run(TOKEN)