import discord as dc
import discord.ext.commands as cmds
import random

channel_id = 1234567890     # Change it
token = 'starbuststream'    # Change it
cmd_prefix = '!'            # Change it
bot = cmds.Bot(command_prefix=cmd_prefix,intents=dc.Intents.all())

@bot.event
async def on_ready():
    print('>> Bot is on ready <<')
    c = bot.get_channel(channel_id)
    await c.send('>> Bot is on ready <<')

img_path = ['imgs\\sample_img1.png', 'imgs\\sample_img2.png']    # Change it

@bot.command()
async def local_img(ctx: cmds.Context, id: int):
    pic = dc.File(img_path[id])
    await ctx.send(file=pic) 

bot.run(token)
