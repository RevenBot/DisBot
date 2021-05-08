import discord
import logging
import os
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# token=os.get.env("")

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
client.run('Nzg5MTYyNDg2MTI5NjIzMDQw.X9uC1g.bmz42V1UeeZsgMhAMxhQH55dEkU')
