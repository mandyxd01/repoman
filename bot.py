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

black = ["Movie","Backup channel ","Channel3","Channel2","Channel1","Paid Channels","Models Collection ๐ Backup","https://assets-1.mdisk.me/assets/apk/Winner11-1.02.apk","โคJoin Channelโค","โก๏ธ","โญ๏ธJOIN OUR BACKUP CHANNEL","Aagya INDIA'S 1st FREE WINNING Fantasy APP","Visit :- www.winner11.net","Install now ๐","https://mdisk.me/convertor/203x360/jn2SYC","@ EZINETWORK","Must watch ๐คฉ๐คฉ๐ฅ๐ฅ๐ฅ๐ฅ","Join Our Telegram Backup Channel In Case This Channel Delete Please Join It Please๐๐","Must watch Guys ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ","Enjoy it โคโคโค","โจ๏ธ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐บ๐ฐ๐๐ฝ๐ด ๐ฝ๐ฐ๐ท๐ธ ๐ฐ๐ฐ๐๐ฐ ๐๐พ๐ท ๐ฟ๐ธ๐ฝ๐ฝ๐ด๐ณ ๐ผ๐ด๐๐๐ฐ๐ถ๐ด ๐ฒ๐ท๐ด๐ฒ๐บ ๐บ๐ฐ๐๐พ","๐ ๐ฑ๐ฐ๐ฒ๐บ๐๐ฟย  ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป","โฌ" ,"โ" ,"=" ,"โโพโโโผโพโโโผโพโโโผโพโโโผโพโโโผโพโโโผโพโโโผโ" ,"๐ฅBackup file๐ฅ" ,"๐ฅJoin channel ๐ฅ" ,"JOIN CHANNEL ๐" ,"Join adult network๐๐ฆ" ,"SHARE OUR CHANNEL๐" ,"๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ ๐ฐ๐ต๐ฎ๐ป๐ป๐ฒ๐น" ,"๐๐๐๐ ๐๐ โช" ,"๐โโ Join Our Backup:- ","Join now best channel" ,"โจ๏ธ SEARCH & JOIN NOW๐","โโโโขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโโโ","โฅ" ,]



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
        
        
        


        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

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
        caption = re.sub("Is IPL season daily 1000k+ prize ๐", "" , caption)
        if media:
            await client.send_file(indsend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(indsend_to , caption)


            
            
############### mix ##########

@client.on(events.NewMessage(chats=mix1))
async def hello2(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word
        
        
        


        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

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
            
            
####### for web eng #######

we = [-1001671942243,-1001607066545]
twe = -1001112334078

@client.on(events.NewMessage(chats=we))
async def hello1(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word
        


        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

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
            await client.send_file(twe ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(twe , caption)
            
            
          


          
print("Bot has been deployed.!")

client.start()
client.run_until_disconnected()





