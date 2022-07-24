import discord as dc
import discord.ext.commands as cmds

channel_id = 1234567890     # Change it
token = 'starbuststream'    # Change it
cmd_prefix = '!'            # Change it
bot = cmds.Bot(command_prefix=cmd_prefix,intents=dc.Intents.all())

@bot.event
async def on_ready():
    print('>> Bot is on ready <<')
    c = bot.get_channel(channel_id)
    await c.send('>> Bot is on ready <<')

@bot.command()
async def say_hi (ctx: cmds.Context):
    await ctx.send('starbuststream')    # change it

img_path = ['imgs\\sample_img1.png', 'imgs\\sample_img2.png']    # Change it

@bot.command()
async def img(ctx: cmds.Context, id: int):
    pic = dc.File(img_path[id])
    await ctx.send(file=pic)

captions = ['i tried so hard', 'and got so far']     # Change it

@bot.command()
async def img_with_caption(ctx: cmds.Context, id: int):   # Finish it
    # pic = dc.File(img_path[id])   # 選擇圖片
    # await ctx.send( ___(A)___ )   # 印出圖片
    # cap = ___(B)___               # 選擇文字
    # await ctx.send(cap)           # 印出文字
    pass

bot.run(token)
