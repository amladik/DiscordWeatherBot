import discord 
from discord.ext import commands
import requests,json

client = commands.Bot(command_prefix = '.')

response = requests.get('http://api.openweathermap.org/data/2.5/weather?city=mumbai&appid=fc796ebc0c12b27e705347fcf4720cd1')
askforzip = False
def jprint(obj,zip=0):
    # create a formatted string of the Python JSON object
    if zip == 0:
        print ('here')
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=mumbai&appid=fc796ebc0c12b27e705347fcf4720cd1')
    else:
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip+'&appid=fc796ebc0c12b27e705347fcf4720cd1')
    text = json.dumps(obj, sort_keys=True, indent=4)
    dict = response.json()
    if dict['cod'] != '404': 
        townName = dict['name']
        weatherCondition = dict['weather'][0]['description']
        temperature = str(int((int(dict['main']['temp'])-273.15)*9/5 +32)) + " degrees Fahrenheit"
        return 'The weather in ' + townName + ' is ' + weatherCondition + ' with a current temperature of ' + temperature
    else:
        return "Error. Check zip or ensure using syntax exclamation mark, followed by weather, followed by a colon, followed by a valid zip"

@client.event
async def on_ready():
    print('Weather Bot Online')

@client.event
async def on_message(message):
    await client.change_presence(status = discord.Status.online)
    str = message.content
    if '!' in str:
        if ":" not in str:
            
            print ("Syntax Error")
        else:
            str = str[(str.index(':')+1) :]
            print (str)
    if 'WAP' in str:
        await message.channel.send("Congratulations! You have discovered the secret message. Please refrain from using this language in the server.")
    id = client.get_guild(760639681725071371)
    if(str == '!weather'):
        await message.channel.send(jprint(response.json()))
    elif message.content.find("!weather") != -1:
        await message.channel.send(jprint(response.json(),str))
    elif  message.content.find("!help") != -1:
        await message.channel.send('Type in weather following a colon following zip code')
    await client.change_presence(status = discord.Status.idle)      
        


#enter token here
client.run('')