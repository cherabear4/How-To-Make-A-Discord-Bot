import discord
from discord.ext import commands, tasks
from itertools import cycle



#                              that is the command prefix like !help
#--------------------------------------↘-------
client = commands.Bot(command_prefix = '>')
#----------------------------------------------




@client.event
async def on_ready():
    #                                                                                ↘What are we playing
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Kami Green | 2b2t.org'))
    print('Bot Ready.')

#This is A Command - ↘Ping so it would be >ping or !ping or -ping
@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

#this is an embed its a lot cleaner than regualr text
@client.command()
async def shops(ctx):
    
    #                          ↘this is the title of the embed
    embed=discord.Embed(title='Anarchy Shops', colour=discord.Color.green())

    #                     ↘sub title                         ↘this is the text
    embed.add_field(name='Availible Shops:', value=f'Text Here')
    await ctx.send(embed=embed)

#                ↘insert your bot token here
client.run('NzUwNDAyOTYyMjQ0ODk0ODMw.X06BOA.amdyFnRmHy5oDFrHy27sUrlT5Hw')


#HOW TO EMEBED
    #embed=discord.Embed(title='test', colour=discord.Color.blue())
    #embed.add_field(name='test', value=f'test')
    #embed.add_field(name='test', value=f'test')
    #await ctx.send(embed=embed)