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


indchats = [-1001675910285]
indsend_to = -1001663052159


fzz = -1001706261502
serD = [-1001442038816, -1001477756331, -1001782270836, -1001250582595]


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
        caption = re.sub("Enjoy it ❤❤❤" , "" , caption)
        caption = re.sub("👉 🅱🅰🅲🅺🆄🅿  🅲🅷🅰🅽🅽🅴🅻" , "" , caption)
        caption = re.sub("🙆‍♀ Join Our Backup:- " , "" , caption)
        caption = re.sub("Join now best channel" , "" , caption)
        caption = re.sub("♨️ SEARCH & JOIN NOW👇" , "" , caption)
        caption = re.sub("☆☆☆••••••••••••••••☆☆☆" , "" , caption)
        caption = re.sub("➥" , "" , caption)
        caption = re.sub("𝐉𝐎𝐈𝐍 𝐔𝐒 ➪" , "" , caption)
        caption = re.sub("𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗰𝗵𝗮𝗻𝗻𝗲𝗹" , "" , caption)
        caption = re.sub("SHARE OUR CHANNEL👇" , "" , caption)
        caption = re.sub("Join adult network🍌💦" , "" , caption)
        caption = re.sub("JOIN CHANNEL 👇" , "" , caption)
        caption = re.sub("🔥Join channel 🔥" , "" , caption)
        caption = re.sub("🔥Backup file🔥" , "" , caption)
        caption = re.sub("▬" , "" , caption)
        caption = re.sub("●╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼●" , "" , caption)
        caption = re.sub("=" , "" , caption)
        caption = re.sub("➖" , "" , caption)


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
            await client.send_file(indsend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(indsend_to , caption)




@client.on(events.NewMessage(chats=fzz))
async def _(event):
    for i in serD:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)


          
print("Bot has been deployed.!")

client.start()
client.run_until_disconnected()





