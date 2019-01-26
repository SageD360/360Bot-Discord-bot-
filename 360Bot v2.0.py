import discord
from discord.ext import commands
import asyncio
from itertools import cycle 

print('360Bot made by SageD360')
print('')

#Add Token here
TOKEN = ''

#Change Prefix here
prefix = input('Please enter the prefix you would like the bot to use: ')
print('')
print('360Bot is loading, this may take some time. If you set your prefix to nothing the bot may not work.')
print('')
client = commands.Bot(command_prefix = prefix)


#Prints a message in the console when the bot is ready
@client.event
async def on_ready():
    print('Bot is online and ready to use.')
    print('')
    print('The prefix is ' + prefix)
    

#Runs every time someone sends a message in your server
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    print('')
    print('Message sent in', channel)
    print('{}: {}'.format(author, content))
    await client.process_commands(message)
    
#Echos back what you say to the bot.
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

#Clears the chat(Must enter a number with the command to tell it how many messages you want it to delete or it will default to 100 messages deleted)
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted')

@client.command()
async def ping():
    await client.say('Pong!')


#Runs every time a message is deleted
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    print('')
    print('Message deleted in', channel)
    print('{}: {}'.format(author, content))


#Gives the Member role to new members of the server if the server has a role named members.
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)
    

    

client.run(TOKEN)
