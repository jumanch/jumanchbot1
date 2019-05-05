#pyenv shell
import discord
import datetime
import random
import math
import copy
import re
from urllib import parse,request
from discord.ext import commands

client = commands.Bot(command_prefix='·', description="El guardian de OPIPARO PEPINO.")

########## HELP ###########


# client.remove_command('help')

# @client.command(pass_context=True)
# async def help(ctx):
    
#     author = ctx.message.author
#     embed = discord.Embed(
#         colour = discord.Colour.orange()
#     )

#     embed.set_author(name='Ayuda')
#     embed.add_field(name='·ping', value='Returns Pong!', inline=False)

#     await client.send_message(author, embed=embed)


##### Comando sueltos

# @client.event()
# async def on_reaction_add(reaction,user):
#     channel = reaction.message.channel
#     await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name,reaction.emoji,reaction.message.content))

# @client.event
# async def on_reaction_remove(reaction,user):
#     channel = reaction.message.channel
#     await client.send_message(channel, '{} has removed {} from: {}'.format(user.name,reaction.emoji,reaction.message.content))

@client.command()
async def opina(ctx,persona:str):
    elite = ['juan','Juan','jumanch','Jumanch','lirin','Lirin','Boss','boss']
    if persona in elite:
        if persona == 'juan' or persona == 'Juan':
            frase_juan = ['Primero dispara y luego pregunta. Y sinó, que se lo digan a Boss','¿Ese al que le gusta matar a sus compañeros no?','Creo que esa persona le debe 50 euros a alguien.','¿Ese al que le gusta matar a sus compañeros no?']
            await ctx.send(random.choice(frase_juan))
        elif persona == 'lirin' or persona == 'Lirin':
            frase_lirin = ['Ten cuidado que esa persona te levanta una dictadura en un momento :eyes:','No le gusta avisar.','No vayas con esa persona a bot, y menos con Zyra o estaras perdidito.','¿Esa es la main Widow de la que me hablaste?']
            await ctx.send(random.choice(frase_lirin))
        elif persona == 'boss' or persona == 'Boss' :
            frase_boss = ['\"Bebé exiliado\", otra forma de decirle que es adoptao.','Cuentan los trobadores que en un servidor de TF2 se cobijaba una história.','Adora a las Zyras Supp <3','No le gusta canalizar.','Es Naruto!!:man_with_gua_pi_mao:','Huelo su peste desde aquí xd']
            await ctx.send(random.choice(frase_boss))        
        elif persona == 'Jumanch' or persona == 'jumanch':
            frase_jumanch = ['Main Zaratustra desde la BETA','Lo conoceréis por películas como \"¡Que te jodan Mickey Rooney!\",  \"¡Hala! Ya se ha roto...\" y \"La culpa de Lirin\"','El verdadero dueño de Tierras de Fuego.:flame::flame:','La justicia llueve del cielo :umbrella:','Si lleva a Torb, la partida está ganada! Más o menos...','Le gusta que no le avisen, ah si, y los vasos de leche','..Papá?','¿Ese al que le gusta matar a sus compañeros no?','OH FUCK!','Que tejodan Mi.. NO.']
            await ctx.send(random.choice(frase_jumanch))
    else:
        await ctx.send("No conozco a ese/a tal {}.".format(persona))



# @client.command()
# async def boss(ctx):
#     frase_boss = ['\"Bebé exiliado\", otra forma de decirle que es adoptao.','Cuentan los trobadores que en un servidor de TF2 se cobijaba una história.','Adora a las Zyras Supp <3','No le gusta canalizar.','Es Naruto!!:man_with_gua_pi_mao:','Huelo su peste desde aquí xd']
#     await ctx.send(random.choice(frase_boss))

# @client.command()
# async def lirin(ctx):
#     frase_lirin = ['Ten cuidado que esa persona te levanta una dictadura en un momento :eyes:','No le gusta avisar.','No vayas con esa persona a bot, y menos con Zyra o estaras perdidito.','¿Esa es la main Widow de la que me hablaste?']
#     await ctx.send(random.choice(frase_lirin))

