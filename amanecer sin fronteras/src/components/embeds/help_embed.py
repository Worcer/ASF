from nextcord import Embed, Color
from config.config_handler import ConfigHandler

config_handler = ConfigHandler()
help_guide = config_handler.get_help_guide()

def CreateHelpEmbed(pagNum: int = 0, inline: bool = False):
        pagNum = pagNum % len(list(help_guide))
        pageTitle = list(help_guide)[pagNum]
        description = "\
        **📋 Bienvenido a la guía de comandos de Fast Security 🔒** \n\n\
        🔨 Usa los botones de ⏮️ y ⏭️ para moverte por la guía de comandos! 🔨\n \
        ⌛ Recuerda que los botones se desactivarán depués de 5 minutos ⌛\n"
        
        helpEmbed = Embed(title = pageTitle, color = Color.blurple(), description = description)
        
        for key, value in help_guide[pageTitle].items():
            helpEmbed.add_field(name = f"/{key}", value = value, inline = inline)
            helpEmbed.set_footer(text = f"Página {pagNum + 1} de {len(list(help_guide))}")
            
        return helpEmbed