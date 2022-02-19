import discord
from discord.ext import commands
import random

class DiceRoller():
    def __init__(self):
        self.setup()
        
    def setup(self):
        print("DiceRoller: Loaded")
    
    def d(self, sides):
        return random.randint(1, sides)

    def roll(self, n, sides):
        return tuple(self.d(sides) for _ in range(n))
    
    def parse_string(self, string):
        temp = string.split('d')
        temp2 = temp[1].split('+')
        parts = [int(temp[0]), int(temp2[0])]
        if(self.index_in_list(temp2, 1)):
            parts.append(int(temp2[1]))
        dice = self.roll(parts[0], parts[1])
        msg = "rolls "+string+". Results: "
        string_dice = [str(element) for element in dice]
        counter=0
        for die in string_dice:
            if(die == str(parts[1]) or die == "1"):
                string_dice[counter] = "**"+die+"**"
            counter=counter+1
        joined_string = ", ".join(string_dice)
        msg += joined_string
        if(self.index_in_list(parts, 2)):
            msg += " + "+str(parts[2])+" = "+str(sum(dice) + parts[2])
        else:
            msg += " = "+str(sum(dice))
        return msg

    def index_in_list(self, a_list, index):
        return index < len(a_list)

class DiceRollerCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.diceroller = DiceRoller()
        
    # Parse !roll verbiage
    @commands.command(aliases=['Roll','r','R'],pass_context=True,brief="Allows you to roll dice.",description='Rolls dice.\nExamples:\n100  Rolls 1-100.\n50-100  Rolls 50-100.\n3d6  Rolls 3 d6 dice and returns total.\nModifiers:\n! Hit success. 3d6!5 Counts number of rolls that are greater than 5.\nmod: Modifier. 3d6mod3 or 3d6mod-3. Adds 3 to the result.\n> Threshold. 100>30 returns success if roll is greater than or equal to 30.\n\nFormatting:\nMust be done in order.\nSingle die roll: 1-100mod2>30\nMultiple: 5d6!4mod-2>2')
    async def roll(self, ctx, roll : str):
        author = ctx.message.author.id
        await ctx.send("<@"+str(author)+"> "+self.diceroller.parse_string(roll))
        
def setup(client):
    client.add_cog(DiceRoller(client))