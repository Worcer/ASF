import datetime

from nextcord.ext import commands, application_checks
from nextcord import Interaction, Embed, Color

from errors.custom_exceptions.command_execution import *

class ErrorHandler(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: Interaction, error):
        
        try:
            error = error.original
            
        except: pass
    
        if isinstance(error, BotIsNotInGuild):
            
            error_embed = Embed(
                title = "🚨| El comando solo funciona en los servidores en los que el bot está.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_embed, ephemeral=True)
            
        elif isinstance(error, MemberIsNotInGuild):
            
            error_embed = Embed(
                title = "🚨| Tú no estás en el servidor objetivo.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_embed, ephemeral=True)
            
        elif isinstance(error, BotCanNotCreateInvite):
            
            error_embed = Embed(
                title = "🚨| El bot no pudo crear ninguna invitación hacia algún canal.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_embed, ephemeral=True)
            
        elif isinstance(error, ExecutionCommandInThisGuildNotAllowed):
            
            error_embed = Embed(
                title = "🚨| Servidor protegido ante este comando.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_embed, ephemeral=True)
            
        elif isinstance(error, ParallelExecutionCommandsNotAllowed):
            
            error_embed = Embed(
                title = "🚨| Ejecución paralela de comando no permitida.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_embed, ephemeral=True)
            
        elif isinstance(error, commands.BotMissingPermissions):
            
            error_embed = Embed(
                title = "😢| No tengo permisos para hacer eso.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_embed, ephemeral=True)
            
        elif isinstance(error, application_checks.errors.ApplicationMissingRole):
            
            error_embed = Embed(
                title = "🚨| Solo las personas con un rol especifico pueden ejecutar este comando.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_embed, ephemeral=True)
            
        elif isinstance(error, IncorrectHexadecimalColorCode):
            
            error_embed = Embed(
                title = "🚨| El código de color introducido no es valido. \n \
                        Por favor introduzca uno correctamente.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_embed, ephemeral=True)
            
        else:
            error_system = Embed(
                title = "🚨| Ocurrío un error interno.",
                color = Color.red(),
                timestamp = datetime.datetime.now())

            await ctx.response.send_message(embed = error_system, ephemeral=True)
            
        print(f"Tipo de exepción: \n {type(error)} \n")
            
def setup(client):
    client.add_cog(ErrorHandler(client))