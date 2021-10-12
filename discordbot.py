import discord

client = discord.Client()


@client.event
async def on_ready():
    print("{0.user} ログインしました".format(client))
    print("/help | 導入サーバー数 : " + str(len(client.guilds)))

    activity = discord.Activity(name="導入サーバー数 : " + str(len(client.guilds)),
    type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower() == ("暇"): 
      await message.channel.send("暇か？だったらしりとりしようぜ！\nプリン！はいおわり！")
    if message.content.lower() == ("キモ" or "きも"):
      await message.channel.send("お前の方がきもいと思うな")
    if message.content.lower() == ("うんこ" or "ウンコ" or "💩"):
      await message.channel.send("俺ウンコ食ったことあるんだぜ！")
    if message.content.lower() == ("/help"):
      await message.channel.send("こいつ俺のこと知りたいらしいぜｗｗ/n教えねぇよｗｗ")

client.run("ODk3MTAxOTI3NzE0Nzg3MzU5.YWQxRg.QiYgkFjKlW-Xho8EGdirmzAX2Ug")
