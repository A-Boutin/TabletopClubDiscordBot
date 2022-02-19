import discord
from discord.ext import commands
import random

class NameGen():
    def __init__(self):
        self.setup()
        
    def setup(self):
        print("NameGen: Loaded")
    
    def line_appender(self, file_path, target):
        file = open(file_path, "r")
        splitfile = file.read().splitlines()
        for line in splitfile:
            target.append(line)

    def name_selector(self, target_list):
        selected = target_list[random.randrange(len(target_list))]
        return selected

    def name_builder(self, first_name_list_path, last_name_list_path):
        first_name_list = []
        last_name_list = []
        
        self.line_appender(first_name_list_path, first_name_list)
        self.line_appender(last_name_list_path, last_name_list)
        
        first_name_selected = self.name_selector(first_name_list)
        last_name_selected = self.name_selector(last_name_list)
        
        name = first_name_selected+" "+last_name_selected
        return name
    
    def name_gen(self, gender: str):
        if(str(gender).upper() == "M" or str(gender).upper() == "MALE"):
            name = self.name_builder("fantasy_names/first_name_male.txt", "fantasy_names/last_name.txt")
            return name
        elif(str(gender).upper() == "F" or str(gender).upper() == "FEMALE"):
            name = self.name_builder("fantasy_names/first_name_female.txt", "fantasy_names/last_name.txt")
            return name
        elif(str(gender).upper() == "N" or str(gender).upper() == "NEUTRAL"):
            first_name_list = []
            last_name_list = []
            
            self.line_appender("fantasy_names/first_name_male.txt", first_name_list)
            self.line_appender("fantasy_names/first_name_female.txt", first_name_list)
            self.line_appender("fantasy_names/last_name.txt", last_name_list)
            
            first_name_selected = self.name_selector(first_name_list)
            last_name_selected = self.name_selector(last_name_list)
            name = first_name_selected+" "+last_name_selected
            return name

class NameGenCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.namegenerator = NameGen()
        
    # Needs proper description
    @commands.command(aliases=['Namegen','NameGen','genname','Genname','GenName','ng','Ng','nG','NG','gn','Gn','gN','GN'],brief="Generates fantasy names for your characters.", description="/namegen [arg]\n\n- arg = Gender of your character.\n\nGenerates fantasy names for your characters")
    async def namegen(self, ctx, arg=None):
        if(arg != None):
            name = self.namegenerator.name_gen(arg)
            await ctx.send(name)
        
def setup(client):
    client.add_cog(NameGen(client))