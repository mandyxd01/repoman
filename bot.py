from random import randint
import re
from time import sleep
import requests
from telethon import TelegramClient , events
import os


id= 12149457
hash = "575877fb0c8586be1e91b618d44f07c5"

print("Starting Deployment..!")

client = TelegramClient("main_session"  , api_id=id , api_hash=hash)

#mdisk_api
mdisk_api = 'C2IGtPmGWkVoKaa0aPoy'

#footer
footer = ''' '''

mix1 = [-1001735663681,-1001607066545,-1001671942243,-1001494780519,-1001717209783]
mix1_to = -1001198221154

indchats = [-1001675910285]
indsend_to = -1001663052159


fzz = -1001706261502
serD = [-1001442038816, -1001477756331,-1001782270836, -1001250582595]

black = ["➡️","⭐️JOIN OUR BACKUP CHANNEL","Aagya INDIA'S 1st FREE WINNING Fantasy APP","Visit :- www.winner11.net","Install now 👇","https://mdisk.me/convertor/203x360/jn2SYC","@ EZINETWORK","Must watch 🤩🤩🔥🔥🔥🔥","Join Our Telegram Backup Channel In Case This Channel Delete Please Join It Please👇👇","Must watch Guys 🔥🔥🔥🔥🔥","Enjoy it ❤❤❤","♨️ 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙺𝙰𝚁𝙽𝙴 𝙽𝙰𝙷𝙸 𝙰𝙰𝚁𝙰 𝚃𝙾𝙷 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙲𝙷𝙴𝙲𝙺 𝙺𝙰𝚁𝙾","👉 🅱🅰🅲🅺🆄🅿  🅲🅷🅰🅽🅽🅴🅻","▬" ,"➖" ,"=" ,"●╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼●" ,"🔥Backup file🔥" ,"🔥Join channel 🔥" ,"JOIN CHANNEL 👇" ,"Join adult network🍌💦" ,"SHARE OUR CHANNEL👇" ,"𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗰𝗵𝗮𝗻𝗻𝗲𝗹" ,"𝐉𝐎𝐈𝐍 𝐔𝐒 ➪" ,"🙆‍♀ Join Our Backup:- ","Join now best channel" ,"♨️ SEARCH & JOIN NOW👇","☆☆☆••••••••••••••••☆☆☆","➥" ,]



##################### foward 1 ###################
@client.on(events.NewMessage(chats=indchats))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word
        
        
        for i in black:
            caption = re.sub(i, "" , caption)


        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            # print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        caption = re.sub("Cricket fans ke liye bahut sunhara mauka khele free contest and win kre daily 1lac"+"+", "" , caption)
        caption = re.sub("Is IPL season daily 1000k+ prize 🏆", "" , caption)
        if media:
            await client.send_file(indsend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(indsend_to , caption)


            
            
############### mix ##########

@client.on(events.NewMessage(chats=mix1))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word
        
        
        for i in black:
            caption = re.sub(i, "" , caption)


        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            # print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(mix1_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(mix1_to , caption)
            
            
####### for all #######

chats = [-1001663052159]
chats_to_send = [-1001696893100, -1001782270836,-1001477756331,-1001142224290,-1001198221154]

messages_toSend = []
messages_sent = []
@client.on(events.NewMessage(pattern=r'\.for',chats = chats))
async def runbollyhandler(event):
    replied_msg = await event.get_reply_message()
    
    chat = await event.get_chat()
    
    msg_id = replied_msg.id
    await client.delete_messages(chat , event.message)
    
    
    
    while 1:
        for ch in chats_to_send:
            try:
                allmsg = await client.get_messages(chat , None , reverse=True , min_id=(msg_id-1) , max_id=(msg_id+10))
            except:
                await client.send_message(720212064 , "Not enogh messages")
                return 0
            if len(allmsg) == 0:
                await client.send_message('@m3nd7' , "Not enogh messages")
                return 0
            messages_toSend = []
            messages_sent = []
            for msg in allmsg:
                    messages_toSend.append(msg)
                    #print(msg)
            while len(messages_sent) != len(messages_toSend):
                ran = randint(0 , len(messages_toSend) -1)
                if not ran in messages_sent:
                    await client.send_message(ch, messages_toSend[ran])
                    messages_sent.append(ran)
                
        msg_id = msg_id+10
        print("sleeping")
        sleep(3600)
        print("wake")
            
            
          


          
print("Bot has been deployed.!")

client.start()
client.run_until_disconnected()





