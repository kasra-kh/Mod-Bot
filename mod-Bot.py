import os
import time
import json
import random
import discord
import requests
import datetime
from asyncio import *
from discord import embeds
from discord import colour
from discord.ext import tasks
from discord.ext import commands
from dhooks import Webhook, Embed
from discord.ext.commands.errors import DisabledCommand

class data():
    icon = "" # your Icon 
    token = "" # Your Bot Token
    prefix = "" #Your Bot Perefix
    svName = "" #Your server Name
    
client = commands.Bot(command_prefix=data.prefix,intents=discord.Intents.all())    

client.remove_command("help")


colors = [0x01b8a1, 0xaa0e6c, 0x390174, 0xf6fa02, 0x5df306, 0x2206f3, 0xfffdfd, 0xff0a0e, 0x850000, 0xe76868, 0x4eca75, 0xb38203, 0xc44400, 0x000000, 0x0517dd, 0x6c6f92, 0x144900, 0xffffff, 0x020246, 0xe209b7, 0x0976e2, 0x3de209, 0xe29209, 0x08a247]

############ Run Discord Bot #############

@client.event
async def on_ready():
    print(f'Bot Ready sucsesfull')
    client.my_current_task = kasra.start() 

############# WELCOME ############# 

@client.event
async def on_member_join(member):
    guild1 = client.get_guild() #server ID
    welcome_channel = guild1.get_channel() #Your channel To send Welcome
    embed = discord.Embed(title='**Welcome**', description=f'Hey {member.mention} , welcome to {data.svName} !', color=random.choice(colors)) 
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text='Developer 001',icon_url=data.icon)
    await welcome_channel.send(embed=embed)
    kobs = client.get_channel()#your channel welcome log
    emd85 = discord.Embed(title='**Welcome Log**',description=f'```New Member Joined Server :)``` Member ID ```{member.name}```',inline=True)
    emd85.set_thumbnail(url=member.avatar_url)
    await kobs.send(embed=emd85)

############## Mute #############

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(cdv, member: discord.Member, *, reason=None):
    guild = cdv.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted🚫")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted🚫")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False, connect=False)
    await member.add_roles(mutedRole, reason=reason)
    embed = discord.Embed(title=f"𝗬𝗼𝘂𝗿 𝗮𝗿𝗲 𝗺𝘂𝘁𝗲𝗱 (** {member.name} **) 𝗿𝗲𝗮𝘀𝗼𝗻 : ( ||**{reason}**|| ) 🚫", colour=random.choice(colors),inline=True)
    embed.set_footer(icon_url=data.icon)
    await cdv.send(embed=embed)

############## un Mute #############

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(cdv, member: discord.Member):
    mutedRole = discord.utils.get(cdv.guild.roles, name="Muted🚫")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title=f"𝗨𝗻𝗺𝘂𝘁𝗲𝗱 ! ** {member.name} **",description=f"𝗨𝗻𝗺𝘂𝘁𝗲𝗱 𝗕𝘆 {cdv.author.name}", colour=random.choice(colors),inline=True)
    embed.set_footer(icon_url=data.icon)
    embed.set_thumbnail(url=data.icon)
    await cdv.send(embed=embed)

############# user info ############# 

@client.command(aliases=["user", "User"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=random.choice(colors), timestamp=ctx.message.created_at,
                          title=f"𝗨𝘀𝗲𝗿 𝗜𝗻𝗳𝗼 {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆 : {ctx.author}", icon_url = ctx.author.avatar_url)

    embed.add_field(name="𝗜𝗗 :", value=member.id)

    embed.add_field(name="𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗢𝗻:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p "))
    embed.add_field(name="𝗝𝗼𝗶𝗻𝗲𝗱 𝗦𝗲𝗿𝘃𝗲𝗿 𝗢𝗻:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p "))

    embed.add_field(name="𝗧𝗼𝗽 𝗥𝗼𝗹𝗲:", value=member.top_role.mention)

    await ctx.reply(embed=embed)

############# lock ############# 

@client.command(aliases=["LOCK", "Lock"], pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel=None):
    if channel == None:
        embed = discord.Embed(title="𝗧𝗮𝗴 𝘁𝗵𝗲 𝗱𝗲𝘀𝗶𝗿𝗲𝗱 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗽𝗹𝗲𝗮𝘀𝗲!", colour=random.choice(colors))
        embed.set_footer(text="𝗹𝗶𝗸𝗲: n!Lock #x", icon_url =data.icon)
        await ctx.reply(embed=embed)
    else:
        the_channel = client.get_channel(channel.id)
        await the_channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=False)
        await channel.send('~~@everyone~~')
        embed = discord.Embed(title="🔒 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗟𝗼𝗰𝗸", colour=random.choice(colors))
        await channel.send(embed=embed)

