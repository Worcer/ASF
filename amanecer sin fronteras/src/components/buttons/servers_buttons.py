import nextcord
from nextcord import Embed, Interaction, Color, ButtonStyle, Guild
from components.embeds.servers_embed import CreateServerEmbed

class ServersButtons(nextcord.ui.View):
    def __init__(self, servers:  list, index: int):
        super().__init__()
        self.value = None,
        self.servers = servers
        self.index = index
        self.embed = CreateServerEmbed(index, servers)
        
    @nextcord.ui.button(label = "⏭️", style = ButtonStyle.blurple)
    async def next_page(self, button: nextcord.ui.Button, ctx: Interaction):
        
        if self.index < (len(self.servers)+9)//10 - 1:
            self.index += 1
            self.embed = self.create_embed(self.index)
            await ctx.response.edit_message(embed=self.embed, view=self)
        
    @nextcord.ui.button(label = "⏮️", style = ButtonStyle.blurple)
    async def previous_page(self, button: nextcord.ui.Button, ctx: Interaction):
        
        if self.index > 0:
            self.index -= 1
            self.embed = self.create_embed(self.index)
            await ctx.response.edit_message(embed=self.embed, view=self)