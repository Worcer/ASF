class ParallelExecutionCommandsNotAllowed(Exception):
    
    def __init__(self, message = None):
        
        if message is None:
            message = "Parallel execution of commands on the same guild is not allowed."
            
        super(ParallelExecutionCommandsNotAllowed, self).__init__(message)


class ExecutionCommandInThisGuildNotAllowed(Exception):
    
    def __init__(self, message = None):
        
        if message is None:
            message = "In this guild you cant execute this command."
            
        super(ExecutionCommandInThisGuildNotAllowed, self).__init__(message)
        
class BotIsNotInGuild(Exception):
    
    def __init__(self, message = None):
        
        if message is None:
            message = "The command only works on servers where the bot is."
            
        super(BotIsNotInGuild, self).__init__(message)
        
class MemberIsNotInGuild(Exception):
    
    def __init__(self, message = None):
        
        if message is None:
            message = "The command only work if the user is in the server."
            
        super(BotIsNotInGuild, self).__init__(message)
        
class BotCanNotCreateInvite(Exception):
    
    def __init__(self, message = None):
        
        if message is None:
            message = "The bot could not create an invitation to any channel."
            
        super(BotCanNotCreateInvite, self).__init__(message)
        
class IncorrectHexadecimalColorCode(Exception):
    
    def __init__(self, message = None):
        
        if message is None:
            message = "Invalid hexadecimal color code."
            
        super(IncorrectHexadecimalColorCode, self).__init__(message)