# @client.command()
# async def juan(ctx):
#     frase_juan = ['Primero dispara y luego pregunta. Y sinó, que se lo digan a Boss','¿Ese al que le gusta matar a sus compañeros no?','Creo que esa persona le debe 50 euros a alguien.','¿Ese al que le gusta matar a sus compañeros no?']
#     await ctx.send(random.choice(frase_juan))

# @client.command()
# async def jumanch(ctx):
#     frase_jumanch = ['Lo conoceréis por películas como \"¡Que te jodan Mickey Rooney!\",  \"¡Hala! Ya se ha roto...\" y \"La culpa de Lirin\"','El verdadero dueño de Tierras de Fuego.:flame::flame:','La justicia llueve del cielo :umbrella:','Si lleva a Torb, la partida está ganada! Más o menos...','Le gusta que no le avisen, ah si, y los vasos de leche','..Papá?','¿Ese al que le gusta matar a sus compañeros no?','OH FUCK!','Que tejodan Mi.. NO.']
#     await ctx.send(random.choice(frase_jumanch))

@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong!!! {round(client.latency * 1000)}ms')

@client.command()
async def motherfuker(ctx):
    await ctx.send("SOY UN HIJO DE PUTA QUE NO SE SUMAR")


# Operaciones aritmeticas 

@client.command()
async def suma(ctx, n1: int,n2: int):
    solucion = n1 + n2
    if solucion == 0:
        await ctx.send("Tu no puedes sumar mas alpacas a la ruta de la leña si no tienes furgoneta.")
    else:
        await ctx.send("Entendido, la suma de {} mas {} da {}".format(n1,n2,solucion))

@client.command()
async def resta(ctx, n1: int,n2: int):
    solucion = n1 - n2
    if solucion == 0:
        await ctx.send("Si tu tienes {} galletas y las repartes entre {} amigos, te sigues quedando con {} galletas y con {} amigos.".format(n1,n2,n1,n2))
    else:
        await ctx.send("Entendido, la resta de {} menos {} da {}".format(n1,n2,solucion))

@client.command()
async def multiplica(ctx, n1: int,n2: int):
    solucion = n1 * n2
    await ctx.send("Entendido, la multiplicación de {} por {} da {}".format(n1,n2,solucion))

@client.command()
async def eleva(ctx, n1: int,n2: int):
    solucion = n1 ** n2
    await ctx.send("Entendido, {} elevado a {} da {}".format(n1,n2,solucion))

@client.command()
async def divide(ctx, n1: int,n2: int):
    solucion = n1 / n2
    try:
        if solucion == 0:
            await ctx.send("Si tu tienes {} galletas y las repartes entre {} amigos, te sigues quedando con {} galletas.".format(n1,n2,n1))
        else:
            await ctx.send("Entendido, la division de {} entre {} da {}".format(n1,n2,solucion))
    except:
        await ctx.send("No me hagas perder el tiempo.")

@client.command(pass_context=True)
async def quienes(ctx, user: discord.Member):
    # await client.say("Su nombre de usuario es: {}".format(user.name))
    # await client.say("Su ID es: {}".format(user.id))
    # await client.say("Su estado es: {}".format(user.status))
    # await client.say("Su mayor rol es: {}".format(user.top_role))
    # await client.say("Se unió en: {}".format(user.joined_at))

    embed = discord.Embed(title=f"Y este quien cojones es..",color=discord.Color.blue())
    embed.add_field(name="Su nombre de usuario es:", value=f"{user.name}")
    embed.add_field(name="Su ID es:", value=f"{user.id}")
    embed.add_field(name="Su estado es: ", value=f"{user.status}")
    embed.add_field(name="Su mayor rol es: ", value=f"{user.top_role}")
    embed.add_field(name="Se unió en: ", value=f"{user.joined_at}")
    embed.set_thumbnail(url=f"{user.avatar_url}")
    await ctx.send(embed=embed)
  






