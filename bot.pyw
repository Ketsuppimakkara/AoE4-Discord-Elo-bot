import os

import discord
from dotenv import load_dotenv

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import gzip
import io

import csv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if(len(message.mentions) == 0):
        return
    else:
        if'AoE4 Elo Bot' in message.mentions[0].name:
            channel = message.channel
            user = str(message.content)[23:]
            
            url = "https://aoe4world.com/dumps"
            request = Request(url) 
            request.add_header('User-Agent','Mozilla/5.0')
            page = urlopen(request).read()
            soup = BeautifulSoup(page,'html.parser') 
            elo = "not found on the leaderboard."

            for rows in soup.find_all(class_="hover:underline"):             
                if("leadersboards_rm_1v1_elo.csv" in rows.get('href')):
                    response = urlopen(rows.get('href'))
                    zippedData = io.BytesIO(response.read())
                    unZippedData = gzip.GzipFile(fileobj=zippedData).read()
                    playerList = str(unZippedData).split('\\n')
                    i = 0
                    while i<len(playerList)-1:
                        playerStats = playerList[i].split(',')
                        if(user == playerStats[1]):
                            elo = playerStats[3]
                            break
                        i = i+1
            result = user+"'s hidden ranked 1v1 elo is "+str(elo)

            await channel.send(result)

client.run(TOKEN)