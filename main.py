from operator import mod
from turtle import color, title
from unicodedata import name
from urllib.parse import uses_relative
from webbrowser import get
import discord
from discord.ext import commands

code = "OTQyMTEzOTQ3NDQyNjI2NjEy.Ygfx_A.j757VpaIF1G3BW1Eui_BQyM-m6I"

client = discord.Client

client = commands.Bot(command_prefix=">")

client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Modmails!"))
    print(f"Logged in as {client.user}")


help_c = """
> `mail` -  Mail to the mods. 
> `res`  -  Respond to a specific user's mail.
> `help` -  Shows this message.
"""


@client.command()
async def help(ctx):
    try:
        user = ctx.message.author
        embed = discord.Embed(title="Commands", description=help_c, color = discord.Color.red())
        embed.set_footer(text="Current prefix: >")
        await user.send(embed=embed)
        e = discord.Embed(title="Check you're direct messages! <:notification:942376750187417600>", color=discord.Color.green())
        await ctx.send(embed=e)
    except:
        error = discord.Embed(title="I can't send you messages.", color = discord.Color.red())
        await ctx.send(embed=error)


@client.command()
async def mail(ctx,*, problem):
    guild = ctx.guild
    mods = discord.utils.get(guild.roles, name="admin")
    try:
        for user in ctx.guild.members:
            if mods in user.roles:
                user = ctx.message.author
                recv = discord.Embed(title="Succesfully sent you're message to the mods!", color = discord.Color.green())
                await ctx.send(embed=recv)
                embed = discord.Embed(title= f"New mail from **{ctx.message.guild.name}**", description= f"> {problem}", color = discord.Color.red())
                embed.set_footer(text=f"User's ID {user.id}")
                await user.send(embed=embed)
                e = discord.Embed(title="Would you like to respond? Type `>res @username <msg>`.", color = discord.Color.red())
                await user.send(embed=e)
            else:
                error = discord.Embed(title="Failed to send. Try again!", color = discord.Color.red())
                await ctx.send(embed=error)
    except:
        error = discord.Embed(title="Somenthing went wrong... Try again!", color = discord.Color.red())
        await ctx.send(embed=error)


@client.command()
async def res(ctx,user : discord.Member,*, msg):
    mod = ctx.message.author
    try:
        embed = discord.Embed(title=f"Dear {user.display_name}", description=msg, color = discord.Color.red())
        embed.set_footer(text=f"From {mod.name}")
        await user.send(embed=embed)
        e = discord.Embed(title=f"Succesfully sent to {user.display_name}.", color = discord.Color.green())
        await ctx.send(embed=e)
    except:
        error = discord.Embed(title="Somenthing went wrong... Try again!", color = discord.Color.red())
        await ctx.send(embed=error)

@client.command()
async def source(ctx):
    embed = discord.Embed(title="Check out the source code on github!", color = discord.Color.red())
    await ctx.send(embed=embed)

client.run(code)