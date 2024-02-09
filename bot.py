from pyrogram import Client, filters


Bot = Client('bot', session_string="BADb_SIAOA9e7MM1oce2mbvJpEFuq7b6pIq2I2WsNn1E1fr2YAMZsXAsPB6wAkwvfu5zIbnR0xvABqwmMSVfdpKJUldIC4GTSY14MaS_vMzj3A69iUZTnIbnZVUYcVPO2kdIkzg_EdMv0LhSC-hUWLs9SJgV-mNRl-NSP-ZHta5Bs8ZCpRf_a2gOrrdnQZ8QjFNh6QUR8BrscP0GX2aobq9WnY_l3eUgMhl9NHMCKkp4Iqk_RW-fBWFXnMCT7cbFaNE8rHlAemiFOSxG5keXvTyPHiHEV1hzrW2a51CDDrRlBZrezqGX_uyOIgWl6LoQdHL5AznNHQZgrCLYiAzI2Thc-vE3XAAAAAFkzPp1AQ")


@Bot.on_message(filters.command('start'))
async def start(c, m):
    await m.reply('Hai Hallo 🔥🔥🔥🔥')
  
 
Bot.run()