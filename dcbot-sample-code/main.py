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

img_path = ['img\owo.png', 'img\qwq.png', 'img\oao.png']    # Change it

@bot.command()
async def local_img(ctx: cmds.Context):
    random_img = random.choice(img_path)
    pic = dc.File(random_img)
    await ctx.send(file=pic)

bot.run(token)
