import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/")


@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.idle,\
        activity=discord.Game("Joulie est dans la place"))

#Commande /regles
@bot.command()
async def regles(ctx):
    await ctx.send("Les règles sont:\n1. Pas d'insultes\n2. Pas de mensonges\n3. Pas de spam")

# créer la commande !bienvenue @pseudo
@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    # recupere le nom
    pseudo = nouveau_membre.mention

    # executer le message de bienvenue
    await ctx.send(f"Bienvenue à {pseudo} sur le serveur discord ! N'oublie pas de faire !regles")

token = "NzkxMDQ0MjE3NDkyNjAyOTMw.X-JbVg.yDaNYuenxLWTzWEhv-E69mApm5w"


print("Lancement du bot")

bot.run(token)