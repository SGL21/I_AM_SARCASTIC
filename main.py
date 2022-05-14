import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()
sad_words = ["sad",'love','replt',"depressed",'pain' ,"unhappy", "angry", "misserable", "depressing","sorrowful","depressed","downcast","saddownhearted","down","despondent","despairing","disconsolate","out of sorts","desolate","wretched","glum","gloomy","doleful","dismal","blue","melancholy","melancholic","low-spirited","mournful","woeful","woebegone","forlorn","crestfallen","broken hearted","heartbroken","inconsolable","grief-stricken","down in the mouth","down in the dumps",'bad', 'blue', 'brokenhearted', 'cast down', 'crestfallen', 'dejected', 'depressed', 'despondent', 'disconsolate', 'doleful', 'down', 'downcast', 'downhearted', 'down in the mouth', 'droopy', 'gloomy', 'glum', 'hangdog', 'heartbroken', 'heartsick', 'heartsore', 'heavyhearted', 'inconsolable', 'joyless', 'low', 'low spirited', 'melancholic', 'melancholy', 'miserable', 'mournful', 'saddened', 'sorrowful', 'sorry', 'unhappy', 'woebegone', 'woeful', 'wretched', 'aggrieved', 'distressed', 'troubled', 'uneasy', 'unquiet', 'upset', 'worried', 'despairing', 'hopeless', 'sunk', 'disappointed', 'discouraged', 'disheartened', 'dispirited', 'suicidal', 'dolorous', 'lachrymose', 'lugubrious', 'plaintive', 'tearful', 'regretful', 'rueful', 'agonized', 'anguished', 'grieving', 'wailing', 'weeping', 'bleak', 'cheerless', 'comfortless', 'dark', 'darkening', 'depressing', 'desolate', 'dismal', 'drear', 'dreary', 'elegiac', 'elegiacal', 'funereal', 'gray' , 'grey', 'morbid', 'morose', 'murky', 'saturnine', 'somber', 'sombre', 'sullen', 'depressing', 'dismal', 'drear', 'dreary', 'heartbreaking', 'heartrending', 'melancholy', 'mournful', 'pathetic', 'saddening', 'sorry', 'tearful', 'teary', 'deplorable', 'distressful', 'grievous', 'lamentable', 'unfortunate', 'woeful', 'discomforting', 'discomposing', 'disquieting', 'distressing', 'disturbing', 'perturbing', 'affecting', 'moving', 'poignant', 'touching', 'discouraging', 'disheartening', 'dispiriting', 'deplorable', 'discreditable', 'disgraceful', 'disreputable', 'ignominious', 'infamous', 'misbegotten', 'notorious', 'shameful', 'abhorrent', 'abominable', 'beastly', 'detestable', 'hateful', 'lousy', 'odious', 'stinking', 'bad', 'inferior', 'lame', 'poor', 'disgusting', 'dishonorable', 'shameful', 'meritless', 'unworthy', 'worthless', 'scandalous', 'shocking', 'sordid', 'unsavory']

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person.",
  'You pagal insaan!',
  'Kuch aur kaam nhi he kya tumhare pass!!!',
  'Chal nikal pehli phursat me!!!',
  'Nice!',
  'javo bornvita piyo!', 
  'nobody cares... Lol', 
  "I'm better than you.",
  'dub maro javo',
  'kabhi shadi nahi hogi teri',       
  'dedhso rupya dega tereko, ye drama band kar',
  "The trouble with most of us is that we'd rather be ruined by praise than saved by criticism.",
  'get lost',
  'vo nahi milegi', 
  'cheh... Another idiot appears!!',
  'Kaha kaha se mu utake ajathe he',  'kudki shakal se kush raho aur kya',
  'im also depressed', 
  'kya kare teri zindigi pehelese jand hai',
  'Tera kuch nahi hosaktha'
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("http://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -"+json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_messages):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_messages)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_messages]



@client.event
async def on_ready():
  print("WE have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.lower()
  
  if msg.startswith("$quotes"):
    quote = get_quote()
    await message.channel.send(quote)
    
  if db["responding"] :
    options = starter_encouragements
    if "encouragements" in db.keys():
      options.extend(db["encouragements"])
    
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]
    
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    if value.lower() == "false":
      db["responding"] = False
      await message.channel.send("Responding is off.")

  if msg.startswith("$help"):
    await message.channel.send("Welcome to I_Am_Sarcastic bot help section!!!")
    await message.channel.send("press $quotes for quotes. ")
    await message.channel.send("press $help for help. ")
    await message.channel.send("press $responding true  - for turning on response for the bot. ")
    await message.channel.send("press $responding false  - for turning off response for the bot. ")
    await message.channel.send("Other actions are done by the bot automatically by observing the USER actions. ")

keep_alive()
my_secret = os.environ['Token']
client.run(my_secret)
