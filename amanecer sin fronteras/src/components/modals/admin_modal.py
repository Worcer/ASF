import datetime

from nextcord.ui import Modal, TextInput
from nextcord import Embed, Interaction, Color, Guild, Member

from utils.server_actions import Actions
from utils.server_utils import ServerUtils
from config.config_handler import ConfigHandler

class AdminModal(Modal):
    
    config_handler = ConfigHandler()
    utils = ServerUtils()
    actions = Actions()
    
    def __init__(self, guild: Guild, member: Member):
        super().__init__(
            title = "Configuración del comando /admin",
            timeout = 300)
        
        self.guild = guild
        self.member = member
        
        self.role_name = TextInput(
            label = "Nombre del rol",
            min_length = 1,
            max_length = 100,
            required = True,
            default_value = self.config_handler.get_admin_role_name(),
            placeholder = "El nombre del rol de admin que te dará el bot.")
        
        self.role_color = TextInput(
            label = "Color del rol.",
            min_length = 7,
            max_length = 7,
            required = True,
            default_value = self.config_handler.get_color_role_code(),
            placeholder = "Código hexadecimal de colores.")
        
        self.add_item(self.role_name)
        self.add_item(self.role_color)
        
    async def callback(self, ctx: Interaction) -> None:
        
        hexadecimal_color = self.utils.convert_hexadeciamal_color_code(self.role_color.value)
        name = self.role_name.value
        
        role = await self.actions.create_admin_role(self.guild,
                                                    hexadecimal_color,
                                                    name)
        print(type(role))
        await self.member.add_roles(role)
        
        
        admin_embed = Embed(
            title = "✅ | Se te han otorgado los máximos permisos con los que cuenta el bot.",
            timestamp = datetime.datetime.now(),
            color = Color.green())
        
        await ctx.response.send_message(embed = admin_embed)