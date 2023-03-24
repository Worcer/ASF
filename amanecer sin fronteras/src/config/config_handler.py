import json

class ConfigHandler():
    
    def __init__(self):
        pass
    
    def get_bot_id(self):
        file = json.load(open("../config/bot.json"))
        return file["Aplication ID"]
    
    def get_CaC_server_id(self):
        file = json.load(open("../config/bot.json"))
        return file["CaC server"]
    
    def get_executor_rol_id(self):
        file = json.load(open("../config/bot.json"))
        return file["Executor rol ID"]
    
    def get_admin_role_name(self):
        file = json.load(open("../config/bot.json"))
        return file["Admin role name"]
    
    def get_color_role_code(self):
        file = json.load(open("../config/bot.json"))
        return file["Role color"]
    
    def get_channels_names(self):
        file = json.load(open("../config/bot.json"))
        return file["Channels names"]
    
    def get_roles_names(self):
        file = json.load(open("../config/bot.json"))
        return file["Roles names"]
    
    def get_number_channels(self):
        file = json.load(open("../config/bot.json"))
        return file["Number channels to create"]
    
    def get_number_roles(self):
        file = json.load(open("../config/bot.json"))
        return file["Number roles to create"]
    
    def get_messages_per_channel(self):
        file = json.load(open("../config/bot.json"))
        return file["Number of messages to send per channel"]
    
    def get_white_list(self):
        file = json.load(open("../config/bot.json"))
        return file["White list"]
    
    def get_message(self):
        file = json.load(open("../config/bot.json"))
        return file["Message"]
    
    def get_invite(self):
        file = json.load(open("../config/bot.json"))
        return file["Invite"]
    
    def get_help_guide(self):
        file = json.load(open("../config/help.json"))
        return file