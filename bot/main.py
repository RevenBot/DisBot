import discord
import os
token=os.environ('DISCORD_BOT_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        channel=message.channel
        print('Nome canale: {0.channel.name} id: {0.channel.id}'.format(message))
        print('Message from {0.author}: {0.content}'.format(message))
        question = str(input("Rispondere "))
        if(question!='0'):
            await channel.send(question)
            return
        print('-------Message from {0.author}: {0.content}'.format(message))
        if(message.author==client.user):
            return
        if(message.author.name=='k REVENGE k'):
            await channel.send('ciao bello')
            await message.add_reaction('❤')
        if(message.author.name=='Varilotto'):
            await message.add_reaction('🤙')
            await channel.send('ciao panzone')

client = MyClient(activity=discord.Game(name='GTA con zRoCky'))
client.run(token)
