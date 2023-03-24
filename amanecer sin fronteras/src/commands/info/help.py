import nextcord
from nextcord.ext import commands
from nextcord import Interaction, ButtonStyle
from nextcord.ui import Button, View

from config.config_handler import ConfigHandler
from components.embeds.help_embed import CreateHelpEmbed

class Help(commands.Cog):

    config_handler = ConfigHandler()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "help",
        description = "🔨 Obten ayuda sobre mis comandos",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    async def invite_command(self, ctx: Interaction):
        
        currentPage = 0
        
        nextButton = Button(label = "⏭️", style = ButtonStyle.blurple)
        previousButton = Button(label = "⏮️", style = ButtonStyle.blurple)
        
        async def next_callback(interaction):
            nonlocal currentPage, send
            currentPage += 1
            
            await send.edit(embed = CreateHelpEmbed(pagNum = currentPage), view=helpView)
            
        async def previous_callback(interaction):
            nonlocal currentPage, send
            currentPage -= 1
            
            await send.edit(embed = CreateHelpEmbed(pagNum = currentPage), view=helpView)
        
        nextButton.callback = next_callback
        previousButton.callback = previous_callback
        
        helpView = View(timeout = 300)
        helpView.add_item(previousButton)
        helpView.add_item(nextButton)
        
        
        send = await ctx.response.send_message(embed = CreateHelpEmbed(pagNum=0), view=helpView)
        
def setup(client):
    client.add_cog(Help(client))