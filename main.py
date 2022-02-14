from email.mime import image
import json
from multiprocessing import Value
from unicodedata import name
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
> `mail`     -   Mail to the mods. 
> `res`      -   Respond to a specific user's mail.
> `help`     -   Shows this message.
> `source`   -   Shows the source code.
> `say`      -   Sends you're message.
> `rules`    -   Shows basic discord rules.
> `support`  -   Support.
"""

basic_rules = """
> **Be respectful, civil, and welcoming.** \n
> **No inappropriate or unsafe content.** \n
> **Do not misuse or spam in any of the channels.** \n
> **Do not join the server to promote your content.** \n
> **Any content that is NSFW is not allowed under any circumstances.** \n
> **Do not buy/sell/trade/give away anything.**"""


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
@commands.has_permissions(kick_members=True)
async def mail(ctx, role : discord.Role,*, problem):

    await ctx.channel.purge(limit=1)
    guild = ctx.guild
    mods = discord.utils.get(guild.roles, name=f"{role}")
    try:
        for user in ctx.guild.members:
            if mods in user.roles:
                user = ctx.message.author
                recv = discord.Embed(title="Succesfully sent you're mail!", color = discord.Color.green())
                await ctx.send(embed=recv)
                embed = discord.Embed(title= f"New mail from **{ctx.message.guild.name}**\nFrom: ``{user}``", description= f"> {problem}", color = discord.Color.red())
                embed.set_thumbnail(url="https://i.ibb.co/TrbrW5Z/new-mail.png")
                embed.set_footer(text=f"To {role}")
                o = await user.send(embed=embed)
                await o.add_reaction("❓")
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
    await ctx.channel.purge(limit=1)
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
    embed = discord.Embed(title=f"Check out the source code on (https://github.com/Erwin-afk/Modmail)!", color = discord.Color.red())
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    embed = discord.Embed(title=f"Current latency: {round(client.latency)* 1000}ms", color = discord.Color.gold())
    await ctx.send(embed=embed)


@client.command()
async def say(ctx,*,msg):
    await ctx.channel.purge(limit=1)
    await ctx.send(msg)


@client.command()
async def support(ctx):
    await ctx.send("Check out the support server!")
    await ctx.send("https://discord.gg/Cq8WDsFcZW")


@client.command()
async def rules(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="`📜`**Basic rules**", description=basic_rules, color = discord.Color.red())
    embed.set_image(url="https://cdn-longterm.mee6.xyz/plugins/commands/images/762115688881586186/037b1d0a1decbf7ffc202d2d38621c319d0cb3955225abd1f8ca9bc74c198589.gif")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx,am=3):
    await ctx.channel.purge(limit=am)
    embed = discord.Embed(title="Cleared {} messages.".format(am), color = discord.Color.green())
    await ctx.send(embed=embed)



client.run(code)