import discord
from discord.ext import commands
import random

from cogs.NameGen import NameGen

class CharacterGen():
    def __init__(self):
        self.namegenerator = NameGen()
        self.setup()
        self._name = ""
        self._race = ""
        self._class = ""
        self._stats = []
        
    def setup(self):
        print("CharacterGen: Loaded")
        
    def name_gen(self, gender):
        return self.namegenerator.name_gen(gender)
    
    def choose_race(self, *supplements):
        races = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "halfling", "half-orc", "human", "tiefling"]
        if(any("MYTHIC" in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("leonin")
            races.append("satyr")
        if(any("WILD" in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("fairy")
            races.append("harengon")
        if(any("STRIX"in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("owlin")
        if(any("ELEMENTAL"in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("aarakocra")
            races.append("genasi")
            races.append("goliath")
        if(any("VOLO"in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("aasimar")
            races.append("bugbear")
            races.append("firbolg")
            races.append("goblin")
            races.append("hobgoblin")
            races.append("kenku")
            races.append("kobold")
            races.append("lizardfolk")
            races.append("orc")
            races.append("tabaxi")
            races.append("triton")
            races.append("yuan-ti pureblood")
        if(any("TORTLE" in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("tortle")
        if(any("EBERRON"in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("changeling")
            races.append("kalashtar")
            races.append("shifter")
            races.append("warforged")
        if(any("MORDEN" in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("gith")
        if(any("GUILD" in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("centaur")
            races.append("loxodon")
            races.append("minotaur")
            races.append("simic hybrid")
            races.append("vedalken")
        if(any("LOCATHAH"in str(supplement).upper() for supplement in supplements) or any("ALL"in str(supplement).upper() for supplement in supplements)):
            races.append("locathah")
        if(any("GRUNG"in str(supplement).upper() for supplement in supplements) or any("ALL" in str(supplement).upper() for supplement in supplements)):
            races.append("grung")
        chosen_race = random.choice(races)
        return chosen_race
    
    def choose_class(self, *supplements):
        classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
        if(any("TASHA" in str(supplement).upper() for supplement in supplements) or any("ALL" in str(supplement).upper() for supplement in supplements)):
            classes.append("artificer")
        chosen_class = random.choice(classes)
        return chosen_class
    
    def stats(self):
        self._stats.clear()
        for i in range(6):
            rolls = []
            for j in range(4):
                rolls.append(random.randint(1, 6))
            rolls.sort(reverse=True)
            self._stats.append(rolls[0]+rolls[1]+rolls[2])
        return self._stats
    
    def chargen(self, *supplements):
        genders=["m","f","n"]
        char_gender = random.choice(genders)
        name = self.name_gen(char_gender)
        stats = self.stats()
        char_race = self.choose_race(supplements)
        char_class = self.choose_class(supplements)
        msg = "**"+name+"**\nRace: "+char_race.capitalize()+"\nClass: "+char_class.capitalize()+" Lvl: 1\nStats: "
        for stat in stats:
            msg += str(stat)+" "
        return msg

class CharacterGenCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.charactergenerator = CharacterGen()
        
    @commands.command(aliases=['Rollstats', 'RollStats', 'rollstat', 'Rollstat', 'RollStat', 'stats', 'Stats'],brief="Rolls for stats for a dnd character.", description="/rollstats\n\nRolls for stats for a dnd character.")
    async def rollstats(self, ctx):
        stats = self.charactergenerator.stats()
        msg=""
        for stat in stats:
            msg += str(stat)+" "
        await ctx.send(msg)
            
    @commands.command(aliases=['Chargen','CharGen','charactergen','Charactergen','CharacterGen','charactergenerate','Charactergenerate','CharacterGenerate','genchar','Genchar','GenChar','generatechar','Generatechar','GenerateChar','generatecharacter','Generatecharacter','GenerateCharacter'],brief="Creates a brief, randomly created dnd character.", description="/chargen [args]\n\n- args = What supplements you'd like implemented in the randomization, separated by spaces.\n\nCreates a brief, randomly created dnd character.")
    async def chargen(self, ctx, *args):
        await ctx.send(self.charactergenerator.chargen(args))
        
def setup(client):
    client.add_cog(CharacterGen(client))