# # no va
# @client.command(pass_context=True)
# async def kick(ctx, user: discord.Member):
#     await ctx.send(":boot: Cya, {}. :)".format(user.name))
#     await Bot.kick(user)

### Youtube

@client.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?'+ query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v='+ search_results[0])

@client.command()
async def cumbia(ctx):
    search = "cumbia drive"
    aleatorio= random.randint(0,40)
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?'+ query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v='+ search_results[aleatorio])
##### Mini- Juegos

@client.command()
async def duda(ctx,*, pregunta_duda):
    respuesta_duda= [ 'Seguramente.','Definitivamente sí.','Sin duda.','SI JODER','Por lo que veo sí..','Sí','Todo apunta que sí','No se yo..','Mejor no te lo digo..','No cuentes con ello.','No','Lo dudo mucho','Nosé, preguntale a Lirin.','Como no se alineen los astros ya me dirás.','De quien será la culpa','QUE 50 EUROS']
    await ctx.send(f'- Pregunta: {pregunta_duda}\n- Respuesta: {random.choice(respuesta_duda)}')    

@client.command()
async def repite(ctx,frase):
    output= ''
    for word in frase:
        output += word
    await ctx.send("{}".format(output))

# @client.command(pass_context=True)
# async def clear(ctx,amount=100):
#     channel = ctx.message.channel
#     messages = []
#     async for message in client.logs_from(channel, limit=int(amount)):
#         messages.append(message)
#     await client.delete_messages(messages)
#     await client.say("Mensajes borrados.")


@client.command()
async def probabilidad(ctx,pregunta):
    
    probabilidad= int(random.randint(0, 100))
    if probabilidad > 9:
        probabilidad2 = copy.copy(probabilidad)
        probabilidad2 = float(probabilidad2/2)
        probabilidad2= math.ceil(probabilidad2)
        pass
    else:
        probabilidad2 = copy.copy(probabilidad)
        probabilidad2 = float(probabilidad2/2)
        probabilidad2= math.ceil(probabilidad2)
    separador = "x"
    respuesta= ""


    if probabilidad >= 90:
        respuesta=" - ¡Enhorabuena!"
    elif probabilidad in range(60,90):
        respuesta=" - Ni tan mal."
    elif probabilidad in range(40,60):
        respuesta=" - UUUUUUuufff."
    elif probabilidad in range(20,40):
        respuesta=" -Lo siento."
    else:
        respuesta="- F."

    embed = discord.Embed(title=f"PROBABILIDADES",description="""Hay un {}% de probabilidades de {}.

                 0%                                 .                                   .                                    .                                    100%
                 A+++++++++++++++++++++++++++++++++++++++++++++++A
                 C{}|
                 A+++++++++++++++++++++++++++++++++++++++++++++++A
                 
                 Guardian{}""".format(probabilidad,pregunta,separador*probabilidad2,respuesta),color=discord.Color.blue())

    await ctx.send(embed=embed)
###################### Info del servidor
@client.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="El mejor servidor jamás creado bla bla bla la culpa de Lirin siempre pero ojo, no abuses del meme o te banearé.",timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.add_field(name="Servidor creado en", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Región", value=f"{ctx.guild.region}")
    embed.add_field(name="ID Servidor", value=f"{ctx.guild.id}")
    # embed.add_field(name="Miembros", value=f"{ctx.message.server.members}")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Icon-round-Question_mark.svg/1024px-Icon-round-Question_mark.svg.png")
    # embed.set_thumbnail(url="{}".format(ctx.guild.icon))
    
    await ctx.send(embed=embed)



# Evento
@client.event
async def on_ready():
    game = discord.Game("Jugando a ser yo.. digo Dios")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Ya estoy online!')

client.run("NTczODE4OTIwNTQ1NTUwMzM4.XMwZNw.9oZMRBa5cT37ZUqax5k5ZBJiAnw")
