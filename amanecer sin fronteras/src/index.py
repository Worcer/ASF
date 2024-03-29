import json

import nextcord
from nextcord.ext import commands
from middlewares.bag import Bag

bag = Bag()

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix = "!", intents = intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    
    print("The bot has been enable")
    await bot.change_presence(status=nextcord.Status.online)
    
def main():
    bag.clear()
    
    extentionsFile = json.load(open("..\config\cogs.json"))
    extentionsList = extentionsFile["cogs"]
    
    for extentions in extentionsList:
        bot.load_extension(extentions)

    bot.run("HERE THE BOT TOKEN")

if __name__ == "__main__": main()
