# importing OS to deal with future files at least ...
import os
from sweb import hweb
# Importing discord library
import discord

# Loading TOKEN from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Instantiate an object of the client
client = discord.Client()

# Prefix of the bot
count = 0
pfx = "."
cmds = ["join","leave","web"]

# A decorator function to start
@client.event
async def on_ready():
  print(f"{client.user} has connected to Discord!\nHello World")

# A decorator function to read message the send response
@client.event
async def on_message(message):
  if (message.author == client.user) or (message.author.bot):
    return

  if message.guild is None:
    embed=discord.Embed(title="Invite me to your **server**", url="https://discordapp.com/oauth2/authorize?client_id=569724616210382875&scope=bot&permissions=277129284672", description="I'm a nice bot under construction", color=0x00ff00)
    embed.set_author(name=f"{message.author.display_name}", url="https://discordapp.com/oauth2/authorize?client_id=569724616210382875&scope=bot&permissions=277129284672", icon_url=f"{message.author.display_avatar}")
    embed.set_thumbnail(url=f"{client.user.display_avatar}")
    embed.set_footer(text="https://discordapp.com/oauth2/authorize?client_id=569724616210382875&scope=bot&permissions=277129284672")
    await message.reply(embed=embed)
    return

  msg = message.content.lower()
  cmd = msg.startswith(pfx)
  author = message.author
  emoji = ["👀","👋","👉","👈","👍"]

  if msg == pfx:
    gds = [x.name for x in client.guilds]
    await message.reply( "\n".join(gds))
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])

  if cmd and (msg[len(pfx):] not in cmds):
    rpl = f"**I'm currently under-development**,{author}"
    global count
    count += 1
    await message.reply(rpl+f"\ncount **{str(count)}**")

  if cmd and (msg[len(pfx):] == cmds[2]):
    try:
      obj = hweb()
      txt = obj.get_data()
      await message.reply(txt)
    except:
      await message.reply("exception")
    await message.reply("web command issued")
    

# Actual start logging-in
client.run(TOKEN)
