import discord
import numpy
import os
import asyncio

from os import path
from json import load, dumps
from datetime import datetime

class BotData():
    def __init__(self):

        self.roll_dict = {}

        self.gmDict = {}

        self.statsDict = {}
        self.prefixDict = {}

        self.embedcolor = discord.Color.from_rgb(165,87,249)

        self.userSet = set()

        self.mongo_uri = ""

        try:
            pyDir = path.dirname(__file__)
            relPath = "..//mongo_uri.txt"
            absRelPath = path.join(pyDir, relPath)
            with open(absRelPath, 'r') as file:
                self.mongo_uri = file.readline().strip()
            print("Mongo Uri loaded successfully.")

        except Exception as e:
            print("Error loading mongo uri: {}".format(e))

        try:
            print("Loading stats from mongo db...")
            print("Stats loaded succesfully")
            raise Exception

        except Exception as e:
            try:
                print(f"Error loading stats: {e}")
                print("Loading stats from disk...")
                pyDir = path.dirname(__file__)
                relPath = "..//_data//stats.txt"
                absRelPath = path.join(pyDir, relPath)
                self.statsDict = load(open(absRelPath))
                print("Stats loaded succesfully")

            except Exception as e:
                print("Error loading stats: {}".format(e))

        try:
            print("Loading users from mongo db...")
            print("Users loaded succesfully")
            raise Exception

        except Exception as e:
            try:
                print(f"Error loading users: {e}")
                print("Loading users from disk...")
                pyDir = path.dirname(__file__)
                relPath = "..//_data//users.txt"
                absRelPath = path.join(pyDir, relPath)
                self.userSet = set(load(open(absRelPath)))
                print("Users loaded succesfully")

            except Exception as e:
                print(f"Error loading GM's: {e}")

        try:
            print("Loading gms from mongo db...")
            print("Gms loaded succesfully")
            raise Exception
        
        except Exception as e:
            try:
                print(f"Error loading GM's: {e}")
                print("Loading gms from disk...")
                pyDir = path.dirname(__file__)
                relPath = "..//_data//gms.txt"
                absRelPath = path.join(pyDir, relPath)
                self.gmDict = load(open(absRelPath))
                print("GM's loaded succesfully")

            except Exception as e:
                print(f"Error loading GM's: {e}")
 
        try:
            print("Loading prefixes from mongo db...")
            print("Prefixes loaded succesfully")
            raise Exception
        
        except Exception as e:
            try:
                print(f"Error loading prefixes: {e}")
                print("Loading prefixes from disk...")
                pyDir = path.dirname(__file__)
                relPath = "..//_data//prefixes.txt"
                absRelPath = path.join(pyDir, relPath)
                self.prefixDict = load(open(absRelPath))
                print("Prefixes loaded succesfully")

            except Exception as e:
                print(f"Error loading prefixes: {e}")

        print("\nTime: " + str(datetime.now()))

    async def string_splitter(self, string, char, max_splits):
        idxs = numpy.array([pos for pos, c in enumerate(string) if char == c])

        split_arr = []
        char_constant = 1800 # Maximum number of chars we will send
        prev_lower = 0

        for i in range(max_splits):
            leq = char_constant * (i+1)
            lower = idxs[idxs < leq].max()
            
            split_arr.append(string[prev_lower:lower])
            prev_lower = lower

            if leq > len(string):
                break

        return split_arr