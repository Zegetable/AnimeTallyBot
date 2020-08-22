import discord
from discord.ext import commands
import asyncio
import random
import CalifaSQL
from CalifaSQL import newTally
from CalifaSQL import searchTally
from CalifaSQL import increTally
from CalifaSQL import printTallies

bot = commands.Bot(command_prefix='!')
baseChance = 2
#qt = quote threshold
qt0 = 0
qt1 = 10
qt2 = 20
qt3 = 30
qt4 = 40
qt5 = 50
existingTallyMatches = 0
quote0= "Good Bye JoJo!"
quote1= "BAKA MONOGA!"
quote2= "What does the scanner say about his power level?"
quote3= "That is why I turned your banana into a gun"
quote4= "Half of my body's made of ramen"
quote5= "lulu lala lu"
quoteVar = ""

#signals whenever the bot is online
@bot.event
async def on_ready():
    print('Quote Bot Online')
    

@bot.event
async def on_message(message):
    if message.author != bot.user and not message.content == "!reportTallies":
        chanceForReply = random.randint(1,60)
        if chanceForReply >= baseChance:
            channel = message.channel
            if chanceForReply >= qt5:
                quoteVar = quote5
            elif chanceForReply >= qt4:
                quoteVar = quote4
            elif chanceForReply >= qt3:
                quoteVar = quote3
            elif chanceForReply >= qt2:
                quoteVar = quote2
            elif chanceForReply >= qt1:
                quoteVar = quote1
            elif chanceForReply >= qt0:
                quoteVar = quote0           
            await channel.send(quoteVar)
            tallyName= message.author.name + '#' + message.author.discriminator
            existingTallyMatches = searchTally(tallyName)
            if existingTallyMatches == 0:
                newTally(tallyName)
            elif existingTallyMatches ==1:
                increTally(tallyName)
            else:
                print("multiple matches found. nani!?")
    await bot.process_commands(message)

#command will result in an embed with individuals and their number of requests
@bot.command()
async def reportTallies(ctx):
    tableResults = printTallies()
    rowString = ""
    for x in tableResults:
        rowString += str(x[1])+ "-\t"+ str(x[0]) +"\n"
    reportEmbed = discord.Embed(title="Quote Tallies", description = rowString)    
    await ctx.send(embed=reportEmbed)



bot.remove_command('help')

bot.run("YOUR DISCORD BOT AUTH CODE HERE")


