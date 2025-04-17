
import discord
from discord.ext import commands

# Activamos los "intents" para que el bot sepa qué puede hacer.
intents = discord.Intents.default()
intents.guilds = True  # Esto es clave para saber cuándo lo invitan a un server.

# Aquí puedes cambiar el prefijo del bot. ¿No te gusta el '+'? Pon el que te dé la gana.
bot = commands.Bot(command_prefix='+', help_command=None, intents=intents)

@bot.event
async def on_ready():
    # Cuando el bot se conecta, lo grita en la consola como todo un pro.
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_guild_join(guild):
    # Este es el mensaje de bienvenida. Puedes cambiar el texto, pero hazlo con cariño.
    embed = discord.Embed(
        title="¡Gracias por invitarme!",  # El título de bienvenida. Hazlo más épico si quieres.
        description="Estoy listo para ayudarte. Usa `+help` para ver todos mis comandos.",  # Spoiler: sí, tiene ayuda.
        color=discord.Color(int("#dbe1e1", 16))  # Este es el color del embed. Cambia el hex si te crees diseñador.
    )
    
    # Aquí se pone el nombre del server. Porque sí, somos agradecidos.
    embed.set_footer(text=f"Servidor: {guild.name}")

    # Si el bot tiene avatar, lo luce como todo un influencer digital.
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)

    # Busca el primer canal donde pueda hablar y lanza su mensaje estelar.
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(embed=embed)
            break  # Una vez enviado, se va a descansar. No molesta más.

# Aquí va tu token secreto. No lo muestres o tu reino se cae.
bot.run('TU_TOKEN')