############# unlock ############# 

@client.command(aliases=["unLOCK", "unLock", "UNLOCK", "Unlock", "UNlock", "UNLock"], pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel):
    if channel == None:
        embed = discord.Embed(title="𝗧𝗮𝗴 𝘁𝗵𝗲 𝗱𝗲𝘀𝗶𝗿𝗲𝗱 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗽𝗹𝗲𝗮𝘀𝗲!", colour=random.choice(colors))
        embed.set_footer(text="𝗹𝗶𝗸𝗲: n!UnLock #x", icon_url =data.icon)
        await ctx.reply(embed=embed)
    else:
        the_channel = client.get_channel(channel.id)
        await the_channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(title="🔒 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘂𝗻𝗟𝗼𝗰𝗸", colour=random.choice(colors))
        await channel.send(embed=embed)

############# Clear ##############

@client.command(description = "Clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit=amount+1)
    embed = discord.Embed(colour=random.choice(colors),title="𝗗𝗲𝗹𝗲𝘁𝗲 𝗠𝗲𝘀𝘀𝗮𝗴𝗲",description=f'{amount} Message Deleted !')
    embed.set_thumbnail(url=data.icon)
    await ctx.send(embed=embed)
    amount = 1
    await ctx.channel.purge(limit=amount)
    amount = 5  

############### Warn Command ###############

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx,member: discord.Member,*,result):
    authorm = ctx.message.author
    embed = discord.Embed(title = ":warning: 𝗪𝗮𝗿𝗻𝗶𝗻𝗴 :warning:",colour=random.choice(colors),description = f"𝘄𝗮𝗿𝗻 ( **{member}** ) 𝗿𝗲𝗮𝘀𝗼𝗻 ( **{result}** ) :no_entry_sign:", inline=True)
    embed.set_thumbnail(url=data.icon)
    await ctx.send(embed=embed)
    embed = discord.Embed(title = ":warning: 𝗪𝗮𝗿𝗻𝗶𝗻𝗴 :warning:",colour=random.choice(colors),description = f"𝘄𝗮𝗿𝗻 ( **{member}** ) 𝗿𝗲𝗮𝘀𝗼𝗻 ( **{result}** ) :no_entry_sign:", inline=True)
    embed.set_thumbnail(url=data.icon)
    await member.send(embed=embed)


############### Avatar #############

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def avatar(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
    icon_url = member.avatar_url

    avatarEmbed = discord.Embed(title = f"{member.name}\'s avatar ", colour=random.choice(colors))

    avatarEmbed.set_image(url = f"{icon_url}")

    avatarEmbed.timestamp = ctx.message.created_at
    avatarEmbed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
    await ctx.send(embed = avatarEmbed) 


################  Announce  ################

@client.command(pass_content=True, aliases=['Announce'])
async def announce(ctx, *, text):
        await ctx.message.delete()
        embed=discord.Embed(title="**Announcement**", color=random.choice(colors))
        embed.set_thumbnail(url=data.icon)
        embed.add_field(name="Message:", value=text, inline=True)
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")

############# HELP ############# 
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(title=f"**{data.svName}**",description='```I came to help you```', colour=random.choice(colors))
    embed.set_thumbnail(url=data.icon)
    embed.set_footer(icon_url=data.icon)
    embed.add_field(name="publice", value="`avatar`,`user`", inline=True)
    embed.add_field(name="Modration", value="`warn`,`mute`,`unmute`", inline=True)
    embed.add_field(name="channel", value="`lock`,`unlock`,`clear`", inline=True)
    await ctx.reply(embed=embed)


############## CoolDown Error ###############

@help.error
async def help_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
        await ctx.send(embed=em)

@avatar.error
async def avatar_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
        await ctx.author.send(embed=em)

############## isinstance Error ###############

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
        description=f"{error}",
        color=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
        description=f"{error}",
        color=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
        description=f"{error}",
        color=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
        description=f"{error}",
        color=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(
        description=f"{error}",
        color=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.errors.NoPrivateMessage):
        embed = discord.Embed(
        description=f"{error}",
        color=random.choice(colors)
        )
        await ctx.reply(embed=embed)

################ Bot Presense ##################

@tasks.loop()
async def kasra():
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{data.prefix}help | {members} Members"),status=discord.Status.dnd)  

################ Run Discord Bot Client ##################

client.run(data.token)