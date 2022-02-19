import discord
from discord.ext import commands, tasks
import random
import json
import asyncio

# Guess will be made with the /guess [word] command in dms
# Wordle 234 # The number of wordles that have passed 2/6 # Your current number of tries

# ⬛🟨⬛⬛⬛titan # The word you inputted
# ⬛🟩🟩⬛🟩 skill

# So Close! # Random message among list, will give an equally random message from a different list when you win
class Wordle():
    def __init__(self):
        self.setup()
        self.content_list = []
        self.current_wordle = ""
        self.current_index = 0
        self.wrong_letter = "⬛"
        self.near_letter = "🟨"
        self.correct_letter = "🟩"
        
    def setup(self):
        print("Wordle: Loaded")
        
    def split(self, word):
        return [char for char in word]
    
    def verify_guess(self, guess):
        wordle_char = self.split(self.current_wordle)
        guess_char = self.split(guess)
        evaluation = [None] * 5
        if(len(guess) > 5 or guess not in self.content_list):
            return "N/A"
        else:
            for i in range(5):
                if(guess_char[i] not in wordle_char):
                    evaluation[i] = self.wrong_letter
                    continue
                elif(guess_char[i] == wordle_char[i]):
                    evaluation[i] = self.correct_letter
                    wordle_char[i] = "_"
                    continue
                elif(guess_char[i] in wordle_char):
                    evaluation[i] = self.near_letter
                    continue
                else:
                    evaluation[i] = self.wrong_letter
                    continue
            return "".join(evaluation)

class WordleCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.wordle.start()
        self.emoticon_list = [":)", ":>", ":3", ">:)", ">:3", ";-;", "o7", ">:(", ":]", ":o", ":O", ":c", ">:[", ">:]", ":D", ">:D", ":p", ":P", ">:p", ">:P", "<3", "<_<", "<-<", ">_>", ">->", "v.v", "V.V", "._.", ".-.", "(◕‿◕✿)", "ʕ •ᴥ•ʔ", "(>_<)", "(>w<)", "<(｀^´)>", "^_^", "(°o°)", "(^_^)/", "(^O^)／", "(≧∇≦)/", "(/◕ヮ◕)/", "^ω^", "＼(°ロ＼)", "(／ロ°)／", "(=_=)", "(=^・^=)", "(´･ω･`)", "(づ￣ ³￣)づ", "(╯°□°）╯︵ ┻━┻", "┬─┬ ノ( ゜-゜ノ)"]
        self.encouraging_msg = ["So Close!", "You Can Do It!", "Almost There!", "You Nearly Have It!"]
        self.in_progress_member_list = {}
        self.completed_member_list = []
        self.wordleclass = Wordle()
        self.wordlemsg = "New Wordle Just Dropped! "

    @tasks.loop(hours=24) # Change to hours=24
    async def wordle(self):
        #Stuff for wordle
        channel = discord.utils.get(self.client.get_all_channels(), name="wordle")
        self.in_progress_member_list.clear()
        self.completed_member_list.clear()
        self.wordleclass.current_index = self.wordleclass.current_index +1
        self.wordleclass.current_wordle = random.choice(self.wordleclass.content_list)
        print("Wordle of the Day: "+self.wordleclass.current_wordle)
        data=None
        with open('config.json') as json_file:
            data = json.load(json_file)
            data['current_wordle'] = self.wordleclass.current_wordle
            data['wordle_index'] = str(self.wordleclass.current_index)
        with open('config.json', 'w') as outfile:
            result = json.dumps(data)
            outfile.write(result)
        await channel.send(self.wordlemsg+str(random.choice(self.emoticon_list)))
        
    @wordle.before_loop
    async def before_wordle(self):
        text_file = open("wordle_wordlist.txt", "r")
        lines = text_file.read()
        self.wordleclass.content_list = lines.split(",")
        
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.wordleclass.current_index = int(data['wordle_index'])
        
        await self.client.wait_until_ready()
        
    @commands.command(aliases=['Guessword','GuessWord','gw','Gw','gW','GW'],pass_context=True)
    async def guessword(self, ctx):
        author = ctx.message.author
        if author not in self.in_progress_member_list:
            self.in_progress_member_list[author] = []
            msg = "To get started just type /guess with the word you'd like to guess!\n Example: /guess apple"
            await author.send(msg)
            
    @commands.command(aliases=['Guess','g','G'],pass_context=True)
    @commands.dm_only()
    async def guess(self, ctx, arg):
        author = ctx.message.author
        if author not in self.in_progress_member_list:
            await author.send("You have to claim that you're starting today's wordle in #the-wordle channel in the server first before guessing for the day!")
        else:
            msg="Wordle "+str(self.wordleclass.current_index)+" "+str(len(self.in_progress_member_list[author])+1)+"/6\n\n"
            if author not in self.completed_member_list:
                # wordle word check logic here
                guess = self.wordleclass.verify_guess(str(arg))
                if(guess != "N/A"):
                    curr_guess = guess+" "+str(arg)
                    self.in_progress_member_list[author].append(curr_guess)
                    for word in self.in_progress_member_list[author]:
                        msg += word+"\n"
                    if(len(self.in_progress_member_list[author]) >= 6):
                        msg += "\nBetter Luck Next Time!"
                        self.completed_member_list.append(author)
                    elif(guess == "🟩🟩🟩🟩🟩"):
                        msg += "\nGood Job! :D"
                        self.completed_member_list.append(author)
                    else:
                        msg+="\n"+random.choice(self.encouraging_msg)
                    await author.send(msg)
                else:
                    await ctx.send("That wasn't a proper guess!")
            else:
                await author.send("You've already completed the wordle for today, silly!")

def setup(client):
    client.add_cog(Wordle(client))