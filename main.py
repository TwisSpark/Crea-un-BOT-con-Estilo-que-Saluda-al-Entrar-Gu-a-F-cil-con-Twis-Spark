import discord
from discord.ext import commands

# Activamos los intents... porque sin esto el bot no se entera de nada.
intents = discord.Intents.default()
intents.guilds = True
intents.members = True  # Le da más poder para funcionar bien.

# Creamos el bot con el prefijo '+' (cambiálo si querés ponerte creativo)
bot = commands.Bot(command_prefix='+', help_command=None, intents=intents)

# Cuando el bot se conecta, lo grita en la consola como un campeón
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Este evento se activa cuando el bot entra a un nuevo servidor
@bot.event
async def on_guild_join(guild):
    try:
        # Armamos el embed como una tarjeta de presentación elegante
        embed = discord.Embed(
            title="¡Gracias por invitarme!",
            description="Estoy listo para ayudarte. Usa `+help` para ver todos mis comandos.",
            color=discord.Color.from_str("#dbe1e1")  # Un gris clarito, elegante pero moderno
        )

        # Le ponemos el nombre del servidor en el pie del embed. Somos agradecidos.
        embed.set_footer(text=f"Servidor: {guild.name}")

        # Si el bot tiene avatar, lo usamos como si fuera su perfil en redes.
        if bot.user.avatar:
            embed.set_thumbnail(url=bot.user.avatar.url)

        # Buscamos un canal donde el bot tenga permiso para hablar y... ¡pum! Manda su saludo.
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send(embed=embed)
                break  # Una vez enviado el mensaje, ya se puede ir a dormir tranquilo.

    except Exception as e:
        # Si algo falla, lo mostramos en consola. Porque sí, hasta los bots cometen errores.
        print(f"Error en on_guild_join: {e}")

# Comando básico para ver si el bot está vivo. Un clásico.
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! Estoy vivo.")

# ¡No te olvides de poner tu token real acá! Si lo olvidás... el bot no arranca ni a palos.
bot.run('TU_TOKEN_AQUÍ')
